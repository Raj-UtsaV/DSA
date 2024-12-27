#ifndef MAIN_H
#define MAIN_H
#define null -1

#include <vector>
#include <queue>
#include <iostream>

// Definition for a binary tree node.
class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Function to convert a vector to a BST
TreeNode* vectorToBST(const std::vector<int>& nums) {
    if (nums.empty() || nums[0] == -1) return nullptr;

    TreeNode* root = new TreeNode(nums[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;

    while (!q.empty() && i < nums.size()) {
        TreeNode* current = q.front();
        q.pop();

        if (nums[i] != -1) {
            current->left = new TreeNode(nums[i]);
            q.push(current->left);
        }
        i++;

        if (i < nums.size() && nums[i] != -1) {
            current->right = new TreeNode(nums[i]);
            q.push(current->right);
        }
        i++;
    }
    return root;
}

// Function to print the BST in-order
void printBST(TreeNode* root) {
    if (!root) return;
    printBST(root->left);
    std::cout << root->val << " ";
    printBST(root->right);
}

#endif // MAIN_H