#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

class TreeNode
{
public:
    int val;
    TreeNode *right;
    TreeNode *left;

    TreeNode(int val) : val(val), right(NULL), left(NULL) {}
};

void insert(TreeNode *root, int val, TreeNode *prev = nullptr)
{
    if (!root)
    {
        TreeNode *node = new TreeNode(val);
        if (val > prev->val)
        {
            prev->right = node;
        }
        else
        {
            prev->left = node;
        }
        return;
    }

    prev = root;
    if (root->val > val)
    {
        insert(root->left, val, prev);
    }

    else
    {
        insert(root->right, val, prev);
    }
}

TreeNode *tree(std::vector<int> pre)
{
    TreeNode *root = NULL;
    if (!pre.size())
        return root;
    root = new TreeNode(pre[0]);

    for (int i = 1; i < pre.size(); i++)
    {
        insert(root, pre[i]);
    }

    return root;
}

TreeNode *Tree(std::vector<int> &pre, int bound, int &i)
{
    if (i == pre.size() || pre[i] > bound)
        return NULL;
    TreeNode *root = new TreeNode(pre[i++]);
    root->left = Tree(pre, root->val, i);
    root->right = Tree(pre, bound, i);
    return root;
}

void print(TreeNode *root)
{
    if (!root)
        return;

    std::cout << root->val << " ";
    print(root->left);
    print(root->right);
}

int main()
{
    std::vector<int> pre{8, 5, 1, 7, 10, 12};

    TreeNode *root = tree(pre);
    print(root);
    std::cout << std::endl;

    int i = 0;
    root = Tree(pre, INT_MAX, i);
    print(root);

    return 0;
}