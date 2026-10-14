# Проект FitLife - MVP версия 1.0
MAX_HEIGHT = 2.5  # максимальный рост.
MIN_HEIGHT = 0.5  # минимальный рост.
MAX_WEIGHT = 500  # максимальный вес. Примерно.
MIN_WEIGHT = 3.5  # минимальный вес. Средний вес ребенка при рождении.
MIN_AGE = 1  # минимальный возраст.
MAX_AGE = 120  # максимальный возраст.
MIN_BMI = 18.5  # минимальный ИМТ
MAX_BMI = 25  # максимальный ИМТ
WATER_PER_KG = 30  # необходимое кол-во выды на кг
ML_TO_L = 1000  # кол-во мл в л

USER_AGE_Q = "Cколько Вам полных лет?"
USER_WEIGHT_Q = "Какой у Вас вес (в кг)? Например, 65.7"
USER_HEIGHT_Q = "Какой у Вас рост (в м)? Например, 1.7"

# Текст знакомства
USER_HELLO = (
    "\nЗдравствуйте, меня зовут FitLifeBot.\n"
    "Я помогаю следить за Вашим здоровьем.\n"
)

# Текст ошибки при вводе неверного числа
USER_ERROR_NUMBER = (
    "\nВы ввели слишком большое или маленькое число.\n"
    "Пожалуйста попробуйте снова."
)

# Текст ошибки при вводе текста или числа с несколькими "," или "."
USER_ERROR_TEXT = (
    "Похоже Вы ввели не число.\n"
    "Пожалуйста, попробуйте снова.\n"
)


# 1. Знакомство

print(USER_HELLO)
user_name = input("Как я могу к Вам обращаться? (Введите свое имя)\n")
user_name = user_name.strip().title()
print("\nЗдравствуйте,", user_name, "!")

# Узнаем возраст

while True:
    user_age = float(input(f"\n{USER_AGE_Q}\n").replace(",", "."))
    try:
        user_age = int(user_age)
        if MIN_AGE < user_age < MAX_AGE:
            break
        else:
            print(USER_ERROR_NUMBER)
    except ValueError:
        print(USER_ERROR_TEXT)

# 2. Сбор данных

# Узнаем вес

while True:
    user_weight = input(f"\n{USER_WEIGHT_Q}\n").replace(",", ".")
    try:
        user_weight = float(user_weight)
        if MIN_WEIGHT < user_weight < MAX_WEIGHT:
            break
        else:
            print(USER_ERROR_NUMBER)
    except ValueError:
        print(USER_ERROR_TEXT)

# Узнаем рост

while True:
    user_height = input(f"\n{USER_HEIGHT_Q}\n").replace(",", ".")
    try:
        user_height = float(user_height)
        if MIN_HEIGHT < user_height < MAX_HEIGHT:
            break
        else:
            print(USER_ERROR_NUMBER)
    except ValueError:
        print(USER_ERROR_TEXT)


# Расчет ИМТ

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Простой расчет результата по данным ИМТ

if bmi <= MIN_BMI:
    bmi_result = "Недостаточная (дефицит) масса тела"
elif MIN_BMI < bmi <= MAX_BMI:
    bmi_result = "Нормальная масса тела"
elif bmi > MAX_BMI:
    bmi_result = "Избыточная масса тела"

# Подсчет воды

water_ml = user_weight * WATER_PER_KG
water_needed = round(water_ml / ML_TO_L, 1)

# Выводим вводные

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")  # имя, возраст
print(f"Ваш вес: {user_weight} кг")  # вес
print(f"Ваш рост: {user_height} м")  # рост

# Выводим расчеты

print(f"Ваш Индекс Массы Тела: {bmi}")  # ИМТ
print(f"По вычисленному ИМТ у Вас: {bmi_result} ")  # выводим результат по ИМТ
print(f"Рекомендуемая норма воды: {water_needed} л. в день")
print("\nРасчет окончен. Будьте здоровы!\n")
