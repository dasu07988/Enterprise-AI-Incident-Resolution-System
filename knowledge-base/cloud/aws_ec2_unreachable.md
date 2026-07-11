# AWS EC2 Instance Unreachable

## Overview

An Amazon EC2 instance is unreachable and cannot be accessed through SSH, RDP, or application endpoints. This incident may impact production workloads hosted on the affected instance.

---

## Symptoms

- SSH or RDP connection fails.
- Application unavailable.
- Health checks fail.
- Ping requests timeout.
- Cloud monitoring reports instance failure.

---

## Possible Causes

- EC2 instance stopped
- Security Group misconfiguration
- Network ACL restrictions
- Route table issue
- Operating system crash
- High CPU or memory utilization

---

## Verification Steps

1. Verify EC2 instance status.
2. Check Security Group rules.
3. Review Network ACL configuration.
4. Verify VPC routing.
5. Check CloudWatch metrics.
6. Review system logs.

---

## Resolution Steps

1. Restart the EC2 instance.
2. Correct Security Group configuration.
3. Restore network routing.
4. Recover operating system.
5. Validate application availability.

---

## Rollback Procedure

- Restore previous network configuration.
- Recover from latest AMI snapshot.
- Validate application services.

---

## Monitoring

Monitor:

- EC2 Status Checks
- CPU Utilization
- Memory Usage
- Network Traffic
- Disk Utilization

---

## Escalation

Severity: Critical

Escalate to:

- Cloud Operations Team
- Platform Engineering Team

---

## References

Runbook ID: CLD-001

Related Services

- AWS EC2
- Amazon CloudWatch
