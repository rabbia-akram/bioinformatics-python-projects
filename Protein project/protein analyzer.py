F = open("Protein project/protein.fasta")
L = F.readlines()
S = ""
for X in L[1:]:
    S = S + X.strip()
print("Length:", len(S))

H = 0
for X in S:
    if X in "AVILMFWC":
        H = H + 1
print("Hydrophobic percent:",round(H / len(S) * 100,2))

B = ""
M = 0
for X in S:
    if S.count(X) > M:
        M = S.count(X)
        B = X
print("Most common amino acid:",B,M)