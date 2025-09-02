
def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Dna = dataset.readline()
        k = dataset.readline()
        #Profile_text =  dataset.read().split("\n")
        Profile = {"A":[], "C": [], "G": [], "T":[]}
        Profile["A"] = [float(i) for i in dataset.readline().split()]
        Profile["C"] = [float(i) for i in dataset.readline().split()]
        Profile["G"] = [float(i) for i in dataset.readline().split()]
        Profile["T"] = [float(i) for i in dataset.readline().split()]
    return Dna.strip(), k.strip(), Profile 

def Pr(text, Profile):
    p = 1
    k = len(text)
    for i in range(k):
        p *= Profile[text[i]][i]
    return p

def ProfileMostProbableKMer(Dna, k, Profile):
    maxP = 0
    kmer = ""
    for i in range(len(Dna) - k + 1):
        text = Dna[i:i+k]
        if Pr(text, Profile) >= maxP:
            maxP = Pr(text, Profile)
            print(text, maxP)
            kmer = text
    return kmer

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30305_3.txt"
    Dna, k, Profile = ReadInput(path)
    print(ReadInput(path))
    print(ProfileMostProbableKMer(Dna, int(k), Profile))

    return 0


if __name__ == main():
    main()