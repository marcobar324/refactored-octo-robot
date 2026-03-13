# refactored-octo-robot

¡https://www.coingecko.com/ brinda un análisis exhaustivo del mercado de las criptomonedas, con información sobre más de 3000 criptomonedas!
Descargue la aplicación para iOS o Android aquí:
https://bit.ly/coingecko-ios
https://bit.ly/coingecko-android

---

## Gestión de ramas / Branch Management

Para más información sobre cómo crear y eliminar ramas en este repositorio, consulta la documentación oficial de GitHub:
[Crear y eliminar ramas en tu repositorio](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)

### Crear una rama

1. Navega a la página principal del repositorio en GitHub.
2. En la vista de árbol de archivos, selecciona el menú desplegable de ramas y haz clic en **Ver todas las ramas**.
3. Haz clic en **Nueva rama**.
4. Escribe un nombre para la nueva rama.
5. Elige el origen (rama base) y haz clic en **Crear rama**.

También puedes crear una rama desde la línea de comandos:

```bash
git checkout -b nombre-de-tu-rama
git push origin nombre-de-tu-rama
```

### Eliminar una rama

Para eliminar una rama fusionada desde GitHub:

1. Navega a la página principal del repositorio.
2. En la vista de árbol de archivos, selecciona el menú desplegable de ramas y haz clic en **Ver todas las ramas**.
3. Junto a la rama que deseas eliminar, haz clic en el icono de papelera.

Para eliminar una rama local y remota desde la línea de comandos:

```bash
# Eliminar rama local
git branch -d nombre-de-tu-rama

# Eliminar rama remota
git push origin --delete nombre-de-tu-rama
```

> **Nota:** No puedes eliminar la rama predeterminada del repositorio sin antes cambiarla. Si la rama está asociada a una solicitud de cambios abierta, debes fusionar o cerrar la solicitud antes de eliminar la rama.