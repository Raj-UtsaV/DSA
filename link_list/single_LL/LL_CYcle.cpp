#include <iostream>
#include <unordered_map>
using namespace std;

class Node
{

public:
    int data;
    Node *next;

    Node(int x)
    {
        this->data = x;
        this->next = nullptr;
    }
};

void brute(int arr[], int n, Node *head)
{
    int arr1[n] = {0};
    Node *temp = head;
    while (temp)
    {
        int x = temp->data;
        for (int i = 0; i < 5; i++)
        {
            if (arr[i] == x)
            {
                arr1[i]++;
            }
            if (arr1[i] == 2)
            {
                cout << "true " << arr[i] << endl;
                return;
            }
        }
        temp = temp->next;
    }
}

void better(Node *head)
{
    Node *temp = head;
    unordered_map<Node *, int> mpp;
    while (temp)
    {
        if (mpp.find(temp) != mpp.end())
        {
            cout << "true " << temp->data << endl;
            return;
        }
        mpp[temp]++;
        temp = temp->next;
    }
    cout << "False " << endl;
}

void optimal(Node *head)
{
    Node *slow = head;
    Node *fast = head;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
        {
            cout << "True " << slow->data;
            return;
        }
    }
    cout << "False";
}

int main()
{
    Node *head = nullptr;
    Node *tail = nullptr;
    int arr[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++)
    {
        if (!head)
        {
            head = new Node(arr[i]);
            tail = head;
        }
        else
        {
            tail->next = new Node(arr[i]);
            tail = tail->next;
        }
    }

    tail->next = head->next; //? create a cycle

    brute(arr, 5, head);
    better(head);
    optimal(head);

    return 0;
}