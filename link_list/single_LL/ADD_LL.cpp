#include <iostream>
#include<vector>
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

void tolist(Node *&head, Node *&tail, vector<int> arr)
{

    int n = arr.size();
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

Node *add(Node *head1, Node *head2)
{
    Node *ansh = NULL;
    Node *anst = NULL;
    int carry = 0;

    while (head1 || head2 || carry)
    {
        int sum = 0;
        if(head1){
            sum += head1->data;
            head1 = head1->next;
        }
        if(head2){
            sum += head2->data;
            head2 = head2->next;
        }

        sum += carry;
        carry = sum / 10;
        Node *new_node = new Node(sum % 10);
        if(!ansh){
            ansh = new_node;
            anst = new_node;
        }
        else{
            anst->next = new_node;
            anst = new_node;
        }

    }
    return ansh;
}

int main()
{
    Node *head1 = NULL;
    Node *tail1 = NULL;
    Node *head2 = NULL;
    Node *tail2 = NULL;

    vector<int> arr1 = {9,9,9,9,9,9};
    vector<int> arr2 = {9,9};

    tolist(head1, tail1, arr1);
    tolist(head2, tail2, arr2);


    print(head1);
    print(head2);

    Node *ans = add(head1, head2);
    print(ans);
    return 0;
}