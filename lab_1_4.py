a = input()
b = input()
if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
    print("фиолетовый")
elif (a == "красный" and b == "жёлтый") or (a == "жёлтый" and b == "красный"):
    print("оранжевый")
elif (a == "синий" and b == "желтый") or (a == "жёлтый" and b == "синий"):
    print("зеленый")
elif a != "синий" or a != "желтый" or a != "красный":
    print("Ошибка")
elif b != "синий" or b != "желтый" or b != "красный":
    print("Ошибка")