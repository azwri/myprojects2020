console.log('Hello World');

// add args
args = process.argv;
if(args[2] == 'add'){
  console.log(+args[3] + +args[4]);
}
// console.log(args);
