from loguru import logger

"""
Ejercicio 3:
Completar la función validate_discount_code con el siguiente objetivo:
● Dada la lista de códigos de descuento vigentes y un código de descuento mencionado por el cliente, devuelve True si la diferencia entre el código mencionado y los códigos vigentes es menor a tres caracteres, en al menos uno de los casos.
Por diferencia se entiende: caracteres que están presentes en el código brindado, pero no en el código evaluado de la lista o viceversa.
"""

_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen"]

def validate_discount_code(discount_code):
    
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o','m', 'V', 'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0','x', 'e', 'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i','v', 'n', 'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """
    try:
        for codes in _AVAILABLE_DISCOUNT_CODES:
            value_1 = set(codes)
            value_2 = set(discount_code)
            if len(value_1 ^ value_2) <= 3:
                return True
        return False
    except Exception as ex:
        logger.info(ex)

print(validate_discount_code("primavera2021"))


