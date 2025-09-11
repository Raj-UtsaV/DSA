#include "main.h";
print_Tree print;
to_BT BT;

int height(BT_Node *root)
{
    if (!root)
        return 0;

    int lHeight = height(root->left);
    int rHeight = height(root->right);

    return 1 + max(lHeight, rHeight);
}

int height_BFS(BT_Node *root){
    if (!root)
        return 0;
    queue<BT_Node *> q;
    q.push(root);
    int h = 0;
    while(q.size()){
        int n = q.size();
        h++;
        while(n--){
            BT_Node *temp = q.front();
            q.pop();
            if(temp->left)
                q.push(temp->left);
            if(temp->right)
                q.push(temp->right);
        }
    }
    return h;
}

int main()
{
    system("cls");

    vector<int> v{3, 9, 20, -1, -1, 15, 7};
    BT_Node *root = BT.Queue(v);

    cout << "Heght of tree is : " << height(root) << endl;
    cout << "Height of tree using BFS is : " << height_BFS(root) << endl;

    return 0;
}