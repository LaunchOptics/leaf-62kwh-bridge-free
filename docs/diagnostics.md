# Diagnostic CAN and reverse-engineering leads

This is a record of **third-party source-study leads**, not an authenticated diagnostic specification for every Nissan LEAF generation.

## Reported BMS diagnostic transport
A review of Matt MacLeod's [nissan-leaf-can-bms](https://github.com/macleod-matt/nissan-leaf-can-bms) identified:
- Request arbitration ID: `0x79B`
- Response arbitration ID: `0x7BB`
- Example request prefixes: `02 21 01` (current/SOC/capacity candidate), `02 21 02` (cell voltage candidate), `02 21 04` (temperature candidate), `02 21 06` (shunt data candidate), `02 21 61` (SOH candidate)
- A flow-control frame of `30 01 00 FF FF FF FF FF` was noted in the source review.

**Do not transmit these frames based solely on this page.** Their meaning, session requirements, safety impact, transport-layer handling, and compatibility with the target ECU have not been validated by this project. The third-party implementation was described as tested on a 2011 pack, not an OEM 62 kWh ZE1 Plus BMS.

## Source audit TODO
Earlier source review raised possible cell-indexing and bitmask (`&&` vs `&`) concerns. These are **unconfirmed code-review leads**, not proven bugs. Revisit the exact repository commit and reproduce the issue before reporting it upstream.

## Diagnostic versus vehicle-control messages
Diagnostic request/response traffic is not interchangeable with the periodic BMS/VCM operational handshake. A successful diagnostic read does not demonstrate safe contactor control or charging interoperability.

## Suggested offline research
- Record diagnostic services by firmware variant and cite code revision.
- Compare decoded values against a known reference with no active injection.
- Separate physical units, raw bytes, scaling, sign, validity flags, and sample rate.
- Identify what is unknown; avoid interpreting arbitrary bytes as verified safety states.
