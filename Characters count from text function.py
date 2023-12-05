### Count each alphabet character from text fuction

import matplotlib.pyplot as plt
from collections import Counter
import string

def plot_char_frequencies(text):
    # Count the frequencies of each alphabet character
    char_counts = Counter(char for char in text if char.isalpha())

    # Extract alphabet characters and their corresponding frequencies
    alphabet = list(string.ascii_uppercase)
    frequencies = [char_counts[char] for char in alphabet]

    # Plot the bar chart
    plt.bar(alphabet, frequencies)
    plt.xlabel("Alphabet Characters")
    plt.ylabel("Frequencies")
    plt.title("Character Frequencies in the Document")
    plt.show()

if __name__ == "__main__":
    # Get the document input from the user
    document = input("Enter the document text: ")

    # Plot the character frequencies
    plot_char_frequencies(document.upper()) # Convert the uppercase for case-insensitivity
