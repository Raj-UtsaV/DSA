#include <iostream>
using namespace std;

class Queue{
    int *arr;
    int maxSize, front, rear;

public:
    Queue(int size){
        this->maxSize = size;
        arr = new int[maxSize];
        front = -1;
        rear = -1;
    }

    void enqueue(int newElement)
    {
        if (rear == maxSize)
        {
            cout << "Queue is full\nExiting..." << endl;
            exit(1);
        }
        if (rear == -1)
        {
            front = 0;

        }
        rear++;
        arr[rear] = newElement;
        cout << "The element pushed is " << newElement << endl;

    }

    int dequeue()
    {
        if (front == -1)
        {
            cout << "Queue Empty\nExiting..." << endl;
        }
        int popped = arr[front];
        if (front==rear)
        {
            front = -1;
            rear = -1;
        }
        front++;
        return popped;
    }
    int top()
    {
        if (front == -1)
        {
            cout << "Queue is Empty" << endl;
            exit(1);
        }
        return arr[front];
    }
    int size()
    {
        return rear - front;
    }
};

int main() {
    Queue q(6);
    q.enqueue(4);
    q.enqueue(14);
    q.enqueue(24);
    q.enqueue(34);
    cout << "The peek of the queue before deleting any element " << q.top() <<endl;
    cout << "The size of the queue before deletion " << q.size() <<endl;
    cout << "The first element to be deleted " << q.dequeue() <<endl;
    cout << "The peek of the queue after deleting an element " << q.top() <<endl;
    cout << "The size of the queue after deleting an element " << q.size() <<endl;
    

    return 0;
}