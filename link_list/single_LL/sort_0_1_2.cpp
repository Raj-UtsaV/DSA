#include <iostream>
#include <vector>
#include <forward_list>
using namespace std;

// forward_list<int> sorted(forward_list<int> list1)
// {
//     forward_list<int> list;
//     int cnt = 0;
//     for (const int &x : list1)
//     {

//         if (x == 0)
//         {
//             list.push_front(0);
//             cnt++;
//         }
//         if (x == 2)
//         {
//             auto it = list.before_begin();
//             for (auto next = list.begin(); next != list.end(); ++it, ++next);
//             list.insert_after(it, 2);
//         }
//         else{
//             auto it = list.before_begin();
//             for (int i = 0; i < cnt && next(it) != list.end(); ++i)
//             {
//                 ++it;
//             }
//             list.insert_after(it, 1);
//         }

//     }
//     return list;
// }

// int main()
// {
//     forward_list<int> given_list = {1, 2, 0, 1, 2, 0, 2, 1, 0, 2, 1};

//     forward_list<int>list = sorted(given_list);
//     for (const int &x : list)
//     {
//         cout << x << " ";
//     }

//     return 0;
// }

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
};

void insert_tail(int data, Node *&head, Node *&tail)
{
    Node *new_Node = new Node(data);
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

void insert_head(int data, Node *&head, Node *&tail)
{
    Node *new_Node = new Node(data);
    if (head == nullptr)
    {
        tail = new_Node;
    }
    new_Node->next = head;
    head = new_Node;
}

void insert_at_position(int data, Node *&head, Node *&tail, int position)
{
    if (position == 1)
    {
        insert_head(data, head, tail);
        return;
    }
    Node *temp = head;
    for (int i = 1; i < position - 1;i++){
        temp = temp->next;
    }
    Node *new_Node = new Node(data);
    new_Node->next = temp->next;
    temp->next = new_Node;

}

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
        insert_tail(arr[i], head, tail);
    }
}

Node *sorted(Node *head)
{

    Node *ansh = nullptr;
    Node *anst = nullptr;
    Node *current = head;
    int cnt = 1;
    while (current)
    {
        if (current->data == 0)
        {
            insert_head(0, ansh, anst);
            cnt++;
        }
        else if (current->data == 2)
        {
            insert_tail(2, ansh, anst);
        }
        else
        {
            
            insert_at_position(1, ansh, anst, cnt);
        }
        current = current->next;
    }
    return ansh;
}

int main()
{
    Node *head = nullptr;
    Node *tail = head;
    vector<int> arr = {0,1,2,1,1,0,2};
    tolist(head, tail, arr);
    print(head);
    Node *ans = sorted(head);
    print(ans);
    return 0;
}