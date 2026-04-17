# API key setup

emlscope's enrichment module uses three free threat-intel APIs. You only need
the keys if you want IOC enrichment — parsing, IOC extraction, header analysis,
and SPF/DKIM/DMARC all work offline.

## VirusTotal

1. Register at https://www.virustotal.com/gui/join-us
2. Get your key at https://www.virustotal.com/gui/my-apikey
3. Free tier: 500 requests/day, 4 requests/minute.

Put the key in `.env` as `VT_API_KEY=...`.

## AbuseIPDB

1. Register at https://www.abuseipdb.com/register
2. Generate a key at https://www.abuseipdb.com/account/api
3. Free tier: 1000 checks/day.

Put the key in `.env` as `ABUSEIPDB_API_KEY=...`.

## AlienVault OTX

1. Register at https://otx.alienvault.com/
2. Get your key from your account settings.
3. Free tier, no hard rate limit (be reasonable).

Put the key in `.env` as `OTX_API_KEY=...`.

## Running without keys

```bash
emlscope suspicious.eml --no-enrich
```

You still get parsing, header forensics, SPF/DKIM/DMARC, IOC extraction, and
attachment hashes — just no TI reputation data.
