//Enemy felled
function ar(armp){
armp = [];
let r = Math.floor(Math.random() * 100);
for (i = 0; i <= r; i++){
    let qq = Math.floor(Math.random() * 1000);
    armp.push(qq);
}
return armp;
};

const prompt = require('prompt-sync')();
let a = ar("L2");
let b = ar("L1");
let c = [];
for (i in a){
    for (j in b){
        if (a[i] == b[j]){
            c.push(a[i]);
            
        }
    }
};
console.log(a);
console.log(b);
console.log(Array.from(new Set(c)));
