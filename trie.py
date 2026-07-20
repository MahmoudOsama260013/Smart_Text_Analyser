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
