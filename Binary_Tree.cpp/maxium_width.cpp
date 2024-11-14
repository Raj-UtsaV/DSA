#include "main.h"

int max_widht(TreeNode *root)
{
    if (!root)
        return 0;
    int ans = 0;
    queue<pair<TreeNode *, long long>> q;
    q.push({root, 0});
    while (q.size())
    {
        int size = q.size();
        long long  mini = q.front().second;
        int first, last;
        for (int i = 0; i < size; i++)
        {
            long long curr_id = q.front().second - mini;
            TreeNode *node = q.front().first;
            q.pop();
            if (i == 0)
                first = curr_id;
            if (i == size - 1)
                last = curr_id;
            if (node->left)
                q.push({node->left, curr_id * 2 + 1});
            if (node->right)
                q.push({node->right, curr_id * 2 + 2});
        }
        ans = max(ans, last - first + 1);
    }
    return ans;
}
int main()
{
    system("cls");
    vector<int> v{1, 3, 2, 5, 3, -1, 9};
    TreeNode *root = BT.Queue(v);
    cout << "Maximum width of the tree is: " << max_widht(root) << endl;
    return 0;
}