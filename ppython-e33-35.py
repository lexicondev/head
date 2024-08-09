from bokeh.plotting import show,figure,output_file
from collections import Counter
import json

bdays = {
    "Names":[],
    "Dates":[]
}
with open('bdjs.json',"r") as inn:
    bdjs = json.load(inn)
mns = []
blum = []
def getbd(sel):
    des = input("Enter the name: ")
    for i in sel['Names']:
        mns.append(i)
    pos = mns.index(des)
    for i in sel['Dates']:
        blum.append(i)
    print(blum[pos])
    adder = input("Enter a name to add: ")
    dater = input("Enter the Bday for that dude: ")
    bdays['Names'].append(adder)
    bdays['Dates'].append(dater)
    with open('bdjs.json',"w") as out:
        json.dump(bdays,out)
    with open('bdjs.json',"r") as inn:
        sel = json.load(inn)
    print(sel)
    output_file("hist.html")
    p = figure()
    p.vbar(x=list(sel['Dates']),top = list(sel['Names']),width = 0.5)
    show(p)
    print(Counter(sel["Dates"]))
getbd(bdjs)
        
