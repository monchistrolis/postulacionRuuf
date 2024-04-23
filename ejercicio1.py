# def cantidad_rectangulos(largo, ancho, largo_panel, ancho_panel):
#     # Calcula el área del techo y el área de un panel solar
#     area_techo = largo * ancho
#     area_panel = largo_panel * ancho_panel

#     # Calcula la cantidad de rectángulos que caben y el área restante
#     cantidad = area_techo // area_panel
#     area_restante = area_techo % area_panel

#     return cantidad, area_restante

# # Ejemplo de uso
# largo = float(input("Ingrese el largo del techo : "))
# ancho = float(input("Ingrese el ancho del techo: "))
# largo_panel = float(input("Ingrese el largo del panel solar: "))
# ancho_panel = float(input("Ingrese el ancho del panel solar: "))

# cantidad, area_restante = cantidad_rectangulos(largo, ancho, largo_panel, ancho_panel)
# print("La cantidad máxima de paneles solares que caben es:", cantidad)
# print("El área restante en el techo es:", area_restante)


def cantidad_rectangulos(largo_techo, ancho_techo, largo_panel, ancho_panel):
    # Verifica si el ancho_techo o el largo_techo del techo son menores que el   # Retorna 0 paneles y el área total del techo

    # Calcula el área del techo y el área de un panel solar
    area_techo = largo_techo * ancho_techo
    area_panel = largo_panel * ancho_panel

    # Calcula la cantidad de rectángulos que caben y el área restante
    cantidad = area_techo // area_panel
    area_restante = area_techo % area_panel

    return cantidad, area_restante


# Ejemplo de medidas 
largo = float(input("Ingrese el largo del techo : "))
ancho = float(input("Ingrese el ancho del techo: "))
largo_panel = float(input("Ingrese el largo del panel solar: "))
ancho_panel = float(input("Ingrese el ancho del panel solar: "))

cantidad, area_restante = cantidad_rectangulos(largo, ancho, largo_panel, ancho_panel)
print("La cantidad máxima de paneles solares que caben es:", cantidad)
print("El área restante en el techo es:", area_restante)
