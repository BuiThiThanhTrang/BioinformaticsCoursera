def ReadTextPattern(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text, Pattern = dataset.readlines()
    return Text.strip(), Pattern.strip()


def PatternCount(Text, Pattern):
    count = 0
    p_l = len(Pattern)
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + p_l] == Pattern:
            count += 1
    return count


def main():
    path = "C:\\Users\\23521\\Downloads\\t.txt"
    text, pattern = ReadTextPattern(path)
    print(PatternCount(text, pattern))
    return 0


if __name__ == main():
    main()