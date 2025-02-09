import pytest
from pydantic import ValidationError
from employee_record_management_system.employee_manager import add_employee, list_employees, search_employee

data = {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "HR",
        "role": "HR",
        "salary": 50000.0
    }

def test_add_employee():
    employee = add_employee(data)
    assert employee["id"] == data["id"]
    assert employee["name"] == data["name"]
    assert employee["age"] == data["age"]
    assert employee["department"] == data["department"]
    assert employee["role"] == data["role"]
    assert employee["salary"] == data["salary"]

def invalid_employee_data():
    data = {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "HR",
        "role": "HR",
        "salary": 50000.0
    }

    with pytest.raises(ValidationError):
        data["id"] = 0
        add_employee(data)

    with pytest.raises(ValueError):
        data["name"] = "J"
        add_employee(data)

    with pytest.raises(ValueError):
        data["age"] = 17
        add_employee(data)

    with pytest.raises(ValueError):
        data["age"] = 66
        add_employee(data)

    with pytest.raises(ValueError):
        data["salary"] = -1
        add_employee(data)