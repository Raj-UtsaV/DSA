#include "main.h"


#define null 0

using namespace std;


void flatten_stack(TreeNode*root){
    if(!root) return;
    stack<TreeNode*> st;
    st.push(root);
    while(!st.empty()){
        TreeNode* curr = st.top();
        st.pop();
        if(curr->right){
            st.push(curr->right);
        }
        if(curr->left){
            st.push(curr->left);
        }
        curr->left = nullptr;
        if(!st.empty()){
            curr->right = st.top();
        }
    }
}

int main(){
    vector<int> v{1,2,5,3,4,null,6};
    TreeNode* root = to_BT::Queue(v);


    flatten_stack(root);
}