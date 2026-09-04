# Operation Hydra – Multi-Vector Cyber Crime Investigation

Academic project for **Assignment 2 – Unit 2: Types of Cyber Crimes**.

## Safety
All data is synthetic. IP addresses use documentation ranges (RFC 5737), domains use `.example`, and no credentials, real financial identifiers, real malware, or operational attack infrastructure are included.

## Repository
- `docs/Operation_Hydra_Final_Report.docx` – editable final report
- `docs/Operation_Hydra_Final_Report.pdf` – PDF submission
- `docs/TOOL_COMMANDS.md` – tools, commands and justifications
- `data/phishing_headers.txt` – four simulated email headers
- `data/transactions.csv` – dummy financial flow
- `data/iocs.csv` – simulated IOCs
- `malware_simulation/` – harmless attachment and analysis script
- `scripts/` – safe parsing and tracing scripts
- `.github/workflows/ci.yml` – GitHub Actions checks
- `screenshots/` – add screenshots of your own local runs if required

## Run locally
```bash
python scripts/ip_header_parser.py
python scripts/transaction_trace.py
python malware_simulation/malware_analysis.py
```

## Authorship Declaration
I declare that this repository is an academic simulation prepared for educational purposes and that all incident artifacts are synthetic.
