#include "main.cpp"
DoublyLinkedList DLL;

vector<pair<int, int>> brute(Node *head, int x)
{
    vector<pair<int, int>> res;
    Node *temp = head;

    while (temp)
    {
        Node *temp1 = temp->next;
        while (temp1 && (temp->data + temp1->data) <= x)
        {
            if (temp->data + temp1->data == x)
            {
                res.push_back(make_pair(temp->data, temp1->data));
            }
            temp1 = temp1->next;
        }
        temp = temp->next;
    }
    return res;
}

vector<pair<int, int>> optimal(Node *head, int x)
{
    vector<pair<int, int>> res;
    Node *tail = head;
    while(tail->next){
        tail = tail->next;
    }

    while(tail!=head){
        if (head->data + tail->data == x)
        {
            res.push_back(make_pair(head->data, tail->data));
        }
        if (head->data + tail->data > x){
            tail = tail->prev;
        }
        else{
            head = head->next;
        }
    }
    return res;
}

void printPairs(vector<pair<int, int>> &pairs)
{
    cout << "Pairs: ";
    for (auto pair : pairs)
    {
        cout << "(" << pair.first << "," << pair.second << ")" << ",";
    }
    cout << "\n";
}

int main()
{
    Node *head = nullptr;
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
    DLL.tolist(v, head);
    DLL.printlist(head);
    vector<pair<int, int>> ansb = brute(head, 7);
    printPairs(ansb);
    vector<pair<int, int>> anso = brute(head, 7);
    printPairs(anso);
    return 0;
}