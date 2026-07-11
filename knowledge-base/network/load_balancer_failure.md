# Load Balancer Failure

## Overview

The load balancer is unable to distribute incoming traffic correctly, causing service degradation or application downtime.

---

## Symptoms

- HTTP 503 errors.
- Uneven traffic distribution.
- Backend servers unreachable.
- Increased application latency.
- Failed health checks.

---

## Possible Causes

- Load balancer configuration error
- Backend server failure
- Health check failure
- Network issue
- SSL certificate problem

---

## Verification Steps

1. Verify load balancer status.
2. Check backend health.
3. Review health check configuration.
4. Validate SSL certificates.
5. Review logs.

---

## Resolution Steps

1. Restart load balancer.
2. Restore backend connectivity.
3. Fix health checks.
4. Replace expired certificates.
5. Verify traffic distribution.

---

## Rollback Procedure

- Restore previous configuration.
- Roll back recent changes.
- Validate service availability.

---

## Monitoring

Monitor:

- Backend Health
- Request Rate
- Error Rate
- Response Time
- Active Connections

---

## Escalation

Severity: Critical

Escalate to:

- Network Team
- Platform Engineering Team

---

## References

Runbook ID: NET-003

Related Services

- Load Balancer
- API Gateway

