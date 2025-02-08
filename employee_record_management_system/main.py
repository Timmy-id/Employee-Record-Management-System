from pydantic import ValidationError
import argparse
import logging
from .employee_manager import add_employee


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


def main():
    parser = argparse.ArgumentParser(description='Employee Record Management System')
    parser.add_argument('--add', nargs=6, help='Add an employee record', metavar=('ID', 'NAME', 'AGE', 'DEPARTMENT', 'ROLE', 'SALARY'))

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
            employee = add_employee(data)
            logger.info(f"Employee record added: {employee}")
        except ValidationError as e:
            logger.error(f"Invalid data: {"errors": e.errors()}")

if __name__ == '__main__':
    main()