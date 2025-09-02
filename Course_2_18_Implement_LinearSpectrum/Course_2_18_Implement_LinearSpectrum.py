
def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Peptide = dataset.read().strip()
    return Peptide

def LinearSpectrum(Peptide):
    l = len(Peptide)
    #Peptide += Peptide[:-1]
    PrefixMass = [0]
    for i in Peptide:
        PrefixMass.append(PrefixMass[-1] + AminoAcidMass[i])
    TheoreticalSpectrum = [0]

    for i in range(1, l): # i is the length of substrings
        for j in range(l - i + 1): # j is the starting position of a substring
            TheoreticalSpectrum.append(PrefixMass[j+i] - PrefixMass[j])
    TheoreticalSpectrum.append(PrefixMass[l])
    return sorted(TheoreticalSpectrum)
    pass


AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30248_2.txt"
    Peptide = ReadInput(path)
    print(*LinearSpectrum(Peptide))
    #print(Text, Peptide)
    #print(*EncodingSubstringDNA(Text, Peptide), sep = '\n')


if __name__ == main():
    main()
