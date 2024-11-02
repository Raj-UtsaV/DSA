#include<iostream>
#include<vector>
#define llu long long unsigned int
using namespace std;

class Node{
    public:
    int data;
    Node *prev;
    Node *next;

    Node(int data){
        this->data = data;
        this->prev = NULL;
        this->next = NULL;
    }
};

class DoublyLinkedList{
    public:
    void tolist(vector<int>&v,Node *&head,Node *tail=nullptr){
        for(llu i = 0; i < v.size();i++){
            Node *new_node = new Node(v[i]);
            if(!head){
                head = new_node;
                tail = new_node;
            }
            else{
                new_node->prev = tail;
                tail->next = new_node;
                tail = new_node;
            }
        }
    }

    void printlist(Node *head)
    {
        Node *temp = head;
        while(temp!=NULL){
            cout<<temp->data<<" ";
            temp = temp->next;
        }
        cout<<endl;
    }
};

