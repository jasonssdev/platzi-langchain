# config.py
import os
from dotenv import load_dotenv, find_dotenv
from utils.paths import ENV_PATH


dotenv_path = ENV_PATH
if not find_dotenv(dotenv_path, raise_error_if_not_found=False):
    raise FileNotFoundError(f".env file not found at {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)


def get_foundation_model_api():
    return {
        "openai": os.getenv("OPENAI_API_KEY", "").strip(),
        "anthropic": os.getenv("ANTHROPIC_API_KEY", "").strip(),
        "gemini": os.getenv("GEMINI_API_KEY", "").strip(),
        "debug": os.getenv("DEBUG", "False").lower() == "true",
        "env": os.getenv("ENV", "development"),
    }


def validate_api_keys(config: dict):
    missing = [
        k for k, v in config.items()
        if not v and k not in ("debug", "env")
        ]
    if missing:
        raise ValueError(f"Missing API keys: {', '.join(missing)}")


foundation_models = get_foundation_model_api()
validate_api_keys(foundation_models)
