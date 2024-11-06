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
        this->left = nullptr;
        this->right = nullptr;
    }
};

BT_Node *to_BT(vector<int> &v)
{
    if (!v.size())
        return nullptr;
    queue<BT_Node *> q;
    BT_Node *root = new BT_Node(v[0]);
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

int max_sum(BT_Node *root, int *maxi)
{
    if (root == nullptr)
    {
        return 0;
    }

    int leftMaxPath = max(0, max_sum(root->left, maxi));
    int rightMaxPath = max(0, max_sum(root->right, maxi));

    *maxi = max(*maxi, leftMaxPath + rightMaxPath + root->data);
    return max(leftMaxPath, rightMaxPath) + root->data;
}

int main()
{
    {
        system("cls");
    }

    // todo In this block write your code
    {
        vector<int> v{3, -2};
        BT_Node *root = to_BT(v);
        int maxi = INT_MIN;
        cout << "Maximum sum of path in the binary tree: ";
        max_sum(root, &maxi);
        cout << maxi << endl;
    }

    return 0;
}