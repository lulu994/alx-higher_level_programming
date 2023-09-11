#!/usr/bin/node
/* Script that computes and prints a factorial */
const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log(1);
} else {
  console.log(recursion(n));
}

function recursion (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * recursion(n - 1);
  }
}
