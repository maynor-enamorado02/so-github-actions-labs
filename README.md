# so-github-actions-labs
Clase Sistemas Operativos










# Docker Workflow - GitHub Actions

Este proyecto demuestra un workflow completo de Docker ejecutándose en GitHub Actions.

## Características

- Construye una imagen Docker simple
- Ejecuta la imagen como contenedor
- Demuestra comunicación entre el contenedor y el host
- Monitorea recursos (CPU, memoria) del contenedor

  ##Cómo ejecutar

1. El workflow se ejecuta automáticamente en cada push a `main`/`master`
2. También se puede ejecutar manualmente desde la pestaña "Actions" en GitHub
3. Revisa los logs del workflow para ver toda la demostración

## Qué demuestra el workflow

- Construcción de imagen**: Usa un Dockerfile básico con Alpine Linux
- Ejecución de contenedor**: Corre en segundo plano con mapeo de puertos
- Comunicación**: Tests HTTP desde el host al contenedor
- Monitoreo**: Uso de CPU, memoria y estado del contenedor

# CI Pipeline con Tests Automatizados

Este proyecto demuestra una pipeline de CI completa con GitHub Actions que ejecuta tests en múltiples sistemas operativos y versiones de Node.js.

## Características

- Tests automatizados en Ubuntu, Windows y macOS
- Soporte para Node.js 18.x y 20.x
- Análisis de código con ESLint
- Reportes de cobertura de tests
- Build de producción
- Badge de estado en tiempo real

## Requisitos

- Node.js 18.x o superior
- npm

## Instalación

```bash
npm install
