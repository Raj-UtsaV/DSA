#pragma once
#define val data

#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <algorithm>

using namespace std;

// Generic TreeNode
template <typename T>
class TreeNode {
public:
    T data;
    TreeNode<T> *left, *right;
    TreeNode(T data) : data(data), left(nullptr), right(nullptr) {}
};

// Print Tree Class
template <typename T>
class PrintTree {
public:
    static void printBinaryTree(TreeNode<T> *root, int space = 0, int height = 10) {
        if (!root) return;
        space += height;
        printBinaryTree(root->right, space);
        cout << endl;
        for (int i = height; i < space; i++)
            cout << " ";
        cout << root->data << "\n";
        printBinaryTree(root->left, space);
    }

    static void printInorder(TreeNode<T> *root) {
        if (!root) return;
        printInorder(root->left);
        cout << root->data << " ";
        printInorder(root->right);
    }

    static void printLevelOrder(TreeNode<T> *root) {
        if (!root) return;
        queue<TreeNode<T> *> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode<T> *node = q.front();
            q.pop();
            cout << node->data << " ";
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
};

// Convert vector to Binary Tree
template <typename T>
class ToBinaryTree {
public:
    static TreeNode<T> *fromVector(vector<T> &v) {
        if (v.empty()) return nullptr;

        auto isNull = [](const T& value) -> bool {
            if constexpr (is_same_v<T, int>) {
                return value == -1;
            } else {
                return value == T(); // Default null value for other types
            }
        };

        queue<TreeNode<T> *> q;
        TreeNode<T> *root = isNull(v[0]) ? nullptr : new TreeNode<T>(v[0]);
        q.push(root);
        size_t i = 1;
        while (i < v.size()) {
            TreeNode<T> *temp = q.front();
            q.pop();
            if (i < v.size()) {
                temp->left = isNull(v[i]) ? nullptr : new TreeNode<T>(v[i]);
                q.push(temp->left);
                i++;
            }
            if (i < v.size()) {
                temp->right = isNull(v[i]) ? nullptr : new TreeNode<T>(v[i]);
                q.push(temp->right);
                i++;
            }
        }
        return root;
    }
};

// Depth-First Search Traversal
template <typename T>
class DFS {
public:
    static void preorder(TreeNode<T> *root) {
        if (!root) return;
        cout << root->data << " ";
        preorder(root->left);
        preorder(root->right);
    }

    static void inorder(TreeNode<T> *root) {
        if (!root) return;
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }

    static void postorder(TreeNode<T> *root) {
        if (!root) return;
        postorder(root->left);
        postorder(root->right);
        cout << root->data << " ";
    }
};

// Breadth-First Search Traversal
template <typename T>
class BFS {
public:
    static vector<vector<T>> levelOrder(TreeNode<T> *root) {
        vector<vector<T>> result;
        if (!root) return result;
        queue<TreeNode<T> *> q;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<T> level;
            while (size--) {
                TreeNode<T> *temp = q.front();
                q.pop();
                level.push_back(temp->data);
                if (temp->left) q.push(temp->left);
                if (temp->right) q.push(temp->right);
            }
            result.push_back(level);
        }
        return result;
    }

    static void printLevelOrder(TreeNode<T> *root) {
        vector<vector<T>> result;
        if (!root) return;
        queue<TreeNode<T> *> q;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<T> level;
            while (size--) {
                TreeNode<T> *temp = q.front();
                q.pop();
                level.push_back(temp->data);
                if (temp->left) q.push(temp->left);
                if (temp->right) q.push(temp->right);
            }
            result.push_back(level);
        }
        
        for(auto i:result){
            for(auto j:i){
                cout<<j<<" ";
            }
            cout<<endl;
        }
    }
};


