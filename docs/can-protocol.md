# CAN protocol and BMS–VCM interaction

**This is a conceptual research note, not a verified message table, control sequence, or safety procedure.**

## Why transmit-only translation is insufficient
The BMS may depend on **incoming** VCM and other ECU messages before producing the expected outgoing data. A correct-looking SOC/voltage message by itself does not demonstrate operational compatibility.

## Contactor interaction (conceptual)
An experienced practitioner described a sequence in which:
1. The VCM requests whether the contactors may safely close.
2. The BMS evaluates conditions and replies with permission or denial.
3. The VCM acts on that permission and sends contactor state information back to the BMS.

Actual message IDs, counters, timing, ownership of physical contactors, and failure behavior **have not been validated by this project**. These details must be confirmed against the specific hardware and firmware versions. No system should ever be modified to fabricate a safety approval.

## Investigation checklist
- Incoming CAN IDs, message sources, and required freshness
- Outgoing BMS messages, data layout, counters, and checksums
- Main-MCU versus SUB-MCU ownership of messages
- Startup, ready, drive, charge, shutdown, and fault states
- Timeouts, mismatches, negative permissions, and safe-failure behavior
- Dependencies on PDM, ABS, airbag, instrument cluster, and other ECUs
- Differences between AZE0 and ZE1 model years/firmware versions

## References
- [Dala — Leaf CAN bus messages](https://github.com/dalathegreat/leaf_can_bus_messages)
- [Dala — Nissan LEAF Battery Upgrade](https://github.com/dalathegreat/Nissan-LEAF-Battery-Upgrade)

Do not assume a public CAN identifier or interpretation applies to every model year. Cite capture conditions and firmware versions when contributing new definitions.
