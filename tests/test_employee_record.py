import pytest
from pydantic import ValidationError
from employee_record_management_system.employee_manager import add_employee, list_employees, search_employee

def test_add_employee():
    data = {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "HR",
        "role": "HR",
        "salary": 50000.0
    }

    employee = add_employee(data)
    assert employee["id"] == data["id"]
    assert employee["name"] == data["name"]
    assert employee["age"] == data["age"]
    assert employee["department"] == data["department"]
    assert employee["role"] == data["role"]
    assert employee["salary"] == data["salary"]

def test_invalid_employee_data():
    with pytest.raises(ValidationError):
        invalid_id_data = {
            "id": -1,
            "name": "John Doe",
            "age": 30,
            "department": "HR",
            "role": "HR",
            "salary": 50000.0
        }
        
        add_employee(invalid_id_data)

    with pytest.raises(ValidationError):
        invalid_name_data = {
            "id": 2,
            "name": "J",
            "age": 30,
            "department": "HR",
            "role": "HR",
            "salary": 50000.0
        }
       
        add_employee(invalid_name_data)

    with pytest.raises(ValueError):
        invalid_age_data = {
            "id": 3,
            "name": "John Doe",
            "age": 17,
            "department": "HR",
            "role": "HR",
            "salary": 50000.0
        }
        
        add_employee(invalid_age_data)

    with pytest.raises(ValidationError):
        invalid_age_data = {
            "id": 4,
            "name": "John Doe",
            "age": 67,
            "department": "HR",
            "role": "HR",
            "salary": 50000.0
        }
        
        add_employee(invalid_age_data)

    with pytest.raises(ValidationError):
        invalid_department_data = {
            "id": 5,
            "name": "John Doe",
            "age": 67,
            "department": 10,
            "role": "HR",
            "salary": -1
        }

        add_employee(invalid_department_data)

    with pytest.raises(ValidationError):
        invalid_role_data = {
            "id": 6,
            "name": "John Doe",
            "age": 67,
            "department": 10,
            "role": "Tech",
            "salary": -1
        }

        add_employee(invalid_role_data)

    with pytest.raises(ValidationError):
        invalid_salary_data = {
            "id": 7,
            "name": "John Doe",
            "age": 67,
            "department": "HR",
            "role": "HR",
            "salary": -1
        }

        add_employee(invalid_salary_data)

def test_list_employee():
    employees = list_employees()
    assert isinstance(employees, list)

def test_search_employee():
    employee = search_employee(1)
    assert employee["id"] == 1