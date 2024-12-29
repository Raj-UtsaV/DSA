#include "main.h"

// Global objects for binary tree operations
// to_BT BT;
// print_Tree print;

/**
 * Finds the path from the root to a node with the given target value.
 * @param root The root of the binary tree.
 * @param ans Vector to store the path from the root to the target node.
 * @param target The target node value.
 * @return True if the target node is found, otherwise false.
 */
bool root_to_node(BT_Node *root, vector<BT_Node*> &ans, int target) {
    if (!root)
        return false;
    ans.push_back(root);
    if (root->data == target)
        return true;
    if (root_to_node(root->left, ans, target) || root_to_node(root->right, ans, target))
        return true;
    ans.pop_back();
    return false;
}

/**
 * Finds the Least Common Ancestor (LCA) of two nodes with values p and q.
 * @param root The root of the binary tree.
 * @param p The value of the first node.
 * @param q The value of the second node.
 * @return The value of the LCA node.
 */
int LCA(BT_Node* root, int p, int q) {
    vector<BT_Node*> p1;
    vector<BT_Node*> q1;
    root_to_node(root, p1, p);
    root_to_node(root, q1, q);
    int i = 0;
    int ans = 0;
    while (i < p1.size() && i < q1.size()) {
        if (p1[i]->data != q1[i]->data) break;
        ans = p1[i]->data;
        i++;
    }
    return ans;
}

/**
 * Finds the Least Common Ancestor (LCA) of two nodes with values p and q using a recursive approach.
 * @param root The root of the binary tree.
 * @param p The value of the first node.
 * @param q The value of the second node.
 * @return The LCA node.
 */
BT_Node* lca(BT_Node* root, int p, int q) {
    if (!root || root->data == p || root->data == q) return root;
    BT_Node* left = lca(root->left, p, q);
    BT_Node* right = lca(root->right, p, q);
    if (!right) return left;
    else if (!left) return right;
    else return root;
}

int main(){
    //system("cls");
    vector<int> v{3,5,1,6,2,0,8,-1,-1,7,4};
    BT_Node*root = BT.Queue(v);
    int p=5, q = 4;
    cout<<LCA(root,p,q)<<endl;
    BT_Node* Lca = lca(root,p,q);
    cout<<Lca->data<<endl;
    return 0;
}