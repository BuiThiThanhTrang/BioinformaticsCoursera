
def ReadTextPattern(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Pattern, Text = dataset.readlines()
    return Text.strip(), Pattern.strip()

def PatternMatching(Text, Pattern):
    positions = []
    p_l = len(Pattern)
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + p_l] == Pattern:
            positions.append(i)
    return positions

def main():
    path = "C:\\Users\\23521\\Downloads\\Vibrio_cholerae.txt"
    #text, pattern = ReadTextPattern(path)
    text = 'ATGACTTCGCTGTTACGCGC' 
    pattern = 'CGC'
    print(*PatternMatching(text, pattern))
    return 0


if __name__ == main():
    main()