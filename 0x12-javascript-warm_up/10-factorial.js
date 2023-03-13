#!/usr/bin/node
function factorial (x) {
  if (x === 0 || x === 1 || isNaN(x)) {
    return 1;
  }
  return x * factorial(x - 1);
}
const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('argument must be a number');
}
console.log(factorial(num));
