# 25 · Classical ML, recommendations, and decision systems

**Prerequisites:** Chapters 1, 3, and 18. **Goal:** recognize when prediction and ranking are more appropriate than free-form generation.

## Not all AI systems generate text

A fraud model scores transaction risk. A recommendation engine ranks items. A demand model predicts future volume. These systems need training data, features, evaluation, serving, monitoring, and feedback just as an LLM application does, but their objectives and failure modes differ.

**Everyday intuition:** deciding which product to show next is a ranking problem; explaining a selected product in clear language is a generation problem. They can share an interface without sharing the same model.

## A recommendation pipeline

Candidate generation selects a manageable set of items from a large catalog. Ranking scores those candidates using user, item, and context features. A policy/reranking layer can enforce availability, diversity, and business constraints. An LLM can explain a recommendation using verified product information; it should not invent the ranking score or stock availability.

Cold-start users and items lack historical interactions. Use explicit preferences, content features, popular eligible items, or an exploration policy rather than pretending all users have a rich history.

## Training and serving consistency

A feature is an input signal such as recent purchase count. Its definition must match between training and serving. If training accidentally includes information only available after an outcome, performance looks excellent offline and fails in production. This is target leakage.

Use time-based splits when predicting future behavior. Log which feature values and model version produced a decision. Monitor missing features, delayed data, distribution changes, and label delay. Labels such as chargebacks may arrive weeks later.

## Metrics and thresholds

| Task | Useful measurements | Important caveat |
|---|---|---|
| Imbalanced classification | Precision, recall, PR-AUC, error cost | Overall accuracy can hide rare-event failure |
| Probability estimation | Calibration and proper scoring rules | A high rank score is not necessarily a probability |
| Recommendations | Recall/nDCG offline; user outcomes online | Clicks alone may reward poor experiences |
| Forecasting | MAE, scaled/relative errors, business cost | Compare a seasonal or simple baseline |

A threshold converts a score into a decision. Choose it using costs and constraints: false-positive review burden, missed fraud, fairness, and available human capacity. A threshold of 0.5 is not automatically correct.

## Feedback loops and experiments

Showing an item changes the chance of observing a click. Training only on observed clicks inherits the previous system's exposure bias. Similarly, reviewing only high-risk transactions changes which labels become available. Account for selection effects when interpreting data.

Use controlled online experiments when appropriate, with guardrails for harm, latency, and business outcomes. Offline gains may not transfer. Track long-term outcomes rather than only engagement proxies.

## Practice and answer

**Question:** 99% of transactions are legitimate. A model says every transaction is legitimate and reaches 99% accuracy. Is it useful for detecting fraud?

**Answer:** it has zero fraud recall. Evaluate the rare class, false-positive burden, missed-loss cost, and operational threshold. Compare against simple rules before adding complexity.

Next: [FDE discovery and delivery](26-fde-discovery-and-delivery.md) · [Index](../INDEX.md)
