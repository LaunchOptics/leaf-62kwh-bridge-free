# Research roadmap

The milestones below are **gates**, not scheduled promises.

## 1. Open research foundation
- [x] Public repository and initial documentation
- [ ] Review and reconcile earlier research PDF against newer findings
- [ ] Source individual technical claims and note confidence levels
- [ ] Collect corrections and community contributions through GitHub issues

## 2. Evidence gathering
- [ ] Identify exact AZE0 and ZE1 Plus donor variants/part numbers
- [ ] Establish authorized access to firmware and tool documentation
- [ ] Determine whether main and SUB MCU images can be extracted and reflashed
- [ ] Record known CAN protocol dependencies, including incoming messages
- [ ] Compare Path A, B, and C with a traceable requirements matrix

## 3. Offline engineering
- [ ] Build a versioned message dictionary with evidence citations
- [ ] Build an offline state-machine model of the BMS/VCM interaction
- [ ] Define expected safe failure outcomes for timeout and invalid inputs
- [ ] Obtain independent review of assumptions and test plans

## 4. Hardware and safety readiness
- [ ] Fundraise and acquire donor hardware
- [ ] Arrange qualified HV supervision, PPE, isolation equipment, and test facilities
- [ ] Validate connector, current sensor, mechanical, and thermal compatibility
- [ ] Establish bench test procedures and stop conditions

## 5. Conditional validation
- [ ] Supervised bench testing with full protection behavior preserved
- [ ] Fault and shutdown validation
- [ ] Only then consider vehicle integration and documentation

**No hardware validation has occurred.** An elegant communication solution is not sufficient evidence of vehicle safety.
