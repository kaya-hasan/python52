export function topla(a, b) {
  return a + b;
}

export function cikar(a, b) {
  return a - b;
}

export const PI = 3.14159;

// 2. yol beraber export
function carp(a, b) {
  return a * b;
}

function bol(a, b) {
  return a / b;
}

export { carp, bol };
