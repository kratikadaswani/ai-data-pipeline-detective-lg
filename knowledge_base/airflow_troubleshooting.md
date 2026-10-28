
# Apache Airflow Troubleshooting Guide

## 1. Task failures

Common symptoms:
- TaskInstance enters the failed state.
- PythonOperator raises an exception.
- A task exits with a non-zero status.

Possible causes:
- Application code errors.
- Missing configuration or environment variables.
- Dependency failures.
- Access restrictions.
- Upstream task failure.

Diagnostic checks:
1. Read the complete task log and traceback.
2. Identify the first relevant exception.
3. Verify required configuration and dependencies.
4. Check upstream task states.
5. Review retries and execution timeouts.

## 2. Tasks stuck in queued state

Possible causes:
- Worker capacity constraints.
- Executor configuration issues.
- Scheduler or queue problems.
- Resource limits.

Diagnostic checks:
1. Check scheduler health.
2. Inspect worker availability and logs.
3. Review executor and queue configuration.
4. Check available resources and concurrency limits.
