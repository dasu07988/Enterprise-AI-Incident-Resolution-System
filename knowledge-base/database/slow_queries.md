# Slow Database Queries

## Overview

Database queries take significantly longer than expected, affecting application performance and user experience.

---

## Symptoms

- Slow application response.
- High database CPU usage.
- Long-running queries.
- Increased user complaints.
- Application timeouts.

---

## Possible Causes

- Missing indexes
- Inefficient SQL statements
- Large table scans
- Storage latency
- High concurrent workload

---

## Verification Steps

1. Identify slow queries.
2. Review execution plans.
3. Check index usage.
4. Monitor database performance.
5. Review server resource utilization.

---

## Resolution Steps

1. Optimize SQL queries.
2. Create missing indexes.
3. Archive unnecessary data.
4. Tune database configuration.
5. Increase database resources if required.

---

## Rollback Procedure

- Restore previous query version.
- Remove incorrect indexes.
- Validate application performance.

---

## Monitoring

Monitor:

- Query Response Time
- Slow Query Count
- CPU Usage
- Index Performance
- Database Throughput

---

## Escalation

Severity: Medium

Escalate to:

- Database Administrator
- Performance Engineering Team

---

## References

Runbook ID: DB-004

Related Services

- Production Database
- Reporting Database

