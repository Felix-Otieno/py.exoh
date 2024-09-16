//Sum of natural number
//Calculating sum of natural number from 1 to n
// Algorithm Steps: Start with a sum of 0.
//                  Loop through numbers from 1 to n.
//                  Add each number to the sum.
//                  Return the total sum.


function sumOfNaturalNumbers(n) {
    sum = 0;

    for(i = 0; i <= n; i++) {
        sum += i;

    }
    return sum
}
console.log(sumOfNaturalNumbers(20));