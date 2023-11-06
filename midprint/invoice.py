from datetime import datetime 
from pydantic import BaseModel, PositiveInt

class Data(BaseModel):
    brandname: str | None
    age: int = 10
    products: dict[str, PositiveInt]

def generate(data):
    data = Data(**data)
    

edata = {
    "brandname": "ayon",
    "products": {
        "hi": 10
    }
}
generate(edata)