class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_color = image[sr][sc]
        if s_color == color:
            return image
        self.dfs(image, sr, sc, color, s_color)
        return image
    def dfs(self, image, sr, sc, color, s_color):
        rows = len(image)
        columns = len(image[0])
        # 1. Boundary and Base Case Checks
        if sr < 0 or sr >= rows or sc < 0 or sc >= columns or image[sr][sc] != s_color:
            return
        
        # 2. Process Current Node
        image[sr][sc] = color
        
        # 3. Recursive calls for neighbors
        self.dfs(image, sr + 1, sc, color, s_color)
        self.dfs(image, sr - 1, sc, color, s_color)
        self.dfs(image, sr, sc + 1, color, s_color)
        self.dfs(image, sr, sc - 1, color, s_color)