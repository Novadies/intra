from example_something_app.models import aggregator
from loader.tools.for_save_to_db_CLASS import DB_ExcelEntry
from logs.logger import log_apps


class AppDB_ExcelEntry(DB_ExcelEntry):
    """ Переопределить если необходимо методы """
    pass


instance_DB_ExcelEntry = AppDB_ExcelEntry(
    aggregator=aggregator,
    engine="Pandas",
    is_validate=True,
    check_compliance=True,
    N=10,
    similar_batch_size=999,
    header=True
)
