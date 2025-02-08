from pydantic import BaseModel, conint, constr, confloat
from enum import Enum


class RoleEnum(str, Enum):
    Manager = "Manager"
    Developer = "Developer"
    Designer = "Designer"
    HR = "HR"
    Sales = "Sales"


class Employee(BaseModel):
    id: int = conint(gt=0)
    name: str = constr(min_length=2)
    age: int = conint(ge=18, le=65)
    department: str
    role: RoleEnum
    salary: float = confloat(gt=0)

    class Config:
        str_strip_whitespace = True
