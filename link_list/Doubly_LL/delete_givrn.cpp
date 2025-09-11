#include <iostream>
#include <vector>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node *prev;

    Node(int data)
    {
        this->data = data;
        this->next = NULL;
        this->prev = NULL;
    }
};

class basicopertaion
{
    public:

    void print(Node *head)
    {
        Node *temp = head;
        while (temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    void tolist(vector<int> arr, Node *&head, Node *tail)
    {

        for (int i = 0; i < arr.size(); i++)
        {
            Node *new_node = new Node(arr[i]);
            if (!head)
            {
                head = new_node;
                tail = new_node;
            }
            else
            {
                tail->next = new_node;
                new_node->prev = tail;
                tail = new_node;
            }
        }
    }
};


void delete_key(Node *&head,int x){


    while(head->data==x){
        head->next->prev = NULL;
        head=head->next;
    }

    Node *temp = head;
    while (temp->next->next )
    {
        if (temp->next->data == x )
        {

            temp->next = temp->next->next;
            temp->next->next->prev = temp->next->prev;
        }
        else{
            temp = temp->next;
        }
    }
}
int main()
{
    vector<int> v = {3,3, 2, 3, 3, 5, 2, 7, 8,3,3};
    basicopertaion bo;
    Node *head = NULL;
    Node *tail = NULL;
    bo.tolist(v, head, tail);
    bo.print(head);
    delete_key(head, 3);
    bo.print(head);
    return 0;
}