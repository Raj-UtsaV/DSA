#include "main.h"

using namespace std;

TreeNode* LCA(TreeNode*root,int p,int q){
    if(!root) return nullptr;

    if(root->val == p || root->val == q) return root;
    if(root->val > p && root->val<q) return root;
    if(root->val >q && root->val < p) return root;

    if(root->val > p && root-> val > q) {
        return LCA(root->left,p,q);
    }

    if(root -> val <p && root->val<q){
        return LCA(root->right,p,q);
    }

    return root;


}

int main(){
    vector<int> v{2,1};
    TreeNode* root = vectorToBST(v);

    int p = 2,q=1;

    cout<<LCA(root,p,q)->val<<endl;

    return 0;
}