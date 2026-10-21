# 24 · Voice, images, and multimodal systems

**Prerequisites:** Chapters 5, 18, and 20. **Goal:** identify what changes when the interface is not just text.

## More modalities mean more stages to evaluate

A text system may receive clean strings. A voice system receives audio with accents, interruptions, silence, and noise. A document system may receive scans, diagrams, and handwritten notes. Errors in perception become errors in downstream reasoning.

**Everyday intuition:** a correct answer to a misheard question is still an unsuccessful conversation.

## Two voice architectures

In a cascade, speech recognition converts audio to text, a language system decides what to say or do, and speech synthesis creates audio. This makes transcripts and component debugging straightforward, while adding boundaries and accumulated latency. A speech-to-speech system can handle audio more directly, but still needs measurable behavior, tool controls, and a reviewable event record.

Evaluate the complete conversation rather than picking stages solely from isolated benchmarks. A transcription model with good average accuracy may still misrecognize account numbers or names that matter to your task.

## Turn-taking and interruptions

Voice activity detection estimates when speech is present. Endpointing decides when a turn has ended. Barge-in lets a user interrupt generated speech. The system must cancel or stop playback appropriately without losing durable business state.

An interrupted sentence is not evidence that an action was canceled. If a booking API already succeeded, the application needs to explain or reconcile that state. Keep action execution separate from audio playback.

| Concern | Measurement or control |
|---|---|
| Perceived delay | End-of-turn to first useful audio |
| Misrecognition | Task-specific word/entity errors |
| Tool safety | Verified identity and explicit action policy |
| Audio quality | Noise, device, language, accent slices |
| Conversation quality | Successful completion and correction rate |
| Cost | Cost per minute and accepted task |

## Images and document vision

For a chart or invoice image, evaluate reading order, units, small text, table relationships, and source regions. Preserve the original page and coordinates for review. A model describing an image confidently does not establish accurate extraction.

Use OCR and layout tools where useful, then compare them against a vision model on representative sources. Include rotated pages, blurred scans, dense tables, and missing pages. A pipeline may combine deterministic image preprocessing, OCR, vision, and human review.

## Generative media

Image/audio/video generation adds asset lifecycle concerns: permitted source material, identity/voice rights, review, provenance, and delivery format. Store versioned prompts and references under appropriate access controls. Keep quality evaluation separate from factual or policy validation.

This handbook's labs do not synthesize voices or media. Their offline design keeps setup small; production modality-specific SDKs require current provider documentation and an explicit evaluation dataset.

## Practice and answer

**Question:** transcription error rate improves, but booking success drops. What might explain it?

**Answer:** the errors that remain may affect crucial entities, endpointing may cut off corrections, interruption handling may be broken, or tool state may diverge from spoken confirmation. Inspect full task traces and slice by critical names/numbers rather than relying on one audio metric.

Next: [Classical ML systems](25-ml-recommendations-and-ranking.md) · [Index](../INDEX.md)
