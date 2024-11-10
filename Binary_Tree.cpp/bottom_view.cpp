#include "main.h"
#include<string>
#include<map>
to_BT BT;
print_Tree print;



vector<int> bottom_view(BT_Node* root){
    vector<int> ans;
    if(!root) return ans;
    map<int,int> mpp;
    queue<pair<BT_Node*,int>> q; 
    q.push({root,0});
    while(q.size()){
        auto temp = q.front();
        q.pop();
        auto node = temp.first;
        auto dist = temp.second;
        mpp[dist] = node->data;
        if(node->left) q.push({node->left,dist-1});
        if(node->right) q.push({node->right,dist+1});
    }
    for(auto &p : mpp) ans.push_back(p.second);
    return ans;
}
int main(){
    system("cls");
    vector<int> v;
    string i = "0";
    while(true){
        cin>>i;if(i == "NIL") break;
        if(i == "N") v.push_back(-1);
        else v.push_back(stoi(i));
    }
    BT_Node* root = BT.Queue(v);
    //print.printBinaryTreeWithArrows(root); 
    vector<int> ans = bottom_view(root);
    print.printvector(ans);

}