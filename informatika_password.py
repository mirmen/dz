print("Verlix Security")
print("===========")
print("Авторизация")
username = input("Логин:")
if username == "admin" :
    print ("Поиск логина в базе данных...")
    print("Успешно! Логин найден..")

else :
    print ("Логин некорректный.. Пожалуйста попробуйте снова")
    exit()


password = input ("Пароль:")
if password  == "adminpass" :
    print ("=====УСПЕШНЫЙ ВХОД=====")
    print ("Добро пожаловать, Администратор")
    # проверка
else :
    print ("Некорректный пароль.." , "Пожалуйста попробуйте снова...")
    exit()