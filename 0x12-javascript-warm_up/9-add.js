#!/usr/bin/node
const var1 = parseInt(process.argv[2]);
const var2 = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(var1, var2));
