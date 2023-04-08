from classes import Robot

from skills.check import check_skills
from skills.build import learn_build_barn, learn_build_home
from skills.floor_count import learn_add_floor, learn_remove_floor


def main():
    print("Создание робота...\n")

    # Создание робота
    robot = Robot("АА001221-56", "В")

    # Проверка способностей
    check_skills(robot)

    # Учим строить дом
    learn_build_home(robot)

    # Учим строить сарай
    learn_build_barn(robot)

    # Меняем имя
    robot.name = "Вита"

    # Проверка способностей
    check_skills(robot)

    # Второе обучение робота
    print("Отправка робота на промышленное предприятие \"ООО Кошмарик\"...\n")

    # Учим строить дополнительный этаж дома
    learn_add_floor(robot)

    # Учим сносить этаж дома
    learn_remove_floor(robot)

    # Меняем имя
    robot.name = "Виталий"

    # Проверка способностей
    check_skills(robot)

    # Доказательство, что может быть создан только один робот

    # Мы можем инициировать создание нового робота, но конструктор всё равно вернёт старого
    new_robot = Robot("ЛЕВАК", "Левый робот")
    print(new_robot == robot)


if __name__ == "__main__":
    main()
