from collections import Counter

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Peptide = dataset.readline().strip()
        Spectrum = dataset.readline().strip().split()
        for i in range(len(Spectrum)):
            Spectrum[i] = int(Spectrum[i])
    return Peptide, Spectrum

def Mass(Peptide):
    return sum([AminoAcidMass[i] for i in Peptide])

def Cyclospectrum(Peptide):
    l = len(Peptide)
    Peptide += Peptide[:-1]
    PrefixMass = [0]
    for i in Peptide:
        PrefixMass.append(PrefixMass[-1] + AminoAcidMass[i])
    TheoreticalSpectrum = [0]

    for i in range(1, l): # i is the length of substrings
        for j in range(l): # j is the starting position of a substring
            TheoreticalSpectrum.append(PrefixMass[j+i] - PrefixMass[j])
    TheoreticalSpectrum.append(PrefixMass[l])
    return sorted(TheoreticalSpectrum)
    pass

def Score(peptide, spectrum):
    peptide_spectrum = Cyclospectrum(peptide)
    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)
    s = 0
    for mass in peptide_counter:
        s += min(peptide_counter[mass], spectrum_counter[mass])
    return s


AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30244_3.txt"
    Peptide, Spectrum = ReadInput(path)
    #print(Peptide, Spectrum)
    print(Score(Peptide, Spectrum))
    #Peptides = CyclopeptideSequencing(Spectrum)


if __name__ == main():
    main()
