# -----------------------------------------------------------
# LAB 03 - Dando formato a la salida
# -----------------------------------------------------------
# Este programa imprime una figura con forma de flecha usando
# la función print().
#
# Cada línea del print representa una fila de la figura.
# Se utilizan espacios para alinear correctamente los asteriscos.
# -----------------------------------------------------------

# Parte superior de la flecha (punta)
print("    *")       # 4 espacios + 1 asterisco
print("   * *")      # 3 espacios + 2 asteriscos separados
print("  *   *")     # 2 espacios + 2 asteriscos con más separación
print(" *     *")    # 1 espacio + forma más ancha

# Parte central (base de la punta)
print("***   ***")   # 3 asteriscos, espacios, 3 asteriscos

# Parte inferior (cuerpo de la flecha)
print("  *   *")     # repetición para dar forma vertical
print("  *   *")
print("  *****")     # base de la flecha

# -----------------------------------------------------------
# Variante usando un solo print con saltos de línea (\n)
# -----------------------------------------------------------

print("\n--- Versión con un solo print ---\n")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")