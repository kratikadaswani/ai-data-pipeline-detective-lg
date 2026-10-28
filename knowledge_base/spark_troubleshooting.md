
# Apache Spark Troubleshooting Guide

## 1. Missing input path

Common error:
AnalysisException: Path does not exist

Possible causes:
- The configured input path is incorrect.
- The expected files have not arrived.
- The source directory was moved or deleted.
- The storage location or filesystem is not mounted or accessible.

Diagnostic checks:
1. Inspect the exact input path in the job configuration.
2. Verify that the expected directory and files exist.
3. Check whether the upstream pipeline completed successfully.
4. For cloud storage, verify the account, container, endpoint, and access permissions.
5. Confirm that the job is using the intended environment and configuration.

Do not assume that a missing-path error proves an authorization failure. Confirm the path and access separately.

## 2. Schema mismatch

Common symptoms:
- AnalysisException involving incompatible data types.
- Failed casts between STRING, INT, BIGINT, or TIMESTAMP.
- Unexpected or missing columns.

Possible causes:
- Upstream data changed its schema.
- A field contains values incompatible with the expected type.
- The job uses an outdated schema definition.

Diagnostic checks:
1. Compare the expected schema with the actual input schema.
2. Inspect representative records for incompatible values.
3. Review recent upstream schema changes.
4. Use explicit casting and validation where appropriate.

## 3. Out-of-memory errors

Common symptoms:
- Java heap space errors.
- Executor lost or killed.
- Container termination due to memory limits.

Possible causes:
- Large partitions or data skew.
- Excessive caching.
- Memory-intensive joins or aggregations.
- Executor memory configuration that does not fit the workload.

Diagnostic checks:
1. Inspect executor logs and memory metrics.
2. Check partition sizes and skew.
3. Review cached DataFrames and their lifecycle.
4. Inspect join strategy and shuffle volume.
5. Validate resource settings before changing them.
