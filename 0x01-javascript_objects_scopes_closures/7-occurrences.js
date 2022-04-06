#!/usr/bin/node
/*
* A function that returns the number of
* Occurrences in a list
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
