
def ReadText(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text = dataset.readlines()[0]
    return Text.strip()


def ReverseComplement(Text):
    Text = Text[::-1]
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    r = ""
    for i in Text:
        r += d[i]
    return r


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30273_2 (1).txt"
    # text = ReadText(path)
    text = "TTGTGTC"
    print(ReverseComplement(text))
    return 0


if __name__ == main():
    main()