#include "main.h"

to_BT BT;
print_Tree print;

void left(BT_Node *root, vector<int> &ans, int level = 0)
{
    if(!root) return;

    if (level == ans.size())
        ans.push_back(root->data);
    left(root->left, ans, level + 1);
    left(root->right, ans, level + 1);

}

void right(BT_Node *root, vector<int> &ans, int level = 0)
{
    if (!root)
        return;

    if (level == ans.size())
        ans.push_back(root->data);
    right(root->right, ans, level + 1);
    right(root->left, ans, level + 1);
}

int main()
{
    system("cls");
    vector<int> v{1,2,3,-1,5,-1,4};
    BT_Node *root = BT.Queue(v);
    vector<int> left_ans, right_ans;
    left(root, left_ans);
    right(root, right_ans);
    cout<<"left_view : ";
    print.printvector(left_ans);
    cout<<"right_view : ";
    print.printvector(right_ans);
    return 0;
}