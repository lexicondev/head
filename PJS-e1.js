function num(x){
    var y;
    while(true){
    y = prompt(x);
    var ParsedInput = parseInt(y);
    if(Number.isInteger(ParsedInput)) {
        break;
    } else {
        console.log("Not a number");
        
    };
};
return ParsedInput;
};


const prompt = require('prompt-sync')();
const currentDate = new Date().getFullYear();
console.log(currentDate);
let nombre = prompt("Enter your name here: ");
let age = num("Enter your number: ");
console.log(age);
if(age >= 100){
    console.log("You're already a hundrerer broooo!!!");
}
    else{
        console.log("Alright then ",nombre,", You will turn 100 in ",100-age," in the year",currentDate+100-age);
    }

