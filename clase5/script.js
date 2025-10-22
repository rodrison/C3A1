// script.js — lógica funcional de la calculadora

let operacion = null;

const inputA = document.querySelector("#input-a");
const inputB = document.querySelector("#input-b");
const botonesOp = document.querySelectorAll(".operations button");
const btnCalcular = document.querySelector("#btn-equals");
const btnLimpiar = document.querySelector("#btn-clear");
const display = document.querySelector("#result-display");

// Seleccionar operación
botonesOp.forEach((btn) => {
  btn.addEventListener("click", () => {
    botonesOp.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    operacion = btn.dataset.op;
  });
});

// Calcular resultado
btnCalcular.addEventListener("click", () => {
  const a = parseFloat(inputA.value);
  const b = parseFloat(inputB.value);

  if (isNaN(a) || isNaN(b)) {
    display.textContent = "Error: ingrese números válidos";
    display.style.color = "#dc2626";
    return;
  }

  if (!operacion) {
    display.textContent = "Seleccione una operación";
    display.style.color = "#dc2626";
    return;
  }

  let resultado;

  switch (operacion) {
    case "+":
      resultado = a + b;
      break;
    case "-":
      resultado = a - b;
      break;
    case "*":
      resultado = a * b;
      break;
    case "/":
      if (b === 0) {
        display.textContent = "Error: división por cero";
        display.style.color = "#dc2626";
        return;
      }
      resultado = a / b;
      break;
  }

  display.textContent = resultado.toFixed(2);
  display.style.color = "#2d3748";
});

// Limpiar
btnLimpiar.addEventListener("click", () => {
  inputA.value = "";
  inputB.value = "";
  display.textContent = "—";
  botonesOp.forEach((b) => b.classList.remove("active"));
  operacion = null;
});
