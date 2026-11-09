#!/usr/bin/env python3
"""Offline index of C switch case labels; manual code review is still required."""
import argparse
import pathlib
import re

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", help="local C source file")
    args = p.parse_args()
    text = pathlib.Path(args.source).read_text(encoding="utf-8", errors="replace")
    for match in re.finditer(r"\bcase\s+(0x[0-9a-fA-F]+)\s*:", text):
        line = text.count("\n", 0, match.start()) + 1
        print(f"{match.group(1)} line {line}")

if __name__ == "__main__":
    main()
