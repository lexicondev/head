function wave(prompto){
    let waved = [];
    let spr = "";
    let toWave = prompto.toLowerCase();
    for (i = 0; i<toWave.length;i++){
        spr = "";
        let bb = Array.from(toWave);
        bb[i] = bb[i].toUpperCase();
        for (j = 0; j<bb.length;j++){
            spr += bb[j];
        }
        waved.push(spr);
        if(spr == toWave){
            waved.pop(spr);
        }
    }
   
  for (i = 0; i<waved.length;i++){
    spr += waved[i];
    if (i !== waved.length-1){
      spr+=","
    }
  }
  return waved;
  }
 wave("Two words");