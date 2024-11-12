#include "main.h"
to_BT BT;
print_Tree print;

bool root_to_node(BT_Node *root, vector<int> &ans, int target)
{
    if (!root)
        return 0;
    ans.push_back(root->data);
    if (root->data == target)
        return true;
    if (root_to_node(root->left, ans, target) || root_to_node(root->right, ans, target))
        return true;
    ans.pop_back();
    return false;
}

void root_to_leaf(BT_Node *root, vector<int> &ans, vector<vector<int>> &result)
{
    if (!root)
    {
        return;
    }
    ans.push_back(root->data);
    if (!root->left && !root->right)
    {
        result.push_back(ans);
    }
    else
    {
        root_to_leaf(root->left, ans, result);
        root_to_leaf(root->right, ans, result);
    }
    ans.pop_back();
}

int main()
{
    system("cls");
    vector<int> v{1, 2, 3, 4, 5};
    BT_Node *root = BT.Queue(v);
    vector<int> ans;
    vector<vector<int>> result;
    root_to_leaf(root, ans, result);
    print.print2dvector(result);
    ans.clear();
    root_to_node(root, ans, 4);
    print.printvector(ans);
    return 0;
}