# Test fixtures

Hand-crafted `.eml` files used by the test suite. These are **not** real phishing
samples — they're synthetic emails built to exercise specific code paths.

Planned fixtures (added alongside the PRs that need them):

- `clean.eml` — benign email; auth passes, no IOCs flagged.
- `phishing_basic.eml` — obvious phishing body, suspicious URLs.
- `spoofed_sender.eml` — From / Return-Path / Reply-To mismatch.
- `with_attachment.eml` — carries an attachment for the hasher module.
- `dkim_fail.eml` — fails DKIM verification.
