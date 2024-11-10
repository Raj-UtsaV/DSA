#include "main.h"
#include <string>
#include <map>
#include <set>

// Global objects for binary tree operations
to_BT BT;
print_Tree print;

class Solution
{
public:
    /**
     * @brief Performs a vertical traversal of a binary tree
     * @param root Pointer to the root of the binary tree
     * @return vector<vector<int>> 2D vector where each inner vector represents a vertical column
     */
    vector<vector<int>> verticalTraversal(BT_Node *root)
    {
        // Map to store nodes: key is x-coordinate, value is another map
        // where key is y-coordinate and value is a multiset of node values
        map<int, map<int, multiset<int>>> nodes;

        // Queue for level-order traversal
        // Each element is a pair of node pointer and its coordinates
        queue<pair<BT_Node *, pair<int, int>>> todo;

        // Push root node with coordinates (0,0)
        todo.push({root, {0, 0}});

        // Level-order traversal
        while (!todo.empty())
        {
            auto p = todo.front();
            todo.pop();
            auto node = p.first;
            auto x = p.second.first, y = p.second.second;
            // Insert node value into the map
            nodes[x][y].insert(node->data);
            if(node->left) todo.push({node->left,{x-1,y+1}});
            if(node->right) todo.push({node->right,{x+1,y+1}});
        }
        vector<vector<int>> ans;
        for (auto &p : nodes)
        {
            vector<int> col;
            for (auto &q : p.second)
            {
                col.insert(col.end(), q.second.begin(), q.second.end());
            }
            ans.push_back(col);
        }
        return ans;
    }
};

int main()
{
    system("cls");
    vector<int> v{3, 9, 20, -1, -1, 15, 7};
    BT_Node *root = BT.Queue(v);
    // print.printBinaryTreeWithArrows(root);
    Solution s;
    vector<vector<int>> ans = s.verticalTraversal(root);
    print.print2dvector(ans); 
    return 0;
}