//Doesn't run here for some reason that has to do with the p-s lib, but felled on online compiler.
//Nevermind that, 2 hrs later and it now works here.

const prompt = require('prompt-sync')();
function divisor(x){
    let list = [];
    let num = prompt(x);
    num = Number(num);
    for (i = 1; i<num; i++){
        if(num%i == 0){
            list.push(i);
        }
    }
    console.log(list);
}
divisor("Enter your number here: ")