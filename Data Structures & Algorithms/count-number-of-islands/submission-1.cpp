class Solution {
private:
    vector<vector<char>> grid;
    vector<vector<bool>> visited;

    void dfs(int i, int j) {
        // if out of bounds, current square is visited or water
        if (i >= grid.size() || j >= grid[0].size() || i < 0 || j < 0 || visited[i][j] || grid[i][j] == '0') {
            return;
        }
        visited[i][j] = true;
        dfs(i+1, j);
        dfs(i-1, j);
        dfs(i, j+1);
        dfs(i, j-1);
    }

public:

    int numIslands(vector<vector<char>>& grid) {
        this->grid = grid;
        visited = vector<vector<bool>>(grid.size(), vector<bool>(grid[0].size(), false));

        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    dfs(i, j);
                    count++;
                }
            }
        }
        return count;
    }
};
