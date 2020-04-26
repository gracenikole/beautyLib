### Calculadora

# Sumar 
def add(x, y):
  return x + y

# Restar
def subtract(x, y):
  return x - y

# Multiplicar
def multiply(x, y):
  return x * y

print("Selecciona una operación.")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")

# Take input from the user 
choice = input("Escoge una opción (1/2/3): ")

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

if choice == '1':
  print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
  print(num1,"*",num2,"=", multiply(num1,num2))
  
else:
  print("Input Inválido")