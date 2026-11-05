"""Clase que representa un producto del inventario."""

class Producto:
    """Representa un producto con código, nombre, precio y existencia."""

    def __init__(self, codigo, nombre, precio, existencia):
        """Inicializa los datos del producto.

        Args:
            codigo (str): Código identificador del producto.
            nombre (str): Nombre del producto.
            precio (float): Precio unitario del producto.
            existencia (int): Cantidad disponible en inventario.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        """Muestra la información del producto en pantalla."""
        print("Información del producto")
        print("------------------------")
        print(f"Código:      {self.codigo}")
        print(f"Nombre:      {self.nombre}")
        print(f"Precio:      {self.precio}")
        print(f"Existencia:  {self.existencia}")


if __name__ == "__main__":
    # Ejemplo de uso
    producto = Producto("P-001", "Laptop Dell", 12500.50, 15)
    producto.mostrar_informacion()
