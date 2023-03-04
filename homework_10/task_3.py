from random import sample


def pemrtuate(text):
    words = text.split()
    
    for i in range(len(words)):
        if len(words[i]) > 3:
            first, *middle, last = words[i]
            new_middle = []
            
            for j in range(0, len(middle), 3):
            
                if j + 3 <= len(middle):
                    original_triple = middle[j:j + 3]
                    permuted_triple = sample(original_triple, 3)
                    while permuted_triple == original_triple:
                        permuted_triple = sample(original_triple, 3)
                    new_middle += permuted_triple
                    
                else:
                    new_middle += middle[j:]
                    
            permuted_word = "".join([first] + new_middle + [last])
            words[i] = permuted_word
            
    return " ".join(words)


def main():
    text = "Не має значення в якому порядку розташовані букви в слові"
    reordered_text = pemrtuate(text)
    print(reordered_text)


if __name__ == "__main__":
    main()
    