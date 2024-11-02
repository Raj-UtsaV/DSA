#include <iostream>
#include<unordered_map>
using namespace std;

class Node{
    public:
        int data;
        Node *next;
         
         Node(int x){
            data = x;
            next = NULL;
         }
};


int brute(Node*head){
    Node *temp = head;
  
    unordered_map<Node *, int> mpp;

    Node *x = NULL;

    while(temp){
        if(mpp.find(temp)!=mpp.end()){
            x = temp;
            break;
        }
        mpp[temp]++;
       
        temp = temp->next;
    }
    

    if(!x){
        return -1;
    }
   

    temp = head;
    int cnt = 0;
    int cnt1 = 0;
    while(temp){
        if(temp == x){
            if(cnt1==1 ){
                return cnt;
            }
            cnt1++;
        }
        if(cnt1==1){
            cnt++;
        }
        temp = temp->next;
    }
    return -1;
}

int better(Node*head){
    Node *temp = head;
    int cnt = 1;
    unordered_map<Node *, int> mpp;
    while(temp){
        if(mpp.find(temp)!=mpp.end()){
            int ans = cnt - mpp[temp];
            return ans;
        }
        mpp[temp] = cnt;
        cnt++;
        temp = temp->next;
    }
    return 0;
}

int optimal(Node*head){
    Node*slow = head;
    Node *fast = head;
    while(fast&&fast->next){
        slow = slow->next;
        fast = fast->next->next;
        if(slow==fast){
            int x = 1;
            fast = fast->next;
            while(slow!=fast){
                x++;
                fast = fast->next;
            }
            return x;
        }
    }
    return 0;
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

    cout<<brute(head)<<endl;
    cout<<better(head)<<endl;
    cout<<optimal(head)<<endl;

    return 0;

}