#include "main.h"

using namespace std;

TreeNode* findMin(TreeNode* node) {
    while (node->left != nullptr) {
        node = node->left;
    }
    return node;
}

TreeNode* deleteNode(TreeNode* root, int val) {
    if (!root) return root;

    if (val < root->val) {
        root->left = deleteNode(root->left, val);
    } else if (val > root->val) {
        root->right = deleteNode(root->right, val);
    } else {
        // Node with only one child or no child
        if (root->left == nullptr) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        } else if (root->right == nullptr) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }

        // Node with two children: Get the inorder successor (smallest in the right subtree)
        TreeNode* temp = findMin(root->right);

        // Copy the inorder successor's content to this node
        root->val = temp->val;

        // Delete the inorder successor
        root->right = deleteNode(root->right, temp->val);
    }
    return root;
}

int main() {
    vector<int> v = {5, 3, 6, 2, 4, 7};
    TreeNode* root = vectorToBST(v);

    cout << "Before Deletion: ";
    printBST(root);
    cout << endl;

    root = deleteNode(root, 5);

    cout << "After Deletion: ";
    printBST(root);
    cout << endl;

    return 0;
}