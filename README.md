# Lab starter: Databricks Apps & CI/CD

Starter project for the hands-on labs. Follow the lab guides (Lab 1 to Lab 3).

```
app/                 FastAPI app (main.py), app.yaml manifest, requirements.txt
databricks.yml       Bundle definition (only the dev target; you add qa and prod in Lab 3)
requirements-dev.txt Dev and test dependencies (pytest, httpx, ruff)
pytest.ini           Points pytest at the app folder
```

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
cd app
uvicorn main:app --port 8000
# open http://localhost:8000/health
```

You will create `tests/` (Lab 2) and the CI/CD pipeline files (Labs 2 and 3) yourself.
A complete reference is in the solution package.
