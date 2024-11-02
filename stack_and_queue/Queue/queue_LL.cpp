#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};

class QueueNode
{
    //! work based on insert at tail
    Node *head = nullptr;
    Node *tail = nullptr;

    public:
    void enqueue(int data){
        Node *new_node = new Node(data);
        if (tail == nullptr)
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

    int dequeue(){
        if (head == nullptr)
        {
            cout << "Queue is empty" << endl;
            return -1;
        }
        int data = head->data;
        Node *temp = head;
        head = head->next;
        delete temp;
        return data;
    }

    int peek(){
        if (head == nullptr)
        {
            cout << "Queue is empty" << endl;
            return -1;
        }
        return head->data;
    }

    int size(){
        int count = 0;
        Node *temp = head;
        while (temp!= nullptr)
        {
            count++;
            temp = temp->next;
        }
        return count;
    }
};

int main(){
    QueueNode q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    cout << "Dequeued element: " << q.dequeue() << endl;
    cout << "Peek element: " << q.peek() << endl;
    cout << "Size of queue: " << q.size() << endl;
    return 0;
}