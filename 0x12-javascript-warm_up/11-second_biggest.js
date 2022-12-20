#!/usr/bin/node
function sortNum (a, b) {
  return a - b;
}
const len = process.argv.length;
let secondBiggest = 0;
if (len > 3) {
  let tab = [];
  for (let i = 2; i < len; i++) {
    tab.push(process.argv[i]);
  }
  tab.sort(sortNum);
  secondBiggest = tab[tab.length - 2];
}
console.log(secondBiggest);
