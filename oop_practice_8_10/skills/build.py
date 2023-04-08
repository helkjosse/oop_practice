from classes import Robot, Building, House, Barn

from l10n.localization import Localization


def learn_build_home(robot: Robot, locale: Localization) -> None:

    def build_home() -> Building:
        print(locale.ROBOT_BUILD_HOME_COMPLETE.format(robot_name=robot.name))
        return House()

    robot.build_home = build_home


def learn_build_barn(robot: Robot, locale: Localization) -> None:

    def build_barn() -> Building:
        print(locale.ROBOT_BUILD_BARN_COMPLETE.format(robot_name=robot.name))
        return Barn()

    robot.build_barn = build_barn
