from pydantic import BaseModel


class charactermodel(BaseModel):
    id:str
    product_name:str
    uid:str
    department:str