# 4 Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6


list_4 = [0, 9, 8, 7, 4, 5, "word", 6, 7, 8]

list_4.insert(2, "hello")
del list_4[6]
print(list_4)