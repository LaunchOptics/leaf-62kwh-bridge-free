#!/usr/bin/env python3
"""Offline comparison of CAN IDs from two text logs. No CAN interface."""
import argparse

def inventory(path):
    ids = set()
    with open(path, encoding="utf-8") as stream:
        for line in stream:
            parts = line.split()
            if len(parts) != 4 or line.lstrip().startswith("#"):
                continue
            try:
                ids.add((parts[1], int(parts[2], 0)))
            except ValueError:
                pass
    return ids

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("recipient")
    p.add_argument("donor")
    args = p.parse_args()
    old, new = inventory(args.recipient), inventory(args.donor)
    for label, group in (("recipient only", old - new),
                         ("donor only", new - old), ("shared IDs", old & new)):
        print(f"\n{label}:")
        for bus, can_id in sorted(group):
            print(f"  {bus} {can_id:#x}")

if __name__ == "__main__":
    main()
