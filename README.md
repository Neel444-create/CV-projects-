Neel Prajapati <br>
Btech Undergrad IIT Hyderabad

## Featured enterprise project

- [Enterprise Leave & Asset Management System](enterprise-leave-asset-management/README.md): an Infosys-inspired FastAPI project with Admin, HR, and Employee RBAC; leave approval workflows; IT asset allocation; relational SQLAlchemy models; and pytest coverage.


### How to run the featured app from GitHub

```bash
git clone https://github.com/<your-github-username>/CV-projects-.git
cd CV-projects-/enterprise-leave-asset-management
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open a second terminal:

```bash
cd CV-projects-/enterprise-leave-asset-management/frontend
npm install
npm run dev
```

Backend docs: `http://127.0.0.1:8000/docs`. Frontend: use the Vite URL shown in the terminal, usually `http://127.0.0.1:5173`.
