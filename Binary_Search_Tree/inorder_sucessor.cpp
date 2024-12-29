#include "main.h"


TreeNode* ird_succesor(TreeNode* root,int val, int ans){
    if(!root) return;

}

int main(){
    std::vector<int> v{1,2,3};

    TreeNode *root =  vectorToBST(v);

    int val = 2;    
    std::cout<<ird_succesor(root,val)->val<<std::endl;

    return 0;

}