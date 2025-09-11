#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node *next;
    
    Node(int data){
        this->data = data;
        this->next = NULL;
    }
};

class Stack{
    //! work based on insert at head so delete the value of last
    Node *head = nullptr;
    public:
    void push(int data){
        Node *new_node = new Node(data);
        if (!new_node)
        {
            cout << "\nStack Overflow";
        }
        new_node->next = head;
        head = new_node;
    }

    void pop(){
        if (head==nullptr)
        {
            cout << "\nStack Underflow";
            return;
        }
        Node *temp = head;
        int x = head->data;
        cout<<"popped element : "<<x<<endl;
        head = head->next;
        delete temp;
    }

    int peek(){
        if(!head){
            cout << "Stack is empty" << endl;
            return -1;
        }
        else
            return head->data;
    }
};

int main(){
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << "Top element is : " << s.peek() << endl;
    s.pop();
    cout << "Top element after pop :  " << s.peek() << endl;
    return 0;
}