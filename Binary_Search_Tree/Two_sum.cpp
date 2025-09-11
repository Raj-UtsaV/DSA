#include "main.h"
#include<stack>

using namespace std;

class BSTIterator{
private:
    stack<TreeNode*> st;
    //reverse ->true = befor
    //reverse -> false = next;
    bool reverse = true;

    void pushALL(TreeNode*node){
        while(node){
            st.push(node);
            if(reverse) node =  node->right;
            else node =  node->left;
        }
    }

public:
    BSTIterator(TreeNode*root , bool isReverse){
        reverse =  isReverse;
        pushALL(root);
    }

    bool hasNext() {return !st.empty();}

    int next(){
        auto node = st.top();
        st.pop();
        if(reverse) pushALL(node->left);
        else pushALL(node->right);
        return node->val;
    }
};

bool twosum(TreeNode*root,int val){
    if(!root) return false;

    BSTIterator l(root,false);
    BSTIterator r(root,1);

    int i = l.next();
    int j = r.next();

    while(i<j){
        if(i+j ==  val) return 1;
        if(i+j < val) i = l.next();
        else j = r.next();
    }

    return 0;
}

int main(){
    vector<int> v{5,3,6,2,4,null,7};
    TreeNode*root = vectorToBST(v);
    int val = 9;
    cout<<twosum(root,val)<<endl;
}