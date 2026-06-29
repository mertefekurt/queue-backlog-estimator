from __future__ import annotations

from queue_backlog_estimator.models import Rule

PROJECT_NAME = 'queue-backlog-estimator'
DESCRIPTION = 'Review queue workload plans for backlog and worker-capacity risk.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'arrival_rate: 500/min worker_capacity: 100/min max_backlog: unknown dlq: none'
MEDIUM_SAMPLE = '\\b(max_backlog\\s*[:=]\\s*(unknown|none|null)|max_backlog unknown)\\b'
CLEAN_SAMPLE = 'arrival_rate 100/min worker_capacity 250/min max_backlog 1000 dlq enabled'

RULES = (
    Rule(
        code='capacity-below-arrival',
        severity='high',
        pattern=(
                    '\\bworker_capacity\\s*[:=]\\s*100/min\\b.*\\barrival_rate\\s*[:=]\\s*500/min\\b|'
                    '\\barrival_rate\\s*[:=]\\s*500/min\\b.*\\bworker_capacity\\s*[:=]\\s*100/min\\b'
                ),
        message='worker capacity appears below arrival rate',
        recommendation='Increase workers, reduce arrival rate, or add backpressure.',
    ),
    Rule(
        code='missing-backlog-limit',
        severity='medium',
        pattern='\\b(max_backlog\\s*[:=]\\s*(unknown|none|null)|max_backlog unknown)\\b',
        message='backlog limit is missing',
        recommendation='Set queue depth alerts and discard policy.',
    ),
    Rule(
        code='missing-dlq',
        severity='low',
        pattern='\\bdlq\\s*[:=]\\s*(none|missing|null)\\b',
        message='dead-letter queue is missing',
        recommendation='Add DLQ handling for poisoned messages.',
    ),
)
