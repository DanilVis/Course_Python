# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Функция для сжатия данных
def rle_encode(data_string):
    res_list = []
    count = 0
    for i in data_string:
        if i == data_string[0]:
            count += 1
        else:
            res_list.append((count, data_string[0]))
            data_string = data_string[count:]
            count = 1
    res_list.append((count, data_string[0]))
    return res_list


# Превразение списка кортежей в строку для сжатых данных
def encoded_str(t_list):
    result = ''
    for item in t_list:
        if item[0] == 1:
            result += item[1]
        else:
            result += str(item[0]) + item [1]
    return result


# Функция для восстановления данных
def rle_decode(data_string):
    res_list = []
    count = 0
    for i in data_string:
        if i.isdigit():
            count += 1
            continue
        else:
            if i == data_string[0]:
                res_list.append((1, i))
            else:
                res_list.append((int(data_string[:count]), i))
            data_string = data_string[count + 1:]
            count = 0
    return res_list


# Превращение списка кортежей в строку для восстановленных данных
def decoded_str(t_list):
    result = ''
    for item in t_list:
        result += item[0] * item[1]
    return result


# Сжатие данных из файла
with open('G:/Seminars/Python/PythonCourse/Seminar5/Homework_5/rle_input.txt', 'r') as data1:
    input_data = data1.read()

output_data = encoded_str(rle_encode(input_data))
print(output_data)

with open('G:/Seminars/Python/PythonCourse/Seminar5/Homework_5/rle_output.txt', 'w') as output1:
    output1.write(output_data)

# Восстановление данных из файла
with open('G:/Seminars/Python/PythonCourse/Seminar5/Homework_5/rle_output.txt', 'r') as data2:
    encoded_data = data2.read()

decoded_data = decoded_str(rle_decode(encoded_data))
print(decoded_data)

with open('G:/Seminars/Python/PythonCourse/Seminar5/Homework_5/rle_input.txt', 'w') as output2:
    output2.write(decoded_data)
