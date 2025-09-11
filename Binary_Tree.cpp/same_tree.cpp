#include "main.h"
to_BT BT;


bool isSame(BT_Node*root1,BT_Node*root2){
    if(!root1 || !root2){
        return root1 == root2;
    }

    return (root1->data == root2->data) && isSame(root1->left,root2->left) && isSame(root1->right,root2->right);
}

 
int main() {
   {
        system("cls");
   }
 
   //todo In this block write your code
   {
        vector<int> v1{1,2,3};
        vector<int> v2{1,2,3};
        BT_Node* root1 = BT.Queue(v1);
        BT_Node* root2 = BT.Queue(v2);

        cout << "Are the two trees same: " << (isSame(root1, root2)? "Yes" : "No") << endl;    
   }
 
    return 0;
}