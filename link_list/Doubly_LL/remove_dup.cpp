#include"main.cpp"
DoublyLinkedList DLL;

void remove(Node*head){
    Node *temp = head;
    Node *front = head->next;
    while(front){
        if(temp->data==front->data){
            temp->next = front->next;
            if(front->next) //? checkig if  there is afront->next node exist
                front->next->prev = temp;
            delete front;
            front = temp->next;
        }
        else{
            temp = temp->next;
            front = front->next;
        }
    }
}

void remove1(Node*head){
    Node *temp = head;
    while(temp&& temp->next){
        Node*front=temp->next;
        while(front && front->data==temp->data){
            front = front->next;
        }
        temp->next = front;
        if(front)
            front->prev = temp;
        temp = temp->next;
    }
}

int main(){
    Node *head = nullptr;
    vector<int> v = {1, 1, 1, 2, 3,4,4};
    DLL.tolist(v, head);
    DLL.printlist(head);
    remove(head);
    DLL.printlist(head);
    remove1(head);
    DLL.printlist(head);
    return 0;

}