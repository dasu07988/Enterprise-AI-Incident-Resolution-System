# Suspicious Login Attempt

## Overview

Multiple failed or unusual login attempts have been detected from unknown users, devices, or geographic locations. This may indicate a brute-force attack or compromised credentials.

---

## Symptoms

- Multiple failed login attempts
- Login attempts from unknown countries
- New device login alerts
- Account lockouts
- Increased authentication failures

---

## Possible Causes

- Brute-force attack
- Credential stuffing
- Compromised user credentials
- Stolen authentication token
- Malicious insider activity

---

## Verification Steps

1. Review authentication logs.
2. Verify source IP addresses.
3. Check user login history.
4. Review MFA events.
5. Analyze SIEM alerts.

---

## Resolution Steps

1. Block suspicious IP addresses.
2. Force password reset.
3. Revoke active sessions.
4. Enable Multi-Factor Authentication.
5. Notify affected users.
6. Monitor for additional activity.

---

## Rollback Procedure

- Restore legitimate user access.
- Remove temporary IP blocks after validation.

---

## Monitoring

Monitor:

- Failed Login Attempts
- Authentication Success Rate
- MFA Events
- Security Alerts

---

## Escalation

Severity: Critical

Escalate to:

- Security Operations Center (SOC)
- Identity Management Team
- Incident Response Team

---

## References

Runbook ID: SEC-001

Related Services

- Identity Provider
- Authentication Service
- SIEM
