#include "main.h"

// bool check(Node *root)
// {
//     if (!root)
//         return 0;
//     if (root->left && root->right)
//         return root->data == (root->left->data + root->right->data);
//     else if (root->right)
//         return root->data == (root->right->data);
//     else
//         return root->data == (root->left->data);
//     if ((root->right) && (root->left))
//         return true;
//     return false;
// }


bool check(Node *root)
{
    if (!root)
        return true;

    if (!root->left && !root->right)
        return true;

    int left_data = (root->left) ? root->left->data : 0;
    int right_data = (root->right) ? root->right->data : 0;

    bool is_sum = (root->data == left_data + right_data);

    return is_sum && check(root->left) && check(root->right);
}


int main()
{
    system("cls");
    vector<int> v{1, 4, 3, 5};
    TreeNode *root = BT.Queue(v);
    cout << check(root) << endl;
    return 0;
}