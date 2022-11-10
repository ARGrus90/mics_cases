import fastapi as _fastapi
from typing import TYPE_CHECKING, List
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

@app.get("/api/products/", response_model=List[_schemas.Product])
async def get_products(
    db: _orm.Session=_fastapi.Depends(_services.get_db)
):
    return await _services.get_all_products(db=db)


@app.get(
    "/api/categories/",
    response_model=List[_schemas.Category]
)
async def get_categories(
    db: _orm.Session=_fastapi.Depends(_services.get_db)
):
    return await _services.get_all_categories(db=db)


@app.get(
    "/api/prodcategories/", 
    response_model=List[_schemas.ProdCategory]
)
async def get_prodcategories(
    db: _orm.Session=_fastapi.Depends(_services.get_db)
):
    return await _services.get_all_prodcategories(db=db)


@app.get(
    "/api/products_and_categories/", 
    response_model=List[_schemas.ProductsAndCategories],
)
async def get_all_products_and_categories(
    db: _orm.Session=_fastapi.Depends(_services.get_db)
):
    return await _services.get_all_products_and_categories(db=db)

