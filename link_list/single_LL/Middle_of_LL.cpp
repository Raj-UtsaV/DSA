#include <iostream>
#include <vector>
#define llu long long unsigned int
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

int length(node *head1)
{
    int cnt = 0;
    node *temp = head1;
    while (temp)
    {
        temp = temp->next;
        cnt++;
    }
    return cnt;
}

node* shift_head_brute(node *head1,int cnt){

    for (int i = 0; i < cnt;i++){
        head1=head1->next;
    }
    return head1;
}

void brute(node*head){
    node *temp = head;
    int cnt = length(temp);
    cnt /= 2;
    temp = shift_head_brute(temp, cnt);
    print(temp);
}

void tolist(){
    vector<int> v = {1, 2,3, 4, 5};
    for (llu i = 0; i < v.size(); i++)
    {
        insert_tail(v[i]);
    }
    print(head);
}

void optimal(node*head1){
    node *slow = head1;
    node *fast = head1;
    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    print(slow);
}

int main()
{
    tolist();
    brute(head);
    optimal(head);

    return 0;
}