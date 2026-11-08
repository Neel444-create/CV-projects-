from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = Workbook()
ws = wb.active
ws.title = "Route Economics"
headers = ["Route","Distance (km)","Ship trip cost (INR)","Air trip cost (INR)","Waterfly trip cost (INR)","Ship cargo (kg)","Air cargo (kg)","Waterfly payload (kg)","Ship cost/kg","Air cost/kg","Waterfly cost/kg","Savings vs air","Savings vs ship","Ship time (hrs)","Air time (hrs)","Waterfly time (hrs)"]
ws.append(headers)
rows = [
 ["Chennai–Port Blair",1200,180000,900000,180000,15000,3000,300,72,4,8],
 ["Kochi–Lakshadweep",400,55000,260000,90000,5000,800,300,24,2,3],
 ["Mumbai–Offshore installation",150,35000,180000,65000,1500,300,300,12,1,1.5],
]
for row in rows:
    ws.append(row[:8] + [None,None,None,None,None] + row[8:])
for r in range(2,5):
    ws.cell(r,9, f'=IFERROR(C{r}/F{r},0)')
    ws.cell(r,10, f'=IFERROR(D{r}/G{r},0)')
    ws.cell(r,11, f'=IFERROR(E{r}/H{r},0)')
    ws.cell(r,12, f'=IFERROR((J{r}-K{r})/J{r},0)')
    ws.cell(r,13, f'=IFERROR((I{r}-K{r})/I{r},0)')
    ws.cell(r,12).number_format = '0.0%'
    ws.cell(r,13).number_format = '0.0%'
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="17365D")
    cell.alignment = Alignment(wrap_text=True, vertical="center")
ws.row_dimensions[1].height = 42
for c in range(1,17):
    ws.column_dimensions[get_column_letter(c)].width = 23
for row in ws.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(vertical="center")
        if cell.column <= 8 or cell.column >= 14:
            cell.fill = PatternFill("solid", fgColor="FFF2CC")
ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions

notes = wb.create_sheet("Assumptions & Notes")
for row in [
 ["Item","Guidance"],
 ["Purpose","Lightweight scenario model, not a quote or investment-grade forecast."],
 ["Currency","INR"],
 ["Waterfly payload","300 kg per project brief; verify current specification."],
 ["Illustrative inputs","Distances, costs, cargo loads and journey times are placeholders, not verified facts."],
 ["How to use","Replace yellow cells with sourced values. Keep trip-cost scope and door-to-door time definitions consistent."],
 ["Savings","Positive savings means Waterfly scenario cost is below comparator cost/kg."],
 ["Operational caveat","Validate range, sea state, permissions, charging, safety and launch/recovery before recommending a route."],
]:
    notes.append(row)
notes.column_dimensions["A"].width = 28
notes.column_dimensions["B"].width = 110
for cell in notes[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="17365D")
for row in notes.iter_rows():
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")

summary = wb.create_sheet("Executive Summary", 0)
summary.merge_cells("A1:B1")
summary["A1"] = "Sea-to-Air | Commercial Feasibility & Unit Economics"
summary["A1"].font = Font(bold=True, size=16, color="FFFFFF")
summary["A1"].fill = PatternFill("solid", fgColor="17365D")
for row in [
 ["Purpose","Compare indicative transport economics across three candidate routes."],
 ["Outputs","Cost/kg, scenario savings vs ship and air, and time comparison."],
 ["Important","All numerical route inputs are illustrative placeholders. Replace with sourced data before conclusions."],
 ["Decision rule","Select a route only when customer value and operational feasibility are both supported."],
]:
    summary.append(row)
summary.column_dimensions["A"].width = 25
summary.column_dimensions["B"].width = 110
for row in summary.iter_rows():
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
wb.save("sea_to_air_unit_economics.xlsx")
print("Created sea_to_air_unit_economics.xlsx")
