#!/usr/bin/env python3
"""Parse only the synthetic Operation Hydra headers; makes no network requests."""
import re
from pathlib import Path
text = Path("data/phishing_headers.txt").read_text(encoding="utf-8")
ips = sorted(set(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)))
domains = sorted(set(re.findall(r"\b[a-zA-Z0-9.-]+\.example\b", text)))
print("Simulated IPs:")
for x in ips: print(" -", x)
print("\nSimulated example domains:")
for x in domains: print(" -", x)
