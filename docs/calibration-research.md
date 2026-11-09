# Calibration and cell-model research

## What Path B changes
An AZE0 BMS communicating natively with the AZE0 VCM still needs correct battery **measurement, estimation, limits, and fault logic** for the OEM ZE1 Plus 62 kWh cell assembly.

Research areas:
1. Open-circuit voltage versus SOC, with temperature dependence and hysteresis.
2. Cell internal resistance versus SOC, temperature, and aging.
3. Capacity, usable energy, SOH and coulomb-counting assumptions.
4. Cell balance thresholds, voltage/temperature monitoring and plausibility.
5. Charge/discharge current limits and cold/hot temperature behavior.
6. Sensor transfer functions, saturation, fault detection, and redundant measurement checks.
7. Firmware-specific calibration layouts and checksums.

**Important:** A plausible SOC display does not demonstrate safe cell protection, and simply copying a table across firmware variants may corrupt unrelated data.

## Public XML definitions
The [SafetyUggs BMS reverse-engineering repository](https://github.com/SafetyUggs/Leaf-BMS-Reverse-Engineering) includes firmware-specific ECUFlash XML directories identified in a locally held repository snapshot:

- `AZE0(4NC0A)/4NC0A.xml`
- `ZE1_40kwh(5SH2D)/5SH2D.xml`
- `ZE0(3NA0D)/3NA0D.xml`
- `ENV200_24(4FA2B)/4FA2B.xml`

Its README explicitly says the XMLs are compatible **only with the listed firmware**. These labels are **examples of published variants**, not a statement that the donor will have one of them. No public ZE1 Plus 62 kWh XML was established from this snapshot.

## Expert-reported developments
BennVenn reported that Path B (AZE0 BMS with OEM Nissan 62 kWh cells) is already performed in practice and that compatible ready-to-flash firmware is commercially offered. This materially updates the earlier PDF's more tentative characterization. The project has **not** purchased or tested such firmware and has not independently verified physical integration requirements.

BennVenn also reported 40 kWh ZE1 firmware availability through a third-party source, but differing bootloaders prevent assuming 40 kWh and 62 kWh firmware are cross-flashable.

## Data to acquire before drawing conclusions
Exact BMS hardware ID, firmware/bootloader revision, permitted XML definitions, source of each calibration, cell chemistry/part number, current sensor model, and qualified acceptance criteria. Avoid publishing purchased or proprietary calibration dumps without authorization.
