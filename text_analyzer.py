
import string
import re

from trie import Trie


class SmartTextAnalyzer:

    def __init__(self):
        self.text = ""
        self.words = []
        self.sentences = []
        self.trie = Trie()
        self.bigram_counts = {}
        self.undo_stack = []
        self.redo_stack = []
        
    def load_text(self):
        """Load text manually or from a file."""
        self.undo_stack.clear()
        self.redo_stack.clear()
        
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
        self.build_trie()
        self.build_bigram_counts()

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
    def search(self,word):
        if not word:
            print("Invalid Input")
            return False
        #clean up the entered wordss
        word =word.lower()
        number_of_result = 0
        requested_word = word.split()
        # find the sentence
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


    
    def menu(self):
        # display menu and call the correct method  
        while True:
               
            print("1. Load Text")
            print("2. Dashboard")
            print("3. Search")
            print("4. Replace Word")
            print("5. Next Word Prediction")
            print("6. Autocompletion")
            print("7. Text Similarity")
            print("8. Undo")
            print("9. Redo")
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
            elif choice == "7":
                self.text_similarity()

            elif choice == "8":
                self.undo()

            elif choice == "9":
                self.redo()
            elif choice == "0":
                print("Goodbye!")
                break
    
            else:
                print("Invalid choice!")
