import re


class SmartTextAnalyzer:

    def __init__(self):
        self.text = ""
        self.words = []
        self.sentences = []

        self.undo_stack = []
        self.redo_stack = []

    # the first member
    def load_text(self):
        # loading the text from file or text and save it
        pass

    def preprocess_text(self):
        # modifying  (self.text,self.words ,self.sentences) variables
        pass

    # the second member
    def dashboard(self):
        """calculate (1. total words 2. unique words 3. character statistics) using (self.words ,self.text)"""

        # Get unique words using a set
        unique_words = set(self.words)

        # Join all words together with no spaces, to count number of characters
        all_chars_no_spaces = "".join(word.strip() for word in self.words)

        # Count how many times each character appears
        freq_char = {}
        for char in all_chars_no_spaces:
            freq_char[char] = freq_char.get(char, 0) + 1

        print("- " * 50)
        print("SMART TEXT ANALYZER DASHBOARD")
        print("- " * 50)
        print(f"Count Of All Words: {len(self.words)}")
        print(f"Count Of Unique Words: {len(unique_words)}")
        print(f"Total Characters Without Spaces: {len(all_chars_no_spaces)}")
        print("- " * 50)
        print("Characters Frequency")
        print("- " * 50)

        # Sort characters from most frequent to least frequent
        sorted_characters = sorted(freq_char.items(), key=lambda x: x[1], reverse=True)

        for char, freq in sorted_characters:
            print(f"{char} → {freq}")

    # the third member
    def search(self):
        # find the word using (self.words ,self.sentences)
        pass

    # fourth member
    def replace_word(self):
        old_word = input("Enter the word you want to replace: ").strip()
        new_word = input("Enter the new word: ").strip()
        if old_word == "" or new_word == "":
            print("Invalid input. Please enter valid words.")
            return

        pattern = rf"\b{re.escape(old_word)}\b"
        matches = re.findall(pattern, self.text, flags=re.IGNORECASE)
        if not matches:
            print("The word was not found in the text.")
            return
        self.undo_stack.append(self.text)
        self.redo_stack.clear()
        self.text = re.sub(pattern, new_word, self.text, flags=re.IGNORECASE)

        self.preprocess_text()
        print(
            f"Replaced {len(matches)} occurrence(s) "
            f"of '{old_word}' with '{new_word}'."
        )

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        self.preprocess_text()
        print("Undo completed successfully.")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        self.preprocess_text()
        print("Redo completed successfully.")

    # after finishing another method (easy)
    def menu(self):
        # display menu and call the correct method
        pass


analyzer = SmartTextAnalyzer()
analyzer.menu()
