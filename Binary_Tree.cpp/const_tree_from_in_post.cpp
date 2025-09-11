#include "main.h"
#include<map>

using namespace std;

TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder, int inStart, int inEnd, int postStart, int postEnd, map<int, int> &mp){
    if(postStart > postEnd || inStart > inEnd){
        return nullptr;
    }

    TreeNode *root = new TreeNode(postorder[postEnd]);

    int inRoot = mp[root->data];
    int numsLeft = inRoot - inStart;

    root->left = buildTree(inorder, postorder, inStart, inRoot-1, postStart, postStart+numsLeft-1, mp);
    root->right = buildTree(inorder, postorder, inRoot+1, inEnd, postStart+numsLeft, postEnd-1, mp);

    return root;
}


int main(){
    vector<int> in{9,3,15,20,7};
    vector<int> post{9,15,7,20,3};

    map<int,int> mpp;

    for(int i = 0; i < in.size(); i++){
        mpp[in[i]] = i;
    }

    TreeNode *root = buildTree(in, post, 0, in.size()-1, 0, post.size()-1, mpp);
    print.printBinaryTreeWithArrows(root);

    return 0;
}
