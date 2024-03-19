# Slow Method (using a linear search): This approach involves storing the nodes in an unsorted list. Each time we need to find the node with the smallest distance, we perform a linear search through the list, which takes O(n) time for each selection, where n is the number of nodes in the queue.

# Faster Method (using a min-heap): A more efficient way to implement the priority queue is by using a min-heap. This data structure allows us to both insert new nodes and find and remove the node with the smallest distance in O(log n) time, significantly speeding up the algorithm.

