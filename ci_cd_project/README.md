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

                
Recursos utilizados:

GitHub Actions Runners: Cada workflow se ejecuta en máquinas virtuales proporcionadas por GitHub (Ubuntu, Windows, macOS).
Lenguaje: Python 3.x
Dependencias: unittest para pruebas, safety para análisis de vulnerabilidades.
Logs: Se generan en app.log para seguimiento del sistema.
Almacenamiento: Archivos temporales creados en el runner para pruebas.

Análisis de performance:

Ubuntu: Ejecución más rápida y estable para pipelines CI/CD.
Windows: Ligeramente más lento debido a inicialización del entorno.
macOS: Similar a Ubuntu, pero con menor disponibilidad en runners gratuitos.
Conclusión: Para proyectos Python, Ubuntu es la opción más eficiente.
