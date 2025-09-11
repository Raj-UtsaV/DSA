#include "main.h"
#include <algorithm>
#include <climits>
using namespace std;

void inorder(TreeNode *root, vector<int> &ans1)
{
    if (!root)
        return;

    inorder(root->left, ans1);
    ans1.push_back(root->val);

    inorder(root->right, ans1);
}
bool isValidBST(TreeNode *root)
{

    if (!root->left && !root->right || !root)
        return 1;

    vector<int> ans1;
    inorder(root, ans1);

    for (int i = 1; i < ans1.size(); i++)
    {

        if (ans1[i - 1] >= ans1[i])
            return 0;
    }

    return 1;
}

bool isValidBSTUtil(TreeNode* root, long long minVal, long long maxVal) {
    if (!root) return true;
    if (root->val <= minVal || root->val >= maxVal) return false;
    return isValidBSTUtil(root->left, minVal, root->val) && isValidBSTUtil(root->right, root->val, maxVal);
}

bool isValidBSt(TreeNode* root) {
    return isValidBSTUtil(root, LLONG_MIN, LLONG_MAX);
}

int main()
{
    vector<int> v{5, 1, 4, null, null, 3, 6};
    TreeNode *root = vectorToBST(v);

    cout << isValidBST(root) << endl;
    cout << isValidBSt(root) << endl;


    return 0;
}
