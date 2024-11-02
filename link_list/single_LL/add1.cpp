#include "1.cpp"
basicoperation bo;

Node *add1(Node*head){
    Node *prev = NULL;
    Node *temp = head;

    while(temp){
        Node *front = temp->next;
        temp->next = prev;
        prev = temp;
        temp = front;
    }
    
    temp = prev;
    int carry = 1;
    while(temp || carry){
        int sum = temp->data + carry;
        carry = sum / 10;
        temp->data = sum % 10;
        if(!temp->next && carry){
            temp->next = new Node(carry);
            carry = 0;
        }
        temp=temp->next;
    }

    head = NULL;
    temp = prev;
    while(temp){
        Node *front = temp->next;
        temp->next = head;
        head = temp;
        temp = front;
    }
    return head;
}
int main()
{
    Node *head = NULL;
    Node*tail=NULL;
    vector<int> v = {1, 9, 9};
    bo.tolist(v, head,tail);
    bo.print(head);
    Node *ans = add1(head);
    bo.print(ans);
    return 0;

}