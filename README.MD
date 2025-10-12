# Proyecto de Automatización de Pruebas

## Propósito

El objetivo de este proyecto es **demostrar las habilidades adquiridas en automatización de pruebas**.  
Incluye scripts que validan funcionalidades de un sitio web de ejemplo, usando buenas prácticas de testing con **Python**, **Selenium** y **pytest**.

Este proyecto sirve como demostración de:

- Automatización de pruebas end-to-end en una aplicación web.
- Organización de scripts y funciones reutilizables.
- Uso de frameworks modernos de testing y herramientas de control de versiones.

---

## Herramientas utilizadas

- **Python**  
- **Selenium**  
- **Google Chrome WebDriver**  
- **pytest**  
- **Git** y **GitHub** para respaldo y versionado  

---

## Estructura del proyecto

```text
TestingQA-Automation/
│
├── utils/                  # Funciones reutilizables
│   ├── __init__.py
│   ├── driver_setup.py     # Configuración y creación del driver de Selenium
│   └── login.py      # Función de login común para los tests
│   └── title_check.py # Función para chequear el título
├── tests/                  # Scripts de prueba
│   ├── __init__.py
│   ├── test_login.py       # Test de login: validación de URL y credenciales
│   ├── test_inventary.py  # Test de inventario: validación de título y productos
│   └── test_badge.py     # Test de carrito: añadir producto y verificar contador
│
└── README.md               # Documentación del proyecto


Instalación de dependencias

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>


Entrar en la carpeta del proyecto:

cd TestingQA-Automation


Instalar las dependencias de Python:

pip install -r requirements.txt


Alternativamente, instalar manualmente:

pip install selenium pytest


Descargar e instalar Chrome WebDriver compatible con tu versión de Chrome:
Descargar ChromeDriver

Colocar el ejecutable en la carpeta del proyecto o en una ruta incluida en el PATH.

Ejecución de las pruebas

Abrir la terminal o consola en la carpeta raíz del proyecto.

Ejecutar todos los tests:

python -m pytest -s tests


-s permite que se vean los print() en consola.

Todos los archivos test_*.py dentro de tests/ serán detectados automáticamente.

Generar un reporte HTML opcional:

python -m pytest --html=report.html -s tests


Para ejecutar un test específico:

python -m pytest -s tests/test_login.py

Descripción de los tests
1. test_login.py

Propósito: Validar que el login funcione con credenciales correctas (standard_user / secret_sauce).

Verificaciones:

La URL contiene /inventory.html tras el login.

Imprime mensaje de éxito en consola.

2. test_inventary.py

Propósito: Explorar el inventario tras el login.

Verificaciones:

El título de la sección es “Products”.

Al menos un producto se encuentra listado.

Imprime nombre y precio del primer producto.

3. test_badge.py

Propósito: Validar la funcionalidad del carrito.

Verificaciones:

Añade el primer producto al carrito.

Comprueba que el contador del carrito muestra 1.

Verifica que el producto agregado aparece listado.

Buenas prácticas

Separar funciones reutilizables en utils/ para evitar código repetido.

Usar pytest fixtures para crear y cerrar instancias del navegador.

Mantener un control de versiones con Git y respaldar en GitHub.

Evitar caracteres especiales en print() si se ejecuta en Windows sin UTF-8.