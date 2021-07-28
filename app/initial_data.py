import logging

from app.db.init_db import init_db
from app.db.load_copies import load_copies
from app.db.load_titles import load_titles
from app.db.load_transaction_type import load_transaction_type
from app.db.load_locations import load_locations
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    # init_db(db)
    # INFO: load this only when it's necessary
    load_copies(db)
    load_titles(db)
    # load_transaction_type(db)
    # load_locations(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
