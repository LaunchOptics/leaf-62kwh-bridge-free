# Hardware, wiring, sensors, and mechanical integration

**Status:** Candidate interfaces only; no recipient/donor vehicles, pack, or OEM wiring diagrams have been measured in this project.

## Battery controller and sensor topology
- Community discussion reported **separate low- and high-current sensing** on the ZE1 configuration versus a **single current sensor** on older AZE0 configurations. This is a part-specific lead, **not** a universal confirmed pinout.
- For Path B, investigate an AZE0-compatible sensor, harness/connector differences, supply voltage, transfer function, signal polarity, range, redundancy, and plausibility monitoring.
- Do not connect arbitrary sensor outputs or repin a harness until the exact schematics and part numbers are compared. A plausible current reading is not evidence of preserved protection.

## Pack electrical interfaces
Investigate the reported **36-position low-voltage/signal connector** with OEM drawings. A shared shell or number of positions does not prove compatible cavity assignments.

Checklist:
- HV positive/negative connectors, keying, insulation, shielding, cable routing
- CAN high/low, termination, grounding, wake/ignition and ECU supply
- HV interlock, crash response, isolation monitoring, contactor feedback
- Battery heater, thermal sensors, charging and PDM connections
- Current sensors, voltage taps, cell-sense topology and temperature monitoring
- Service disconnect and service procedures

## Mechanical installation
Community conversions have discussed **approximately 40 mm spacers/adapters**, but this project has **no measured drawing** validating that number. The 62 kWh pack is generally heavier/larger than earlier packs; exact mass and geometry depend on the donor variant.

Verify:
- Underbody geometry, ground clearance, jacking points, suspension travel
- Mounting rails, structural load paths, fastener engagement, corrosion and sealing
- Crash-load considerations, pack enclosure clearances and road-debris exposure
- Measured axle loads and whether spring/suspension changes are warranted
- Donor/recipient model-year and market-specific differences

**No mounting design, adapter dimensions, torque values, or spring recommendation is approved by this project.**

## Part-number worksheet
| Item | Recipient AZE0 | Donor ZE1 Plus | Evidence |
|---|---|---|---|
| Battery assembly | TBD | TBD | OEM catalog / label needed |
| BMS/LBC | TBD | TBD | ECU labels and firmware IDs needed |
| Current sensor(s) | TBD | TBD | OEM electrical diagram needed |
| Signal connector | TBD | TBD | Manufacturer/cavity map needed |
| HV connector / HVIL | TBD | TBD | OEM electrical diagram needed |
| Mounts and spacers | TBD | TBD | Measured drawings needed |
| Charger/PDM variant | TBD | TBD | Parts and network mapping needed |

No physical work should proceed on the strength of a community photo or anecdotal connector match.
