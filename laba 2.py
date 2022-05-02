import re
buffer_len = 1
flag2=False
flag=False
work_buffer = ""
pattern = '[0-9a-zA-Zа-яА-ЯёЁ]+'
h = 0
try:
    while 1:
        k = input('Введите число k:')
        if (k >= '1') and (k <= '9'):
            digit = int(k)
            break
        else:
            print('введите число большее нуля')
    with open("laba 2.txt", 'r+', encoding='utf-8') as file:
        print("\n Результат работы программы \n")
        buffer = file.read(buffer_len)
        flag = True
        if not buffer:
            print("\n Рабочий файл пустой, измените содержание файла")
        while buffer:
            work_buffer += buffer
            if re.findall(r'[.!?]', buffer):
                if len(work_buffer) == 1:
                    work_buffer = ""
                    flag = True
                if not flag:
                    h += 1
                if len(re.findall(pattern, work_buffer)) == digit:
                    if not work_buffer[0] == " ":
                        work_buffer = " " + work_buffer
                    print("Предложение", h + 1, ":", work_buffer[:len(work_buffer) - 1])
                    flag2 = True
                work_buffer = ""
                flag = False
            buffer = file.read(buffer_len)
        if not flag2:
            print("\n нет предложений подходящих под условие")
        if h == 0:
            print("\n в файле нет предложений подходящих к условию")
except FileNotFoundError:
    print("\n Файл laba 2.txt в директории проекта не обнаружен."
          "\n Добавьте файл в директорию или переименуйте существующий")
