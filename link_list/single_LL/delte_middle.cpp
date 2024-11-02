#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int x)
    {
        this->data = x;
        this->next = NULL;
    }
};

void find(Node *&head)
{

    if (!head || !head->next)
    {
        head = NULL;
        return;
    }
    Node *slow = head;
    Node *fast = head;
    Node *prev = NULL;
    while (fast && fast->next)
    {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    if (slow->next)
    {
        slow->data = slow->next->data;
        Node *temp = slow->next;
        slow->next = slow->next->next;
        delete temp;
    }
    else
    {
        delete slow;
        prev->next = NULL;
    }
}

Node *deleteMiddle(Node *head)
{

    if (head == NULL || head->next == NULL)
    {
        return NULL;
    }

    Node *slow = head;
    Node *fast = head;
    fast = head->next->next;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    slow->next = slow->next->next;
    return head;
}

int main()
{

    Node *head = NULL;
    Node *tail = NULL;

    int arr[] = {1,3};
    for (int i = 0; i < 2; i++)
    {
        Node *new_node = new Node(arr[i]);
        if (!head)
        {
            head = new_node;
            tail = head;
        }
        else
        {
            tail->next = new_node;
            tail = new_node;
        }
    }
    Node *temp = deleteMiddle(head);
    while (temp)
    {
        cout << temp->data << " ";
        temp = head->next;
    }
    find(head);
    while (head)
    {
        cout << head->data << " ";
        head = head->next;
    }

    return 0;
}