#include "main.h"

to_BT BT;
print_Tree print;


bool root_to_node(BT_Node *root, vector<BT_Node*> &ans, int target)
{
    if (!root)
        return 0;
    ans.push_back(root);
    if (root->data == target)
        return true;
    if (root_to_node(root->left, ans, target) || root_to_node(root->right, ans, target))
        return true;
    ans.pop_back();
    return false;
}

int LCA(BT_Node*root,int p,int q){
    vector<BT_Node*> p1;
    vector<BT_Node*> q1;
    root_to_node(root, p1, p);
    root_to_node(root, q1, q);
    int i=0;
    int ans = 0;
    while(i<p1.size() && i<q1.size()){
        if(p1[i]->data != q1[i]->data) break;
        ans = p1[i]->data;
        i++;
    }
    return ans;
}


BT_Node* lca(BT_Node* root,int p,int q ){
    if(!root || root->data==p || root->data==q) return root;
    BT_Node* left = lca(root->left,p,q);
    BT_Node* right = lca(root->right,p,q);
    if(!right) return left;
    else if(!left) return right;
    else return root;
}

int main(){
    system("cls");
    vector<int> v{3,5,1,6,2,0,8,-1,-1,7,4};
    BT_Node*root = BT.Queue(v);
    int p=5, q = 4;
    cout<<LCA(root,p,q)<<endl;
    BT_Node* Lca = lca(root,p,q);
    cout<<Lca->data<<endl;
    return 0;


}