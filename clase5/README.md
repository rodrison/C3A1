
---

## `README.md`
```markdown
# Clase05 - Calculadora (Vista estática)

## Estructura de la carpeta
Clase05/
- index.html       ← vista HTML estática
- estilos.css      ← hoja de estilos externa
- selectors.md     ← hoja de ruta con selectores para testing UI
- README.md        ← este archivo

## Cómo abrir
1. Abrí la carpeta `Clase05`.
2. Abrí `index.html` con tu navegador (doble clic o arrastrar al navegador).
3. No requiere servidor ni JS adicional (vista estática).

## Verificación rápida con DevTools
1. Abrí la página y presioná `F12` para abrir DevTools.
2. En la pestaña *Elements*, buscá por los IDs listados en `selectors.md` (ej: `#input-a`).
3. En la pestaña *Console*, probá:
   ```js
   // comprobar presencia única
   !!document.querySelector('#input-a')           // true si existe
   document.querySelectorAll('.op-button').length // cantidad de botones de operación
   document.querySelector('#result-display').textContent // contenido del resultado
