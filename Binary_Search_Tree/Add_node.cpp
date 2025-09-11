#include "main.h"

using namespace std;

void addNode(TreeNode *root, int val, TreeNode *node) {
    if (!root) return;

    if (val < root->val) {
        if (root->left) {
            addNode(root->left, val, node);
        } else {
            root->left = node;
        }
    } else {
        if (root->right) {
            addNode(root->right, val, node);
        } else {
            root->right = node;
        }
    }
}

int main() {
    vector<int> v{4, 2, 7, 1, 3};
    int val = 5;

    TreeNode *root = vectorToBST(v);

    TreeNode* node = new TreeNode(val);
    addNode(root, val, node);

    cout << "In-order traversal of the BST after adding node: ";
    printBST(root);
    cout << endl;

    return 0;
}
