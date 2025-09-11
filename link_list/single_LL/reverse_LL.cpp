#include <iostream>
#include <vector>
using namespace std;

class node
{
public:
    int data;
    node *next;

    node(int d)
    {
        data = d;
        next = nullptr;
    }
};

node *insert_head(int data, node *head)
{
    node *new_node = new node(data);
    new_node->next = head;
    head = new_node;
    return head;
}

void print(node *head)
{
    node *temp = head;
    while (temp)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void brute(node *head)
{
    node *head1 = nullptr;
    while (head)
    {
        head1 = insert_head(head->data, head1);
        head = head->next;
    }

    print(head1);
}

void optimal(node *head)
{
    node *temp = head;
    node *prev = nullptr;
    while (temp)
    {

        node *front = temp->next;
        temp->next = prev;
        prev = temp;
        temp = front;
    }

    print(prev);
}

void recursive(node*&head,node*prev=nullptr){
    if (head == nullptr && head->next == nullptr)
    {
        head = prev;
        return;
    }
    node *next = head->next;
    head->next = prev;
    recursive(next, head);
}

int main()
{
    node *head = nullptr;

    vector<int> v = {5, 4, 3, 2, 1};
    for (int i = 0; i < v.size(); i++)
    {
        head = insert_head(v[i], head);
    }
    cout << "Default link list: ";
    print(head);
    brute(head);
    optimal(head);
    // recursive(head);
    // print(head);
    return 0;
}
