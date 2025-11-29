function greet(name = 'World') {
  return `Hello, ${name}! from CI Pipeline`;
}

function add(a, b) {
  return a + b;
}

module.exports = { greet, add };

if (require.main === module) {
  console.log(greet('CI Pipeline User'));
  console.log('Suma de 2 + 3:', add(2, 3));
}
