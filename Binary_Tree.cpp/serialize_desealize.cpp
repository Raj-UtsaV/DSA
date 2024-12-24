#include "main.h"
#define null 0

using namespace std;

string serilize(BT_Node *root)
{
    if (!root) return "null";
    string res;
    queue<BT_Node *> q;
    q.push(root);
    while (!q.empty())
    {
        auto curr = q.front();
        q.pop();
        if (curr)
        {
            res += to_string(curr->data) + ",";
            q.push(curr->left);
            q.push(curr->right);
        }
        else
        {
            res += "null,";
        }
    }
    //cout<<res;
    return res;
}

/**
 * @brief Deserializes a string representation of a binary tree into a binary tree structure.
 * 
 * This function takes a string representation of a binary tree, where nodes are separated by commas
 * and "null" represents a null node, and reconstructs the binary tree. The string is expected to be
 * in level-order traversal format.
 * 
 * @param data The string representation of the binary tree.
 * @return BT_Node* The root node of the deserialized binary tree. Returns nullptr if the input string is "null".
 * 
 * The function works as follows:
 * 1. If the input string is "null", it returns nullptr.
 * 2. It splits the input string by commas to extract individual node values.
 * 3. It uses a queue to reconstruct the binary tree level by level.
 * 4. It creates the root node from the first value and pushes it into the queue.
 * 5. It iterates through the remaining values, creating left and right children for each node in the queue.
 * 6. It returns the root node of the reconstructed binary tree.
 */
BT_Node* de_serilize(string data)
{
    if (data == "null") return nullptr;
    vector<string> v;
    string temp;
    for (size_t i = 0; i < data.size(); i++)
    {
        if (data[i] == ',')
        {
            v.push_back(temp);
            temp.clear();
        }
        else
        {
            temp += data[i];
        }
    }
    queue<BT_Node *> q;
    BT_Node *root = new BT_Node(stoi(v[0]));
    q.push(root);
    int i = 1;
    while (!q.empty())
    {
        auto curr = q.front();
        q.pop();
        if (v[i] != "null")
        {
            curr->left = new BT_Node(stoi(v[i]));
            q.push(curr->left);
        }
        i++;
        if (v[i] != "null")
        {
            curr->right = new BT_Node(stoi(v[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}



int main()
{
    vector<int> v{};

    BT_Node *root = to_BT::Queue(v);

    print_Tree::printTree(root);

    string res = serilize(root);

    root = de_serilize(res);


    print_Tree::printTree(root);

    return 0;
}
