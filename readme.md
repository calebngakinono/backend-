# First Backend

This is just a small demo app for fastapi backend.

## Setup

Initial setup:

```bash
python -m venv .venv #Create a virtual environment because we aren't barbarians
source .venv/bin/activate #Activate virtual environment
pip install -r requirements.txt # Install required packages
```

## How to run

```bash
source .venv/bin/activate #(if not already done)
uvicorn main:app --reload # If it says port 800 is already in use, add --port 8001
```
