class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root    

        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()

            current_node = current_node.children[character]

        current_node.is_end_of_word = True
        current_node.frequency += 1

    def find_prefix_node(self, prefix):
        current_node = self.root

        for character in prefix:
            if character not in current_node.children:
                return None

            current_node = current_node.children[character]

        return current_node

    def collect_words(self, node, current_word, results):
        if node.is_end_of_word:
            results.append((current_word, node.frequency))

        for character, child_node in node.children.items():
            self.collect_words(
                child_node,
                current_word + character,
                results
            )

    def autocomplete(self, prefix):
        prefix_node = self.find_prefix_node(prefix)

        if prefix_node is None:
            return []

        results = []

        self.collect_words(prefix_node, prefix, results)

        results.sort(key=lambda item: item[1], reverse=True)

        return results
    
# MAIN CLASS
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
    def search(self , word):
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
        return number_of_result > 0
    #fourth member
    def replace_word(self):
        # modify self.text and call preprocess_text() to update (self.words ,self.sentences)
        # we may need to save the previous text before replacing if we choose undo/redo feature
        pass
    # after finishing another method (easy)
    def next_word_prediction(self):
        pass

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

        
    # after finishing another method (easy)
    def menu(self):
        # display menu and call the correct method  
        pass


analyzer = SmartTextAnalyzer()
analyzer.menu()
