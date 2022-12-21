#!/usr/bin/node
let liste = require('./100-data').list;
console.log(liste);
liste = liste.map((i, j) => {
  return i * j;
});
console.log(liste);
