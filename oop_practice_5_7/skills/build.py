from classes import Robot, Building, House, Barn


def learn_build_home(robot: Robot) -> None:

    def build_home(self) -> Building:

        print(f"{self.name} только что построил дом!")
        return House()

    robot.build_home = build_home


def learn_build_barn(robot: Robot) -> None:

    def build_barn(self) -> Building:

        print(f"{self.name} только что построил сарай!")
        return Barn()

    robot.build_barn = build_barn
