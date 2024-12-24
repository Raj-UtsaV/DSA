#include "main.h"
#include<map>




using namespace std;



BT_Node *buildTree(vector<int> &inorder, vector<int> &preorder, int inStart, int inEnd, int preStart, int preEnd, map<int, int> &mp){
    if(preStart > preEnd || inStart > inEnd){
        return nullptr;
    }

    BT_Node *root = new BT_Node(preorder[preStart]);

    int inRoot = mp[root->data];
    int numsLeft = inRoot - inStart;

    root->left = buildTree(inorder, preorder, inStart, inRoot-1, preStart+1, preStart+numsLeft, mp);
    root->right = buildTree(inorder, preorder, inRoot+1, inEnd, preStart+numsLeft+1, preEnd, mp);

    return root;
}

int main(){
    vector<int> in{9,3,15,20,7};
    vector<int> pre{3,9,20,15,7};

    
    map<int,int> mpp;
    for(int i = 0; i < in.size(); i++){
        mpp[in[i]] = i;
    }

    BT_Node *root = buildTree(in, pre, 0, in.size()-1, 0, pre.size()-1, mpp);

    print.printBinaryTreeWithArrows(root);



    return 0;


}