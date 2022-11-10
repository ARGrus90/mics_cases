import pydantic as _pydantic
from pydantic.schema import Optional


class Product(_pydantic.BaseModel):
    id: int
    name: str

    class Config:
        orm_mode=True


class Category(_pydantic.BaseModel):
    id: int
    name: str

    class Config:
        orm_mode=True


class ProdCategory(_pydantic.BaseModel):
    product_id: int
    category_id: int


    class Config:
        orm_mode=True


class ProductsAndCategories(_pydantic.BaseModel):
    product_name: Optional[str]
    category_name: Optional[str]

    class Config:
        orm_mode=True    
