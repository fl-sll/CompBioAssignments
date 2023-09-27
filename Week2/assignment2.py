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

    #// Switch key value pairs
    ta = {v:k for k,v in ta.items()}

    if amino in ta:
        return ta[amino]
    else:
        return None

#// Creating rna from amino acid
def make_rna(c):
    rna = ""
    for i in c:
        rna += translate(i)
    return rna

#// Counts the frequency of each codon in the polypeptide chain
def counter(a):
    d = {}
    for j in range(0, len(a),3):
        rn = a[j:j+3]
        if rn in d:
            d[rn] += 1
        else:
            d[rn] = 1

    for k,v in d.items():
        print(f"{k} = {v}")

def main():
    #// take polypeptide chain from user
    amino = input("Input Amino = ").upper()
    print(" ")
    #// print corresponding rna formed from the polypeptide chains
    print(f"mRNA = {make_rna(amino)}")
    #// counts the frequency of each codon
    counter(make_rna(amino))

main()