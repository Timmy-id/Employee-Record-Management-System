from pydantic import ValidationError
import argparse
from .employee_manager import add_employee, list_employees, search_employee


def main():
    parser = argparse.ArgumentParser(description='Employee Record Management System')
    parser.add_argument('--add', nargs=6, help='Add an employee record', metavar=('ID', 'NAME', 'AGE', 'DEPARTMENT', 'ROLE', 'SALARY'))
    parser.add_argument('--list', action='store_true', help='List all employee records')
    parser.add_argument('--search', type=int, metavar='ID', help='Search an employee record by ID')

    args = parser.parse_args()

    if args.add:
        data = {
            "id": int(args.add[0]),
            "name": args.add[1],
            "age": int(args.add[2]),
            "department": args.add[3],
            "role": args.add[4],
            "salary": float(args.add[5])
        }

        try:
            add_employee(data)
        except ValidationError as e:
            print(e.errors())
    
    if args.list:
        employees = list_employees()
        for emp in employees:
            print(emp)

    if args.search:
        data = args.search
        search_employee(data)

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == '__main__':
    main()