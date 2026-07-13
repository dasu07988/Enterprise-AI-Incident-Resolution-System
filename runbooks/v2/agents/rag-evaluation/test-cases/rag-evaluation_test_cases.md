# RAG Evaluation Agent Test Cases

## Objective

Validate that the RAG Evaluation Agent accurately evaluates the quality of retrieved enterprise knowledge.

---

## Test Case 1

Incident:

Payment API returns HTTP 500 errors after deployment.

Expected

- Retrieval score above 0.90
- Knowledge complete
- Quality Excellent

---

## Test Case 2

Incident

Corporate VPN unavailable.

Expected

- Relevant retrieval
- Good quality

---

## Test Case 3

Incident

Authentication failure

Expected

- Missing knowledge detected
- Retrieval score below 0.50
- Recommendation for additional retrieval

---

## Acceptance Criteria

- Valid JSON
- Accurate relevance scoring
- No hallucinations
- Enterprise reasoning