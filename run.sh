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

# Load host/port from config (config/<APP_ENV>/config.yaml). Default: APP_ENV=local
export APP_ENV="${APP_ENV:-local}"
HOST=$(python -c "from app.config import get_config; print(get_config().host)")
PORT=$(python -c "from app.config import get_config; print(get_config().port)")
RELOAD=$(python -c "from app.config import get_config; print(get_config().reload)")

echo "Starting server (env=$APP_ENV) at http://$HOST:$PORT"
exec uvicorn app.main:app --host "$HOST" --port "$PORT" $([ "$RELOAD" = "True" ] && echo "--reload")
