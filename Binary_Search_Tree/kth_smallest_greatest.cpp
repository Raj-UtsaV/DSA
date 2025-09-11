#include "main.h"

using namespace std;

void inorder(TreeNode *root, vector<int> &res)
{
    if (!root)
        return;

    inorder(root->left, res);
    res.push_back(root->val);
    inorder(root->right, res);
}

int findKthSmallest(TreeNode *root, int *ans, int *cnt) {
    if (!root)
        return *ans;

    findKthSmallest(root->left, ans, cnt);
    if (*cnt == 0)
        return *ans;

    (*cnt)--;
    if (*cnt == 0) {
        *ans = root->val;
        return *ans;
    }

    findKthSmallest(root->right, ans, cnt);
    return *ans;
}


int main()
{
    vector<int> v{3, 1, 4, null, 2};
    TreeNode *root = vectorToBST(v);

    vector<int> res;
    inorder(root, res);

    int k = 1;
    cout << "Kth smallest element is: " << res[k - 1] << endl;
    cout << "Kth largest element is: " << res[res.size() - k] << endl;

    int ans = 0;
    int cnt = k-1;
    cout << "Kth smallest element is: " << findKthSmallest(root, &ans, &cnt) << endl;
    

    return 0;
}