#!/usr/bin/env bash
# Run the FastAPI app (activate venv and start uvicorn)
set -e
cd "$(dirname "$0")"
ROOT="$(pwd)"

if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
else
  echo "Error: venv not found at $ROOT/venv" >&2
  exit 1
fi

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Starting server at http://0.0.0.0:8000"
exec uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
