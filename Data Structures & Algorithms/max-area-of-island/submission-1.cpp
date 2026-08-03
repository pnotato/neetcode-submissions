// logic, dfs, keep track of max island size.

class Solution {
private:
    vector<vector<int>> grid;
    vector<vector<bool>> visited;
    

    int dfs(int i, int j) {
        if (i >= grid.size() || j >= grid[0].size() || i < 0 || j < 0) {
            return 0;
        }
        if (visited[i][j] || grid[i][j] == 0) {
            return 0;
        }
        visited[i][j] = true;
        return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1) + 1;
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        this->grid = grid;
        this->visited = vector<vector<bool>>(grid.size(), vector<bool>(grid[0].size(), false));
        int maxSize = 0;

        for (int i=0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (!visited[i][j] && grid[i][j] == 1) {
                    int size = dfs(i, j);
                    maxSize = maxSize > size ? maxSize : size;
                }
            }
        }
        return maxSize;
    }
};
