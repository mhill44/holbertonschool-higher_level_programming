#!/usr/bin/node
/*
* A class: square that defines a sq and inherits
* from Square of 5-square.js
*/
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
