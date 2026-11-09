# Research log and evolving conclusions

## Initial phase — literature and code review
- Defined target: AZE0 (2013–2017) recipient, OEM ZE1 Plus 62 kWh donor pack.
- Compared five architectures A–E.
- Studied Dala's public bridge code as the strongest concrete map of protocol differences.
- Produced preliminary research PDFs; they are **snapshots** and may not reflect newer findings.
- No project-owned vehicle, pack, firmware extraction, or measurement data.

## Early practitioner discussion
- Explored Path B current-sensor/harness differences and SOC/IR calibration requirements.
- Clarified that a VIVNE demonstration of older-BMS reflashing with upgraded cells is **not** proof of an intact OEM ZE1 Plus pack conversion.
- Identified version-specific SafetyUggs XML definitions and J2534 reflashing research.

## November 2026 — BennVenn discussion (paraphrased)
- **Path B status revised:** BennVenn reported that AZE0 BMS firmware adapted to OEM 62 kWh Nissan cells is already used in practice and commercially available. The project has not validated a particular implementation.
- **Path A complexity clarified:** ZE1 BMS reportedly uses a main MCU and SUB/safety MCU, with cross-checking and a cyclic safety signal; both may require modifications.
- **Bidirectional CAN requirement:** BMS needs incoming VCM/ECU traffic; a contactor-permission and state-feedback handshake must be understood, not just outgoing telemetry.
- **Firmware-first approach:** Firmware analysis was recommended over interpreting isolated CAN logs; captures remain necessary for validation.
- **Firmware access open question:** BennVenn reported testing ZE1 extraction tools, but the project has not confirmed both-MCU dump/reflash support.
- **Bootloader caveat:** 40 kWh and 62 kWh ZE1 BMSs reportedly have different bootloaders, despite similar hardware.

## Public feedback — November 2026
MyNissanLeaf contributors **ginetto** and **ukoda** encouraged moving the research into a public GitHub repository, improving discoverability and making community contributions more durable. This repository was created in response.

## What has NOT happened
No car or pack purchased; no original project CAN logs; no firmware images independently analyzed; no BMS or VCM patched; no contactor or charge behavior tested; no physical conversion demonstrated.

Future log entries should include date, source, exact revision, evidence, what changed, and what remains unknown.


## November 2026 — direct follow-up: both ZE1 MCUs (BennVenn, practitioner report)

In response to the project's explicit question whether ZE1 extraction tooling can dump both main and SUB MCU firmware and whether modified firmware can be reflashed, BennVenn replied:

> "yes, it can extract both. modified firmware, if checksums are correct and the code is working can be flashed over can."

**Change from earlier uncertainty:** Both-MCU extraction is now **explicitly practitioner-confirmed**. Modified firmware reflashing over CAN is also reported as possible, conditional on correct checksums and functioning code. The statement does **not** specify exact hardware/firmware variants, flashing procedure, recovery guarantees, or whether both MCU images can independently be reflashed in every target configuration. No project-owned validation has occurred.

### Separate ZE1 capacity-reprogramming exchange (other Discord participant)

BennVenn answered that reprogramming a ZE1 40 kWh LBC/BMS for a larger 62–64 kWh pack is possible and asked for the replacement cells' discharge-curve data. He stated that firmware is locked to the individual BMS and not transferable as a shared image. He suggested a GODIAG GD101 J2534 interface; later clarified that other J2534 interfaces may work but require user debugging, and distinguished the correct reflash application from another app.

**Scope limitation:** This exchange concerns ZE1 BMS capacity adaptation, not ZE1 BMS ↔ AZE0 VCM interoperability. The firmware-lock statement may describe BennVenn's delivered reflash files; it should not be generalized to all Nissan firmware without further evidence.
