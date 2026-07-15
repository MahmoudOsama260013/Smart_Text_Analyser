class SmartTextAnalyzer:

    def __init__(self):
        self.text = ""
        self.words = []
        self.sentences = []
    # the first member
    def load_text(self):
        # loading the text from file or text and save it
        pass

    def preprocess_text(self):
        #modifying  (self.text,self.words ,self.sentences) variables
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
      #fourth member
    def replace_word(self):
        # modify self.text and call preprocess_text() to update (self.words ,self.sentences)
        # we may need to save the previous text before replacing if we choose undo/redo feature
        pass
    def next_word_prediction(self):
        pass
      # after finishing another method (easy)
    def menu(self):
        # display menu and call the correct method  
        while True:
                while True:
        print("\n===== Smart Text Analyzer =====")
        print("1. Load Text")
        print("2. Dashboard")
        print("3. Search")
        print("4. Replace Word")
        print("5. Next Word Prediction")
        print("6. Autocompletion")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.load_text()

        elif choice == "2":
            self.dashboard()

        elif choice == "3":
            word = input("Enter word to search: ")
            self.search(word)

        elif choice == "4":
            self.replace_word()

        elif choice == "5":
            self.next_word_prediction()

        elif choice == "6":
            prefix = input("Enter prefix: ").lower()
            self.autocompletion(prefix)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
        pass


analyzer = SmartTextAnalyzer()
analyzer.menu()
