# Thincrs - Python Avanzado
## Reto 1 - Sistema de gestión de inventarios

### Funciones disponibles

- ### **add_product()**
- **update_product()**
- **search_product()**
- **change_quantity()**
- **clear_inventory()**
- **show_all()**

#### Add Product
Te permite añadir un nuevo producto solicitándote Nombre, Descripción, Precio y Cantidad.

#### Update Product
Te permite reescribir todos los valores de los atributos anteriores.

#### Search Product
Te permite buscar por un producto. Soporta búsqueda por nombre, precio y cantidad.

#### Sort Products
Te permite ordenar los productos por alguno de sus atributos: nombre, precio o cantidad. 

#### Change Quantity
Te permite cambiar la cantidad de algún producto. A diferencia de Update Product, únicamente funciona en cantidad, y no te pide el valor por el cual reemplazarlo, más bien te solicita un valor para aumentar o disminuir la cantidad. Por ejemplo, si tenemos 10 muestras del producto X, al aumentar su cantidad por 5, el nuevo valor será 15. Igualmente, al soportar números negativos, se puede usar -5 para que el nuevo valor sea 5. Especialmente útil para manejar stock del producto en tiempo real.

#### Clear Inventory
Borra todo el inventario.

#### Show All
Muestra todos los productos del inventario junto a sus propiedades.
