def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else: print("Syntax error")
      
#no se si a alguien le sale esto pero definir aquí arriba cada una de vuestras funciones

def main():
    print("Bienvenidos a nuestra calculadora")
    print("1. Sumar")
    print("2. Restar")  
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
 
  opcion = int(input("Selecciona una opción (1/2/3/4): "))
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))

  if opcion == 1
    print("Resultado:", sumar(num1, num2)")

  elif opcion == 2
    print("Resultado:", restar(num1, num2)")

  elif opcion == 3
    print("Resultado:", multiplicar(num1, num2)")

  elif opcion == 4
    print("Resultado:", dividir(num1, num2)")
          
                
  #añadir otras opciones de la calculadora

   else:
    print("Syntax error")

if __name__ == "__main__":
    main()

#no se si a alguien le sale esto pero definir aquí arriba cada una de vuestras funciones

          