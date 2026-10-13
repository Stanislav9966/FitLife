# Проект FitLife - MVP версия 1.0
max_height = 2.5  # максимальный рост.
min_height = 0.5  # минимальный рост.
max_weight = 500  # максимальный вес. Примерно.
min_weight = 3.5  # минимальный вес. Средний вес ребенка при рождении.
min_age = 1  # минимальный возраст.
max_age = 120  # максимальный возраст.
user_age_q = "Cколько Вам полных лет?"
user_weight_q = "Какой у Вас вес (в кг)? Например, 65.7"
user_height_q = "Какой у Вас рост (в м)? Например, 1.7"

# 1. Знакомство

print("\nЗдравствуйте, меня зовут FitLifeBot.\n")
print("Я помогаю следить за Вашим здоровьем.")
user_name = input("Как я могу к Вам обращаться? (Введите свое имя)\n")
user_name = user_name.title()
print("\nЗдравствуйте,", user_name, "!")

# Узнаем возраст

while True:
    user_age = float(input(f"\n{user_age_q}\n").replace(",", "."))
    try:
        user_age = int(user_age)
        if min_age < user_age < max_age:
            break
        else:
            print("\nВы ввели слишком большое или маленькое число.")
            print("Пожалуйста, попробуйте снова.")
    except ValueError:
        print("\nПохоже Вы ввели не число.")
        print("Пожалуйста, попробуйте снова.")

# 2. Сбор данных

# Узнаем вес

while True:
    user_weight = input(f"\n{user_weight_q}\n").replace(",", ".")
    try:
        user_weight = float(user_weight)
        if min_weight < user_weight < max_weight:
            break
        else:
            print("\nВы ввели слишком большое или маленькое число.")
            print("Пожалуйста, попробуйте снова.")
    except ValueError:
        print("\nПохоже Вы ввели не число.")
        print("Пожалуйста, попробуйте снова.")

# Узнаем рост

while True:
    user_height = input(f"\n{user_height_q}\n").replace(",", ".")
    try:
        user_height = float(user_height)
        if min_height < user_height < max_height:
            break
        else:
            print("\nВы ввели слишком большое или маленькое число.")
            print("Пожалуйста, попробуйте снова.")
    except ValueError:
        print("\nПохоже Вы ввели не число.")
        print("Пожалуйста, попробуйте снова.")


# Расчет ИМТ

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Простой расчет результата по данным ИМТ

if bmi <= 18.5:
    bmi_result = "Недостаточная (дефицит) масса тела"
elif 18.5 < bmi <= 25:
    bmi_result = "Нормальная масса тела"
elif bmi > 25:
    bmi_result = "Избыточная масса тела"

# Подсчет воды

water_ml = user_weight * 30
water_needed = round(water_ml / 1000, 1)

# Выводим вводные

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")  # имя, возраст
print(f"Ваш вес: {user_weight} кг")  # вес
print(f"Ваш рост: {user_height} м")  # рост

# Выводим расчеты

print(f"Ваш Индекс Массы Тела: {bmi}")  # ИМТ
print(f"По вычисленному ИМТ у Вас: {bmi_result} ")  # выводим результат по ИМТ
print(f"Рекомендуемая норма воды: {water_needed} л. в день")
print("\nРасчет окончен. Будьте здоровы!\n")
