#!/usr/bin/env python3
"""Trace the dummy transaction graph."""
import csv, collections
edges=[]
with open("data/transactions.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        edges.append((r["from_id"],r["to_id"],r["amount"],r["timestamp"],r["transaction_id"]))
g=collections.defaultdict(list)
for a,b,amt,ts,tx in edges: g[a].append((b,amt,ts,tx))
for a in sorted(g):
    for b,amt,ts,tx in g[a]:
        print(f"{tx}: {a} -> {b} | {amt} | {ts}")
print("\nNo banking, UPI, card, blockchain or external API is accessed.")
