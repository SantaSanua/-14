array = [int(x) for x in input("Введіть елементи масиву через пробіл: ").split()]
try:
    search = int(input("Яке число найти?"))
except:
    print("невірно задане число")
    

if search in array:
    print(f"Масив містить значення {search}.")
else:
    print(f"Масив не містить значення {search}.")
