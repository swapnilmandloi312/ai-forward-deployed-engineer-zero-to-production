# 05 · Tokens, attention, and transformers

**Prerequisites:** Chapters 1–2. **Goal:** connect model internals to practical limits.

## Tokens are the model's units of text

A tokenizer converts text into IDs from a vocabulary. A token may represent a word, part of a word, punctuation, or another sequence. There is no universal conversion from words or characters to tokens: the tokenizer, language, formatting, and content all matter. Count with the selected model's tokenizer or provider tooling when estimating real requests.

**Everyday intuition:** a tokenizer cuts a message into reusable pieces, somewhat like building a word from letter tiles. The pieces are not the same across every game.

The input context includes more than the user's question. System instructions, tool definitions, conversation history, retrieved passages, and sometimes provider-specific internal representations consume the available budget. Leave room for the output and any model-specific reasoning allowance.

## What attention does

An embedding maps each token ID to numbers. Position information helps represent order. Attention computes how information at different positions should influence the representation at a given position. In simplified notation:

`Attention(Q, K, V) = softmax(QKᵀ / sqrt(d_k)) V`

Queries and keys determine weights; values provide information combined using those weights. Multiple attention heads learn different relationships. Feed-forward layers transform the resulting representations. Repeating these blocks creates a transformer.

You do not need to implement this formula to ship an API application, but you should understand that attention is a numerical operation, not a guarantee that a model correctly understands the user's intent.

## Training and inference

In a common causal language-model setup, training adjusts weights to improve prediction of subsequent tokens. At inference time, a decoder model processes the prompt and generates tokens step by step. Pretraining creates broad capability; later adaptation can shape instruction following or task behavior. Training objectives and architectures differ across models.

During **prefill**, the model processes the supplied context. During **decode**, it produces new tokens. A key-value cache stores intermediate attention information so previous positions need not be recomputed in the same way for every new token. Larger context and more concurrent sequences consume more cache memory.

## Why this changes architecture

| Model behavior | System consequence |
|---|---|
| Output is usually generated sequentially | Long answers can increase waiting time substantially |
| Context is finite | History, tools, and evidence need explicit budgets |
| Long inputs consume compute and memory | “Send every document” may be slow and expensive |
| Learned associations can be wrong | Fluent answers still need external evaluation |
| Tokenization varies | A language-specific workload may cost more than a rough English estimate |

Streaming can improve the time before users see content. It does not reduce all underlying work, and partial content must not be mistaken for a validated final result.

## Worked example

Suppose the allowed request budget is 16,000 tokens. Instructions use 1,500, tools use 2,000, history uses 3,000, and you reserve 2,500 for output. At most 7,000 remain for evidence and any other input overhead. Rather than truncating randomly, rank evidence, remove duplicates, preserve essential source metadata, and reject or summarize excess history under a documented policy.

This arithmetic is illustrative; the exact context accounting and maximum output constraints depend on the model API.

## Practice and answer

**Question:** Why can a short question have a high input cost?

**Answer:** the question may be accompanied by thousands of tokens of instructions, retrieved text, tool schemas, and conversation history. Measure the complete serialized request and provider usage, not just the visible question.

Further reading: [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

Next: [Model selection](06-model-selection.md) · [Index](../INDEX.md)
