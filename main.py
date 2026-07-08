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
        #calculate (1. total words 2. unique words 3. character statistics) using (self.words ,self.text)
        pass
        # the third member 
    def search(self , word):
        #clean up the entered wordss
        word =word.lower()
        number_of_result = 0
        #splite the entered words 
        requested_word = word.split(" ")
        for sentence_idx,sentence in enumerate(self.sentences , start=1):
            #check if the entered words in the current sentence
            if word in sentence:
                #split the current sentence 
                words_in_sentence = sentence.split(" ")
                #Find words position in the sentence
                for word_idx , current_word  in enumerate(words_in_sentence , start=1) :
                    if requested_word == words_in_sentence[word_idx -1 : word_idx -1 + len(requested_word)]:
                        number_of_result+=1
                        print(f"{number_of_result}: {sentence}")
                        print (f"Found in sentence {sentence_idx}, word position {word_idx}")
        return number_of_result > 0
    #fourth member
    def replace_word(self):
        # modify self.text and call preprocess_text() to update (self.words ,self.sentences)
        # we may need to save the previous text before replacing if we choose undo/redo feature
        pass
    # after finishing another method (easy)
    def menu(self):
        # display menu and call the correct method  
        pass


analyzer = SmartTextAnalyzer()
analyzer.menu()
