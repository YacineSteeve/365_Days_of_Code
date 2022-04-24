const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('\nEnter x: ', (answer) => {
  console.log(`\nx = ${answer}`)
  rl.close()
})
