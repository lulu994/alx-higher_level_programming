#!/usr/bin/node
/* Script that prints the first argument passed to it */
const firstArgument = process.argv[2];
if (firstArgument === undefined) console.log('No argument');
else console.log(firstArgument);
