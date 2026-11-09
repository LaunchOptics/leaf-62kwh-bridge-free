# Research archive audit — 2026-11-09

**Audit scope:** Compared the published GitHub research index against locally available prior project PDF reports and the archived Dala `Nissan-LEAF-Battery-Upgrade-main.zip` source snapshot. This is a **documentation/source audit**, not a hardware, firmware-binary, or electrical validation.

## Confirmed against the archived 2-port bridge source

Source: `Software/CANBRIDGE-2port/source/Src/can-bridge-firmware.c` in the local `Nissan-LEAF-Battery-Upgrade-main.zip` snapshot (archive folder dated 2026-10-21). These line numbers are **snapshot-relative**, not a pinned upstream Git commit.

| ID | Lines in snapshot | Verified source behavior | Scope warning |
|---|---:|---|---|
| `0x1ED` | 211–214 | Sets `My_Battery = MY_BATTERY_62KWH` | Detection in this bridge; not a complete protocol definition |
| `0x50C` | 360–365 | Copies `ALU_question`; sends `0x625`, `0x5C5`, `0x3B8` to battery-side bus | Meaning of generated payloads not verified |
| `0x59E` | 797–808 | In `MY_LEAF_2014` branch, rewrites QC full/remaining capacity fields, with 23,000 Wh compatibility constant and CRC | Generation-specific; not actual pack energy |
| `0x1F2` | 771–775 | Reads charging state and 80% charge-limit request from VCM | Additional conditional behavior follows |
| `0x603`, `0x68C` | 811–816 | Resets state and sends `0x605`, `0x607` toward battery | Startup-related code, not verified safe sequence |
| `0x1DB` | 265 onward | Frame handler present | Bit semantics need deeper audit |
| `0x390`, `0x393` | 100–101, 367 onward | Synthetic PDM-related frames defined and used in a `MY_LEAF_2011` branch | Do **not** generalize to AZE0 |

The 3-port source also contains corresponding handlers, but a full branch-by-branch equivalence check has **not** been completed.

## Coverage checked

Major material from the **Comprehensive Technical Research** and **Evidence Based Technical Research** PDFs is represented across:
- [approaches](approaches.md)
- [CAN message matrix](can-message-matrix.md)
- [CAN protocol](can-protocol.md)
- [diagnostics](diagnostics.md)
- [firmware research](firmware-research.md)
- [firmware tools](firmware-tools.md)
- [calibration](calibration-research.md)
- [hardware](hardware-integration.md)
- [safety](safety-validation.md)
- [research log](research-log.md)

The repository also includes the newer **November 2026** BennVenn-reported findings absent from older PDF revisions.

## Corrections / unresolved audit items

1. **Not a literal transcription of every source.** Earlier PDFs have additional explanatory paragraphs, examples, and source citations that were condensed. The claim that the repository has *everything* would be inaccurate.
2. **Unpinned source revision.** The inspected ZIP is a dated snapshot, not a verifiable upstream commit SHA. Pin source references before treating line numbers as durable.
3. **CAN meaning remains conditional.** The presence of a bridge handler does not prove its behavior applies to every AZE0/ZE1 Plus combination. Neither message counters nor timing/state-machine completeness is established.
4. **Path B is source-reported, not project-tested.** BennVenn's claim that adapted AZE0 firmware for OEM 62 kWh cells is in use materially improves the evidence, but this project has not verified a physical build.
5. **Main/SUB MCU support remains unresolved.** Extracting protected firmware, reflashing modified firmware, and preserving the SUB MCU safety logic are separate questions.
6. **No exact hardware comparison.** Connector cavities, current sensors, cell-sense layout, firmware variants, mounting dimensions, and HV integration remain unverified.
7. **No original experiments.** No vehicles, logs, original firmware dumps, tests, or validated safety results.
8. **Tools are offline utilities.** The Python scripts are published, but this audit did not execute a test suite against real logs. Their output cannot establish CAN signal semantics or safety.

## Evidence classification

- **Source-code verified:** specific handlers above, within the archived snapshot.
- **Practitioner-reported:** BennVenn's Path B availability, dual-MCU behavior, bootloader differences, and handshaking descriptions.
- **Hypothesis:** Path A feasibility, physical adaptation of any exact pack, and full firmware compatibility.
- **Project-tested:** **None**.

## Next evidence tasks

- Pin upstream commit IDs and compare the 2-port and 3-port branch conditions.
- Build a traceable message-by-message table: source bus, destination bus, sender, receiver, DLC, checksum, counters, timing, and state.
- Audit the earlier PDFs paragraph-by-paragraph and note any omitted unique claims.
- Recheck the published diagnostic implementation against the exact target BMS variant.
- Verify tool compatibility separately for ZE1 main and SUB MCU, without attempting safety-bypass testing.
- Obtain OEM diagrams and exact part/firmware IDs before making wiring or calibration claims.

**Bottom line:** The public repository is a substantial, candid research archive suitable for community review, but not a complete, source-pinned, experimentally verified engineering specification.
