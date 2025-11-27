# Proyecto de Automatización de Pruebas

## Propósito


El objetivo de este proyecto es demostrar habilidades adquiridas en automatización de pruebas web y API.  
Incluye pruebas E2E con Selenium, manejo de datos externos, generación de logs, uso de Faker, comunicación con APIs y aplicación de buenas prácticas utilizando Page Object Model (POM), pytest y utilidades reutilizables.

Este proyecto sirve como demostración de:

- Automatización de pruebas end-to-end en una aplicación web.
- Automatización de pruebas API externas.
- Lectura de datos desde archivos CSV y JSON.
- Generación de datos dinámicos con Faker.
- Implementación de logs centralizados.
- Organización modular con Page Object Model.
- Uso de frameworks de testing y control de versiones con Git/GitHub.

---

## Herramientas utilizadas

- **Python**
- **Selenium**
- **pytest**
- **Faker**
- **Requests** (para pruebas API)
- **Google Chrome WebDriver**
- **Git y GitHub**
- **logging** (Python, implementación propia en `utils/logger.py`)

---

## Estructura del proyecto

```text
TestingQA-Automation/

├── utils/ # Funciones reutilizables
│ ├── init.py
│ ├── driver_setup.py # Configuración del driver Selenium
│ ├── login.py # (Versión antigua, aún puede usarse si aplica)
│ ├── title_check.py # Función para validar títulos
│ ├── json_reader.py # Lectura de archivos JSON
│ ├── data.py # Lectura de archivos CSV / configuración
│ └── logger.py # Logger central del proyecto
├── pages/ # Page Object Model (POM)
│ ├── login_page.py
│ ├── inventory_page.py
│ └── cart_page.py
├── datos/
│ ├── data_login.csv # Datos de prueba para login
│ └── productos.json # Datos de productos
├── logs/
│ └── suite.log # Log general generado durante la ejecución
├── tests/ # Scripts de prueba
│ ├── test_login.py # Login clásico
│ ├── test_login_faker.py # Login usando Faker
│ ├── test_inventary.py # Validación de inventario
│ ├── test_badge.py # Carrito (UI)
│ ├── test_badge_json.py # Validación carrito usando datos JSON
│ └── test_api_reqres.py # Test API externa Reqres
├── conftest.py # Fixtures para pytest
├── run_tests_files.py # Ejecuta los tests y genera reporte HTML
└── README.md

```
---

## Instalación de dependencias

Clonar el repositorio:

git clone <https://github.com/DanOlmed/pre-entrega-automation-testing-Daniel-Olmedo.git>


Entrar en la carpeta del proyecto:

+ cd TestingQA-Automation

Alternativamente, instalar manualmente:

+ pip install selenium pytest faker requests

Dependencias adicionales que usa el proyecto:

+ faker → genera nombres, mails, contraseñas falsas.

+ requests → permite hacer pruebas API.

+ logging → ya viene integrado con Python, pero se implementó un logger personalizado en utils/logger.py.


+ Descargar e instalar Chrome WebDriver compatible con tu versión de Chrome:
Descargar ChromeDriver

+ Colocar el ejecutable en la carpeta del proyecto o en una ruta incluida en el PATH.

## Ejecución de las pruebas

+ Abrir la terminal o consola en la carpeta raíz del proyecto.

### Ejecutar todos los tests:
+ Primer método: 
Para ejecutar todos los tests y ademas generar el reporte, se debe correr el archivo run_tests_files.py

+ Segundo método: 
```
python -m pytest -s tests 

 -s permite que se vean los print() en consola.

Todos los archivos test_*.py dentro de tests/ serán detectados automáticamente.
```

### Generar un reporte HTML opcional:
```
python -m pytest --html=report.html -s tests
```

### Para ejecutar un test específico:

```
python -m pytest -s tests/test_login.py
```

### Descripción de los tests
```
1. test_login.py

Login con credenciales válidas.

Verifica URL final.

Imprime mensaje de éxito.

2. test_login_faker.py

Login generado dinámicamente con Faker.

Útil para pruebas negativas o de validación.

3. test_inventary.py

Revisa inventario tras el login.

Verifica título “Products”.

Valida que existan productos.

4. test_badge.py

Añade un producto al carrito.

Verifica badge = 1.

Comprueba que aparece en el carrito.

5. test_badge_json.py

Lee datos desde productos.json.

Valida información del carrito usando datos externos.

6. test_api_reqres.py

Prueba API pública Reqres con Requests.

Verifica respuesta, códigos y estructura JSON.

Útil para demostrar habilidades API testing.
```

## Nuevas implementaciones destacadas
✔ Logger centralizado

Se implementó un logger en utils/logger.py que:

+ genera el archivo logs/suite.log,

+ registra pasos, errores y estados de ejecución,

+ mejora la trazabilidad de los tests.

✔ Uso de Faker

Permite generar datos dinámicos:

+ nombres

+ emails

+ contraseñas

+ usuarios aleatorios para pruebas negativas

✔ Lectura de datos externos

Ahora los tests pueden leer:

CSV → credenciales (datos/data_login.csv)

JSON → productos del carrito (datos/productos.json)

✔ Tests API agregados

Se incorporó un módulo para probar la API Reqres usando Requests.

✔ Page Object Model (POM)

Se añadieron clases para representar:
```
LoginPage

InventoryPage

CartPage

Esto mejora la mantenibilidad y escalabilidad del proyecto.

```

## Buenas prácticas aplicadas

+ Reutilización de funciones dentro de utils/.

+ Uso de Page Object Model para mejor organización.

+ Uso de fixtures en conftest.py.

+ Uso de logs centralizados.

+ Uso de datos externos para test parametrizados.

+ Separación clara entre tests UI, tests con datos y tests API.

+ Control de versiones con Git y respaldo en GitHub.
