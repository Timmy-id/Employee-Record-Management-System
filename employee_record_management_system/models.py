from pydantic import BaseModel, conint, constr, confloat, Field
from enum import Enum


class RoleEnum(str, Enum):
    Manager = "Manager"
    Developer = "Developer"
    Designer = "Designer"
    HR = "HR"
    Sales = "Sales"


class Employee(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=2)
    age: int = Field(ge=18, le=65)
    department: str
    role: RoleEnum
    salary: float = Field(gt=0)

    class Config:
        str_strip_whitespace = True
