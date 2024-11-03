//? for every node 
//? height left - height right <= 1

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class BT_Node
{
public:
    int data;
    BT_Node *left;
    BT_Node *right;

    BT_Node(int data)
    {
        this->data = data;
        left = right = nullptr;
    }
};


BT_Node *to_BT(vector<int> v)
{
    queue<BT_Node *> q;
    BT_Node *root = new BT_Node(v[0]);
    q.push(root);
    int i = 1;
    while(i < v.size()){
        auto temp = q.front();   
        q.pop();
        if(i < v.size() && v[i]!= -1){
            temp->left = new BT_Node(v[i]);
            q.push(temp->left);
        }
        i++;
        if(i<v.size() && v[i] != -1){
            temp->right = new BT_Node(v[i]);
            q.push(temp->right);
        }
        i++;
    }
    return root;
}

int height(BT_Node *root)
{
    if (!root)
        return 0;

    int lHeight = height(root->left);
    int rHeight = height(root->right);

    return 1 + max(lHeight, rHeight);
}

bool isBalanced_brute(BT_Node *root) {
    if (root == nullptr) return true;  // Base case: if the node is null, it's balanced

    int lHeight = height(root->left);  // Calculate the height of the left subtree
    int rHeight = height(root->right); // Calculate the height of the right subtree

    if (abs(lHeight - rHeight) > 1) return false;  // If the difference in heights is more than 1, it's not balanced

    bool left = isBalanced_brute(root->left);  // Recursively check if the left subtree is balanced
    bool right = isBalanced_brute(root->right); // Recursively check if the right subtree is balanced

    if (!left || !right) return false;  // If either the left or right subtree is not balanced, the tree is not balanced
    return true;  // If both subtrees are balanced and the height difference is within 1, the tree is balanced
}


int isBalanced_optimized(BT_Node *root){
    if (!root)
        return 0;

    int lHeight = height(root->left);
    if(lHeight == -1) return -1;
    int rHeight = height(root->right);
    if(rHeight == -1) return -1;

    if (abs(lHeight - rHeight) > 1) return -1;  

    return 1 + max(lHeight, rHeight);
}



int main()
{
    {
        system("cls");
    }

    // todo In this block write your code
    {
        vector<int> v{3,9,20,-1,-1,15,7};
        BT_Node *root = to_BT(v);
        cout << "Is balanced: " << isBalanced_brute(root) << endl;


        cout << "Is balanced: ";
        isBalanced_optimized(root) != -1 ?  cout<<1 : cout<<0;
        cout << endl;

    }

    return 0;
}