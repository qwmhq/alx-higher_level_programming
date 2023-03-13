#!/usr/bin/node
function factorial (x) {
  if (x === 0 || x === 1 || isNaN(x)) {
    return 1;
  }
  return x * factorial(x - 1);
}
const num = Number(process.argv[2]);
console.log(factorial(num));
