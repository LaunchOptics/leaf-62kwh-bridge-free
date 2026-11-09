# Safety requirements and validation gates

**This is a research checklist, not a certification or HV service procedure.** Nissan EV packs contain lethal high voltage. Any future physical work requires OEM documentation, suitable facilities/equipment, and qualified supervision.

## Non-negotiable principles
- Never bypass crash, isolation, HVIL, watchdog, contactor permission, or battery-fault protections.
- Do not synthesize a false 'safe to close' response to force READY.
- Preserve genuine BMS/SUB MCU disagreement detection and safe shutdown.
- A dashboard SOC reading, successful diagnostic response, or READY state alone is **not** validation.
- A bridge-free design is not inherently safer than a correctly engineered bridge.

## Gate 0 — Preconditions
Exact vehicle/donor variants, ECU and firmware IDs, OEM manuals, qualified HV supervision, documented emergency response, and isolation/PPE requirements.

## Gate 1 — Electrical and mechanical documentation
Pin-to-pin comparison; current/temperature sensing; pack mounting and loads; charger/PDM topology; contactor ownership; all safety-critical inputs and feedback.

## Gate 2 — Passive evidence
Authorized captures from known-good configurations across sleep, wake, READY, drive, charge, shutdown and faults where safe/available. Capture metadata and firmware versions. **Do not** induce safety faults in a vehicle for research.

## Gate 3 — Offline models
Reconstruct message/state dependencies; exercise missing, late, invalid, contradictory, and stale input cases in software. Define safe outcomes, not just successful startup.

## Gate 4 — Independent bench review
Qualified review of over/undervoltage, overcurrent, thermal limits, sensor implausibility, isolation, HVIL, contactor failure, comms timeout, charge termination, regen, and fault escalation. Numerical limits must come from authoritative specifications, not guesses.

## Gate 5 — Conditional vehicle integration
Only after all safety-critical unknowns are resolved and a supervised acceptance plan exists.

**NO-GO:** Unknown critical message, unvalidated calibration, unresolved HV interface, uncontrolled contactor behavior, missing shutdown path, or unknown fault response.
