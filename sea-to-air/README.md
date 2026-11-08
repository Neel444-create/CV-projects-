# Sea-to-Air: Commercial Feasibility & Unit Economics

A lightweight commercial assessment of autonomous sea-cargo transportation across three Indian routes. It compares conventional shipping, air freight and a proposed 300 kg autonomous sea-cargo service.

> Independent case study. Not affiliated with Waterfly. Starter values are illustrative placeholders, not verified Waterfly pricing, performance, customer demand or route approvals.

## Routes
1. Chennai–Port Blair: island supply chains and time-sensitive small cargo.
2. Kochi–Lakshadweep: essential supplies, spares and urgent shipments.
3. Mumbai–offshore installations: tools, spares and compact maintenance equipment.

These are screening candidates, not confirmed operating routes. Suitability depends on actual range, payload, weather, permissions, infrastructure and customer demand.

## Scope
- Screen routes using distance, demand indicators, urgency and existing transport.
- Compare ship, air freight and proposed autonomous service.
- Model trip cost, cost/kg and customer savings.
- Rank routes using a weighted score.
- Outline a small measurable pilot.

Out of scope: vehicle engineering, navigation design, certification, detailed safety case, port operations and fleet scheduling.

## Structure
- `assumptions/route_assumptions.csv`: editable starter assumptions.
- `model/build_model.py`: creates the Excel workbook.
- `research/research_framework.md`: route research checklist.
- `deliverables/pilot_proposal.md`: pilot discussion draft.

## Run
`pip install -r requirements.txt`
`python model/build_model.py`

Output: `deliverables/sea_to_air_unit_economics.xlsx`.

## Core formulas
- Cost/kg = trip cost / delivered payload (kg)
- Customer savings = incumbent trip cost − proposed service trip cost
- Savings % = savings / incumbent trip cost
- Weighted score = sum of criterion score × criterion weight

Replace all starter values with sourced data before drawing conclusions. Compare like-for-like shipment weight, endpoints, handling and service scope. Record source URL, publication date, unit and access date.

## Suggested sources
Port authorities and traffic reports; Ministry of Ports, Shipping and Waterways; Directorate General of Shipping; Airports Authority of India; Andaman & Nicobar and Lakshadweep administrations; offshore operator disclosures; and direct freight quotations.

## Status
Initial project scaffold. Research validation and final route selection are pending.
