// factorial-an operation that describes taking any whole number and multiplying it by every lesser value until you get to one.

function factorial(n) {
    let fact = 1;  // Initialize factorial as 1
  
    // Loop from 1 to n
    for (let i = 1; i <= n; i++) {
      fact *= i;  // Multiply fact by the current number
    }
  
    return fact;  // Return the factorial
  }
  
  console.log(factorial(5));  // Example: Factorial 