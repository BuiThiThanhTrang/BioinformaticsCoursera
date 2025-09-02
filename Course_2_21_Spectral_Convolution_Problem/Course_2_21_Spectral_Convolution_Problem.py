
def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Spectrum = dataset.read().strip().split()
        for i in range(len(Spectrum)):
            Spectrum[i] = int(Spectrum[i])
    return Spectrum

def SpectralConvolution(Spectrum):
    l = len(Spectrum)
    Conv = []
    for i in range(l):
        for j in range(i + 1, l):
            Conv.append(Spectrum[j] - Spectrum[i])
    Conv = [i for i in Conv if i != 0 and i in range(57, 201)]
    return Conv

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30246_4 (1).txt"
    Spectrum = ReadInput(path)
    print(Spectrum)
    print(*SpectralConvolution(Spectrum))
    pass

if __name__ == main():
    main()
