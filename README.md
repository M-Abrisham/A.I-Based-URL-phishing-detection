# emlscope

> Phishing email triage for SOC analysts — parse an `.eml`, extract and enrich
> IOCs, produce an IR report.

**Status: pre-alpha.** Project skeleton only; features are being built
milestone-by-milestone. See [roadmap](#roadmap).

---

## What it does

You get a suspicious email. You save it as `.eml`. You run:

```bash
emlscope suspicious.eml --output report.md
```

emlscope:

1. **Parses** the raw MIME message.
2. **Analyzes headers** — Received chain, From/Return-Path/Reply-To mismatches.
3. **Verifies SPF / DKIM / DMARC** via DNS.
4. **Extracts IOCs** — URLs, IPs, domains, file hashes — and defangs them.
5. **Hashes attachments** — MD5 / SHA-1 / SHA-256.
6. **Enriches IOCs** through VirusTotal, AbuseIPDB, and AlienVault OTX.
7. **Scores risk** on a 0-100 scale.
8. **Maps to MITRE ATT&CK** (T1566 and subtechniques).
9. **Renders an IR report** in Markdown or JSON.

---

## Roadmap

| Milestone | Scope | Status |
|---|---|---|
| M0 | Project scaffolding | In progress |
| M1 | `.eml` parsing + IOC extraction | Planned |
| M2 | Header forensics + SPF/DKIM/DMARC | Planned |
| M3 | Threat-intel enrichment + attachment analysis | Planned |
| M4 | Risk scoring + MITRE mapping + report generation | Planned |
| M5 | CLI polish + README / samples | Planned |

---

## Setup

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup.
See [docs/api_setup.md](docs/api_setup.md) for threat-intel API keys.
See [docs/architecture.md](docs/architecture.md) for the pipeline design.

---

## License

[MIT](LICENSE)
