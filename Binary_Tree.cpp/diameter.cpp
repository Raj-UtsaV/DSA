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

    BT_Node(int x) : data(x), left(NULL), right(NULL) {}
};

BT_Node *to_BT(vector<int> &v)
{
    if (!v.size())
        return nullptr;
    queue<BT_Node *> q;
    auto root = new BT_Node(v[0]);
    q.push(root);
    int i = 1;
    while (i < v.size())
    {
        auto temp = q.front();
        q.pop();
        if (i < v.size() && v[i] != -1)
        {
            temp->left = new BT_Node(v[i]);
            q.push(temp->left);
        }
        i++;
        if (i < v.size() && v[i] != -1)
        {
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
    return 1 + max(height(root->left), height(root->right));
}

void diameter_brute(BT_Node *root, int *maxi)
{
    if (!root)
        return;
    int lh = height(root->left);
    int rh = height(root->right);

    *maxi = max(*maxi, lh + rh);

    diameter_brute(root->left, maxi);

    diameter_brute(root->right, maxi);
}

int diameter_optimize(BT_Node *root, int maxi){
    if(!root) return 0;
    int lHeight = diameter_optimize(root->left,maxi);
    int rHeight = diameter_optimize(root->right,maxi);

    maxi = max(maxi, lHeight+rHeight);

    return max(lHeight, rHeight) + 1;
    
}

int main()
{
    {
        system("cls");
    }

    // todo In this block write your code
    {
        vector<int> v{1, 2, 3, 4, 5};
        BT_Node *root = to_BT(v);

        int maxi = 0;
        diameter_brute(root, &maxi);
        cout << "Diameter: " << maxi << endl;
        maxi = diameter_optimize(root, maxi);
        cout << "Diameter: " << maxi << endl;


        // Additional test cases
        vector<int> v2{1, 2, 3, -1, -1, 4, 5};
        BT_Node *root2 = to_BT(v2);
        maxi = 0;
        diameter_brute(root2, &maxi);
        cout << "Diameter: " << maxi << endl;
        maxi = diameter_optimize(root2, maxi);
        cout << "Diameter: " << maxi << endl;
    }

    return 0;
}