#!/usr/bin/node
function convert (num, base) {
  const d = '0123456789abcdef';
  if (Math.floor(num / base)) {
    convert(Math.floor(num / base), base);
  }
  process.stdout.write(d[num % base]);
}

convert(16, 16);
