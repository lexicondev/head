const prompt = require('prompt-sync')();

function num(x){
    var nomero;
    while(true){
        nomero = prompt(x);
        var ParsedInput = parseInt(nomero);
        if(Number.isInteger(ParsedInput)){
            break;
        }
        else{
            console.log("Not a number");
        }
    }
    return ParsedInput;
}

let y = num("What's your number? ");
let divider = num("What's your divider num? ");
if(y%2 == 0 && y%4 == 0){
    console.log(y,"is an even number and is also a multiple of 4");
}
else if(y%2 == 0){
    console.log(y,"indeed is an even number");
}
else{
    console.log(y, "is an odd number");
}

if(y%divider == 0){
    console.log(y,"divides evenly on",divider);
}
else{
    console.log(y, "doesn't divide evenly on",divider);
}