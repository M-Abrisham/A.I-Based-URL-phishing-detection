# Architecture

## Overview

emlscope takes a suspicious `.eml` file and runs it through a staged pipeline,
producing an IR report. Each stage is a standalone module so it can be tested
(and reused) independently.

```
.eml file
   │
   ▼
┌───────────────┐
│  parser.py    │  parse raw MIME → structured email object
└───────┬───────┘
        │
        ├──► headers/analyzer.py   (Received chain, spoof detection)
        ├──► headers/auth.py       (SPF / DKIM / DMARC)
        ├──► iocs/extractor.py     (URLs, IPs, domains, hashes)
        │        │
        │        └──► iocs/defanger.py    (hxxps://evil[.]com)
        │
        ├──► attachments/hasher.py    (MD5 / SHA-1 / SHA-256)
        ├──► attachments/filetype.py  (magic-byte detection)
        │
        └──► enrichment/              (TI lookups on extracted IOCs)
                 ├─ virustotal.py
                 ├─ abuseipdb.py
                 ├─ otx.py
                 └─ cache.py          (JSON cache, respects API quotas)
        │
        ▼
┌──────────────────┐
│  scoring/risk.py │  combine signals → 0-100 risk score
└────────┬─────────┘
         │
         ▼
┌───────────────────┐
│  mitre/mapper.py  │  findings → ATT&CK TTPs (T1566.*)
└────────┬──────────┘
         │
         ▼
┌────────────────────────┐
│  report/generator.py   │  Jinja2-rendered Markdown or JSON report
└────────────────────────┘
```

## Design principles

1. **Offline by default.** Parsing, IOC extraction, header analysis, and DKIM
   work without any API keys. Enrichment is opt-in.
2. **Enrichers are pluggable.** `enrichment/base.py` defines an `Enricher`
   interface; adding a new TI source (URLhaus, ThreatFox, MISP) is a new file.
3. **Defang on output.** Every IOC that appears in a report is defanged so
   reports are safe to share in Slack/email/tickets.
4. **Cache API responses.** Quotas are real. The cache lives on disk as JSON
   keyed by IOC, with configurable TTL.
5. **Speak the shared vocabulary.** Findings map to MITRE ATT&CK so reports
   fit into existing SOC playbooks.

## Output formats

- **Markdown** — human-readable IR report, safe to paste into tickets.
- **JSON** — structured findings for downstream tooling (SIEM ingest, SOAR).
