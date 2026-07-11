# Database Deadlock

## Overview

Two or more database transactions are waiting indefinitely for resources held by each other, preventing successful transaction completion.

---

## Symptoms

- Transactions fail.
- Query execution hangs.
- Increased response time.
- Database timeout errors.
- Application performance degradation.

---

## Possible Causes

- Concurrent transactions
- Poor query design
- Long-running transactions
- Table locking
- Missing indexes

---

## Verification Steps

1. Review deadlock logs.
2. Identify blocked sessions.
3. Analyze SQL execution plans.
4. Check transaction history.
5. Monitor lock statistics.

---

## Resolution Steps

1. Terminate blocked transactions.
2. Optimize SQL queries.
3. Reduce transaction duration.
4. Add required indexes.
5. Restart affected services if necessary.

---

## Rollback Procedure

- Restore previous query version.
- Reverse recent schema changes.
- Validate application functionality.

---

## Monitoring

Monitor:

- Deadlock Count
- Query Execution Time
- Lock Wait Time
- Database Performance

---

## Escalation

Severity: Medium

Escalate to:

- Database Administrator
- Application Support Team

---

## References

Runbook ID: DB-003

Related Services

- Production Database
