
import pandas as pd
from loguru import logger
_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate","Granizado", "Limon", "Dulce de Leche"], "quantity":[3,10,0,5]})

def is_product_available(product_name, quantity):

    try:
        _PRODUCT_DF.set_index("product_name",inplace=True)
        value = _PRODUCT_DF.loc[product_name]
        if quantity <= value["quantity"]:
            return  True
        else:
            return  False
    except Exception as ex:
        logger.info(f'el producto {product_name} no es valido', {ex})
        