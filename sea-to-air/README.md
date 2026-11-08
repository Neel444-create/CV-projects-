# Sea-to-Air: Commercial Feasibility & Unit Economics

Independent, lightweight commercial case study assessing whether a 300 kg-class autonomous sea-cargo service could serve urgent small shipments on selected Indian routes. Not affiliated with Waterfly.

> **Evidence discipline:** Public route facts are documented in the route feasibility assessment and source register. Commercial rates, eligible shipment volumes and vehicle operating costs are not publicly verified. Do not treat any illustrative starter inputs as market facts.

## Routes screened
1. Chennai–Port Blair
2. Kochi–Lakshadweep (specify island endpoint)
3. Mumbai offshore (specify installation / transfer point)

## Preliminary finding
Mumbai offshore is the leading **customer-discovery hypothesis**, not a proven economic winner or approved operating route. Existing OSV/PSV and helicopter logistics mean a proposed service should target urgent, compact maintenance spares and complement incumbent operations.

## Repository structure
- `assumptions/route_assumptions.csv` — original illustrative inputs; do not cite as market facts.
- `assumptions/source_register.csv` — source URLs and evidence notes.
- `model/build_model.py` — starter model generator.
- `research/research_framework.md` — customer research checklist.
- `research/route_feasibility_report.md` — public-source route assessment.
- `deliverables/pilot_proposal.md` — pilot discussion draft.
- `deliverables/consulting_deck_outline.md` — 10-slide storyline.

## Complete deliverables
The updated Excel model, Word route feasibility report, and PowerPoint deck are available in the project conversation as downloadable files and in the packaged ZIP. The workbook separates public route evidence from commercial inputs and leaves unknown prices/volumes blank.

## Unit economics
- Incumbent cost/kg = incumbent trip cost / actual delivered kg
- Proposed cost/kg = proposed trip cost / actual delivered kg
- Savings per shipment = incumbent trip cost − proposed trip cost
- Savings % = savings / incumbent trip cost
- Monthly savings = savings per shipment × eligible monthly shipments

Use like-for-like shipment weight, handling, endpoints and service scope. Do not compare passenger fares with cargo rates or use port-wide tonnage as addressable demand for a 300 kg vehicle.

## Pilot decision gates
Confirm vehicle payload and range with reserve, weather envelope, permissions, safety-zone access, customer shipment profile, incumbent cost baseline and willingness to participate before proposing a paid pilot.

## Status
Preliminary route screen and commercial framework complete. Customer interviews, operator technical validation and verified unit economics remain open.
