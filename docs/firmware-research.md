# BMS firmware research

## Evidence categories
- **Source-reported:** Direct account from an experienced practitioner; not independently replicated here.
- **Inferred:** Working hypothesis that needs evidence.
- **Project-tested:** Reproduced with documented setup and results. **None yet.**

## Source-reported findings (BennVenn / SafetyUggs)
Based on technical discussion relayed to the project, not an independently verified teardown:

1. The ZE1 BMS contains a **main MCU** and **SUB/safety MCU**.
2. The main MCU sends most battery status messages. The SUB MCU reportedly emits a cyclic safety-OK message about every 10 ms and also receives vehicle CAN data.
3. The two controllers compare measurements/results; mismatches can trigger shutdown.
4. Adapting ZE1 firmware to AZE0 vehicle expectations may involve **both** MCUs.
5. ZE1 40 kWh and 62 kWh BMSs reportedly share closely related hardware, but different bootloaders mean firmware images cannot be assumed cross-flashable.
6. Firmware analysis is preferred over interpreting isolated CAN captures, although captures remain useful to validate observed behavior.
7. AZE0 BMS firmware adapted to OEM 62 kWh cells reportedly exists as an established alternative.

**Unresolved:** Whether the available ZE1 extraction and reflash tooling supports both MCUs; the exact firmware versions, hardware variants, permission to redistribute images, and the complete safety implications.

## Research method
- Identify exact donor BMS part number, firmware version, and provenance.
- Use authorized firmware images and published analysis tools.
- Map receive/transmit handlers and state transitions with confidence labels.
- Compare against known AZE0 messages and corroborate with controlled captures.
- Test offline models first; seek independent qualified review before any HV bench/vehicle activity.
- Never bypass safety approvals, watchdogs, interlocks, or shutdowns.

## References
- [SafetyUggs — Leaf BMS Reverse Engineering](https://github.com/SafetyUggs/Leaf-BMS-Reverse-Engineering)
- [SafetyUggs — Nissan/Renault BMS/LBC/VCM KWP Reflash Tool](https://github.com/SafetyUggs/Nissan-Renault-BMS-LBC-VCM-KWP-Reflash-Tool)

**Important:** A diagnostic reflash tool is not automatically an MCU firmware extraction tool. Tool capabilities must be checked against documentation and hardware before making claims.
