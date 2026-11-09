# Bridge-Free Nissan LEAF 62 kWh Battery Conversion

**Status: Preliminary research / fundraising — no conversion has been built or validated.**

A student-led, open-source investigation into installing a complete OEM Nissan LEAF Plus (ZE1) **62 kWh battery pack** in a **2013–2017 Nissan LEAF (AZE0)**, while investigating approaches that do **not require a permanently installed external CAN translation bridge**.

This repository is intended to be the central, publicly accessible record of the project: research, sources, unresolved questions, test plans, and eventual results, including setbacks.

> **Safety:** EV battery packs contain potentially lethal high voltage. This repository is not a conversion guide, and no design or firmware described here is validated for use in a vehicle. Never defeat isolation monitoring, contactor interlocks, fault shutdowns, or BMS safety logic. Physical HV work requires suitable equipment and qualified supervision.

## Objectives

- Investigate whether the original **ZE1 Plus BMS** can be adapted to communicate directly with AZE0 vehicle systems.
- Document the established alternative of using an **AZE0 BMS** with OEM 62 kWh cells, including the necessary firmware, sensor, wiring, and safety considerations.
- Compare both approaches with the established **CAN bridge** option.
- Publish sources, findings, limitations, and validation evidence openly.

## Approaches under consideration

| Path | Concept | Research status |
| --- | --- | --- |
| **A — ZE1 BMS firmware adaptation** | Retain OEM 62 kWh pack and ZE1 BMS; adapt its incoming and outgoing vehicle CAN behavior to AZE0 expectations | **Unproven**; primary reverse-engineering research focus |
| **B — AZE0 BMS adaptation** | Use a suitably adapted older AZE0 BMS with OEM 62 kWh cells, sensors, and wiring | **Reported as established by experienced practitioners**; no project-specific validation |
| **C — CAN bridge** | Retain ZE1 BMS and use an external translator between generations | Existing open-source reference / practical fallback |
| **D — ZE1 VCM transplant** | Adapt a newer vehicle control module to the older car | Not prioritized; broad cross-ECU compatibility concerns |
| **E — AZE0 VCM firmware modification** | Adapt older VCM firmware to the ZE1 BMS | Not prioritized; high safety-critical scope |

See [research approaches](docs/approaches.md) and [CAN protocol questions](docs/can-protocol.md).

## Key research findings so far

These are **preliminary notes**, not conclusions verified by our own firmware extraction or physical testing:

- Experienced BMS reverse engineer **BennVenn / SafetyUggs** reports that AZE0 BMS firmware adapted for OEM Nissan 62 kWh cells is already available and used in practice (Path B). Specific physical installation and safety requirements remain to be established.
- BennVenn reports the ZE1 BMS has a **main MCU and a SUB/safety MCU** with coordinated safety checks. Path A may require analyzing and modifying **both** firmwares.
- Path A requires **two-way CAN compatibility**. The BMS does not merely transmit SOC and voltage; incoming VCM messages and a contactor-permission/state handshake are also important.
- BennVenn reports the ZE1 40 kWh and 62 kWh BMS hardware is closely related, but their different bootloaders prevent assuming firmware images are interchangeable.
- No ZE1 Plus firmware dump has been independently examined in this project.

See [firmware research](docs/firmware-research.md) for attribution and open questions.

## Project status

- [x] Initial architecture and alternative approaches documented
- [x] Public repository established
- [ ] Confirm exact donor-pack and BMS part numbers
- [ ] Obtain authorized firmware images / public definitions for analysis
- [ ] Document message-level compatibility from verified evidence
- [ ] Develop offline protocol/state-machine tests
- [ ] Obtain project hardware and qualified HV supervision
- [ ] Bench validation, fault-injection-safe test planning, and vehicle integration (future, conditional on safety review)

**No vehicles or donor pack have been purchased.** The project is currently fundraising. The $7,000 target is a fundraising goal, not a validated engineering cost estimate.

## Detailed research archive

The original research PDFs were reviewed and their major technical findings organized into versioned, searchable notes below. These pages include newer November 2026 practitioner reports not present in the older PDFs.

| Topic | Research document |
|---|---|
| Conversion alternatives | [Five paths](docs/approaches.md) |
| Detailed candidate CAN IDs | [CAN dependency matrix](docs/can-message-matrix.md) |
| BMS ↔ VCM state/handshake | [CAN protocol research](docs/can-protocol.md) |
| Diagnostic request/response leads | [Diagnostic CAN](docs/diagnostics.md) |
| Dual MCUs and firmware questions | [Firmware research](docs/firmware-research.md) |
| Read vs write vs extraction tooling | [Firmware tools](docs/firmware-tools.md) |
| SOC/IR tables and sensor calibration | [Calibration research](docs/calibration-research.md) |
| Connectors, current sensors, mounts | [Hardware integration](docs/hardware-integration.md) |
| Fault behavior and validation gates | [Safety and validation](docs/safety-validation.md) |
| Chronology and changing conclusions | [Research log](docs/research-log.md) |
| Fundraising and actual project stage | [Funding and status](docs/funding-and-status.md) |
| Offline source/log scripts | [Research tools](tools/README.md) |
| Sources and acknowledgments | [References](docs/sources.md) |

**Provenance note:** Several findings derive from prior project PDF research and public-code reviews; they are not new hardware measurements. Source-specific branch and commit auditing remains on the roadmap. The PDF link below is an earlier research snapshot, not a source of current test results.

## Documentation

- [Research approaches](docs/approaches.md)
- [Firmware research](docs/firmware-research.md)
- [CAN and contactor handshake research](docs/can-protocol.md)
- [Roadmap and validation gates](ROADMAP.md)
- [Sources and acknowledgments](docs/sources.md)
- [Contributing](CONTRIBUTING.md)

## Discussion and support

- [MyNissanLeaf project thread](https://mynissanleaf.com/threads/high-school-student-attempting-62-kwh-leaf-swap-via-bms-reverse-engineering-open-source.39638/)
- [Preliminary research document (Google Drive)](https://drive.google.com/file/d/1K7zyg2MCnwrswAz3TXE_jZ2o5wwVPW7J/view?usp=sharing) — earlier snapshot; some newer findings are documented here instead
- [Project fundraiser](https://gofund.me/30b3b4781)

## Openness and provenance

Findings are tagged as **source-reported**, **inferred**, **unverified**, or **project-tested** as appropriate. Please submit corrections with a source or reproducible evidence. Do not upload proprietary firmware dumps, private conversations, credentials, or copyrighted calibration files without permission.

This is an independent student research effort, not affiliated with or endorsed by Nissan or the cited researchers.
