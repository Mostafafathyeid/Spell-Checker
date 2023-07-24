class TreeNode:           # use Tree allows to efficiently search by using dfs
    def __init__(self):
        self.children = {}
        self.end = False # end of word

class SpellChecker:
    def __init__(self):
        self.root = TreeNode()

    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.end = True

    def build_dictionary(self, words):  # Time complexity: O(n*m) & space cpmlexity: O(n*m)
        for word in words:
            self.insert(word)

    def add_word(self, word):           # Time complexity: O(m) & space cpmlexity: O(m)
        self.insert(word)

    def nearest_words(self, word, max_results=4):   # Time complexity: O(k*m) & space cpmlexity: O(m)
        def dfs(node, prefix, result):
            if len(result) >= max_results:
                return
            if node.end:
                result.append(prefix)

            for char, child_node in node.children.items():
                dfs(child_node, prefix + char, result)

        results = []
        current_node = self.root
        prefix = ""

        for char in word:
            if char not in current_node.children:
                return results
            current_node = current_node.children[char]
            prefix += char

        dfs(current_node, prefix, results)
        return results
    

if __name__ == "__main__":
    d = open("dictionary.txt", encoding='cp437')
    data = d.read()
    list1 = data.split("\n")
    #print(list1[0])
    #print(list1[44000])
    d.close()

    spell_checker = SpellChecker()
    spell_checker.build_dictionary(list1)

    word_to_check = "aa"
    nearest_words = spell_checker.nearest_words(word_to_check)
    print(f"Nearest words to '{word_to_check}': {nearest_words}")

    word_to_check = "apppppppp"
    nearest_words = spell_checker.nearest_words(word_to_check)
    print(f"Nearest words to '{word_to_check}': {nearest_words}")

    word_to_add = "orange"
    spell_checker.add_word(word_to_add)
    print(f"'{word_to_add}' added to the dictionary.")

    word_to_check = "orange"
    nearest_words = spell_checker.nearest_words(word_to_check)
    print(f"Nearest words to '{word_to_check}': {nearest_words}")


