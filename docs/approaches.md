# Conversion approaches

**Research status:** This project has not purchased or tested a vehicle, pack, BMS, or firmware image. This is a comparison of hypotheses and practitioner reports, not installation instructions.

## Path A — Retain and adapt the ZE1 Plus BMS
Retain the complete 62 kWh OEM pack, ZE1 BMS, and original sensors. Investigate whether its firmware can be made compatible with the older AZE0 vehicle without a permanently powered CAN bridge.

The difficulty is **bidirectional** communication, not just reformatting outgoing battery status frames. The VCM and BMS exchange requests, safety permissions, contactor-state feedback, and other data. Expert reports suggest both the main and SUB MCU may require analysis/modification. This path is **unproven**.

## Path B — Adapt an AZE0 BMS for OEM 62 kWh cells
Use an older AZE0 BMS with appropriate calibration for Nissan 62 kWh cells. BennVenn reports that ready-to-flash AZE0 firmware for this application exists and is used in practice. That report does **not** validate a particular donor pack or physical installation.

Open questions include harness/connector pinout, current sensor selection, calibration/part-number compatibility, contactor and HV integration, and complete fault handling. Avoid assuming a firmware image alone makes the conversion safe.

## Path C — CAN bridge
Retain the newer BMS and translate messages for the older car using an external device. Dala's [open-source battery-upgrade project](https://github.com/dalathegreat/Nissan-LEAF-Battery-Upgrade) is a key reference. This is a practical fallback, not a failure of the research goal.

## Path D — Transplant ZE1 VCM
Replacing the older VCM would introduce dependencies on other older vehicle systems (PDM, ABS, cluster, climate, etc.). Not a current priority.

## Path E — Modify AZE0 VCM firmware
Modifying the older vehicle's central controller could affect motor torque, contactors, and other safety-critical behavior. Not a current priority.

## Decision criteria
For any approach, compare reproducible evidence of compatibility, preservation of protections, failure behavior, maintainability, additional hardware, and the availability of qualified validation. **Do not rank an approach as safe merely because it uses OEM hardware or eliminates an external bridge.**
