#include "main.cpp"
DoublyLinkedList DLL;


void delete_given(Node*&head,int x){
    Node *temp = head;
    while(temp){
        if(temp->data==x){
            if(temp==head){
                head = head->next;
            }
            Node *front = temp->next;
            Node *back = temp->prev;
            if(front)
                front->prev = back;
            if(back)
                back->next = front;
            delete temp;
            temp = front;
        }
        else temp=temp->next;
    }
}
int main()
{
    Node *head = nullptr;
    vector<int> v = {1, 3, 5, 53, 2, 43, 3, 32, 45, 3, 3};
    DLL.tolist(v, head);
    DLL.print_fwd(head);
    delete_given(head,3);
    DLL.print_fwd(head);

    return 0;
}