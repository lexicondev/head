from bokeh.plotting import show, output_file, figure
import json
from collections import Counter

monts = {

    "01": 'Jan',
    "02": 'Feb',
    "03": 'Mar',
    "04": 'Apr',
    "05": 'May',
    "06": 'Jun',
    "07": 'Jul',
    "08": 'Aug',
    "09": 'Sep',
    "10": 'Oct',
    "11": 'Nov',
    "12": 'Dec'
}

with open("bdjs.json","r") as inn:
    bdjs = json.load(inn)
output_file("hist.html")
"""def j2l(lis,o):
    bb = []
    dd = []
    for i in Counter(lis.keys()):
        bb.append(i)
    for j in Counter(lis.values()):
        dd.append(j)
    if o == 1:
        return bb
    else:
        return dd
"""

"""y = j2l(bdjs,2)
x = list(Counter(y).keys())
y  = list(Counter(y).values())
"""
mon_in_js = []
y = []
for i in bdjs.values():
    for j in i.split():
        pp = list(j)[0:2]
        qq = "" + str(pp[0])+str(pp[1])
        mon_in_js.append(qq)
#x_range = mon_in_js
xran = []
for i in mon_in_js:
    for j in monts.keys():
        if i == j:
            xran.append(monts[j])
        else:
            continue
y.extend(Counter(mon_in_js).values())
# create a figure
p = figure(x_range=list(monts.values()))

# create a histogram
p.vbar(x=xran, top=y, width=0.5)

# render (show) the plot
show(p)