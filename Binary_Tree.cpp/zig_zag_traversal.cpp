#include "main.h"
to_BT BT;
print_Tree print;

vector<vector<int>> vec(BT_Node *root)
{
    vector<vector<int>> result;
    queue<BT_Node *> q;
    if (root == NULL)
        return result;
    q.push(root);
    bool left_trav = false;
    while (!q.empty())
    {
        int size = q.size();
        vector<int> level;
        while (size--)
        {
            BT_Node *temp = q.front();
            q.pop();
            if (temp->left)
                q.push(temp->left);
            if (temp->right)
                q.push(temp->right);
            level.push_back(temp->data);
        }
        if (left_trav)
        {
            reverse(level.begin(), level.end());
        }
        left_trav = !left_trav;
        result.push_back(level);
    }
    return result;
}

int main()
{
    {
        system("cls");
    }

    // todo In this block write your code
    {
        vector<int> v{3, 9, 20, -1, -1, 15, 7};
        BT_Node *root = BT.Queue(v);
        vector<vector<int>> result = vec(root);
        for (const auto &level : result)
        {
            print.printvector(level);
            cout << endl;
        }
    }

    return 0;
}