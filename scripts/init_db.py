import app.models.domain  # noqa: F401
from app.db.base import Base
from app.db.session import engine


def main() -> None:
    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully.")


if __name__ == "__main__":
    main()
