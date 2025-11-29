
# Proyecto Final: CI/CD Pipeline Completo Multi-Plataforma

Este repositorio contiene una aplicación simple en **Python** con pruebas unitarias, generación de logs y un pipeline **CI/CD** que se ejecuta en **Ubuntu**, **Windows** y **macOS**. Incluye workflow de **escaneo de seguridad** y workflow de **release automático**.

---

## Parte 3: Documentación de la arquitectura

### 1) Diagrama de interacción (conceptual)

```
[Developer] ---> [GitHub Repo]
       |             |
       |        Triggers Workflows
       |             |
       v        +-------------------+
                | GitHub Actions    |
                |-------------------|
                | CI Pipeline       |
                | Security Scan     |
                | Release Workflow  |
                +-------------------+
                     |   |   |
                     v   v   v
          Ubuntu Runner  Windows Runner  macOS Runner
                     |   |   |
                     v   v   v
                Ejecuta pruebas, genera logs, reportes
```

### 2) Recursos del sistema utilizados
- **Runners de GitHub Actions:** Máquinas virtuales Ubuntu, Windows y macOS.
- **Lenguaje:** Python 3.12 (fijado para evitar incompatibilidades de paquetes).
- **Dependencias:** `coverage` para reportes de cobertura.
- **Logs:** `app.log` generado por la aplicación durante su ejecución.
- **Artefactos:** `coverage.xml` y reporte HTML `htmlcov/` subidos por workflow.

### 3) Análisis de performance entre diferentes OS
- **Ubuntu:** Arranca más rápido y suele compilar/instalar paquetes con menos fricción.
- **Windows:** Inicialización del entorno toma ligeramente más tiempo; PowerShell por defecto.
- **macOS:** Similar a Ubuntu, pero runners gratuitos tienen menos capacidad simultánea.
- **Conclusión:** Para Python, Ubuntu es la opción más eficiente; se mantiene compatibilidad en Windows y macOS.

---

## Estructura del proyecto

```
.
├── app.py
├── utils.py
├── tests/
│   └── test_app.py
├── requirements.txt
└── .github/
    └── workflows/
        ├── ci-pipeline.yml
        ├── security-scan.yml
        └── release.yml
```

---

## Cómo ejecutar localmente

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -v
python app.py
```

---

## Notas
- `coverage` está **fijado** a una versión estable compatible con Python 3.12.
- El workflow usa únicamente comandos **cross-platform** (`python -m ...`) para mayor robustez.
