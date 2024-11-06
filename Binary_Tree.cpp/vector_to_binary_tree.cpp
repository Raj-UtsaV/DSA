#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include "main.h"

print_Tree print;

using namespace std;

BT_Node *to_BT_Queue(vector<int> &v) {
    if (v.empty()) return nullptr;
    queue<BT_Node *> q;
    BT_Node *root = new BT_Node(v[0]);
    q.push(root);
    int i = 1;
    while (i < v.size()) {
        BT_Node *temp = q.front();
        q.pop();
        if (i < v.size() && v[i] != -1) {
            temp->left = new BT_Node(v[i]);
            q.push(temp->left);
        }
        i++;
        if (i < v.size() && v[i] != -1) {
            temp->right = new BT_Node(v[i]);
            q.push(temp->right);
        }
        i++;
    }
    return root;
}


BT_Node *to_BT_List(vector<int> &v)
{
    if (v.empty())
        return nullptr;

    list<BT_Node *> ls;
    BT_Node *root = new BT_Node(v[0]);
    ls.push_back(root);
    int i = 1;
    while (i < v.size())
    {
        BT_Node *temp = ls.front();
        ls.pop_front();

        if (i < v.size())
        {
            temp->left = new BT_Node(v[i++]);
            ls.push_back(temp->left);
        }
        if(i<v.size()){
            temp->right = new BT_Node(v[i++]);
            ls.push_back(temp->right);
        }
    }
    return root;
}

int main()
{
    system("cls"); // Clears the console screen

    vector<int> v{1, 2, 3,-1, 4,-1, 5, 6, 7};
    BT_Node *root_queue = to_BT_Queue(v);
    print.printBinaryTreeWithArrows(root_queue);
    cout<<endl;
    BT_Node *root_list = to_BT_List(v);
    print.printLevelOrder(root_list);

    return 0;
}
