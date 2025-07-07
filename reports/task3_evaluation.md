# 🧪 Task 3 - RAG Evaluation Report

**Project**: Intelligent Complaint Analysis  
**Task**: Task 3 – Build & Evaluate Retrieval-Augmented Generation (RAG)  
**LLM Used**: `google/flan-t5-base`  
**Device**: CPU  
**Date**: 2025-07-01

---

## 🔍 Evaluation Results

### ❓ Question 1:

**Why are users unhappy with Buy Now, Pay Later?**  
**Answer:**

> they want to make things difficult for their customers and increase the likelihood of late fee revenue by forcing payments to be made through slow and inconvenient methods for no reasons other than truist s animosity and greed

**Top Sources:**

- "to allow payments to be made online after xxxx days... forcing payments to be made through..."
- "to mislead and get an interest payment from a regularly paying customer..."

**Score (1-5):** `___`  
**Comments:** `___`

---

### ❓ Question 2:

**What common issues do customers report for credit cards?**  
**Answer:**

> unusual issues

**Top Sources:**

- "protect customer interests and accurately report credit information..."
- "unusual issues instead of the normal credit card activity... comenity is inept..."

**Score (1-5):** `___`  
**Comments:** `___`

---

### ❓ Question 3:

**Are there complaints about money transfer delays?**  
**Answer:**

> yes

**Top Sources:**

- "which has led to further misunderstandings... required extensive wait times and multiple transfers..."
- "not provide any information other than there is sometimes a delay..."

**Score (1-5):** `___`  
**Comments:** `___`

---

### ❓ Question 4:

**What are the main pain points for personal loan customers?**  
**Answer:**

> high late payment and interest fees they have no interest in what s best for the customer

**Top Sources:**

- "a bigger issue and abuse of marketing to trap customers into debt..."
- "how difficult is it not to bring minds together... what causes debt is not always over spending..."

**Score (1-5):** `___`  
**Comments:** `___`

---

### ❓ Question 5:

**Do customers mention fraud in savings accounts?**  
**Answer:**

> no

**Top Sources:**

- "consumers from fraudulent transactions on their credit card accounts..."
- "instead of accepting any disputes this constitutes consumer fraud..."

**Score (1-5):** `___`  
**Comments:** `___`

---

## ✅ Summary

- The RAG system successfully generated answers grounded in retrieved complaint text.
- Some outputs are direct and accurate (e.g., BNPL & loan issues), while others (e.g., fraud or credit card answers) lack depth or specificity.
- Improving prompt engineering and chunk relevance filtering may enhance results.

---
