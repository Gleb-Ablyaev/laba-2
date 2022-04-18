import re
buffer_len = 1
work_buffer = ""
b = ""

try:
    while 1:
        print("\n введите число k")
        number = (input("k="))
        if '0' <= number <= '9':
            k = int(number)
            break
        else:
            print('это не цифра')

    with open("laba 2.txt", "r") as file:
        print("\n результат работы программы \n")
        buffer = file.read(buffer_len)

        if not buffer:
            print("\n рабочий файл пустой, измените содержание файла")

        while buffer:
            work_buffer += buffer
            if re.findall(r'[.!?]', buffer):
                b = re.split(r'\W', work_buffer)
                b = b[:len(b)-1]
                if len(b) == k:
                    print(work_buffer)
                g = ""
                work_buffer = ""

            buffer = file.read(buffer_len)
        if re.findall(r'[^.!?]', work_buffer):  # Если буфер переполнен и нет окончания предложения
            print("\nФайл *.txt не содержит знаков окончания предложения.\nОткорректируйте файл *.txt в директории или переименуйте существующий *.txt файл.")


except FileNotFoundError:
    print("\n файл *.txt в директории проекта не обнаружен.\n Добавьте файл в директорию или переименуйте существующий")
