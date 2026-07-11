# DNS Failure

## Overview

The Domain Name System (DNS) service is unable to resolve hostnames to IP addresses, causing applications and users to lose connectivity to internal or external services.

---

## Symptoms

- Applications cannot resolve hostnames.
- Website unavailable.
- API connection failures.
- Timeout errors.
- Intermittent connectivity issues.

---

## Possible Causes

- DNS server outage
- Incorrect DNS configuration
- Network connectivity issues
- Expired DNS records
- Firewall blocking DNS traffic

---

## Verification Steps

1. Run DNS lookup (nslookup/dig).
2. Verify DNS server availability.
3. Check DNS configuration.
4. Test network connectivity.
5. Review DNS logs.

---

## Resolution Steps

1. Restart DNS service.
2. Restore DNS configuration.
3. Flush DNS cache.
4. Verify DNS records.
5. Test hostname resolution.

---

## Rollback Procedure

- Restore previous DNS configuration.
- Revert DNS changes.
- Validate name resolution.

---

## Monitoring

Monitor:

- DNS Query Success Rate
- DNS Response Time
- Server Availability
- Error Rate

---

## Escalation

Severity: High

Escalate to:

- Network Team
- Infrastructure Team

---

## References

Runbook ID: NET-001

Related Services

- Internal DNS
- Public DNS

