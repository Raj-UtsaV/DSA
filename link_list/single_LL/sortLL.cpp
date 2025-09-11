#include <iostream>
#include <vector>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int d)
    {
        data = d;
        next = nullptr;
    }

    Node(int d, Node*next1){
        data = d;
        next = next1;
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

    void tolist(vector<int> arr, Node *&head, Node *tail)
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
};

void brute(Node *head1)
{
    Node *head = head1;
    while (head)
    {
        int min_val = head->data;
        Node *temp = head->next;
        Node *new_node = head;
        while (temp)
        {
            if (temp->data < min_val)
            {
                min_val = temp->data;
                new_node = temp;
            }
            temp = temp->next;
        }

        if (new_node->data < head->data)
        {
            min_val = head->data;
            head->data = new_node->data;
            new_node->data = min_val;
        }

        head = head->next;
    }
}

class mergesort
{
    //! using merge sort to sort nodes
public:
    Node* merge(Node *list1, Node *list2){
        Node *dummyNode = new Node(-1);
        Node *current = dummyNode;
        while (list1 && list2)
        {
            if (list1->data <= list2->data)
            {
                current->next = list1;
                list1 = list1->next;
            }
            else
            {
                current->next = list2;
                list2 = list2->next;
            }
            current = current->next;
        }
        if(list1 != nullptr){
            current->next = list1;
        }
        else{
            current->next = list2;
        }
        return dummyNode->next;
    }
    Node *find_mid(Node *head)
    {

        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }

        Node *slow = head, *fast = head->next;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    Node *optimal(Node *head)
    {
        if (!head || !head->next)
        {
            return head;
        }
        Node *mid = find_mid(head);
        Node *left = head;
        Node *right = mid->next;
        mid->next = nullptr;

        left = optimal(left);
        right = optimal(right);

        return merge(left, right);
    }
};

int main()
{
    Node *head = nullptr;
    Node *tail = nullptr;
    vector<int> v = {1, 513, 42, 100, 3242, 512};

    basicoperation b;
    b.tolist(v, head, tail);
    b.print(head);

    brute(head);
    b.print(head);
    mergesort optimal1;
    Node *head1 = optimal1.optimal(head);

    b.print(head1);
    return 0;
}