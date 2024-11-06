import heapq

# Creating Huffman tree node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left  # node left of current node
        self.right = right  # node right of current node
        self.huff = ''  # tree direction (0/1)

    def __lt__(self, nxt):  # Check if curr frequency less than next nodes freq
        return self.freq < nxt.freq

def printnodes(node, val=''):
    # Concatenate current node's Huffman code (0 or 1)
    newval = val + str(node.huff)

    # Traverse left and right children if they exist
    if node.left:
        printnodes(node.left, newval)
    if node.right:
        printnodes(node.right, newval)

    # if node is an edge node then display its huffman code
    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol, newval))

if __name__ == "__main__":
    # User input for characters and their frequencies
    chars = input("Enter the characters (separated by spaces): ").split()
    freq = list(map(int, input("Enter the frequencies (separated by spaces): ").split()))

    # Ensure the number of characters matches the number of frequencies
    if len(chars) != len(freq):
        print("Error: The number of characters and frequencies must match.")
    else:
        # Priority queue to store nodes
        nodes = []

        for i in range(len(chars)):  # Converting characters and frequencies into Huffman tree nodes
            heapq.heappush(nodes, node(freq[i], chars[i]))

        # Construct the Huffman Tree
        while len(nodes) > 1:
            # Remove the two nodes of lowest frequency
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            # Assign binary codes to the nodes
            left.huff = 0
            right.huff = 1

            # Combining the 2 smallest nodes to create new node as their parent
            newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            heapq.heappush(nodes, newnode)

        # Print the Huffman codes
        print("Huffman codes:")
        printnodes(nodes[0])  # Passing root of Huffman Tree
