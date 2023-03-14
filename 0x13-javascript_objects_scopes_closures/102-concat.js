#!/usr/bin/node
const fs = require('fs/promises');

if (process.argv.length !== 5) {
  console.error('three arguments are required!');
  process.exit(1);
}

const sourcePath1 = process.argv[2];
const sourcePath2 = process.argv[3];
const destinationPath = process.argv[4];

async function concat (src1, src2, dest) {
  try {
    const fileContent1 = await fs.readFile(src1, { encoding: 'utf8' });
    const fileContent2 = await fs.readFile(src2, { encoding: 'utf8' });
    await fs.writeFile(dest, fileContent1 + fileContent2);
  } catch (err) {
    console.error(err);
  }
}

concat(sourcePath1, sourcePath2, destinationPath);
