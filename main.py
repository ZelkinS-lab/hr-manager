from employee import Employee
class HRManager:
    def __init__(self):
        self.spisok = []

    def add_employee(self, employee):
        self.spisok.append(employee)

    def biggest_employee(self):
        biggest_zp = 0
        biggest_name = ""
        biggest_otdel = ""
        for employee in self.spisok:
            if employee.zp > biggest_zp:
                biggest_zp = employee.zp
                biggest_name = employee.name
                biggest_otdel = employee.otdel

        return f"Самый дорогой сотрудник: {biggest_name} с зарплатой {biggest_zp} из отдела {biggest_otdel}"

    def save(self):
        with open("employee.txt", "w") as file:
                for emp in self.spisok:
                        file.write(f"{emp.name};{emp.otdel};{emp.zp}\n")

    def load(self):
        try:
                with open("employee.txt", "r") as file:
                        lines = file.readlines()
        except FileNotFoundError:
                print("Файл пуст!")
                return
        for line in lines:
                cline_line = line.strip()
                if cline_line == "":
                    continue
                employee = Employee.load(cline_line)
                self.spisok.append(employee)


def main():
        manager = HRManager()
        manager.load()

        while True:
                print("\n=== УПРАВЛЕНИЕ ПЕРСОНАЛОМ ===")
                print("1. Добавить сотрудника")
                print("2. Показать самого дорогого")
                print("3. Сохранить и выйти")

                choice = input("Выбери действие: ")

                if choice == "1":
                        name = input("Имя: ")
                        otdel = input("Отдел: ")
                        try:
                                zp = int(input("Зарплата: "))
                        except ValueError:
                                print("Ошибка! Зарплата должна быть числом.")
                                continue

                        # Создаем сотрудника через dataclass
                        emp = Employee(name, otdel, zp)
                        manager.add_employee(emp)
                        print("Сотрудник добавлен!")

                elif choice == "2":
                        print(manager.biggest_employee())

                elif choice == "3":
                        manager.save()
                        print("До свидания!")
                        break
                else:
                        print("Неверный ввод.")


if __name__ == "__main__":
        main()
