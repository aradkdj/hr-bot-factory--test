# Import all the models, so that Base has them before being imported by alembic
from app.db.base_class import Base  # noqa: F401
