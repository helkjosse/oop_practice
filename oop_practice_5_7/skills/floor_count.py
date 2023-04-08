from classes import Robot, Building


def learn_add_floor(robot: Robot) -> None:

    def add_floor(self, building: Building) -> None:

        building.floors += 1
        print(f"{self.name} только что увеличил количество этажей на 1!")

    robot.add_floor = add_floor


def learn_remove_floor(robot: Robot) -> None:
    """
    Научить робота увеличивать количество этажей
    """

    def remove_floor(self, building: Building) -> None:
        """
        Построить 1 этаж у постройки
        """

        if building.floors == 1:
            print(f"{self.name} не может больше уменьшить количество этажей!")

        else:
            building.floors -= 1
            print(f"{self.name} только что уменьшил количество этажей на 1!")

    robot.remove_floor = remove_floor
