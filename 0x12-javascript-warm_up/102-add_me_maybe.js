#!/usr/bin/node
function addMeMaybe (number, func) {
  func(number + 1);
}
module.exports = { addMeMaybe };
