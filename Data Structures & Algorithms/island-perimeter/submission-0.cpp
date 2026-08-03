class Solution {
private:
    vector<vector<int>> grid;
    vector<vector<bool>> visited;

    int dfs(int i, int j) {
        if (i >= grid.size() || j >= grid[0].size() || i < 0 || j < 0 || grid[i][j] == 0) {
            return 1;
        }
        if (visited[i][j]) {
            return 0;
        }

        visited[i][j] = true;
        int perim = dfs(i, j+1);
        perim += dfs(i+1, j);
        perim += dfs(i, j-1);
        perim += dfs(i-1, j);

        return perim;

    }

public:
    int islandPerimeter(vector<vector<int>>& grid) {
        this->grid = grid;
        this->visited = vector<vector<bool>>(grid.size(), vector<bool>(grid[0].size(), false));

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    return dfs(i, j);
                }
            }
        }

        return 0;
    }
};