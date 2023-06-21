class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        max_side = 0
        
        # Create an auxiliary 1D array to store the previous row's values
        prev_row = [0] * (cols + 1)
        
        # Iterate over each cell in the matrix
        for i in range(1, rows + 1):
            # Create a variable to store the value of the previous column
            prev_col = 0
            
            for j in range(1, cols + 1):
                # Store the current cell value before updating it
                temp = prev_row[j]
                
                if matrix[i - 1][j - 1] == '1':
                    # Calculate the side length of the current square based on the surrounding cells
                    prev_row[j] = min(prev_row[j - 1], prev_row[j], prev_col) + 1
                    max_side = max(max_side, prev_row[j])
                else:
                    # If the current cell is '0', set the value in the auxiliary array to 0
                    prev_row[j] = 0
                
                # Update the value of the previous column for the next iteration
                prev_col = temp
        
        # Return the area of the largest square
        return max_side * max_side