#Anton and Polyhedrons          https://codeforces.com/contest/785/problem/A
ref = {'Tetrahedron': 4,
        'Cube': 6,
        'Octahedron': 8,
        'Dodecahedron': 12,
        'Icosahedron': 20}
n = input()
n = int(n)
res = 0
bank = [i for i in range(n)]
for i in range(n):
    bank[i] = input("")
for i in bank:
    res+=ref[i]
print(res)