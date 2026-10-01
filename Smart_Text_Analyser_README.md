# Smart Text Analyzer

A modular command-line text analysis application built with Python. The project provides several text-processing utilities, including text statistics, search and replacement, autocomplete using a Trie, next-word prediction using bigram frequencies, text similarity analysis, and undo/redo support.

## Features

- Load text manually or from a text file
- Clean and preprocess text
- Display a text-analysis dashboard
- Count total words, unique words, characters, and character frequencies
- Search for words and show their sentence and position
- Replace words using case-insensitive matching
- Undo and redo text replacements
- Autocomplete words using a Trie data structure
- Predict likely next words using bigram frequencies
- Compare two texts using Jaccard similarity
- Display common words and similarity interpretation

## Project Structure

```text
Smart_Text_Analyser/
├── main.py
├── text_analyzer.py
├── trie.py
├── .gitignore
└── .gitattributes
```

### `main.py`

The entry point of the application. It creates a `SmartTextAnalyzer` object and starts the interactive menu.

### `text_analyzer.py`

Contains the main `SmartTextAnalyzer` class and implements the application's text-processing features.

### `trie.py`

Implements the `TrieNode` and `Trie` classes used for prefix-based autocomplete.

## How It Works

### Text preprocessing

The application converts text to lowercase, removes punctuation while preserving apostrophes, separates the text into words and sentences, and prepares the data structures required by the other features.

### Dashboard

The dashboard displays:

- Total number of words
- Number of unique words
- Total characters excluding spaces
- Character frequencies

### Word Search

Users can search for a word in the loaded text. The application displays matching sentences and the position of the word.

### Replace, Undo, and Redo

Words can be replaced throughout the text using case-insensitive regular-expression matching. Previous versions of the text are stored in undo and redo stacks.

### Autocomplete with Trie

The project uses a Trie data structure to efficiently store words and find words that begin with a given prefix. Suggestions are ordered using stored word frequencies.

### Next-Word Prediction

The analyzer builds bigram frequency counts from adjacent words in the loaded text. When the user enters a word, the application suggests the most frequent word or words that follow it.

### Text Similarity

Two texts can be compared using Jaccard similarity:

```text
Jaccard Similarity = |Intersection| / |Union|
```

The application reports:

- Unique words in each text
- Number of common words
- Total unique words
- Similarity percentage
- A descriptive interpretation of the similarity

## Technologies and Concepts

- Python
- Object-Oriented Programming
- Trie data structure
- Dictionaries and Sets
- Regular Expressions
- Stack-based Undo/Redo
- Bigram frequency analysis
- Jaccard Similarity
- File handling
- Modular program design

## Requirements

The project uses only the Python standard library and does not require external packages.

Recommended:

```text
Python 3.x
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/MahmoudOsama260013/Smart_Text_Analyser.git
```

Move into the project directory:

```bash
cd Smart_Text_Analyser
```

Run the application:

```bash
python main.py
```

## Menu

```text
1. Load Text
2. Dashboard
3. Search
4. Replace Word
5. Next Word Prediction
6. Autocompletion
7. Text Similarity
8. Undo
9. Redo
0. Exit
```

## What I Practiced

This project provided practical experience with:

- Designing a modular Python application
- Implementing custom data structures
- Processing and analyzing text
- Building prefix-based search with a Trie
- Using frequency-based language patterns
- Implementing similarity measures
- Managing application state with undo/redo stacks
- Working collaboratively on a software project

## Contributors

- Mahmoud Osama Hassan Alsagga
- Mahmoud Hamdi Ahmed Abu Saada
- Anas Mohammed Hamdan AbuQuta
- Ramadan Fadi Ramadan Ziara

## Future Improvements

Possible improvements include:

- Add automated unit tests
- Add a graphical or web-based interface
- Save processed text and analysis results
- Improve tokenization and sentence splitting
- Add stop-word filtering and stemming/lemmatization
- Extend next-word prediction beyond simple bigrams
- Add more advanced text-similarity methods
