# Firmware tooling: capability and limitations

This page distinguishes **read/extraction**, **reflash/write**, **calibration editing**, and **reset/diagnostics**. These are different capabilities.

| Resource | Publicly described function | Important limitation |
|---|---|---|
| [SafetyUggs BMS Reverse Engineering](https://github.com/SafetyUggs/Leaf-BMS-Reverse-Engineering) | Disassembly notes and firmware-specific ECUFlash XML definitions | XML does not imply a complete firmware dump or universal compatibility |
| [Nissan/Renault KWP Reflash Tool](https://github.com/SafetyUggs/Nissan-Renault-BMS-LBC-VCM-KWP-Reflash-Tool) | J2534/KWP BMS/LBC reflashing, some VCM operations, resets | Tested functions differ by ECU generation; **not automatically a protected-MCU extraction tool** |
| [Renesas V850 Fault Injection Tool](https://github.com/SafetyUggs/Renesas-V850-Fault-Injection-Tool) | Extraction of read-protected Renesas V850 firmware through fault injection | Risk of permanent erase/damage; **no off-vehicle execution instructions reproduced here** |
| [Dala battery-upgrade firmware](https://github.com/dalathegreat/Nissan-LEAF-Battery-Upgrade) | Public bridge firmware for cross-generation CAN adaptation | A bridge implementation, not a ZE1 BMS firmware patch |

## Evidence from the available tool README snapshots
- The KWP reflash README describes ZE0/AZE0 KWP flashing tests and some ZE1 reset support. That **does not establish** full ZE1 Plus main+SUB MCU flashing.
- The Renesas V850 fault-injection README describes extracting read-protected MCU firmware and explicitly warns that fault injection can trigger unintended erase or corruption.
- BennVenn separately reported having developed and tested ZE1 BMS extraction tooling. **Still unresolved:** whether both the main and SUB MCU can be dumped and safely reflashed with modified images.

## Bootloaders and variants
BennVenn reported ZE1 40 kWh and 62 kWh BMS hardware similarity but **different bootloaders**. Do not attempt cross-flashing based on board similarity.

## Safe research boundary
Analyze public source, documentation, and authorized images offline. Do not attempt fault injection or firmware modification on a connected HV battery. No tool here is endorsed as safe for a specific ECU; bench experiments require qualified personnel, spare hardware, recovery plans, and independent safety review.
