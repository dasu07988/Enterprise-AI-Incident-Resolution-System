# IAM Permission Error

## Overview

Users or services cannot access AWS resources because of insufficient IAM permissions.

---

## Symptoms

- Access Denied errors
- AWS API failures
- Deployment failures
- Unauthorized requests

---

## Possible Causes

- Missing IAM policy
- Incorrect IAM role
- Expired credentials
- Resource policy restrictions

---

## Verification Steps

1. Verify IAM policies.
2. Review IAM roles.
3. Validate AWS credentials.
4. Check CloudTrail logs.
5. Test AWS API access.

---

## Resolution Steps

1. Assign correct IAM permissions.
2. Update IAM policies.
3. Rotate credentials if necessary.
4. Verify successful access.

---

## Rollback Procedure

- Restore previous IAM policy.
- Revert permission changes.

---

## Monitoring

Monitor:

- IAM Authentication
- Access Denied Events
- CloudTrail Logs

---

## Escalation

Severity: High

Escalate to:

- Cloud Security Team
- Cloud Operations Team

---

## References

Runbook ID: CLD-002

Related Services

- AWS IAM
- CloudTrail
