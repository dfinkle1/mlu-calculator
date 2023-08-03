def calculate_morphemes(word):
    # Define a list of common English suffixes and irregular forms
    suffixes_and_irregulars = ['s', 'es', 'ed', 'ing', 'en', 'er', 'est', 'ly', 'able', 'ible', 'un', 're']

    # Initialize the count of morphemes
    num_morphemes = 0

    # Process the word while it's not an empty string
    while word:
        # Check if the word is an irregular form (e.g., 'was')
        if word in suffixes_and_irregulars:
            num_morphemes += 1
            break

        # Check if the word ends with a known suffix or irregular form
        found_suffix = False
        for suffix in suffixes_and_irregulars:
            if word.endswith(suffix):
                num_morphemes += 1
                word = word[:-len(suffix)]
                found_suffix = True
                break

        if not found_suffix:
            # No known suffix or irregular form found, consider the whole word as a root
            num_morphemes += 1
            break

    return num_morphemes

def count_utterances(paragraph):
    # Count the number of utterances (sentences) based on '.'
    num_utterances = paragraph.count('.')

    return num_utterances

def main():
    print("Welcome to the Morpheme and Utterance Counter!")
    print("Enter a paragraph, and I will count the number of morphemes and utterances in it.")

    paragraph = input("Enter the paragraph (or 'exit' to quit):\n")

    while paragraph.lower() != 'exit':
        # Split the paragraph into sentences based on '.'
        num_utterances = count_utterances(paragraph)

        # Split the paragraph into words
        words = paragraph.split()

        # Calculate the total number of morphemes in the paragraph
        total_morphemes = sum(calculate_morphemes(word) for word in words)

        # Calculate MLU (morphemes divided by utterances)
        if num_utterances > 0:
            mlu = total_morphemes / num_utterances
        else:
            mlu = 0

        print(f"\nThe paragraph contains {num_utterances} utterances (sentences).")
        print(f"The paragraph contains {total_morphemes} morphemes.")
        print(f"The MLU (Morphemes per Utterance) for the paragraph is: {mlu:.2f}\n")

        paragraph = input("Enter the paragraph (or 'exit' to quit):\n")

if __name__ == "__main__":
    main()
