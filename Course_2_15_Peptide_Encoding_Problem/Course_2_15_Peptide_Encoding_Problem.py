def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text = dataset.readline().strip()
        Peptide = dataset.readline().strip()
    return Text, Peptide

def ReverseComplement(Text):
    Text = Text[::-1]
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    r = ""
    for i in Text:
        r += d[i]
    return r

def DNA2tRNA(Text):
    s = ['U' if i == 'T' else i for i in Text]
    return ''.join(s)

def tRNA2Peptide(Pattern):
    LastIdx = (len(Pattern) // 3 - 1) * 3
    Peptide = ''
    for i in range(0, LastIdx + 1, 3):
        Peptide += GeneticCode[Pattern[i:i+3]]
    return Peptide

def EncodingSubstringRNA(TextRNA, Peptide):
    Length = len(Peptide) * 3
    Positions = []
    for i in range(len(TextRNA) - Length + 1):
        Substring = TextRNA[i:i+Length]
        #print(tRNA2Peptide(Substring))
        if Peptide == tRNA2Peptide(Substring):
            Positions.append(i)
    return Positions

def EncodingSubstringDNA(TextDNA, Peptide):
    #print(DNA2tRNA(ReverseComplement(TextDNA)))
    Pos53 = EncodingSubstringRNA(DNA2tRNA(TextDNA), Peptide)
    Pos35 = EncodingSubstringRNA(DNA2tRNA(ReverseComplement(TextDNA)), Peptide)
    Substrings = []
    Length = len(Peptide) * 3
    for i in Pos53:
        Substrings.append(TextDNA[i:i+Length])
    for i in Pos35:
        Substrings.append(TextDNA[-i - Length:-i])
    return Substrings

GeneticCode = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 
               'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 
               'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 
               'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I', 
               'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 
               'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 
               'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 
               'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 
               'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D', 
               'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 
               'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 
               'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 
               'UAA': '', 'UAC': 'Y', 'UAG': '', 'UAU': 'Y', 
               'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 
               'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 
               'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'}


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30213_7.txt"
    Text, Peptide = ReadInput(path)
    #Text = DNA2tRNA(Text)
    print(*EncodingSubstringDNA(Text, Peptide), sep = '\n')


if __name__ == main():
    main()
