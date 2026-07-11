# Database Down

## Overview

The primary production database is unavailable, preventing applications from reading or writing data. This incident impacts multiple business services and requires immediate investigation.

---

## Symptoms

- Database connection failures
- Applications cannot retrieve data
- Transaction failures
- Login failures
- HTTP 500 errors
- Increased application downtime

---

## Possible Causes

- Database server failure
- Network connectivity issue
- Storage failure
- Database service stopped
- Hardware failure
- Cloud infrastructure outage

---

## Verification Steps

1. Verify database server availability.
2. Check database service status.
3. Test database connectivity.
4. Review database logs.
5. Verify storage availability.
6. Check server CPU and memory.
7. Confirm network connectivity.

---

## Resolution Steps

1. Restart the database service.
2. Restore server connectivity.
3. Recover failed storage if required.
4. Fail over to the standby database.
5. Verify application connectivity.
6. Confirm successful transactions.

---

## Rollback Procedure

- Restore previous database snapshot if required.
- Switch traffic back to the primary database.
- Validate database integrity.

---

## Monitoring

Monitor:

- Database Availability
- Connection Count
- Query Response Time
- Replication Status
- Storage Utilization
- CPU Usage

---

## Escalation

Severity: Critical

Escalate to:

- Database Administrator
- Platform Engineering Team
- Infrastructure Team

---

## References

Runbook ID: DB-001

Related Services

- Production Database
- Customer Portal
- Payment Service

