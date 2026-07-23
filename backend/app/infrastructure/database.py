import os
from collections.abc import Generator
from pathlib import Path

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session, sessionmaker


def read_secret(file_path: str) -> str:
    path = Path(file_path)

    if not path.is_file():
        raise RuntimeError(f"Secret file does not exist: {path}")

    value = path.read_text(encoding="utf-8").strip()

    if not value:
        raise RuntimeError(f"Secret file is empty: {path}")

    return value


def build_database_url() -> URL:
    password_file = os.environ["POSTGRES_PASSWORD_FILE"]

    try:
        port = int(os.getenv("POSTGRES_PORT", "5432"))
    except ValueError as error:
        raise RuntimeError("POSTGRES_PORT must be an integer") from error

    return URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["POSTGRES_USER"],
        password=read_secret(password_file),
        host=os.getenv("POSTGRES_HOST", "db"),
        port=port,
        database=os.environ["POSTGRES_DB"],
    )


# echo=True logs every SQL statement to stdout; intended for local/dev
# debugging, not production.
engine = create_engine(
    build_database_url(),
    echo=os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true",
    pool_pre_ping=True,
    connect_args={"connect_timeout": int(os.getenv("POSTGRES_CONNECT_TIMEOUT", "5"))},
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
