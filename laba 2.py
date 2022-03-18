import time

try:
    while 1:
        print("\n введите число k")
        number = (input("k="))
        if number >= '0' and number <= '9':
            k = int(number)
            break
        else:
            print('это не цифра')
    start=time.time()
    with open("laba 2.txt","r") as file:
        print("\n результат работы программы \n")
        data=file.read()

        if not data:
            print("\n рабочий файл пустой, измените содержание файла")

        if data:
            mass = data.split('.')
            mass2 = []
            i = 1

            print("\n предложения согласно условию:")
            for i in range(0, len(mass)):
                mass2.append(mass[i].split())
                if len(mass2[i]) == k:
                    print(mass[i], '.')

    finish=time.time()
    result=finish-start
    print("program time: " + str(result) + "seconds.")

except FileNotFoundError:
    print("\n файл laba 2.txt в директории проекта не обнаружен.\n Добавьте файл в директорию или переименуйте существующий")
