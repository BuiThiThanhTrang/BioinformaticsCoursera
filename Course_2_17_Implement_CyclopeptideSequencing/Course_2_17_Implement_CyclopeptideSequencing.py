from collections import Counter

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Spectrum = dataset.read().strip().split()
        for i in range(len(Spectrum)):
            Spectrum[i] = int(Spectrum[i])
    return Spectrum

def Mass(Peptide):
    return sum([AminoAcidMass[i] for i in Peptide])

def Expand(Peptides):
    AminoAcids = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    for i in range(len(Peptides)):
        p = Peptides.pop(0)
        for a in AminoAcids:
            Peptides.append(p+a)
    return Peptides
    pass

def linear_spectrum(peptide):
    prefix_mass = [0]
    for m in peptide:
        prefix_mass.append(prefix_mass[-1] + AminoAcidMass[m])
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)

def Consistent(peptide, spectrum):
    peptide_spectrum = linear_spectrum(peptide)
    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)
    for mass in peptide_counter:
        if peptide_counter[mass] > spectrum_counter[mass]:
            return False
    return True

def CyclopeptideSequencing(Spectrum):
    CandidatePeptides = ['']
    FinalPeptides = []
    #print(max(Spectrum))
    while len(CandidatePeptides) > 0:
        CandidatePeptides = Expand(CandidatePeptides)
        #print(CandidatePeptides)
        #print([Mass(i) for i in CandidatePeptides])
        for Peptide in CandidatePeptides:
            if Mass(Peptide) == max(Spectrum):
                if Cyclospectrum(Peptide) == Spectrum and (not (Peptide in FinalPeptides)):
                    FinalPeptides.append(Peptide)
                CandidatePeptides = [i for i in CandidatePeptides if i != Peptide]
                print(Peptide)
            elif not Consistent(Peptide, Spectrum):
                CandidatePeptides = [i for i in CandidatePeptides if i != Peptide]
            if Mass(Peptide) > max(Spectrum):
                CandidatePeptides = [i for i in CandidatePeptides if i != Peptide]
        #print(CandidatePeptides)
    return FinalPeptides

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


AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30217_6 (1).txt"
    Spectrum = ReadInput(path)
    print(Spectrum)
    Peptides = CyclopeptideSequencing(Spectrum)

    for p in Peptides:
        #print(p)
        l = [str(AminoAcidMass[a]) for a in p]
        print('-'.join(l), end = ' ')
    print()

    with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        for p in Peptides:
        #print(p)
            l = [str(AminoAcidMass[a]) for a in p]
            #print('-'.join(l), end = ' ')
            #f.write('-'.join(l), end = ' ')
    #print(Expand(['']))
    #print(Text, Peptide)
    #print(*EncodingSubstringDNA(Text, Peptide), sep = '\n')


if __name__ == main():
    main()
