# TODO: описать базовый класс


class Human:
    def __init__(self, name: str, age: int):
        """
            Создание и подготовка к работе объекта "человек"

            :param name: Его работа. Приватный, т. к. изменение должно реализоваться через методы.
            :param age: Его возраст. Приватный, т. к. изменение должно реализоваться через методы.

            Примеры:
            >>> person1 = Human('Mike', 19)
        """
        if not isinstance(name, str):
            raise TypeError('name must be str')
        self._name = name
        if not isinstance(age, int):
            raise TypeError('age must be int')
        self._age = age

    def __str__(self) -> str:
        return f'{self._name}, {self._age} years old'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"

    def be_bored_do_nothing(self) -> None:
        """
            Метод, реализующий пустую трату времени объектом.
            Не наследуется, т. к. некоторые люди не могут впустую тратить время.
        """
        self._age += 1

    def change_the_name(self, new_name: str) -> None:
        """
            Метод, реализующий сменну имени объектом.
            Наследуеться, т. к. смена имени для всех проходит одинаково.
        """
        self._name = new_name


# TODO: описать дочерний класс
class Grad_Student(Human):
    def be_bored_do_nothing(self) -> None:
        """
            Метод, реализующий "пустую" трату времени объектом.
        """
        self._age += 1
        print('Вы провели какое-то исследование вместо того, чтобы сделать перерыв.')
