immutable_var = ([1, 2], "PuP", True)
print(immutable_var)
immutable_var[0][0] = 5
# Мы можем изменять элементы внутреннего списка, но не сам список, т.е. мы можем поменять вышеуказанные значения внутри списка (1 на 5), но не можем поменять порядок, тип данных или полностью изменить часть коллекции кортежа.
print(immutable_var)

mutable_var = [1, 15, "Пупа дупа", False]
print(mutable_var)
mutable_var[1] = "Шик пошик"
mutable_var[3] = 315
print(mutable_var)
#В спикске мы можем полность менять всю структуру, как и указано выше.