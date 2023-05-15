# Add view
from starlette_admin import DropDown
from starlette_admin.contrib.sqla import ModelView

from main import admin
from tests.models import Tenant, Item, Product

# from tests.models import Header, Detail

admin.add_view(
    DropDown(
        "Tests",
        icon="fa fa-list",
        views=[
            # ModelView(Header),
            # ModelView(Detail),
            ModelView(Tenant),
            ModelView(Item),
            ModelView(Product),
        ],
    )
)
