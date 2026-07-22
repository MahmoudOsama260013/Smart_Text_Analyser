class SmartTextAnalyzer:

    def __init__(self):
        self.text = ""
        self.words = []
        self.sentences = []
        self.trie = Trie()
    # the first member
    def load_text(self):
        # loading the text from file or text and save it
        pass

    def preprocess_text(self):
        #modifying  (self.text,self.words ,self.sentences) variables
        pass
      # the second member 
    def dashboard(self):
        #calculate (1. total words 2. unique words 3. character statistics) using (self.words ,self.text)
        pass
      # the third member 
    def search(self):
        #clean up the entered wordss
        word =word.lower()
        number_of_result = 0
        requested_word = word.split()
        for sentence_idx,sentence in enumerate(self.sentences , start=1):
            words_in_sentence = sentence.split()
            #Find word position in the sentence
            for word_idx , current_word  in enumerate(words_in_sentence , start=1) :
                if requested_word == words_in_sentence[word_idx -1 : word_idx -1 + len(requested_word)]:
                    number_of_result+=1
                    print(f"{number_of_result}: {sentence}")
                    print (f"Found in sentence {sentence_idx}, word position {word_idx}")
        if number_of_result == 0 :
            print("Word not found")
        return number_of_result > 0
      #fourth member
    def replace_word(self):
        # modify self.text and call preprocess_text() to update (self.words ,self.sentences)
        # we may need to save the previous text before replacing if we choose undo/redo feature
        pass
    def next_word_prediction(self):
        pass
      # after finishing another method (easy)
        #Build the Trie 
    def build_trie(self):
        self.trie = Trie()
        for word in self.words:
            self.trie.insert(word)

    def autocompletion(self , prefix):
        suggestions = self.trie.autocomplete(prefix)

        if not suggestions:
            print("No suggestions found.")
            return

        print("\nAutocomplete suggestions:")

        for word , frequency in suggestions:
            print(f"{word}")
    def menu(self):
        # display menu and call the correct method  
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
