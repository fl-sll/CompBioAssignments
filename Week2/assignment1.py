def translate_codon(cod):
    tc = {"GCT":"Ala (A)", "GCC":"Ala (A)", "GCA":"Ala (A)", "GCG":"Ala (A)",
           "TGT":"Cys (C)", "TGC":"Cys (C)", "GAT":"Asp (D)", "GAC":"Asp (D)", "GAA":"Glu (E)", "GAG":"Glu (E)",
            "TTT":"Phe (F)", "TTC":"Phe (F)", "GGT":"Gly (G)", "GGC":"Gly (G)", "GGA":"Gly (G)", "GGG":"Gly (G)",
            "CAT":"His (H)", "CAC":"His (H)", "ATA":"Ile (I)", "ATT":"Ile (I)", "ATC":"Ile (I)", "AAA":"Lys (K)",
            "AAG":"Lys (K)", "TTA":"Leu (L)", "TTG":"Leu (L)", "CTT":"Leu (L)", "CTC":"Leu (L)", "CTA":"Leu (L)", 
            "CTG":"Leu (L)", "ATG":"Met (M)", "AAT":"Asn (N)", "AAC":"Asn (N)", "CCT":"Pro (P)", "CCC":"Pro (P)", 
            "CCA":"Pro (P)", "CCG":"Pro (P)", "CAA":"Gln (Q)", "CAG":"Gln (Q)", "CGT":"Arg (R)", "CGC":"Arg (R)", 
            "CGA":"Arg (R)", "CGG":"Arg (R)", "AGA":"Arg (R)", "AGG":"Arg (R)", "TCT":"Ser (S)", "TCC":"Ser (S)",
            "TCA":"Ser (S)", "TCG":"Ser (S)", "AGT":"Ser (S)", "AGC":"S ","ACT":"Thr (T)", "ACC":"Thr (T)", 
            "ACA":"Thr (T)", "ACG":"Thr (T)", "GTT":"Val (V)", "GTC":"Val (V)", "GTA":"Val (V)", "GTG":"Val (V)", 
            "TGG":"Trp (W)", "TAT":"Tyr (Y)", "TAC":"Tyr (Y)", "TAA":"_","TAG":"_","TGA":"_"
    }
    if cod in tc:
        return tc[cod]
    else:
        return None
    
def complement(dna):
    comp = []
    for i in dna:
        if i == "T":
            comp.append("A")
        elif i == "A":
            comp.append("T")
        elif i == "G":
            comp.append("C")
        elif i == "C":
            comp.append("G")
    c = ""
    for i in comp:
        c += i
    return c

def mrna(l):
    rn = []
    for i in l:
        if i == "T":
            rn.append("A")
        elif i == "A":
            rn.append("U")
        elif i == "G":
            rn.append("C")
        elif i == "C":
            rn.append("G")
    r = ""
    for i in rn:
        r += i
    return r


def amino(complement):
    acid = ""
    if len(complement)%3 == 0:
        for i in range(0, len(complement), 3):
            codon = complement[i : i+3]
            if i != len(complement)-3:
                acid+= translate_codon(codon) + " - "
            else:
                acid += translate_codon(codon)
    
    return acid

def main():
    dna = input("Input DNA = ").upper()
    print(" ")
    print("Complement = " + complement(dna))
    print("mRNA = " + mrna(dna))
    print("Aminoacid = " + amino(complement(dna)))

main()