from enum import unique
import sqlalchemy as _sql
import database as _database


class Product(_database.Base):
    __tablename__= "products"
    id = _sql.Column(_sql.INTEGER, primary_key=True, index=True)
    name = _sql.Column(_sql.String, nullable=False, index=True)


class Category(_database.Base):
    __tablename__ = "categories"
    id = _sql.Column(_sql.INTEGER, primary_key=True, index=True)
    name = _sql.Column(_sql.String, nullable=False, index=True)


class ProdCategory(_database.Base):
    __tablename__ = "prodcategories"
    product_id = _sql.Column(
        _sql.INTEGER, 
        _sql.ForeignKey("products.id"), nullable=False)
    category_id = _sql.Column(
        _sql.INTEGER, 
        _sql.ForeignKey("categories.id"), nullable=False)
    __table_args__ = (_sql.PrimaryKeyConstraint(
        'product_id', 
        'category_id', name='prod_cat_uc' ),)