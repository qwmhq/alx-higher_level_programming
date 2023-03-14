#!/usr/bin/node
exports.converter = function (base) {
  function convert (num) {
    const d = '0123456789abcdefhijklmnopqrstuvwxyz';
    if (!Math.floor(num / base)) {
      return d[num % base];
    }
    return convert(Math.floor(num / base)) + d[num % base];
  }
  return convert;
};
