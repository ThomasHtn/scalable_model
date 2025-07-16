from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    age: int
    workclass: str
    fnlwgt: int
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str
    income: str

    class Config:
        orm_mode = True

class UserIn(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str