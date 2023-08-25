class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
    
    # Create a dictionary to store the longest chain length for each word
        word_chain = {}
    
    # Initialize the longest chain length
        max_chain_length = 1
    
        for word in words:
        # Initialize the chain length for the current word as 1
            word_chain[word] = 1

            # Generate all possible predecessors of the current word
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]

                # Check if the predecessor is in the dictionary
                if predecessor in word_chain:
                    # Update the chain length for the current word
                    word_chain[word] = max(word_chain[word], word_chain[predecessor] + 1)

            # Update the maximum chain length
            max_chain_length = max(max_chain_length, word_chain[word])

        return max_chain_length
        