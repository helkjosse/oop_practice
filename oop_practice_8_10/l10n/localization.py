class Localization:
    ROBOT_CREATE = "Создаём робота...\n"
    ROBOT_PRACTICE = "Отправка робота на промышленное предприятие \"ООО Кошмарик\"...\n"

    ROBOT_BUILD_HOME_COMPLETE = "{robot_name} только что построил дом!"
    ROBOT_BUILD_BARN_COMPLETE = "{robot_name} только что построил сарай!"

    ROBOT_CHECK_SKILLS = "Проверка способностей у робота {robot_name}"
    ROBOT_CHECK_HOME_SKILL = "Постройка дома: {}"
    ROBOT_CHECK_BARN_SKILL = "Постройка сарая: {}"
    ROBOT_CHECK_FLOOR_ADD_SKILL = "Добавить этаж к постройке: {}"
    ROBOT_CHECK_FLOOR_REMOVE_SKILL = "Снести этаж с постройки: {}"

    ROBOT_FLOOR_ADD = "{robot_name} только что увеличил количество этажей на 1!"
    ROBOT_FLOOR_REMOVE = "{robot_name} только что уменьшил количество этажей на 1!"
    ROBOT_FLOOR_REMOVE_FAIL = "{robot_name} не может уменьшить количество этажей у одноэтажной постройки!"

    ROBOT_NAME_V1 = "В"
    ROBOT_NAME_V2 = "Вита"
    ROBOT_NAME_V3 = "Виталий"


class EnglishLocalization(Localization):
    ROBOT_CREATE = "Creating robot...\n"
    ROBOT_PRACTICE = "Sending a robot to an industrial plant \"OOO Koshmarik\"...\n"

    ROBOT_BUILD_HOME_COMPLETE = "{robot_name} have just built the home!"
    ROBOT_BUILD_BARN_COMPLETE = "{robot_name} have just built the barn!"

    ROBOT_CHECK_SKILLS = "Checking skill {robot_name}"
    ROBOT_CHECK_HOME_SKILL = "Build home: {}"
    ROBOT_CHECK_BARN_SKILL = "build barn: {}"
    ROBOT_CHECK_FLOOR_ADD_SKILL = "Add floor: {}"
    ROBOT_CHECK_FLOOR_REMOVE_SKILL = "Remove floor: {}"

    ROBOT_FLOOR_ADD = "{robot_name} have just added 1 floor to building!"
    ROBOT_FLOOR_REMOVE = "{robot_name} have just remove 1 floor from building"
    ROBOT_FLOOR_REMOVE_FAIL = "{robot_name} can't remove any floor from 1 floor building!"

    ROBOT_NAME_V1 = "V"
    ROBOT_NAME_V2 = "Vita"
    ROBOT_NAME_V3 = "Vitaliy"
