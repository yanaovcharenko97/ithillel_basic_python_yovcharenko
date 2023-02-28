from random import sample


def pemrtuate(text):
    words = text.split()
    for i in range(len(words)):
        if len(words[i]) > 3:
            first, *middle, last = words[i]
            while True:
                permuted_middle = sample(middle, len(middle))
                if permuted_middle != middle:
                    permuted_word = "".join([first, *permuted_middle, last])
                    words[i] = permuted_word
                    break
                else:
                    continue
    return " ".join(words)


def main():
    text = "Не має значення в якому порядку розташовані букви в слові"
    reordered_text = pemrtuate(text)
    print(reordered_text)


if __name__ == "__main__":
    main()
