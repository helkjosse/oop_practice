from classes import Robot

from l10n.localization import Localization


def check_skills(robot: Robot, locale: Localization) -> None:
    print(locale.ROBOT_CHECK_SKILLS.format(robot_name=robot.name))
    print(locale.ROBOT_CHECK_HOME_SKILL.format(hasattr(robot, 'build_home')))
    print(locale.ROBOT_CHECK_BARN_SKILL.format(hasattr(robot, 'build_barn')))
    print(locale.ROBOT_CHECK_FLOOR_ADD_SKILL.format(hasattr(robot, 'add_floor')))
    print(locale.ROBOT_CHECK_FLOOR_REMOVE_SKILL.format(hasattr(robot, 'remove_floor')))
    print()
