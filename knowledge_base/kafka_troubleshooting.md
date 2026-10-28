
# Apache Kafka Troubleshooting Guide

## 1. Producer or consumer timeout

Common symptoms:
- TimeoutException.
- Requests timing out while contacting brokers.
- Consumer unable to fetch records.

Possible causes:
- Brokers are unreachable.
- Incorrect bootstrap server configuration.
- DNS or network problems.
- Incorrect advertised.listeners configuration.
- Broker overload or request delays.

Diagnostic checks:
1. Verify the bootstrap server addresses and ports.
2. Check DNS resolution and network connectivity.
3. Review broker logs and health.
4. Check advertised.listeners and security settings.
5. Inspect request latency and consumer lag.

## 2. Consumer lag

Common symptoms:
- Consumer lag continuously increases.
- Records are processed more slowly than they arrive.

Possible causes:
- Slow processing.
- Insufficient consumer parallelism.
- Downstream database or API bottlenecks.
- Repeated failures or expensive transformations.

Diagnostic checks:
1. Measure consumer lag over time.
2. Inspect processing throughput and error rates.
3. Review downstream latency.
4. Check consumer group membership and partition assignment.
5. Inspect retry behavior and processing time.
