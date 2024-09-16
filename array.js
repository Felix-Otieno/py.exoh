//Largest Number in an Array
function findLargestNumber(arr) {
    let largest = arr[0];  // Assume the first number is the largest
  
    // Loop through the array
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] > largest) {
        largest = arr[i];  // Update largest if current number is greater
      }
    }
  
    return largest;  // Return the largest number found
  }
  
  console.log(findLargestNumber([3, 8, 2, 9, 4]));  // Example: Largest = 12