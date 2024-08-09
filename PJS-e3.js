const prompt = require('prompt-sync')();
const numbers = [1,2,3,4,5,6,7,8,9,10];
let LTF = []
let N2F = prompt("Enter the number to lesser thaner: ")
for (i in numbers){
    if(numbers[i] < N2F){

    LTF.push(numbers[i]);
    }
}
console.log(LTF)