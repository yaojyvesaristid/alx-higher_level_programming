#!/usr/bin/node
//JS script

let var1 = 'undefined';
let var2 = 'undefined';
if (process.argv.length === 3) {
    var1 = process.argv[2];
} else if (process.argv.length > 3) {
    var1 = process.argv[2];
    var2 = process.argv[3];
}
console.log(`${var1} is ${var2}`);
