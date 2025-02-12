from task_1 import Physicist, Bodybuilder, Polyglot
student1 = Physicist('none', 'something')
gymbro = Bodybuilder(19, 'none', 100)
adonis = Polyglot(10, 80)
if __name__ == "__main__":
    try:
        student1.get_a_life(1)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        gymbro.get_injured(1)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        adonis.acquire_a_language(1)
    except TypeError:
        print('Ошибка: неправильные данные')
