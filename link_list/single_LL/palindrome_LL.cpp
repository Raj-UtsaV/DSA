#include <iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

class Node
{
    public:
    int data;
    Node *next;

    Node(int x)
    {
        data = x;
        next = nullptr;
    }
};


void print(Node*head){
    while(head){
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

bool brute(Node*head){
    string s;
    Node *temp = head;
    while(temp){
        s += to_string(temp->data);
        temp = temp->next;
    }
    string s1 = s;
    reverse(s1.begin(), s1.end());
    if(s==s1)
        return 1;
    return 0;
}

Node* reverse(Node *head)
{
    Node *temp = head;
    Node *prev = nullptr;
    while (temp)
    {

        Node *front = temp->next;
        temp->next = prev;
        prev = temp;
        temp = front;
    }
    return prev;
}


bool optimal(Node*head){
    Node*slow=head;
    Node*fast=head;
    while(fast->next&&fast->next->next){
        slow=slow->next;
        fast = fast->next->next;
    }
    fast = slow->next;
    slow->next = nullptr;
    fast = reverse(fast);

    while(fast){
        if(head->data!=fast->data){
            return 0;
        }
        head = head->next;
        fast = fast->next;
    }
    return 1;
}

int main()
{
    Node *head = nullptr;
    Node *tail = head;
    vector<int> arr = {1, 0,  0, 1};

    for (int i = 0; i < arr.size(); i++)
    {
        Node *new_Node = new Node(arr[i]);
        if (head == nullptr)
        {
            head = new_Node;
            tail = new_Node;
        }
        else
        {
            tail->next = new_Node;
            tail = new_Node;
        }
    }

    cout << brute(head)<<endl;
    cout << optimal(head)<<endl;

    return 0;
}