class SmartTextAnalyzer:

    def __init__(self):
        self.text = ""
        self.words = []
        self.sentences = []
        self.bigram_counts = {}
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
        if not self.words:
            print("No text loaded! Please load text first.")
            return
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
    
    def build_bigram_counts(self):
        self.bigram_counts = {}
        # build bigram counts: {word : {next_word: count}}
        for i in range(len(self.words) - 1):
            word = self.words[i]
            next_word = self.words[i + 1]
            if word not in self.bigram_counts:
                self.bigram_counts[word] = {}
            self.bigram_counts[word][next_word] = self.bigram_counts[word].get(next_word, 0) + 1
            
    def next_word_prediction(self):
        if not self.words:
            print("No text loaded!")
            return
        # keep asking until we get a valid word or the user exits
        while True:
            target_word = input("Enter the word to get next (or 'exit' to cancel): ").strip().lower()
            if target_word == "exit":
                return
            if target_word not in self.bigram_counts:
                print("Sorry the word not found, try again")
            else:
                next_words_freq = self.bigram_counts[target_word]
                break
            
        # find the next word(s) with the highest frequency 
        max_count = 0
        most_freq_words = []
        for next_word, freq in next_words_freq.items():
            if freq > max_count:
                max_count = freq
                most_freq_words = [next_word]  # reset list, new max found
            elif freq == max_count:
                most_freq_words.append(next_word)  # add to list
                
        # display results
        print(f"( {len(most_freq_words)} ) words match")
        for suggestion in most_freq_words:
            print(f"{target_word} {suggestion}")
            
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
