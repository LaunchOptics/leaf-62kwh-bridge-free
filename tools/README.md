# Offline research utilities

These are **read-only, standard-library Python scripts** for examining text logs and public source code. They do **not** connect to or transmit on a CAN bus, flash an ECU, or validate safety.

Expected CAN text format:
```text
12.345 battery 0x1DB 11AABBCCDDEEFF00
12.355 battery 0x1DB 11AABBCCDDEEFF01
```

Run:
```bash
python tools/can_inventory.py sample.log
python tools/compare_ids.py recipient.log donor.log
python tools/scan_bridge_cases.py path/to/can-bridge-firmware.c
```

Compare logs captured in equivalent states. A shared ID or cadence does not establish identical signal meaning. Record model year, ECU firmware, capture point, and source revision. Never upload private vehicle data without consent.
