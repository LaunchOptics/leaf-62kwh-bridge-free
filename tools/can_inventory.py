#!/usr/bin/env python3
"""Offline inventory of text CAN logs; no CAN interface or transmit capability.

Input format (whitespace separated):
    timestamp_seconds bus 0xID HEXBYTES
Example:
    12.345 battery 0x1DB 11AABBCCDDEEFF00
"""
import argparse
import collections
import statistics

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("log", help="local text log file")
    args = p.parse_args()
    records = collections.defaultdict(list)
    malformed = 0
    with open(args.log, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 4:
                malformed += 1
                continue
            ts, bus, can_id, payload = parts
            try:
                t = float(ts)
                i = int(can_id, 0)
                raw = bytes.fromhex(payload)
                if not 0 <= i <= 0x1FFFFFFF:
                    raise ValueError("invalid CAN ID")
            except ValueError:
                malformed += 1
                continue
            records[(bus, i)].append((t, len(raw)))
    print("bus,can_id,count,dlc_values,median_period_ms")
    for (bus, can_id), rows in sorted(records.items()):
        timestamps = sorted(t for t, _ in rows)
        deltas = [b - a for a, b in zip(timestamps, timestamps[1:])]
        period = f"{statistics.median(deltas) * 1000:.2f}" if deltas else ""
        dlcs = "|".join(map(str, sorted({n for _, n in rows})))
        print(f"{bus},{can_id:#x},{len(rows)},{dlcs},{period}")
    if malformed:
        print(f"# skipped malformed lines: {malformed}")

if __name__ == "__main__":
    main()
