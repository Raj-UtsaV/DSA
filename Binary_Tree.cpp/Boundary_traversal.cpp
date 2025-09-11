#include "main.h"
#include <string>
to_BT BT;
print_Tree print;


bool isleaf(BT_Node* root){
  if(!root->left && !root->right) return true;
  else return false;
}

void addLeftBoundary(BT_Node*root,vector<int>&res){
    auto curr = root->left;
    while(curr){
        if(!isleaf(curr)) res.push_back(curr->data);
        if(curr->left) curr = curr->left;
        else curr = curr->right;
    }
}

void addRightBoundary(BT_Node* root,vector<int>&res){
    auto curr = root->right;
    vector<int> tmp;
    while(curr){
        if(!isleaf(curr)) tmp.push_back(curr->data);
        if(curr->right) curr = curr->right;
        else curr = curr->left;
    }
    for(int i = tmp.size()-1;i>=0;i--){
        res.push_back(tmp[i]);
    }
}

void addLeaves(BT_Node*root,vector<int>&res){
    if(isleaf(root)){
        res.push_back(root->data);
        //cout<<root->data<<" ";
        return;
    }
    if(root->left) addLeaves(root->left,res);
    if(root->right) addLeaves(root->right,res);
}

vector<int> printBoundary(BT_Node*root){
    vector<int>res;
    if(!root) return res;
    if(!isleaf(root)) res.push_back(root->data);
    addLeftBoundary(root,res);
    addLeaves(root,res);
    addRightBoundary(root,res);
    return res;
}

int main(){
    system("cls");
    vector<int> v;
    string i="0";
    while(true){
        cin>>i;
        if(i == "NIL") break;
        if(i=="N") v.push_back(-1);
        else v.push_back(stoi(i));
    }
    BT_Node* root = BT.Queue(v);
    //print.printBinaryTreeWithArrows(root);
    vector<int> boundary = printBoundary(root);
    print.printvector(boundary);
    return 0;
}