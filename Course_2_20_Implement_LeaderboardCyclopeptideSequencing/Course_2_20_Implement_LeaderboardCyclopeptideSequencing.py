from collections import Counter

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        N = dataset.readline().strip()
        Spectrum = dataset.read().strip().split()
        for i in range(len(Spectrum)):
            Spectrum[i] = int(Spectrum[i])
    return int(N), Spectrum

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

def linear_spectrum(peptide):
    prefix_mass = [0]
    for m in peptide:
        prefix_mass.append(prefix_mass[-1] + AminoAcidMass[m])
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)

def LinearScore(peptide, spectrum):
    peptide_spectrum = linear_spectrum(peptide)
    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)
    s = 0
    for mass in peptide_counter:
        s += min(peptide_counter[mass], spectrum_counter[mass])
    return s

def Score(peptide, spectrum):
    peptide_spectrum = Cyclospectrum(peptide)
    peptide_counter = Counter(peptide_spectrum)
    spectrum_counter = Counter(spectrum)
    s = 0
    for mass in peptide_counter:
        s += min(peptide_counter[mass], spectrum_counter[mass])
    return s

def Trim(Leaderboard, Spectrum, N):
    Leaderboard = sorted(Leaderboard, key=lambda p: LinearScore(p, Spectrum), reverse=True)
    LastIdx = N - 1
    if len(Leaderboard) <= N:
        return Leaderboard
    else:
        for i in range(N, len(Leaderboard)):
            if LinearScore(Leaderboard[i], Spectrum) == LinearScore(Leaderboard[N-1], Spectrum):
                LastIdx = i
    return Leaderboard[:LastIdx + 1]

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    Leaderboard = ['']
    FinalPeptides = ['']
    while len(Leaderboard) > 0:
        Leaderboard = Expand(Leaderboard)
        for Peptide in Leaderboard:
            if Mass(Peptide) == max(Spectrum):
                #if Score(Peptide, Spectrum) > Score(FinalPeptides[-1], Spectrum):
                FinalPeptides.append(Peptide)
                #Leaderboard = [i for i in Leaderboard if i != Peptide]
            if Mass(Peptide) > max(Spectrum):
                Leaderboard = [i for i in Leaderboard if i != Peptide]
        Leaderboard = Trim(Leaderboard, Spectrum, N)
    return FinalPeptides


#--- GLOBAL VARIABLE ---
AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
                 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 
                 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
#--- GLOBAL VARIABLE ---


def main():
    path = "C:\\Users\\23521\\Downloads\\i.txt"
    N, Spectrum = ReadInput(path)
    #print(N, Spectrum)
    Peptides = LeaderboardCyclopeptideSequencing(Spectrum, N)
    #print(Peptides)
    MaxScore = max(Peptides, key=lambda p: Score(p, Spectrum))
    MaxScore = Score(MaxScore, Spectrum)
    #print(MaxScore)

    Final = []
    for p in Peptides:
        if Score(p, Spectrum) == MaxScore:
            Final.append(p)
    #Final = list(set(Final))
    #print(Final)
    #print(len(Final))
    Output = []
    for p in Final:
        #print(p)
        l = [AminoAcidMass[a]for a in p]
        #print('-'.join(l), end = ' ')
        Output.append(l)
        #print()

    print(*Output, sep = '\n')

    for p in Output:
        l = [str(a) for a in p]
        print('-'.join(l), end = ' ')
    print()

if __name__ == main():
    main()
