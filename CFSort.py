#Sort the Array                 https://codeforces.com/contest/451/problem/B

n = int(input())
x = list(map(int, input().split()))
c = 0
if x == sorted(x):
    print(f'yes\n1 1')
else:
    for i in range(len(x)):
        if i != len(x)-1:
            if c > 2:
                break
            else:
                if x[i] < x[i+1] and c <= 2:
                    continue
                else:
                    c+= 1
                    if c > 2:
                        print('no')
                        exit()
                    if c == 1:
                        a = i
                        for z in range(a+1,len(x)):
                            if z != len(x) and c != 2:
                                if x[a] > x[z]:
                                    continue
                                else:
                                    c+=1
                                    b = z-1
                                    y = list(x[0:a]) + list(reversed(x[a:b+1])) + list(x[b+1:len(x)+1])   
                                    x = y
                                    if x[a] > x[a+1]:
                                        print('no')
                                        exit()
                                    b+=1
                                break
                        else:
                            c+=1
                            b = z
                            y = list(x[0:a]) + list(reversed(x[a:b+1])) + list(x[b+1:len(x)+1])
                            x = y
                            if a== 0:
                                if x[a] > x[a+1]:
                                    print('no')
                                    exit()
                            else:
                                if x[a] > x[a+1] or x[a-1] > x[a]: 
                                    print('no')
                                    exit()
                            b+=1
                            
    if c > 2:
        print('no')
    else: 
        print(f'yes\n{a+1} {b}')
            
