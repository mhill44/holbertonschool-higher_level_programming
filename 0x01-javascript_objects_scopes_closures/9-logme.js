#!/usr/bin/node
/*
* Prints a number of args already printed
* And the new arg value
*/
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
