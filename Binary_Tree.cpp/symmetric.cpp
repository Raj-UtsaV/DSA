//? similar traversal both side
//? root left right == root right left

#include "main.h"
to_BT BT;
print_Tree print;

bool issymmetric(BT_Node *root1, BT_Node *root2)
{
    if (root1 == NULL || root2 == NULL)
        return root1 == root2;
    return (root1->data == root2->data
     && issymmetric(root1->left, root2->right) 
     && issymmetric(root1->right, root2->left));
}

int main()
{
    system("cls");
    vector<int> v{1,2,2,3,4,4,3};
    BT_Node *root = BT.Queue(v);
    bool is_symmetric = issymmetric(root, root);
    cout << "Is the tree symmetric: " << (is_symmetric? "Yes" : "No") << endl;
    return 0;
}