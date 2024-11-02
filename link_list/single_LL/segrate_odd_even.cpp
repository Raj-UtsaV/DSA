#include "1.cpp"

basicoperation bo;

void brute(Node * head, Node * &tail)
{
    if (!head)
        return; // Check if the list is empty

    Node *temp = head;
    Node*end = tail;
    Node *prev = NULL;
    int cnt = 0;

    while (temp!=end)
    {
        cnt++;
        if (cnt % 2 == 0)
        {

            bo.insert_tail(temp->data,tail);
            prev->next = temp->next->next;
            Node *front = temp->next;
            delete temp;
            temp = front;
        }
        else{
            prev = temp;
            temp=temp->next;
        }


    }
    bo.print(head);
}


void optimal(Node*head){
    Node *oddhead = NULL;
    Node *evenhead = NULL;
    Node*oddtail = NULL;
    Node*eventail = NULL;
    int cnt = 0;
    Node*temp = head;
    while(temp){
        Node *new_node = new Node(temp->data);
        if (cnt % 2 == 0)
        {

            if (!evenhead)
            {
                evenhead = new_node;
                eventail = new_node;
            }
            else
            {
                eventail->next = new_node;
                eventail = new_node;
            }
         }
         else{
            if(!oddhead){
                oddhead = new_node;
                oddtail = new_node;
            }
            else{
                 oddtail->next = new_node;
                 oddtail = new_node;
 
            }
            
         }
         cnt++;
         Node *front = temp->next;
         delete temp;
         temp = front;
    }
    eventail->next = oddhead;
    bo.print(evenhead);


}
int main()
{
    Node *head = NULL;
    Node *tail = NULL;
    vector<int> v = {1, 2, 3, 4, 5};
    bo.tolist(v, head, tail);
    bo.print(head);
    optimal(head);
    //brute(head, tail);
    return 0;
}