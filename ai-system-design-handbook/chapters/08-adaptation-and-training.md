# 08 · RAG, fine-tuning, and model adaptation

**Prerequisites:** Chapters 5–7. **Goal:** distinguish giving a model information from changing its learned behavior.

## Four different levers

Prompting changes the instructions and examples in the request. Retrieval-augmented generation, or RAG, fetches evidence at request time. Fine-tuning changes model weights using additional training. Distillation trains a student using signals from a teacher or another learning process. These can be combined; they solve different problems.

**Everyday intuition:** a reference book gives a person fresh information; practice changes how the person performs a task. RAG is closer to the reference book. Fine-tuning is closer to practice.

| Need | First approach to test | Why |
|---|---|---|
| Current internal policies with citations | RAG | Documents can change without retraining |
| Consistent specialized output behavior | Prompting, then fine-tuning if needed | Behavior may benefit from many high-quality examples |
| Exact arithmetic or business constraints | Deterministic tools | Weights are not a reliable transaction ledger |
| Smaller model for a well-defined task | Distillation/fine-tuning | A narrow task may transfer to a cheaper student |
| Missing evidence or unclear requirements | Improve data/task definition | Training does not create a trustworthy ground truth |

## The minimum training vocabulary

A training set teaches the model. A validation set supports choices such as hyperparameters and stopping. A test set estimates performance after those choices are complete. Leakage occurs when evaluation information influences learning or appears in the training data, including near-duplicates.

Overfitting means performing well on familiar examples while generalizing poorly. Split by the real source of dependence: customer, document family, time period, or author when appropriate. Random row splitting can hide leakage if multiple rows come from the same document.

## SFT, LoRA, and preference methods

Supervised fine-tuning uses example inputs and desired outputs. Full fine-tuning updates the model's parameters broadly. LoRA learns smaller low-rank updates to selected weights, reducing trainable parameter count and often training memory needs. QLoRA combines quantized base weights with adapter training. Exact memory savings and supported deployment paths depend on the implementation.

Preference optimization uses information about preferred outputs to shape behavior. RLHF commonly includes human preference data and reinforcement learning stages; DPO is a different optimization approach using preference pairs. Neither name guarantees factuality, safety, or good performance on your workload.

## A responsible adaptation experiment

Start with a strong prompt baseline and an error taxonomy. Ask which errors training could fix. Curate examples, remove duplicates, verify permissions, and keep evaluation separate. Train a small candidate. Compare it with the baseline on quality, critical slices, latency, serving cost, and regression cases. Publish an experiment record even if training loses.

For synthetic data, validate samples rather than assuming a stronger teacher is always right. Repeating its mistakes thousands of times amplifies those mistakes. If teachers generate evaluation labels too, use independent human checks to avoid circular scoring.

## Worked example

A support assistant cites correct policies but writes inconsistent response formats. Improve the prompt and schema first. If formatting failures persist across many examples, adaptation may help. If the assistant cannot find this week's policy, fixing retrieval and freshness is the more direct intervention.

## Practice and answer

**Question:** Can fine-tuning replace authorization-filtered retrieval?

**Answer:** no. Weights do not provide a reliable per-request permission check or a current document access boundary. Keep identity, policy, and evidence access in application infrastructure regardless of adaptation.

Further reading: [LoRA paper](https://arxiv.org/abs/2106.09685), [QLoRA paper](https://arxiv.org/abs/2305.14314), [DPO paper](https://arxiv.org/abs/2305.18290).

Next: [Serving and inference](09-serving-and-inference.md) · [Index](../INDEX.md)
