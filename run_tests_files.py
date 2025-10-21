import pytest

test_files =[
    "tests/test_login.py",
    "tests/test_inventary.py",
    "tests/test_badge.py"
]

#argumentos para ejecutar las pruebas = archivos de prueba + reporte html + verbosidad
pytest_args = test_files +  ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)