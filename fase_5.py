
'''
Nombre: Harold David Muñoz Maldonado
Grupo: 213022B_2201
Ingeniería de sistemas
'''
import time

inventario = [
    ["ART-001", "Resmas de papel A4",          12,  50],
    ["ART-002", "Tóner impresora HP",            3,  10],
    ["ART-003", "Bolígrafos azules",            95,  80],
    ["ART-004", "Grapadora de escritorio",       2,   5],
    ["ART-005", "Papel adhesivo",               18,  30],
]



def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0



def mostrar_inventario(inventario):
    print("\n" + "=" * 65)
    print("                   INVENTARIO ACTUAL")
    print("=" * 65)
    print(f"  {'Código':<10} {'Artículo':<30} {'Actual':>7} {'Mínimo':>7}  {'Estado'}")
    print("-" * 65)
    for articulo in inventario:
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        estado = "⚠ BAJO" if stock_actual < stock_minimo else "✓ OK"
        print(f"  {codigo:<10} {nombre:<30} {stock_actual:>7} {stock_minimo:>7}  {estado}")
    print("=" * 65)
    time.sleep(2.5)



def generar_lista_pedidos(inventario):
    print("\n" + "=" * 50)
    print("       LISTA DE PEDIDOS - REABASTECIMIENTO")
    print("=" * 50)
    hay_pedidos = False
    for articulo in inventario:
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        cantidad = calcular_pedido(stock_actual, stock_minimo)
        if cantidad > 0:
            print(f"  {nombre:<35} → Pedir: {cantidad} unidades")
            hay_pedidos = True
    if not hay_pedidos:
        print("  Todo el inventario está en orden. Sin pedidos pendientes.")
    print("=" * 50)
    time.sleep(1.0)

def buscar_articulo(inventario, codigo):
    for i, articulo in enumerate(inventario):
        if articulo[0].upper() == codigo.upper():
            return i
    return -1



def actualizar_stock(inventario):
    print("\n--- ACTUALIZAR STOCK ---")
    mostrar_inventario(inventario)
    codigo = input("  Ingrese el código del artículo a actualizar: ").strip()
    indice = buscar_articulo(inventario, codigo)
    if indice == -1:
        print(f"  ✗ No se encontró el artículo con código '{codigo}'.")
        return
    nombre       = inventario[indice][1]
    stock_actual = inventario[indice][2]
    print(f"  Artículo : {nombre}")
    print(f"  Stock actual: {stock_actual}")
    try:
        nuevo_stock = int(input("  Nuevo stock actual: "))
        if nuevo_stock < 0:
            print("  ✗ El stock no puede ser negativo.")
            return
        inventario[indice][2] = nuevo_stock
        print(f"  ✓ Stock de '{nombre}' actualizado a {nuevo_stock} unidades.")
    except ValueError:
        print("  ✗ Valor inválido. Ingrese un número entero.")
        time.sleep(1.0)



def agregar_articulo(inventario):
    print("\n--- AGREGAR ARTÍCULO ---")
    codigo = input("  Código del artículo (ej. ART-006): ").strip()
    if buscar_articulo(inventario, codigo) != -1:
        print(f"  ✗ Ya existe un artículo con el código '{codigo}'.")
        return
    nombre = input("  Nombre del artículo: ").strip()
    if not nombre:
        print("  ✗ El nombre no puede estar vacío.")
        return
    try:
        stock_actual = int(input("  Stock actual: "))
        stock_minimo = int(input("  Stock mínimo requerido: "))
        if stock_actual < 0 or stock_minimo < 0:
            print("  ✗ Los valores de stock no pueden ser negativos.")
            return
        inventario.append([codigo, nombre, stock_actual, stock_minimo])
        print(f"  ✓ Artículo '{nombre}' agregado correctamente.")
    except ValueError:
        print("  ✗ Valores inválidos. Ingrese números enteros.")
        time.sleep(1.0)



def eliminar_articulo(inventario):
    print("\n--- ELIMINAR ARTÍCULO ---")
    mostrar_inventario(inventario)
    codigo = input("  Ingrese el código del artículo a eliminar: ").strip()
    indice = buscar_articulo(inventario, codigo)
    if indice == -1:
        print(f"  ✗ No se encontró el artículo con código '{codigo}'.")
        return
    nombre = inventario[indice][1]
    confirmacion = input(f"  ¿Eliminar '{nombre}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        inventario.pop(indice)
        print(f"  ✓ Artículo '{nombre}' eliminado correctamente.")
    else:
        print("  Operación cancelada.")
        time.sleep(1.0)



def menu():
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║     SISTEMA DE AUDITORÍA DE STOCK    ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Ver inventario                   ║")
        print("║  2. Ver lista de pedidos             ║")
        print("║  3. Actualizar stock de un artículo  ║")
        print("║  4. Agregar nuevo artículo           ║")
        print("║  5. Eliminar artículo                ║")
        print("║  6. Salir                            ║")
        print("╚══════════════════════════════════════╝")
        opcion = input("  Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            generar_lista_pedidos(inventario)
        elif opcion == "3":
            actualizar_stock(inventario)
        elif opcion == "4":
            agregar_articulo(inventario)
        elif opcion == "5":
            eliminar_articulo(inventario)
        elif opcion == "6":
            print("\n  Hasta luego.\n")
            break
        else:
            print("  ✗ Opción inválida. Ingrese un número entre 1 y 6.")


menu()