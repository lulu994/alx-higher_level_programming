#!/usr/bin/node
/* Script that print 'x' times "C is fun" */
const x = parseInt(process.argv[2]);
if (x === undefined || isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
