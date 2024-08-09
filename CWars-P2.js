function A2S(lis){
    spr = "";
    for (i = 0; i < lis.length;i++){
      spr+=lis[i]
    }
    return spr;
  }
  function toCamelCase(str){
    cameled = [];
    work = Array.from(str);
    for (i = 0; i<work.length;i++){
      if (work[i] == "-" || work[i] == "_"){
        work[i+1] = work[i+1].toUpperCase();
      }
      else{

        cameled.push(work[i]);
      }
      
    }
    for (i = 0; i<cameled.length;i++){
        if(cameled[i] == "-" || cameled[i] == "_"){
            cameled.pop(i);
        }
    }
    console.log(cameled);
    console.log(A2S(cameled));
    
  }
  toCamelCase("Hello-eople")