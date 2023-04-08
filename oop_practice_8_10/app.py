from classes import Robot

from skills.check import check_skills
from skills.build import learn_build_barn, learn_build_home
from skills.floor_count import learn_add_floor, learn_remove_floor

from l10n.localization import Localization, EnglishLocalization


def main():

    lang_select = input("Выберите язык / Select language (ru, en): ")
    if lang_select == "en":
        locale = EnglishLocalization()
    else:
        locale = Localization()

    print(locale.ROBOT_CREATE)

    # Создание робота
    robot = Robot("АА001221-56", locale.ROBOT_NAME_V1)

    # Проверка способностей
    check_skills(robot, locale)

    # Обучение робота — постройка дома
    learn_build_home(robot, locale)

    # Обучение робота — постройка сарая
    learn_build_barn(robot, locale)

    # Изменение имени
    robot.name = locale.ROBOT_NAME_V2

    # Проверка способностей
    check_skills(robot, locale)

    # Второе обучение робота
    print(locale.ROBOT_PRACTICE)

    # Обучение робота — добавить этаж к постройке
    learn_add_floor(robot)

    # Обучение робота — снести этаж у постройки
    learn_remove_floor(robot)

    # Изменение имени
    robot.name = locale.ROBOT_NAME_V3

    # Проверка способностей
    check_skills(robot, locale)

    # Доказательство, что может быть создан только один робот

    # Можем инициировать создание нового робота, но конструктор всё равно вернёт экземпляр "Вита"
    new_robot = Robot("ЛЕВАК", "Левый робот")
    print(new_robot == robot)


if __name__ == "__main__":
    main()
