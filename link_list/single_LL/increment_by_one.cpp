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

// todo  Default arguments
node *head = nullptr;
node *tail = nullptr;

// todo: Insert at tail
void insert_tail(int data)
{
    node *new_node = new node(data);
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

void print(node *head1)
{
    node *temp = head1;
    while (temp)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void increment(node *head)
{
    node *temp = head;
    if (temp->next == nullptr)
    {
        head->data = head->data + 1;
        return;
    }
    while (temp->next)
    {
        temp = temp->next;
    }
    temp->data = temp->data + 1;
}

int main()
{
    vector<int> v = {9};
    for (int i = 0; i < v.size(); i++)
    {
        insert_tail(v[i]);
    }
    print(head);
    increment(head);
    print(head);
    return 0;
}