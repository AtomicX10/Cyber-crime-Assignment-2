# Tool Commands & Justification

## Local safe analysis
```bash
python scripts/ip_header_parser.py
python scripts/transaction_trace.py
python malware_simulation/malware_analysis.py
```

## Optional tools for a real authorized investigation
- MXToolbox — mail/DNS authentication checks.
- VirusTotal — authorized hash/URL reputation checking.
- AbuseIPDB — IP reputation context.
- WHOIS/RDAP — domain registration context.

No external target is queried by this repository.
