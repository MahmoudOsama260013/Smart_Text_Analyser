import string

class SmartTextAnalyzer:

    def __init__(self):
        self.text = ""
        self.words = []
        self.sentences = []
    # the first member
    def load_text(self):
        print("Choose input method:")
        print("1. Enter text manually")
        print("2. Load text from file")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nEnter your text. Type $$END_TEXT$$ on a new line when finished.\n")
            lines = []
            while True:
                line = input()
                if line.strip() == "$$END_TEXT$$":
                    break
                lines.append(line)
            self.text = "\n".join(lines)
            
        elif choice == "2":
            path = input("Enter file path: ")
            try:
                with open(path, "r", encoding="utf-8") as file:
                    self.text = file.read()
            except Exception as e:
                print("Error:", e)
                return
        
        self.preprocess_text()
        print("\nText processed and lists are ready!")

    def preprocess_text(self):
        temp = self.text
        temp = temp.replace('!', '.')
        temp = temp.replace('?', '.')
        self.sentences = [s.strip() for s in temp.split('.') if s.strip()]
        punctuation = string.punctuation.replace("'", "")  
        translator = str.maketrans("", "", punctuation)
        clean_text = self.text.lower().translate(translator)
        self.words = clean_text.split()
      # the second member 
    def dashboard(self):
        #calculate (1. total words 2. unique words 3. character statistics) using (self.words ,self.text)
        pass
      # the third member 
    def search(self):
        # find the word using (self.words ,self.sentences)
        pass
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
