from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas
from sqlalchemy.sql import select as _select
from sqlalchemy import or_

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_all_products(
    db: "Session") -> List[_schemas.Product]:
    products = db.query(_models.Product).all()
    return list(map(_schemas.Product.from_orm, products))


async def get_all_categories(
    db: "Session") -> List[_schemas.Category]:
    categories = db.query(_models.Category).all()
    return list(map(_schemas.Category.from_orm, categories))


async def get_all_prodcategories(
    db: "Session") -> List[_schemas.ProdCategory]:
    prodcategories = db.query(
        _models.ProdCategory.product_id,
        _models.ProdCategory.category_id).all()
    return list(map(_schemas.ProdCategory.from_orm, prodcategories))


async def get_all_products_and_categories(db: "Session") -> \
    List[_schemas.ProductsAndCategories]:
    products_and_categories = (db.query(
        _models.Product.name.label('product_name'),
        _models.Category.name.label('category_name')) 
        .select_from(_models.Product) 
        .join(_models.ProdCategory, full=True)
        .filter(
            or_ (
                _models.Product.id == _models.ProdCategory.product_id,
                _models.ProdCategory.product_id == None
            )
        )
        .join(_models.Category, full=True)\
        .filter(
            or_(
                _models.Category.id == _models.ProdCategory.category_id,
                _models.ProdCategory.category_id == None
            )
        )).all()

    return products_and_categories