from enum import Enum
import random


class Position(Enum):
    JUNIOR = 0
    MIDDLE = 1
    SENIOR = 2


class Employee:
    def __init__(self, first_name: str, last_name: str, patronymic_name: str,
                 salary: int, position: Position = Position.JUNIOR) -> None:
        self.__first_name__ = first_name
        self.__last_name__ = last_name
        self.__patronymic_name__ = patronymic_name
        self.__position__ = position
        self.__salary__ = salary

    @property
    def first_name(self):
        return self.__first_name__

    @property
    def last_name(self):
        return self.__last_name__

    @property
    def patronymic_name(self):
        return self.__patronymic_name__

    @property
    def position(self):
        return self.__position__

    @property
    def salary(self):
        return self.__salary__

    def __str__(self):
        return f"ФИО: {self.__first_name__} {self.__last_name__} {self.__patronymic_name__}\n" \
               f"Должность: {self.__position__.name}\n" \
               f"Зарплата: {self.__salary__} руб.\n"


class EmployeeList:
    def __init__(self):
        self.__li__ = []

    def sort_employees_by_criteria(self, criteria):
        self.__li__.sort(key=criteria)

    def dismiss_employees_by_criteria(self, criteria):
        new_employees_list = list(filter(criteria, self.__li__))
        fired_employees = set(self.__li__) - set(new_employees_list)
        self.__li__ = new_employees_list
        return list(fired_employees)

    def add_employee(self, first_name, last_name, patronymic_name):
        position = random.choice(list(Position))
        salary = random.randint(80000, 100000)
        new_employee = Employee(first_name, last_name, patronymic_name, salary, position)
        self.__li__.append(new_employee)
        return new_employee

    def get_employee_list(self):
        return self.__li__


if __name__ == "__main__":
    employee_list = EmployeeList()
    people_list = open("peoples.txt", 'r+', encoding="utf-8")

    for people in people_list.readlines():
        print("ФИО: ", people)

        if input("Принимать этого человека? Если да, введите \'1\': ") == "1":
            a = people.split()
            employee_list.add_employee(a[0], a[1], a[2])

    employee_list.dismiss_employees_by_criteria(lambda x: x.first_name != 'Алексей')  # Увольняем Алексея
    employee_list.sort_employees_by_criteria(lambda x: x.salary * (x.position.value + 1))  # Сортировка по должности

    employee_list_writer = open("employees.txt", 'w+', encoding="utf-8")
    for employee in employee_list.get_employee_list():
        employee_list_writer.write(employee.__str__())
        employee_list_writer.write("\n")
