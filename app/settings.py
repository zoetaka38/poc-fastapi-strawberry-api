import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings, extra="allow"):
    DB_URI: str
    DB_RO_URI: str
    DB_ECHO: bool = False
    API_PLACE: str = "sls"
    RACK_ENV: str = "development"
    LOG_LEVEL: str = "DEBUG"
    POOL_RECYCLE_TIME: str = ""

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / f"config/{os.environ['APP_CONFIG_FILE']}.env",
        case_sensitive=True,
    )


settings = Settings()
