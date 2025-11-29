
# Estrategia de Rollback

- Mantener releases versionadas (tags `v*`).
- Para rollback, crear un tag `vX.Y.Z-rollback` apuntando al release estable previo y ejecutar `deploy.yml` sobre ese tag.
- También se provee un job manual `workflow_dispatch` que puede desplegar un commit/tag específico.
