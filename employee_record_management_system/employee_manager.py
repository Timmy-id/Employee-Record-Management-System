import os
import json
from .models import Employee

FILE_STORAGE = 'employees.json'

def add_employee(data: Employee):
    if not os.path.isfile(FILE_STORAGE):
        with open(FILE_STORAGE, 'w') as f:
            json.dump([], f)
    with open(FILE_STORAGE, 'r') as f:
        file_data = json.load(f)

        if len(file_data) == 0:
            new_employee = Employee(**data)
            employee_data = [Employee(**emp) for emp in file_data]
            employee_data.append(new_employee.model_dump())
            with open(FILE_STORAGE, 'w') as f:
                json.dump([new_employee.model_dump()], f, indent=4)
            return new_employee.model_dump()
        
        check_id = [emp['id'] for emp in file_data]

        if data['id'] in check_id:
            print('Employee ID already exist')
            return

        new_employee = Employee(**data)
        employee_data = [Employee(**emp) for emp in file_data]
        employee_data.append(new_employee.model_dump())
        with open(FILE_STORAGE, 'w') as f:
            json.dump([emp.model_dump() for emp in employee_data], f, indent=4)
        
        return new_employee.model_dump()

def list_employees():
    if not os.path.isfile(FILE_STORAGE):
        print('No employee records found')
        return
    if os.path.getsize(FILE_STORAGE) == 0:
        print('No employee records found')
        return
    with open(FILE_STORAGE, 'r') as f:
        file_data = json.load(f)
        
        if len(file_data) == 0:
            print('No employee records found')
            return file_data
        return file_data
    
def search_employee(id: int):
    if not os.path.isfile(FILE_STORAGE):
        print('No employee records found')
        return
    if os.path.getsize(FILE_STORAGE) == 0:
        print('No employee records found')
        return
    with open(FILE_STORAGE, 'r') as f:
        file_data = json.load(f)
        
        if len(file_data) == 0:
            print('No employee records found')
            return

        employees_data = [Employee(**emp) for emp in file_data]
        for employer in employees_data:
            if employer.id == id:
                print(employer.model_dump())
                return
        print(f'Employee with ID {id} not found')
        return
            