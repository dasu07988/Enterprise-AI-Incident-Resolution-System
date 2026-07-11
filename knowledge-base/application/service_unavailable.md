# Service Unavailable (HTTP 503)

## Overview

The application service is temporarily unavailable and returns HTTP 503 responses. This usually indicates backend overload, maintenance, or dependency failures.

---

## Symptoms

- HTTP 503 Service Unavailable errors.
- Users cannot access the application.
- API requests fail.
- Increased service downtime.
- Health checks fail.

---

## Possible Causes

- Application overload
- Backend service unavailable
- Load balancer issues
- Infrastructure failure
- Scheduled maintenance
- Dependency outage

---

## Verification Steps

1. Verify application health checks.
2. Review load balancer status.
3. Check backend service availability.
4. Inspect infrastructure monitoring.
5. Verify deployment status.
6. Review application logs.

---

## Resolution Steps

1. Restart failed services.
2. Restore backend connectivity.
3. Scale application instances.
4. Resolve infrastructure issues.
5. Validate load balancer configuration.
6. Confirm service availability.

---

## Rollback Procedure

- Roll back recent deployments.
- Restore previous infrastructure configuration.
- Verify application availability.

---

## Monitoring

Monitor:

- Service Availability
- HTTP 503 Error Rate
- API Latency
- Load Balancer Health
- Infrastructure Health
- Backend Service Status

---

## Escalation

Severity: Critical

Escalate to:

- Platform Engineering Team
- Infrastructure Team
- DevOps Engineer
- Incident Manager

---

## References

Runbook ID: APP-005

Related Services

- API Gateway
- Application Service
- Load Balancer
