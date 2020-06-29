from pywinauto.application import Application
import math
from decimal import Decimal
import numpy as np
from termcolor import colored

#Путь к файлу
path = "C:\\Projects\\CalculatorAutoTest\\"

#Открытие файла
app = Application().start(path + "Calculator_1.exe")

#Вывод доступных контролов
#app.Calculator.print_control_identifiers()

#Открытие файла
report = open(path + "Result.txt", 'w')

#Генерация тестового массива
list1 = np.arange(1, 10)
list2 = np.logspace(2, 9, dtype = 'int')

#Объеденение массивов
joinedList = np.concatenate([list1, list2]) 

#Проверка "LogBase"
print("-----LOG10-----")
for n in joinedList:
    app.Calculator.Edit.set_text(n)
    app.Calculator.button.click()
    
    #Получение результата из программы
    texts = app.Calculator.Static2.texts()
    resultApp = float(texts[0].replace(',', '.'))
    
    #Расчет ожидаемого результата
    resultMath = math.log10(n)
    resultMath = round(resultMath, 14)
    
    #Вывод результата
    textResult = 'Ввод - ' + str(n) + ', log10, ' + str(resultApp) + ' | ' + str(resultMath)

    if resultApp == resultMath:
        print(textResult + colored(' OK', 'green'))
    else:
        report.write(textResult + ' ERROR' "\n")
        print(textResult + colored(' ERROR', 'red'))

#Проверка "Square"
print("-----SQRT-----")
for n in joinedList:
    app.Calculator.Edit.set_text(n)
    app.Calculator.button2.click()
    
    #Получение результата из программы
    texts = app.Calculator.Static2.texts()
    resultApp = float(texts[0].replace(',', '.'))
    
    #Расчет ожидаемого результата
    resultMath = math.sqrt(n)
    resultMath = round(resultMath, 14)
    
    #Вывод результата
    textResult = 'Ввод - ' + str(n) + ', sqrt, ' + str(resultApp) + ' | ' + str(resultMath)

    if resultApp == resultMath:
        print(textResult + colored(' OK', 'green'))
    else:
        report.write(textResult + ' ERROR' "\n")
        print(textResult + colored(' ERROR', 'red'))

report.close()
