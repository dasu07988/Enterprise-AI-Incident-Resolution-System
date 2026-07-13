# Multi-Intent Analysis Agent Test Cases

## Objective

Validate that the Multi-Intent Analysis Agent correctly identifies multiple incidents within a single enterprise incident report.

---

## Test Case 1

Incident Report:

Payment API returns HTTP 500 errors after deployment.
Database latency increased to 3000ms.
Redis cache unavailable.

Expected:

- Detect 3 incidents
- Identify application, database, and infrastructure incidents
- Detect relationships between incidents

---

## Test Case 2

Incident Report:

Corporate VPN unavailable.
DNS resolution failures observed.

Expected:

- Detect 2 incidents
- Identify network-related relationship

---

## Test Case 3

Incident Report:

Authentication service unavailable.
Users report login failures.
Identity Provider health checks failing.

Expected:

- Detect 3 incidents
- Correctly identify dependency between Identity Provider and authentication failures

---

## Acceptance Criteria

- Valid JSON output
- Correct incident count
- No hallucinated incidents
- Clear relationship detection
- Professional enterprise reasoning