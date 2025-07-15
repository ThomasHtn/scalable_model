import os
import sys
from logging.config import fileConfig

# Add folder parent in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from alembic import context
from sqlalchemy import engine_from_config, pool

from database.db_init import Base
from database.models import user_model  # noqa: F401

# Config Alembic
config = context.config
fileConfig(config.config_file_name)

# Inject dynamic database URL
config.set_main_option(
    "sqlalchemy.url", os.getenv("DATABASE_URL", "sqlite:///./census.db")
)
target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
