from collections import Counter

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Leaderboard = dataset.readline().strip().split()
        Spectrum = dataset.readline().strip().split()
        N = dataset.readline().strip()
        for i in range(len(Spectrum)):
            Spectrum[i] = int(Spectrum[i])
    return Leaderboard, Spectrum, int(N)

def Mass(Peptide):
    return sum([AminoAcidMass[i] for i in Peptide])

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


#--- GLOBAL VARIABLE ---
AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
                 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 
                 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
#--- GLOBAL VARIABLE ---


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30249_3.txt"
    Leaderboard, Spectrum, N = ReadInput(path)
    print(Leaderboard, Spectrum, N)
    print(*Trim(Leaderboard, Spectrum, N))

if __name__ == main():
    main()
