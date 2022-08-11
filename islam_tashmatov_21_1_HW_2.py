# Создать класс Company: —> атрибуты (company_bank, company_name)
# Создать класс Person: —> атрибуты (first_name, last_name, salary) и наследовть его от Company
#
# создать 2 метода для класса Person:
# 1) get_salary —> при вызове
# сделать проверку на то что если у компании недостаточно средств для выдачи зп сотруднику то выводить:
#  “У компании не достаточно средств!”
#
# или же:
# отнять от капитала комании(company_bank) зарплату сотрудника(Person.salary)
#
# 2) person_info —> выводит информацию о сотруднике (first_name, last_name, salary)
class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):
    salary = None

    def __init__(self, first_name, last_name, salary, company_bank, company_name):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        print(f"{self.company_name}: У компании не достаточно средств!"
              f"{self.company_bank}: У банка есть деньги!{Person.salary}")

    def person_info(self):
        print(f'first_name: {self.first_name}\n'
              f'last_name: {self.last_name}\n'
              f'salary: {self.salary}\n'
              )
