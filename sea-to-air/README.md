# Sea-to-Air: Commercial Feasibility & Unit Economics

Independent, lightweight commercial case study assessing whether a 300 kg-class autonomous sea-cargo service could serve urgent small shipments on selected Indian routes. Not affiliated with Waterfly.

> **Evidence discipline:** public connectivity facts are cited in `research/route_assessment.md`. Commercial rates, eligible shipment volumes and vehicle operating costs are not publicly verified in this project. The updated model intentionally leaves those inputs blank until customer quotes or operator data are obtained.

## Routes screened
1. Chennai–Port Blair
2. Kochi–Lakshadweep (must specify island endpoint)
3. Mumbai offshore (must specify installation / transfer point)

## Key preliminary finding
Mumbai offshore is the leading **customer-discovery hypothesis**, not a proven economic winner or an approved operating route. Existing OSV/PSV and helicopter logistics mean the proposed service should target urgent, compact maintenance spares and complement incumbent operations.

## Repository structure
- `assumptions/route_assumptions.csv` — original illustrative inputs; do not cite as market facts.
- `model/build_model.py` — initial model generator (starter version).
- `research/research_framework.md` — research checklist.
- `research/route_assessment.md` — evidence-based route screen.
- `research/source_register.csv` — source register.
- `deliverables/pilot_proposal.md` — pilot discussion draft.
- `deliverables/consulting_deck_outline.md` — 10-slide storyline.

## Updated deliverables
The current, source-aware Excel model, route feasibility report and PowerPoint deck are provided as downloadable attachments in the project conversation. The workbook separates public route evidence from commercial inputs and does not fabricate prices or shipment volumes.

## Commercial model logic
- Incumbent cost/kg = incumbent trip cost / actual delivered kg
- Proposed cost/kg = proposed trip cost / actual delivered kg
- Savings per shipment = incumbent trip cost − proposed trip cost
- Savings % = savings / incumbent trip cost
- Monthly savings = savings per shipment × eligible monthly shipments

Use like-for-like shipment weight, handling, endpoints and service scope. Do not compare passenger fares with cargo rates or use port-wide tonnage as addressable demand for a 300 kg vehicle.

## Pilot decision gates
Confirm vehicle payload and range with reserve, weather envelope, permissions, safety-zone access, customer shipment profile, incumbent cost baseline and willingness to participate before proposing a paid pilot.
