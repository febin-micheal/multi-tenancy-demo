# Import all the models, so that Base has them before being
# imported by Alembic
from utils.models import Base
from tests.models import *
