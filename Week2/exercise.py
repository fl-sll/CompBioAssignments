def check(dna):
    seqm = dna.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T")
    if valid == len(seqm):
        return True
    else:
        return False

def counter(a):
    freq = {}
    for i in a.upper():
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def percentagecounter(d):
    dnalen = sum(d.values())
    print("DNA length = " + str(dnalen))

    percent_g,percent_c = 0,0
    if "G" in d:
        percent_g = (d.get("G") / dnalen) * 100
    if "C" in d:
        percent_c = (d.get("C") / dnalen) * 100

    print(f"G = {percent_g}%")
    print(f"C = {percent_c}%")


def main():
    dna = input("Input DNA = ").upper()
    print(check(dna))
    print(counter(dna))
    percentagecounter(counter(dna))

main()