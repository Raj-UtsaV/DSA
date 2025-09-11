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

void insert_tail(int data)
{
    node *new_node = new node(data);
    if (head == nullptr)
    {
        head=tail = new_node;

    }
    else
    {
        tail->next = new_node;
        tail = new_node;
    }
}

void insert_head(int data)
{
    node *new_node = new node(data);
    if (head == nullptr)
    {
        tail = new_node;
    }
    new_node->next = head;
    head = new_node;
}

void insert_at_position(int data, int position)
{
    if (position < 1)
    {
        cout << "Enter valid position";
        return;
    }
    if (position == 1)
    {
        insert_head(data);
        return;
    }
    node *temp = head;
    for (int i = 1; i < position - 1 && temp; i++)
    {
        temp = temp->next;
    }
    if (temp == nullptr)
    {
        cout << "Position out of range";
        return;
    }
    if (!temp->next)
    {
        insert_tail(data);
        return;
    }
    node *new_node = new node(data);
    new_node->next = temp->next;
    temp->next = new_node;
}

void delete_head()
{
    if (head == nullptr)
    {
        cout << "List is empty" << endl;
        return;
    }
    node *temp = head;
    head = head->next;
    delete temp;
}

void delete_tail()
{
    if (head == nullptr)
    {
        cout << "List is empty" << endl;
        return;
    }
    if (!head->next)
    {
        delete head;
        head = nullptr;
        return;
    }
    node *temp = head;
    while (temp->next->next)
    {
        temp = temp->next;
    }

    //?  Delete the last node
    delete temp->next;
    //? Set the second-to-last node's next to NULL
    temp->next = NULL;
}

void delete_Position(int position)
{
    if (position < 1)
    {
        cout << "Position should be >= 1." << endl;
        return;
    }

    if (position == 1)
    {
        delete_head();
        return;
    }

    node *temp = head;
    for (int i = 1; i < position - 1 && temp; ++i)
    {

        temp = temp->next;
    }

    // todo: !temp->next bcs if temp at tail node then next node to be deleted is null
    if (!temp || !temp->next)
    {
        cout << "Position out of range." << endl;
        return;
    }
    node *nodeToDelete = temp->next;
    temp->next = temp->next->next;
    delete nodeToDelete;
}

void print()
{
    node *temp = head;
    while (temp)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main()
{
    vector<int> v = {1, 2, 3};
    for (int i = 0; i < v.size(); i++)
    {
        insert_tail(v[i]);
    }
    print();
    insert_at_position(10, 4);
    print();
    delete_head();
    print();
    delete_tail();
    print();
    delete_Position(2);
    print();

    return 0;
}