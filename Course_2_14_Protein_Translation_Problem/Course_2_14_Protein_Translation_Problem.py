def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text = dataset.read().strip()
    return Text

def tRNA2Peptide(Pattern):
    LastIdx = (len(Pattern) // 3 - 1) * 3
    Peptide = ''
    for i in range(0, LastIdx + 1, 3):
        Peptide += GeneticCode[Pattern[i:i+3]]
    return Peptide

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
    path = "C:\\Users\\23521\\Downloads\\dataset_30213_4.txt"
    RNA = ReadInput(path)
    print(tRNA2Peptide(RNA))


if __name__ == main():
    main()
