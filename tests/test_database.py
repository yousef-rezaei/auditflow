from sqlalchemy import inspect

import app.models.domain  # noqa: F401
from app.db.base import Base
from app.db.session import engine


def test_expected_tables_exist():
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)

    tables = set(inspector.get_table_names())

    expected_tables = {
        "organizations",
        "questionnaire_templates",
        "questionnaire_assignments",
    }

    assert expected_tables.issubset(tables)
