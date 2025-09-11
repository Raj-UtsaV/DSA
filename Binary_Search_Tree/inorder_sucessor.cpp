#include "main.h"


TreeNode* inorder_successor(TreeNode* root, int val) {
    TreeNode* successor = nullptr;

    while (root) {
        if (val >= root->val) root = root->right;
        else {
            successor = root;
            root = root->left;
        }
    }

    return successor;
}

int main() {
    std::vector<int> v{2,1,3};

    TreeNode *root = vectorToBST(v);

    int val = 2;    
    std::cout << inorder_successor(root, val)->val << std::endl;

    return 0;
}