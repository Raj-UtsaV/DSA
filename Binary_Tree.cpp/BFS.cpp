// aks level order traversal

//! traverse horizontally

#include "main.cpp"
print_Tree print;
to_BT BT; // return root

class BFS
{
public:
    vector<vector<int>> vec(BT_Node*root){
        vector<vector<int>> result;
        queue<BT_Node*> q;
        if(root==NULL) return result;
        q.push(root);
        while(!q.empty()){
            int size = q.size();
            vector<int> level;
            while(size--){
                BT_Node*temp = q.front();
                q.pop();
                if(temp->left) q.push(temp->left);
                if(temp->right) q.push(temp->right);
                level.push_back(temp->data);
            }
            result.push_back(level);
        }
        return result;
    }
};
int main()
{
    system("cls");
    BT_Node *root;
    vector<int> v{3, 9, 20, -1, -1, 15, 7};
    root = BT.Queue(v);

    BFS bfs;
    vector<vector<int>> ans = bfs.vec(root);
    for(const auto& level:ans){
        print.printvector(level);
        cout<<endl;
    }
}