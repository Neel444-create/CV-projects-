"""Build editable Sea-to-Air unit economics workbook."""
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"assumptions"/"route_assumptions.csv").open(newline="",encoding="utf-8") as f: routes=list(csv.DictReader(f))
wb=Workbook(); ws=wb.active; ws.title="Read Me"
for x in [["SEA-TO-AIR | COMMERCIAL FEASIBILITY"],["Purpose","Compare ship, air and proposed autonomous sea-cargo economics."],["Important","All starter figures are illustrative placeholders, not verified market or Waterfly data."],["How to use","Edit blue cells in Inputs; formula sheets update."],["Units","INR, kg, km and hours."],["Caution","Compare like-for-like shipment weight, endpoints, handling and service scope."],["Payload reference","300 kg is a case-study assumption; confirm actual specifications."]]: ws.append(x)
inp=wb.create_sheet("Inputs")
inp.append(["Route","Distance (km)","Monthly cargo (kg)","Urgency (1-5)","Current mode","Ship trip cost (INR)","Air trip cost (INR)","Proposed trip cost (INR)","Ship payload (kg)","Air payload (kg)","Proposed payload (kg)","Ship time (hours)","Air time (hours)","Proposed time (hours)","Suitability (1-5)","Pilot access (1-5)","Demand score (1-5)"])
for r in routes: inp.append([r["route"],float(r["distance_km"]),float(r["monthly_addressable_cargo_kg"]),float(r["urgency_score"]),r["existing_mode"]]+[float(r[k]) for k in ["ship_trip_cost_inr","air_trip_cost_inr","waterfly_trip_cost_inr","ship_payload_kg","air_payload_kg","waterfly_payload_kg","ship_transit_hours","air_transit_hours","waterfly_transit_hours","route_suitability_score","pilot_access_score","demand_score"]])
econ=wb.create_sheet("Route Economics"); econ.append(["Route","Mode","Trip cost (INR)","Payload (kg)","Cost/kg (INR)","Transit time (hours)","Cost vs ship (INR)","Savings vs ship (%)"])
for ir in range(2,len(routes)+2):
    for mode,cc,pc,tc in [("Ship","F","I","L"),("Air freight","G","J","M"),("Proposed service","H","K","N")]:
        rr=econ.max_row+1; sr=rr-((rr-2)%3)
        econ.append([f"=Inputs!A{ir}",mode,f"=Inputs!{cc}{ir}",f"=Inputs!{pc}{ir}",f"=IFERROR(C{rr}/D{rr},0)",f"=Inputs!{tc}{ir}",f"=C{rr}-C{sr}",f"=IFERROR((C{sr}-C{rr})/C{sr},0)"])
score=wb.create_sheet("Route Score"); score.append(["Route","Urgency","Savings potential","Demand","Suitability","Pilot access","Weighted score / 5"]); score.append(["Weights",0.25,0.25,0.20,0.20,0.10,""])
for n,ir in enumerate(range(2,len(routes)+2),start=3): score.append([f"=Inputs!A{ir}",f"=Inputs!D{ir}",f"=IFERROR(MAX(1,MIN(5,5*(1-Inputs!H{ir}/MAX(Inputs!F{ir},1)))),1)",f"=Inputs!Q{ir}",f"=Inputs!O{ir}",f"=Inputs!P{ir}",f"=SUMPRODUCT(B{n}:F{n},B2:F2)"])
summary=wb.create_sheet("Summary"); summary.append(["Route","Ship cost/kg","Air cost/kg","Proposed cost/kg","Proposed time (hrs)","Savings vs ship (%)","Weighted score"])
for ir in range(2,len(routes)+2):
    base=2+(ir-2)*3
    summary.append([f"=Inputs!A{ir}",f"='Route Economics'!E{base}",f"='Route Economics'!E{base+1}",f"='Route Economics'!E{base+2}",f"=Inputs!N{ir}",f"='Route Economics'!H{base+2}",f"='Route Score'!G{ir+1}"])
summary.append([]); summary.append(["Interpretation","Highest score is a screening signal only. Validate demand, route feasibility and actual quotations before selecting a pilot."])
for sh in wb.worksheets:
    sh.freeze_panes="A2"
    if sh.max_row>1: sh.auto_filter.ref=sh.dimensions
    for c in sh[1]: c.font=Font(bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="17365D"); c.alignment=Alignment(wrap_text=True,vertical="center")
    sh.row_dimensions[1].height=34
    for col in range(1,sh.max_column+1):
        vals=[str(sh.cell(row,col).value or "") for row in range(1,sh.max_row+1)]
        sh.column_dimensions[get_column_letter(col)].width=min(max(max(map(len,vals),default=10)+2,12),42)
    for row in sh.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(vertical="center",wrap_text=True)
for row in inp.iter_rows(min_row=2,min_col=2):
    for c in row: c.font=Font(color="0070C0")
for row in econ.iter_rows(min_row=2):
    row[2].number_format='₹#,##0'; row[4].number_format='₹#,##0.00'; row[6].number_format='₹#,##0'; row[7].number_format='0.0%'
for row in summary.iter_rows(min_row=2,max_row=len(routes)+1):
    for c in row[1:4]: c.number_format='₹#,##0.00'
    row[5].number_format='0.0%'
for row in score.iter_rows(min_row=3,max_row=len(routes)+2,min_col=7,max_col=7): row[0].number_format='0.00'
score.conditional_formatting.add("G3:G5",ColorScaleRule(start_type="min",start_color="F8696B",mid_type="percentile",mid_value=50,mid_color="FFEB84",end_type="max",end_color="63BE7B"))
out=ROOT/"deliverables"/"sea_to_air_unit_economics.xlsx"; out.parent.mkdir(parents=True,exist_ok=True); wb.save(out); print(f"Workbook created: {out}")
