import logging
import os
import json
from .models import Employee

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

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
            employee_data.append(new_employee.dict())
            with open(FILE_STORAGE, 'w') as f:
                json.dump([new_employee.dict()], f, indent=4)
            return new_employee.dict()
        
        check_id = [emp['id'] for emp in file_data]

        if data['id'] in check_id:
            print('Employee ID alredy exist')
            return

        new_employee = Employee(**data)
        employee_data = [Employee(**emp) for emp in file_data]
        employee_data.append(new_employee)
        with open(FILE_STORAGE, 'w') as f:
            json.dump([emp.dict() for emp in employee_data], f, indent=4)
        
        return new_employee.dict()
