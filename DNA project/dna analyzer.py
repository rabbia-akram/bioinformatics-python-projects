def count (A):
    print("A:",A.count(("A")))
    print("T:",A.count(("T")))
    print("G:",A.count(("G")))
    print("C:",A.count(("C")))
count("ATGCGTAC")

F = open("DNA project/sequence.fasta")
L = F.readlines()
S = ""
for X in L[1:]:
    S = S + X.strip()
print(len(S))
count(S)

def gc(A):
    G = A.count("G")
    C = A.count("C")
    print("GC content:",round((G + C)/ len(A) * 100,2))
gc(S)

def rc(A):
    B = ""
    for X in A:
        if X == "A":
            B = B + "T"
        elif X == "T":
            B = B + "A"
        elif X == "G":
            B = B + "C"
        elif X == "C":
            B = B + "G"
    C = B[::-1]
    print("Reverse complement:" ,C[:50])
rc("ATGC")
rc(S)

