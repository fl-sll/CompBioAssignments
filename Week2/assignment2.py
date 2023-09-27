def translate(amino):
    ta = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }

    ta = {v:k for k,v in ta.items()}
    if amino in ta:
        return ta[amino]
    else:
        return None

# def take_amino(am):
#     complement = []
#     for i in am:
#         if am in ta:
#             complement.append(ta.get(i))
#     return complement

def make_rna(c):
    rna = ""
    for i in c:
        rna += translate(i)
    return rna

def counter(a):
    d = {}
    for i in a:
        t = translate(i)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1

    for k,v in d.items():
        print(f"{k} = {v}")



def main():
    amino = input("Input Amino = ").upper()
    print(" ")
    print(f"mRNA = {make_rna(amino)}")
    counter(amino)

main()