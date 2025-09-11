#include <iostream>
#include <vector>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node *prev;

    Node(int data)
    {
        this->data = data;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

Node *head = nullptr;
Node *tail = head;

void insert_head(int data)
{
    Node *new_node = new Node(data);
    if (!head)
    {
        head = new_node;
        tail = new_node;
        return;
    }
    head->prev = new_node;
    new_node->next = head;
    head = new_node;
}

void insert_tail(int data)
{
    Node *new_node = new Node(data);
    if (!head)
    {
        head = new_node;
        tail = new_node;
        return;
    }
    tail->next = new_node;
    new_node->prev = tail;
    tail = new_node;
}

void print_fwd()
{
    Node *temp = head;
    while (temp)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void print_bwd()
{
    Node *temp = tail;
    while (temp)
    {
        cout << temp->data << " ";
        temp = temp->prev;
    }
    cout << endl;
}

void insert_position(int position,int data){
    //position++; //?gfg striver sheet question
    if(position<1){
        cout << "Enter a valid position";
        return;
    }
    if(position==1){
        insert_head(data);
        return;
    }
    Node*temp=head;

    //? traversing to the node before jaha node insert krna hai
    for(int i=1;i<position-1 && temp;i++){
        temp=temp->next;
    }
    if(!temp){
        cout << "out of range";
        return;
    }

    //? inseting at tail
    if(!temp->next){
        insert_tail(data);
        //Node *new_node = new Node(data);
        // temp->next = new_node;
        // new_node->prev = temp;
        // tail = new_node;
        return;
    }
    Node *new_node = new Node(data);
    new_node->prev=temp;
    new_node->next=temp->next;
    temp->next->prev = new_node;
    temp->next = new_node;
}

void delete_head()
{
    if (head == nullptr)
    {
        cout << "List is empty " << endl;
        return;
    }
    Node *temp = head;
    head = head->next;
    head->prev = nullptr;
    delete temp;
}

void delete_tail()
{
    if (head == nullptr)
    {
        cout << "List is empty " << endl;
        return;
    }
    Node *temp = tail;
    tail = tail->prev;
    tail->next = nullptr;
    delete temp;
}

void delete_position(int position)
{
    if (position < 1)
    {
        cout << "Enter a valid position"<<endl;
        return;
    }
    if (position == 1)
    {
        head = head->next;
        head->prev = nullptr;
        return;
    }

    Node *temp = head;
    for (int i = 1; i < position  && temp; i++)
    {
        temp = temp->next;
    }
    if (!temp )
    {
        cout << "out of range"<<endl;
        return;
    }

    if(!temp->next){
        temp->prev->next = nullptr;
        tail = temp->prev;
        return;
    }
    

    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;

    delete temp;
}

int main()
{
    vector<int> v = {1, 2, 3, 4, 5};
    for (int i = 0; i < v.size(); i++)
    {
        // insert_head(v[i]);
        insert_tail(v[i]);
    }

    print_fwd();
    insert_position(5 , 40);
    print_fwd();
    delete_head();
    print_fwd();
    delete_tail();
    print_fwd();
    delete_position(1);
    print_fwd();
    print_bwd();

    return 0;
}