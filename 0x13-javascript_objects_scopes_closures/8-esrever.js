#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  const len = list.length;
  for (let i = 0; i < len / 2; i++) {
    temp = list[i];
    list[i] = list[len - (1 + i)];
    list[len - (1 + i)] = temp;
  }
  return list;
};
