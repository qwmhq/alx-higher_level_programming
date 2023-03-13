#!/usr/bin/node
const args = process.argv.slice(2);
const argc = args.length;
if (argc < 2) {
  console.log(0);
} else {
  console.log(args.map(Number).sort((a, b) => b - a)[1]);
}
