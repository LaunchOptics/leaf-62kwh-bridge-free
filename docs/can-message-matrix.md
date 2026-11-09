# CAN message dependency matrix (research)

**Scope:** These are candidate dependencies identified in earlier project research by inspecting Dala's public bridge code. **Not** a verified ZE1 Plus ↔ AZE0 signal database. The branch, build revision, source/destination bus, payload meaning, and timing must be established for each target variant.

| CAN ID | Observed or reported role | Why it matters | Confidence / remaining question |
|---|---|---|---|
| `0x1ED` | Bridge recognizes 62 kWh battery generation; also discussed in separate ZE1 downgrade work | Battery identification and charging compatibility | Public-code lead; determine exact conditions |
| `0x1DB` | Battery status/SOC-related handling and checksum recalculation in some branches | SOC, state, current-related representation | Public-code lead; bit semantics and direction unverified here |
| `0x50C` | In a bridge branch, triggers battery-side generation of `0x625`, `0x5C5`, `0x3B8` | Newer BMS needs inputs, not just output translation | Public-code lead; determine legitimate source and purpose |
| `0x59E` | Quick-charge capacity/remaining-energy edits and CRC in AZE0-related handling | DC charging and energy semantics | Public-code lead; no universal interpretation |
| `0x1F2` | Charging state and charge-limit request handling | Charging permissions and limits | Public-code lead; variant-specific |
| `0x50A` | Different generation-dependent frame lengths/layouts | Payload compatibility | Public-code lead; exact layout unverified |
| `0x605`, `0x607` | Generated/sent toward newer battery in startup handling | Wake/handshake dependency | Public-code lead; function unverified |
| `0x390`, `0x393` | PDM-related synthetic frames in older ZE0 branches | Example of generation-specific bridge behavior | **Do not assume applies to AZE0** |
| `0x603`, `0x68C` | Startup/pairing candidate handlers in earlier source study | State transitions | Requires direct branch audit |
| `0x5EB` | Additional battery generation/identification candidate | Model-year detection | Requires direct branch audit |
| `0x79B` / `0x7BB` | Diagnostic request/response IDs reported by third-party BMS diagnostic tooling | Offline diagnostics, distinct from cyclic vehicle-control CAN | Source-reported; verify model and protocol |

## Method to make this actionable
For each message, record: **source repo + commit SHA + path + line**, applicable recipient/donor years, source bus, destination bus, frequency, payload length, sender, receiver, checksum/counter, state dependency, what the bridge does (PASS / MODIFY / GENERATE / BLOCK / STATEFUL), and independent evidence.

A matching CAN ID does **not** imply a matching payload. A bridge handler's existence does **not** imply it runs for the intended AZE0/ZE1 combination.

## Selected source leads
- [Dala — battery upgrade](https://github.com/dalathegreat/Nissan-LEAF-Battery-Upgrade)
- [Dala — CAN message research](https://github.com/dalathegreat/leaf_can_bus_messages)
- [Dala — battery downgrade](https://github.com/dalathegreat/Nissan-LEAF-Battery-Downgrade)
- [Matt MacLeod — BMS diagnostic CAN project](https://github.com/macleod-matt/nissan-leaf-can-bms)

Earlier PDF research also noted a bridge code path that uses a legacy **23,000 Wh representation** when rewriting capacity fields. That value is a compatibility behavior in that branch, **not the actual energy capacity** of a 62 kWh pack.
