Neel Prajapati <br>
Btech Undergrad IIT Hyderabad

## Featured enterprise project

- [Enterprise Leave & Asset Management System](enterprise-leave-asset-management/README.md): an Infosys-inspired FastAPI + React project with Admin, HR, and Employee RBAC; leave approvals; IT asset allocation; relational SQLAlchemy models; and pytest coverage.

**Resume description:** Built an Infosys-style Enterprise Leave & Asset Management System using FastAPI, React, and SQLAlchemy, featuring Admin/HR/Employee RBAC, leave approval workflows, IT asset allocation, seeded demo users, and pytest-covered API flows.

### Run the featured app from GitHub

```bash
git clone https://github.com/<your-github-username>/CV-projects-.git
cd CV-projects-/enterprise-leave-asset-management
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

In a second terminal:

```bash
cd CV-projects-/enterprise-leave-asset-management/frontend
npm install
npm run dev
```

- Backend API docs: `http://127.0.0.1:8000/docs`
- Frontend: the Vite URL shown in the terminal, usually `http://127.0.0.1:5173`
