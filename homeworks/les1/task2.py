"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time_in_second = input("введите время в секундах:")
hours = float(time_in_second)/3600
hours = int(hours)
minutes = (float(time_in_second)-hours*3600)/60
minutes = int(minutes)
seconds = float(time_in_second)-hours*3600-minutes*60
seconds = int(seconds)
print(f"время: {hours}:{minutes}:{seconds}")
