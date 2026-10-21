# Security notes and reporting

The bundled labs are offline educational examples using synthetic data. They are not hardened services, real identity systems, or complete provider integrations. Read each lab's stated boundaries before adapting it.

Never put API keys, patient/customer records, private documents, environment files, or sensitive traces into an issue or pull request. If a secret is exposed, revoke/rotate it through the appropriate service; deleting a visible line does not remove it from Git history.

For a sensitive vulnerability, use GitHub's private vulnerability reporting if enabled, or an established private maintainer channel. If neither is available, open a minimal issue requesting a private reporting channel without disclosing exploitable details or personal data. Do not claim a private reporting feature is enabled unless you can see it.

For ordinary reproducible lab bugs, use a synthetic minimal example with interpreter version, command, expected behavior, and actual safe error output.
