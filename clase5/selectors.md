# Selectors - Clase05 (calculadora)

Este documento lista los selectores CSS/DOM que usaremos como "hoja de ruta" para futuros tests UI (Selenium / Playwright / Cypress).

| Elemento (descripción)                  | Selector CSS / ID / Name                      | Propósito / Nota de verificación |
|-----------------------------------------|-----------------------------------------------|----------------------------------|
| Formulario principal                     | `#calc-form` / `form[name="calcForm"]`        | Punto de entrada del formulario. Único en la página. |
| Input número A                           | `#input-a` / `input[name="a"]`                | Input número A. ID estable y único. |
| Input número B                           | `#input-b` / `input[name="b"]`                | Input número B. ID estable y único. |
| Botón sumar                              | `#btn-add` / `button[name="add"]`             | Operación suma. Usar para test rápido (smoke). |
| Botón restar                             | `#btn-sub` / `button[name="sub"]`             | Operación resta. |
| Botón multiplicar                        | `#btn-mul` / `button[name="mul"]`             | Operación multiplicar. |
| Botón dividir                            | `#btn-div` / `button[name="div"]`             | Operación dividir (test de excepción). |
| Botón calcular                           | `#btn-equals` / `button[name="equals"]`       | Ejecuta cálculo (si se implementa JS). |
| Botón limpiar                            | `#btn-clear` / `button[name="clear"]`         | Limpia campos. |
| Output resultado                         | `#result-display` / `output[name="result"]`   | Campo donde se muestra el resultado. aria-live=polite. |
| Sección operaciones (fieldest)           | `.operations` / `fieldset[aria-label="Operaciones"]` | Grupo de botones (útil para localizar operaciones). |

## Cómo verificar selectores en DevTools
1. Abrí la página `index.html` en el navegador.  
2. Presioná `F12` → pestaña *Elements*.  
3. Usá `Ctrl+F` y pegá el selector (ej: `#input-a`) para comprobar que apunta a un único elemento.  
4. En la consola de DevTools probá:  
   ```js
   document.querySelector('#input-a') // devuelve el elemento o null
   document.querySelectorAll('.op-button').length // número de botones de operación
