data = [line for line in open('input.txt', 'r').read().split('\n') if line.strip()]

unSafe = 0

for i in data:
    newList = list(map(int, i.split()))
    is_increasing = None  # Inicialmente desconocido
    
    for j in range(len(newList) - 1):
        num1 = newList[j]
        num2 = newList[j + 1]
        difference = abs(num1 - num2)
        
        # Verificar si la diferencia está fuera del rango permitido
        if difference > 3 or difference == 0:
            unSafe += 1
            break
        
        # Determinar la dirección en la primera iteración
        if is_increasing is None:
            is_increasing = num1 < num2
        
        # Verificar que la dirección sea consistente
        if (num1 < num2) != is_increasing:
            unSafe += 1
            break

# El número de informes seguros es el total menos los inseguros
safe = len(data) - unSafe
print(safe)
