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

void tolist(Node *&head, Node *&tail, int arr[])
{

    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++)
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
}

Node *delete_kth_back(Node *head, int k)
{
    if (head == NULL)
    {
        return NULL;
    }

    int length = 0;
    Node *temp = head;
    while (temp != NULL)
    {
        length++;
        temp = temp->next;
    }
    temp = head;
    length -= k;

    if (length <= 0)
    {
        return head;
    }

    for (int i = 0; i < length - 1; i++)
    {
        temp = temp->next;
    }

    if (!length)
    {
        return head->next;
    }

    else
    {
        temp->next = temp->next->next;
    }
    return head;
}

Node *optimal(Node *head, int k)
{
    Node *slow = head;
    Node *fast = head;

    for (int i = 0; i < k;i++){
        fast = fast->next;
    }

    if (fast == NULL)
        return head->next;

    while(fast->next){
        slow = slow->next;
        fast = fast->next;
    }

    Node *temp = slow->next;
    slow->next = slow->next->next;
    delete temp;
    return head;
}

int main()
{

    Node *head = NULL;
    Node *tail = NULL;

    int arr[] = {1, 2};
    int n = 1;

    tolist(head, tail, arr);

    Node *brute = delete_kth_back(head, n);
    print(brute);
    Node *Optimal = optimal(head, n);
    print(Optimal);

    return 0;
}