*Fundamentos de Python*
-Descripción general-

#Este repositorio contiene el desarrollo de los laboratorios de la guía "Fundamentos de Python", abarcando conceptos básicos como impresión en pantalla, literales, operadores y variables. Cada sección incluye scripts en Python y la explicación correspondiente en este archivo.
#----------------------------------------------
Sección 1 – Función print()
#---------------------------------------------
LAB: Trabajando con la función print()

*Código utilizado*

print("¡Hola, Mundo!")
print("Isabuitrago")

*Preguntas*

¿Qué ocurre al eliminar las comillas?
Se genera un error de tipo NameError porque Python interpreta el texto como una variable no definida.
¿Qué ocurre al eliminar los paréntesis?
Se genera un error de tipo SyntaxError porque la función print requiere paréntesis.

*Conclusión*
La función print() permite mostrar texto en pantalla y requiere el uso correcto de comillas y paréntesis.

#-------------------------------------------------
LAB: La función print() y sus argumentos

*Código utilizado*

print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

*Salida*
ProgrammingEssentialsin...Python

*Explicación*

sep permite definir el separador entre palabras.
end permite definir cómo termina la línea.
#-------------------------------------------
LAB: Dando formato a la salida

*Código utilizado*

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

*Conclusión*
Se puede controlar la salida usando espacios, saltos de línea y caracteres especiales.
 
 #-----------------------------------------------------------
Sección 2 – Literales
#---------------------------------------------------------

LAB: Literales de Python - Cadenas

*Código utilizado*

print("2")
print(2)

*Pregunta*
¿Cuál es la diferencia entre ambos?

*Respuesta*

"2" es una cadena de texto.
2 es un número entero.

*Conclusión*
Los literales representan datos directamente en el código y su tipo depende de su formato.

#------------------------------------------------------------
Sección 3 – Operadores
#------------------------------------------------------------

Ejercicios de operadores

Se resolvieron manualmente y se verificaron en Python.

*Ejemplo*
Expresión: 5 + 3 * 2
Resultado: 11

*Explicación*
La multiplicación se realiza primero por prioridad de operadores.

*Conclusión*
El orden de operaciones es:

Paréntesis
Potencias
Multiplicación y división
Suma y resta
Sección 4 – Variables

#-------------------------------------------------------------
LAB: Variables

*Código utilizado*

john = 3
mary = 5
adam = 6

total_apples = john + mary + adam

print(john, mary, adam)
print("Total de manzanas:", total_apples)

*Conclusión*
Las variables permiten almacenar datos y utilizarlos en operaciones.

#-------------------------------------------------------------
LAB: Convertidor de unidades

*Código utilizado*

miles = 7.38
kilometers = 12.25

kilometers = miles * 1.61
print(miles, "millas son", round(kilometers, 2), "kilómetros")

kilometers = 12.25
miles = kilometers / 1.61
print(kilometers, "kilómetros son", round(miles, 2), "millas")

*Explicación*
Se aplican fórmulas matemáticas para convertir unidades de medida.

#--------------------------------------------------------------
LAB: Operadores y expresiones
*Código utilizado*

x = 0
x = float(x)

y = 3 * x**3 - 2 * x**2 + 3 * x - 1

print("y =", y)

*Resultados de prueba*
x = 0 → y = -1.0
x = 1 → y = 3.0
x = -1 → y = -9.0

*Conclusión*
Las expresiones permiten combinar operadores para resolver cálculos matemáticos.

#------------------------------------------------------------
LAB – Algoritmos

Se desarrolló un programa con menú que resuelve 16 problemas relacionados con mecánicas de videojuegos, como:

Cálculo de puntaje
Tiempo de juego
Daño total
Experiencia
Porcentajes
Promedios

*Ejecución*

python src/puntaje_final_jugador.py

*Conclusión*
Este laboratorio integra todos los conceptos aprendidos: variables, operadores, entrada de datos y lógica de programación.

*Conclusión general*

Este proyecto permitió comprender y aplicar los fundamentos de Python mediante ejercicios prácticos. Se desarrollaron habilidades en el uso de variables, operadores, estructuras básicas y resolución de problemas.
