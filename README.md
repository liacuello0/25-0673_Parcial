# Pruebas Unitarias para DummyJSON API

## 📌 Descripción
Este proyecto implementa pruebas unitarias para la API de DummyJSON utilizando `pytest`. Las pruebas verifican diversas funcionalidades, como la obtención, creación, actualización y eliminación de productos, así como la validación de imágenes generadas.

## 📂 Estructura del Proyecto
- `pruebas.py`: Archivo que contiene las pruebas unitarias.
- `README.md`: Documentación del proyecto.

## 🛠️ Instalación y Configuración
### 1️⃣ Clonar el Repositorio
```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### 2️⃣ Crear un Entorno Virtual (Opcional pero Recomendado)
```sh
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate    # En Windows
```

### 3️⃣ Instalar Dependencias
```sh
pip install -r requirements.txt
```
> **Nota:** Si no tienes `pip`, instala las dependencias con:
> ```sh
> python -m pip install pytest requests
> ```

## 🚀 Ejecución de las Pruebas
Para ejecutar las pruebas, usa el siguiente comando:
```sh
pytest pruebas.py
```
Esto mostrará el resultado de cada prueba y posibles errores detectados.

## 📌 Casos de Uso Cubiertos
| Prueba | Descripción |
|--------|-------------|
| `test_get_all_products` | Verifica que se obtienen correctamente los productos de la API. |
| `test_get_single_product` | Comprueba la obtención de un producto específico. |
| `test_create_product` | Valida la creación de un nuevo producto. |
| `test_update_product` | Asegura que la actualización de un producto funciona correctamente. |
| `test_delete_product` | Verifica la eliminación de un producto. |
| `test_get_image` | Comprueba la correcta generación de una imagen desde la API. |
