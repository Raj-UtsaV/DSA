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

int main()
{
    {
        system("cls");
    }

    // todo In this block write your code
    {
        vector<int> v{};
        BT_Node *root = to_BT(v);
        
    }

    return 0;
}