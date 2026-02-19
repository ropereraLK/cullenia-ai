# Environment configs

One folder per environment: **local**, **dev**, **stg**, **prod**.

Each contains `config.yaml` with:

| Key         | Description                |
|------------|----------------------------|
| `environment` | Environment name          |
| `host`     | Bind address (e.g. `127.0.0.1` or `0.0.0.0`) |
| `port`     | Server port                |
| `debug`    | Debug mode                 |
| `reload`   | Enable uvicorn `--reload`  |

**Usage**

- Set `APP_ENV` to choose which config is loaded (default: `local`):

  ```bash
  export APP_ENV=dev
  ./run.sh
  ```

- In Python: `from app.config import get_config; get_config().host`, etc.

You can add more keys to each `config.yaml` and extend `app.config.Settings` as needed.
