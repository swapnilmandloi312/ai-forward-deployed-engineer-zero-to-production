# 23 · Token costs, capacity, and business value

**Prerequisites:** Chapters 3, 6, and 18. **Goal:** calculate the cost of a useful outcome.

## Start with units

For a simple request, model cost is:

`input_tokens × input_price_per_million / 1,000,000 + output_tokens × output_price_per_million / 1,000,000`

Actual bills may distinguish cached input, cache writes, reasoning usage, audio, images, batches, storage, tools, or long-context tiers. Use the provider's current pricing and observed usage for the actual model. This handbook uses fictional rates to teach arithmetic rather than publish an expiring price table.

**Everyday intuition:** a cheap ingredient does not guarantee a cheap finished meal if preparation, waste, and corrections are expensive.

## Worked model-cost example

Assume 10,000 requests/day, 2,000 input tokens, 400 output tokens, and fictional prices of $2/input-million and $8/output-million. Per request: `$0.004 + $0.0032 = $0.0072`. Daily base model cost: `$72`. For 30 identical days: `$2,160`.

This excludes retries, embeddings, reranking, hosting, monitoring, storage, network, and human review. If an average retry repeats a complete request, expected attempts scale cost; retries that occur before billable work have a different effect. Measure real usage rather than assuming every error costs zero or a full request.

## Cost per accepted task

Let total period cost include model calls, infrastructure, operations, and review. Divide by the number of tasks accepted under the agreed quality standard. A cheaper model with more corrections can increase this metric.

Track per tenant and task type. One long-document customer can dominate spend while ordinary chat looks inexpensive. Apply budgets to maximum input/output sizes, agent steps, retries, concurrency, and total spend. Use alerts before and enforcement at the budget boundary.

## An honest ROI example

Assume 1,000 tasks/month. Manual work takes ten minutes each; assisted work including review takes four. Potential capacity released is `1,000 × 6 / 60 = 100 hours/month`. At an assumed fully loaded $20/hour, the illustrative capacity value is $2,000/month.

If the system costs $700/month, the modeled net benefit is $1,300/month before implementation and other effects. This is **not** automatically $1,300 in cash savings. The organization must redeploy the released capacity or reduce actual expense. Include error costs, adoption, process changes, and maintenance.

## Optimize in the right order

Remove unnecessary calls and oversized context. Reduce repeated failures. Use deterministic calculations. Test smaller models or specialized routing. Consider batching for delay-tolerant tasks. Evaluate caching with freshness and access requirements. Compare self-hosting only with realistic utilization and operating effort.

Do not optimize only token prices while ignoring the reviewer queue. A small increase in model spend may be worthwhile if it reduces correction time without harming critical behavior.

## Practice and answer

**Question:** an automation releases 100 hours/month but nobody changes staffing or output. Can you claim $2,000 in realized savings?

**Answer:** report estimated capacity released, then separately measure how that capacity was used. Distinguish modeled value, realized productivity, revenue impact, and actual expense reduction.

Build: [capacity and cost calculator](../labs/README.md). Template: [ROI worksheet](../templates/roi-worksheet.md).

Next: [Voice and multimodal systems](24-voice-and-multimodal.md) · [Index](../INDEX.md)
