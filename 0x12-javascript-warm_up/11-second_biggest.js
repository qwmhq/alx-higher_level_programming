#!/usr/bin/node
const args = process.argv.slice(2);
console.log(args.map(Number).sort((a, b) => a - b)[1]);
