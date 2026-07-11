# Amazon S3 Access Denied

## Overview

Applications or users cannot access objects stored in Amazon S3 because of permission or bucket policy issues.

---

## Symptoms

- Access Denied message
- Object download fails
- Upload failure
- Backup process fails

---

## Possible Causes

- Incorrect bucket policy
- IAM permission issue
- Public access blocked
- Expired credentials

---

## Verification Steps

1. Verify IAM permissions.
2. Review bucket policy.
3. Check object ACL.
4. Validate AWS credentials.
5. Test bucket access.

---

## Resolution Steps

1. Correct IAM permissions.
2. Update bucket policy.
3. Remove unnecessary restrictions.
4. Verify application connectivity.

---

## Rollback Procedure

- Restore previous bucket policy.
- Restore IAM permissions.

---

## Monitoring

Monitor:

- S3 Requests
- Access Denied Events
- Storage Usage

---

## Escalation

Severity: Medium

Escalate to:

- Cloud Operations Team
- Security Team

---

## References

Runbook ID: CLD-003

Related Services

- Amazon S3

