def input_number():
    while True:
        a = input("Введите число: ")
        try: 
            return float(a)
        except: 
            try:
                return complex(a)
            except: 
                print("Неверный ввод! Попробуйте ввести число ещё раз.")


def input_operation():
    while True:
        print("Введите номер операции: ")
        print("1 - Сложение +")
        print("2 - Вычитание -")
        print("3 - Умножение *")
        print("4 - Деление /")
        #print("0 - Возврат")
        op = input()
        if op not in ["1","2","3","4"]:
            print("Такой операции нет")
            continue
        return op
    