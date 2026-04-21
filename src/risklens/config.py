"""Environment-driven runtime settings."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    environment: str
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    db_schema: str
    data_dir: str

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            environment=os.getenv("RISKLENS_ENV", "dev"),
            db_host=os.getenv("RISKLENS_DB_HOST", "localhost"),
            db_port=int(os.getenv("RISKLENS_DB_PORT", "5432")),
            db_name=os.getenv("RISKLENS_DB_NAME", "risklens"),
            db_user=os.getenv("RISKLENS_DB_USER", "postgres"),
            db_password=os.getenv("RISKLENS_DB_PASSWORD", "postgres"),
            db_schema=os.getenv("RISKLENS_SCHEMA", "core"),
            data_dir=os.getenv("RISKLENS_DATA_DIR", "./data"),
        )
