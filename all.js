let sum = 0;
function sumOfAll(n) {
    for(i = 1; i < n; i++) {
        sum += i;
    }
    return sum;
}
console.log(sumOfAll(20));