from tools import create_circle, create_rect, create_triangle


def main() -> None:
    figure_list = []

    print("Создание списка фигур")
    print()
    dimensions = int(input("Введите количество измерений пространств: "))
    figure_count = int(input("Введите количество фигур в списке: "))
    print()

    for i in range(figure_count):
        print(f"Фигура №{i + 1}")
        cycle = True

        while cycle:
            figure_type = input("Введите тип фигуры: ").lower()

            if figure_type in ["0", "треугольник"]:
                figure = create_triangle(dimensions)

            elif figure_type in ["1", "прямоугольник", "квадрат"]:
                figure = create_rect(dimensions)

            elif figure_type in ["2", "окружность", "круг"]:
                figure = create_circle(dimensions)

            else:
                print("Такого типа фигуры не существует! Попробуйте ещё раз!")
                continue

            figure_list.append(figure)
            cycle = False

        print("Фигура создана и добавлена в список")
        print()

    figure_list = sorted(figure_list, key=lambda s: s.get_area())
    response = "Список отсортирован по показателям площади\nСписок фигур: \n"

    for i in figure_list:
        response += "\t" + i.output() + "\n"

    else:
        print("Ваш результат: ", response)


# Запуск через "python3 app.py"
if __name__ == "__main__":
    main()
