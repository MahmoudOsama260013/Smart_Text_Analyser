import string

class SmartTextAnalyzer:
    def __init__(self):
        self.text = ""          
        self.words = []         
        self.sentences = []       

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
        
    def dashboard(self):
        print(f"\nTotal words: {len(self.words)}")
        print(f"Unique words: {len(set(self.words))}")
        chars = [c for c in self.text if c not in string.whitespace]
        print(f"Total characters (no spaces): {len(chars)}")

    def menu(self):
        self.load_text()
        while True:
            print("\n1. Dashboard\n2. Exit")
            choice = input("Choice: ")
            if choice == "1":
                self.dashboard()
            elif choice == "2":
                break

if __name__ == "__main__":
    analyzer = SmartTextAnalyzer()
    analyzer.menu()
