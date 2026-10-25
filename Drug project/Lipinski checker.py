def lipinski(N, W, L, D, H):
    P = 0
    if W <= 500:
        P = P + 1
    if L <= 5:
        P = P + 1
    if D <= 5:
        P = P + 1
    if H <= 10:
        P = P + 1
    print(N, "passes",P,"of 4 rules")
Z = [["Aspirin",180.16, 1.2, 1, 4],
     ["Paracetamol",151.16, 0.5, 2, 2],
     ["Ibuprofen", 206.28, 3.5, 1, 2],
     ["Caffeine", 194.19, -0.1, 0, 3],
     ["Cyclosporine",1202.6, 7.5, 5, 12 ],]
for X in Z:
    lipinski(X[0], X[1], X[2], X[3], X[4])