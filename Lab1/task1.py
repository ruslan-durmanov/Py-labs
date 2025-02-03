import doctest


class Physicist:
    def __init__(self, occupation: str, hobbies: str = None):
        """
        Создание и подготовка к работе объекта "физик"

        :param occupation: Его работа
        :param hobbies: Его хобби

        Примеры:
        >>> student1 = Physicist('not a janitor')
        Nice
        """
        if not isinstance(occupation, str):
            raise TypeError('Occupation must be a string')
        if occupation.casefold() == 'janitor'.casefold() or occupation.casefold() == 'coder'.casefold():
            raise ValueError('Really?')
        self.occupation = occupation
        if hobbies is None:
            print('Nice')
        self.hobbies = hobbies
        self.semesters_passed = 0
        self.social_life = None

    def survive_the_midterms(self) -> bool:
        """
        Функция которая проверяет пережил ли студент зимнюю сессию

        :return: пережил ли студент зимнюю сессию (Boolean)
        :raise: ValueError мы не допускаем ничего кроме благодетели

        Примеры:
        >>> student1 = Physicist('not a janitor')
        Nice
        >>> student1.survive_the_midterms()
        True
        """
        if self.hobbies is None:
            return True
            self.semesters_passed += 1
        else:
            if self.hobbies.casefold() == 'vice'.casefold():
                raise ValueError('We do not do that here, lil bro.')
            return False

    def get_a_life(self, want_a_life: str = 'no') -> None:
        """
        Функция, позволяющая увеличить количество пройденных семестров или дать объекту личную жизнь

        :param want_a_life: нужна ли физику личная жизнь
        :raise: TypeError: get_a_life должен быть строкой

        Примеры:
        >>> student1 = Physicist('not a janitor')
        Nice
        >>> student1.get_a_life()
        """
        if not isinstance(want_a_life, str):
            raise TypeError('hobbies must be a string')
        if want_a_life.casefold() == 'no'.casefold() or 'nope'.casefold():
            self.semesters_passed += 1
            return
        if self.semesters_passed <= 4:
            print('Nope')
        else:
            self.social_life = 'exists'


class Bodybuilder:
    def __init__(self, age_in_years: int, occupation: str, weight: float):
        """
        Создание и подготовка к работе объекта "бодибилдер"

        :param age_in_years: возраст в годах
        :param occupation: работа, если она есть
        :param weight: вес в килограммах

        Примеры:
        >>> gymbro = Bodybuilder(19, 'none', 100)
        """
        if not isinstance(age_in_years, int):
            raise TypeError('Age is just a number, an integer to be exact')
        self.age_in_years = age_in_years
        if not isinstance(occupation, str):
            raise TypeError('Occupation must be a string')
        if occupation.casefold() == 'physicist'.casefold():
            print('How?')
        self.occupation = occupation
        if not isinstance(weight, (float, int)):
            raise TypeError('Weight must be a number')
        self.weight = weight
        self.bodyfat_percentage = 20

    def train(self) -> tuple:
        """
        Функция которая улучшает физические показатели бодибилдера и возвращает их

        :return: процент жира, вес, вес без учета жира

        Примеры:
        >>> gymbro = Bodybuilder(19, 'none', 100)
        >>> gymbro.train()
        (19, 101, 81.81)
        """
        if self.bodyfat_percentage > 6:
            self.bodyfat_percentage -= 1
        self.weight += 1
        fat_free_mass = self.weight * (100 - self.bodyfat_percentage) / 100
        return self.bodyfat_percentage, self.weight, fat_free_mass

    def get_injured(self, gravity: str = 'severe') -> None:
        """
        Функция которая реализует травму

        :param: gravity: насколько серьёзна травма
        :raises: TypeError: тяжесть травмы должна быть строкой

        Примеры:
        >>> gymbro = Bodybuilder(19, 'none', 100)
        >>> gymbro.get_injured()
        """
        if not isinstance(gravity, str):
            raise TypeError('Gravity must be a string')
        if gravity.casefold() == 'severe'.casefold():
            self.age_in_years += 1
            self.bodyfat_percentage += 5
            self.weight += 3
        else:
            self.age_in_years += 1


class Polyglot:
    """
    Создание и подготовка к работе объекта "полиглот"

    :param num_of_languages: количество языков
    :param age_in_years: возраст в годах

    Примеры:
    >>> adonis = Polyglot(10, 80)
    """

    def __init__(self, num_of_languages: int, age_in_years: int):
        if not isinstance(num_of_languages, int):
            raise TypeError('How is that possible? Fractional number of languages, seriously?')
        if num_of_languages == 1:
            raise ValueError('Monolingual≠polyglot')
        self.num_of_languages = num_of_languages
        if not isinstance(age_in_years, int):
            raise TypeError('How is that possible? Fractional age, seriously?')
        self.age_in_years = age_in_years

    def check_for_altzheimers(self) -> str:
        """
        Функция которая проверяет на болезнь Альцгеймера

        :return: какова вероятность болезни Альцгеймера у объекта

        Примеры:
        >>> adonis = Polyglot(10, 80)
        """
        if self.age_in_years <= 50:
            return 'Come in later'
            if self.num_of_languages == 2:
                return 'No'
            elif self.num_of_languages == 3:
                return 'Nope'
        else:
            return 'Definitely not altzheimers'

    def acquire_a_language(self, did_work_hard: str = 'yes') -> None:
        """
        Функция которая реализует изучение новых языков

        :param did_work_hard: насколько жестко велась работа
        :raise: ValueError: did_work_hard должен быть строкой

        Примеры:
        >>> adonis = Polyglot(10, 80)
        """
        if not isinstance(did_work_hard, str):
            raise TypeError('Did_work_hard must be a string')
        if did_work_hard.casefold() == 'yes'.casefold():
            self.num_of_languages += 1
