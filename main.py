import string

class SmartTextAnalyzer:

    def __init__(self):
         """Initialize the analyzer with empty text and data structures"""
        self.text = ""    # Raw text input
        self.words = []   # List of all words after preprocessing
        self.sentences = []  # List of sentences after preprocessing
    # the first member
    def load_text(self):
        """
        Load text either manually or from a file
        Manual input: Type $$END_TEXT$$ on a new line to finish
        File input: Provide full file path
        """
        print("Choose input method:")
        print("1. Enter text manually")
        print("2. Load text from file")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nEnter your text. Type $$END_TEXT$$ on a new line when finished.\n")
            lines = []
            while True:
                line = input()
                if line.strip() == "$$END_TEXT$$": # Sentinel to stop input
                    break
                lines.append(line)
            self.text = "\n".join(lines)  # Join with newlines
            
        elif choice == "2":
            path = input("Enter file path: ")
            try:
                with open(path, "r", encoding="utf-8") as file:
                    self.text = file.read()
            except Exception as e:
                print("Error:", e)
                return  # Exit if file fails to load
        # Preprocess after loading
        self.preprocess_text()
        print("\nText processed and lists are ready!")

    def preprocess_text(self): 
        temp = self.text  # Step 1: Replace ! and ? with . for sentence splitting
        temp = temp.replace('!', '.')
        temp = temp.replace('?', '.')
        self.sentences = [s.strip().lower() for s in temp.split('.') if s.strip()]   # Step 2: Split into sentences
        punctuation = string.punctuation.replace("'", "")   # Step 3: Remove punctuation for word processing
        translator = str.maketrans("", "", punctuation) # ✅ FIXED: Keep apostrophes
        clean_text = self.text.lower().translate(translator)
        self.words = clean_text.split()
        self.build_trie()
        self.build_bigram_counts()

    def _calculate_similarity(self, text2):
    """
    Calculate Jaccard Similarity between master text and second text
    Returns: similarity score and sets of words
    """
    # Use existing preprocessed words for master text
    words1 = set(self.words)  # Already preprocessed
    
    # Process the second text using existing _extract_words() method
    words2 = self._extract_words(text2)
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    # Simplified similarity calculation
    similarity = len(intersection) / len(union) if union else 0.0
    
    return similarity, words1, words2, intersection, union

def _get_second_text(self):
    """Get second text from user - reusable UI method"""
    print("\nChoose input method for second text:")
    print("1. Enter text manually")
    print("2. Load text from file")
    choice = input("Enter your choice: ")
    
    second_text = ""
    
    if choice == "1":
        print("\nEnter your text. Type $$END_TEXT$$ on a new line when done:")
        lines = []
        while True:
            line = input()
            if line.strip() == "$$END_TEXT$$":
                break
            lines.append(line)
        second_text = "\n".join(lines)
        
    elif choice == "2":
        path = input("Enter file path: ")
        try:
            with open(path, "r", encoding="utf-8") as file:
                second_text = file.read()
        except Exception as e:
            print("❌ Error:", e)
            return None
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")
        return None
    
    return second_text

def _interpret_similarity(self, similarity):
    """Interpret similarity score"""
    if similarity >= 0.7:
        return "✅ Very High Similarity - Texts are almost identical!"
    elif similarity >= 0.5:
        return "👍 High Similarity - Texts share significant content!"
    elif similarity >= 0.3:
        return "📖 Moderate Similarity - Texts share some content!"
    elif similarity >= 0.1:
        return "🔍 Low Similarity - Texts have little in common!"
    else:
        return "❌ Very Low Similarity - Texts are completely different!"

def _display_common_words(self, intersection):
    """Display common words between texts"""
    if not intersection:
        return
    
    if len(intersection) <= 20:
        print("\n📚 Common words:")
        print(f"   {', '.join(sorted(intersection))}")
    else:
        print(f"\n📚 Showing first 20 common words (out of {len(intersection)}):")
        print(f"   {', '.join(sorted(intersection)[:20])}")

def text_similarity(self):
    """
    Text Similarity Detector - Main UI method
    Uses helper methods for calculation and display
    """
    print("\n" + "="*50)
    print("📊 TEXT SIMILARITY DETECTOR")
    print("="*50)
    
    # Check if text has been preprocessed
    if not self.words:
        print("❌ No text loaded! Please load text first.")
        return
    
    # Get second text from user
    second_text = self._get_second_text()
    
    # Check if user cancelled or entered invalid input
    if second_text is None:
        return
    
    # Check if text is empty or only whitespace
    if not second_text.strip():
        print("❌ No text provided!")
        return
    
    # Calculate similarity using reusable helper
    similarity, words1, words2, intersection, union = self._calculate_similarity(
        second_text
    )
    
    # Display results
    print("\n" + "="*50)
    print("📈 SIMILARITY RESULTS")
    print("="*50)
    print(f"📝 Main text words: {len(words1)} unique words")
    print(f"📝 Second text words: {len(words2)} unique words")
    print(f"🔗 Common words: {len(intersection)}")
    print(f"🔗 Total unique words (union): {len(union)}")
    print(f"\n📊 Jaccard Similarity Score: {similarity:.2%}")
    print(f"📊 Similarity Score (0-1): {similarity:.4f}")
    
    # Interpret the result
    print("\n📌 Interpretation:")
    print(f"   {self._interpret_similarity(similarity)}")
    
    # Show common words
    self._display_common_words(intersection)
    
    print("="*50)
    
    # Return result for potential future use
    return similarity
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
