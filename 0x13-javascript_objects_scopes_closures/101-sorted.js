#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

const keys = Object.keys(dict);
for (let i = 0; i < keys.length; i++) {
  const newKey = dict[keys[i]];
  const newValue = keys[i];
  if (Object.prototype.hasOwnProperty.call(newDict, newKey)) {
    newDict[newKey].push(newValue);
  } else {
    newDict[newKey] = [newValue];
  }
}

console.log(newDict);
