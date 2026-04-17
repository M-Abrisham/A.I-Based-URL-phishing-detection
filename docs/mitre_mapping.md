# MITRE ATT&CK mapping

emlscope tags findings with MITRE ATT&CK techniques so reports plug into
existing SOC playbooks.

## Techniques covered

| Technique | Name | Trigger in emlscope |
|---|---|---|
| T1566 | Phishing | Default tag for any suspicious email |
| T1566.001 | Spearphishing Attachment | Email carries an attachment |
| T1566.002 | Spearphishing Link | Suspicious URL in body |
| T1566.003 | Spearphishing via Service | Sender from webmail + spoof signals |
| T1598 | Phishing for Information | Body asks for credentials/PII |
| T1204.001 | User Execution: Malicious Link | High-confidence malicious URL |
| T1204.002 | User Execution: Malicious File | Attachment with known-bad hash |

## Mapping logic

The mapping is implemented in `src/emlscope/mitre/mapper.py`. Each analyzer
contributes tags based on what it finds; the mapper de-duplicates and returns
the final list of techniques for the report.
