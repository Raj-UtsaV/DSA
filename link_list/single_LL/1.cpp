#include<iostream>
#include<vector>
using namespace std;

class Node{
    public:
        int data;
        Node *next;

        Node(int x){
            data = x;
            next = NULL;
        }
};

class basicoperation
{
public:
    void print(Node *head)
    {
        Node *node = head;
        while (node != nullptr)
        {
            cout << node->data << " ";
            node = node->next;
        }
        cout << endl;
    }

    void tolist(vector<int> arr, Node *&head, Node *&tail)
    {
        int n = arr.size();
        for (int i = 0; i < n; i++)
        {
            Node *new_node = new Node(arr[i]);
            if (head == nullptr)
            {
                head = new_node;
                tail = new_node;
            }
            else
            {
                tail->next = new_node;
                tail = new_node;
            }

        }
    }

    void insert_tail(int data,Node*&tail)
    {
        Node *new_node = new Node(data);
            tail->next = new_node;
            tail = new_node;
        
    }
};
