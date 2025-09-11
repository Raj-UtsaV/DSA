#include <iostream>
#include<unordered_map>
using namespace std;

class Node{
    public:
    int data;
    Node* next;

    Node(int x){
        data = x;
        next = nullptr;
    }
};

void better(Node*head){
    Node* temp = head;
    unordered_map<Node *, int> mpp;
    // int x = INT_MIN;
    // Node *ans;

    while(temp){
        if(mpp.find(temp)!=mpp.end()){
            cout << "Cycle at node " << temp->data << endl;
            break;
        }
        mpp[temp] = temp->data;
        temp = temp->next;
    }

    // if(x == INT_MIN) {
    //     cout << "No Cycle" << endl;
    //     return;
    // }

    // temp = head;
    // while(temp){
    //     if(temp==ans){  //? here we not compare using data bcs data might be repeatating
    //         cout << "Cycle at node " << &temp << endl;
    //         return;
    //     }
    //     temp = temp->next;
    // }
}

void brute(int arr[], int n, Node *head)
{
    int arr1[n] = {0};
    Node *temp = head;
    while (temp)
    {
        int x = temp->data;
        for (int i = 0; i < 5; i++)
        {
            if (arr[i] == x)
            {
                arr1[i]++;
            }
            if (arr1[i] == 2)
            {
                cout << "true " << temp->data << endl;
                return;
            }
        }
        temp = temp->next;
    }
    cout << "False";
}

void optimal(Node*head){
    Node *slow = head;
    Node *fast = head;
    while(slow && fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
        if(fast ==  slow){
            slow = head;
        
            while(slow!=fast){
                slow = slow->next;
                fast = fast->next;
            }
            cout << "Cycle at node " << slow->data << endl;
            break;
        }
    }
    
}

void better1(Node*head){
    Node *temp = head;
    unordered_map<Node *, int> mpp;
    while(temp){
        if(mpp.count(temp)!=0){
            cout << "Cycle at node " << temp->data << endl;
            break;
        }
        mpp[temp]++;
        temp = temp->next;
    }

}

int main() {
    Node *head = nullptr;
    Node *tail = nullptr;
    int arr[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++)
    {
        if (!head)
        {
            head = new Node(arr[i]);
            tail = head;
        }
        else
        {
            tail->next = new Node(arr[i]);
            tail = tail->next;
        }
    }

    tail->next = head->next; //? create a cycle
    brute(arr, 5, head);
    better(head);
    optimal(head);
    better1(head);
    return 0;
}