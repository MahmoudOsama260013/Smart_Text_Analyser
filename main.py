import string

class SmartTextAnalyzer:

    def __init__(self):
        """Initialize empty data structures."""
        self.text = ""
        self.words = []
        self.sentences = []

    def load_text(self):
        """Load text manually or from a file."""
        print("Choose input method:")
        print("1. Enter text manually")
        print("2. Load text from file")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter your text. Type $$END_TEXT$$ on a new line when done:")
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
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")
            return

        self.preprocess_text()
        print("\n✅ Text processed and lists are ready!")

    def preprocess_text(self):
        """
        Clean and split text into sentences and words.
        IMPORTANT: Uses _clean_text() for consistency.
        """
        # Replace ! and ? with . to split sentences properly
        temp = self.text.replace('!', '.').replace('?', '.')
        
        # Split sentences using _clean_text() to avoid duplicate logic
        self.sentences = [
            self._clean_text(s)
            for s in temp.split('.')
            if s.strip()
        ]
        
        # Reuse _clean_text() for entire text to extract words
        clean_text = self._clean_text(self.text)
        self.words = clean_text.split()

    def _clean_text(self, text):
        """
        Remove punctuation, convert to lowercase, strip whitespace.
        IMPORTANT: Keeps apostrophes to preserve contractions (don't).
        """
        punctuation = string.punctuation.replace("'", "")  # Keep apostrophes
        translator = str.maketrans("", "", punctuation)
        return text.lower().translate(translator).strip()

    def _extract_words(self, text):
        """
        Extract unique words as a Set.
        IMPORTANT: Set removes duplicates automatically.
        """
        clean = self._clean_text(text)
        return set(word for word in clean.split() if word)  # Filter empty strings

    def _calculate_similarity(self, text2):
        """
        Compute Jaccard Similarity = |Intersection| / |Union|.
        IMPORTANT: Uses Sets for O(1) intersection/union operations.
        """
        words1 = set(self.words)                 # Master text words
        words2 = self._extract_words(text2)      # Second text words

        intersection = words1.intersection(words2)
        union = words1.union(words2)

        # Avoid division by zero
        similarity = len(intersection) / len(union) if union else 0.0

        return similarity, words1, words2, intersection, union

    def _get_second_text(self):
        """Get second text from user (manual or file)."""
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
        """Interpret similarity score with descriptive labels."""
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
        """Display common words (limit to 20 for readability)."""
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
        MAIN METHOD: Text Similarity Detector.
        Appears in menu as option #5.
        Returns similarity score (float) or None on error.
        """
        print("\n" + "="*50)
        print("📊 TEXT SIMILARITY DETECTOR")
        print("="*50)

        # Validate text is loaded
        if not self.words:
            print("❌ No text loaded! Please load text first.")
            return None

        # Get second text
        second_text = self._get_second_text()
        if second_text is None:
            return None
        if not second_text.strip():
            print("❌ No text provided!")
            return None

        # Calculate similarity
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

        # Interpret result
        print("\n📌 Interpretation:")
        print(f"   {self._interpret_similarity(similarity)}")

        # Show common words
        self._display_common_words(intersection)

        print("="*50)

        # Return similarity for potential future use
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
