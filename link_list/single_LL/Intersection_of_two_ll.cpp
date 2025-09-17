#include "1.cpp"
#include <unordered_map>

void creatinglink(Node *head1, Node *&tail2)
{
    // if (!head1 || !tail2)
    //     return; // Check for null pointers

    Node *temp = head1;
    for (int i = 0; i < 4 && temp; i++)
    { // Ensure we don't go out of bounds
        temp = temp->next;
    }

    if (temp)
    { // Only link if temp is not null
        tail2->next = temp->next;
    }
}

void ans(Node *head1, Node *head2)
{
    unordered_map<Node *, int> mpp;
    while (head1)
    {
        if (mpp.find(head1) != mpp.end())
        {
            cout << "Common node at " << head1->data << endl;
            return;
        }
        mpp[head1] = head1->data; // Store the node itself as key, and data as value (though data isn't strictly needed for finding intersection)
        head1 = head1->next;
    }

    while (head2) {
        if (mpp.find(head2) != mpp.end()) {
            cout << "Common node at " << head2->data << endl;
            return;
        }
        head2 = head2->next;
    }
    cout << "bhakk";
}

int getDifference(Node *head1, Node *head2)
{
    int len1 = 0, len2 = 0;
    while (head1 != NULL || head2 != NULL)
    {
        if (head1 != NULL)
        {
            ++len1;
            head1 = head1->next;
        }
        if (head2 != NULL)
        {
            ++len2;
            head2 = head2->next;
        }
    }
    return len1 - len2; // if difference is neg-> length of list2 > length of list1 else vice-versa
}

// utility function to check presence of intersection
Node *brute(Node *head1, Node *head2)
{
    int diff = getDifference(head1, head2);
    if (diff < 0)
        while (diff++ != 0)
            head2 = head2->next;
    else
        while (diff-- != 0)
            head1 = head1->next;
    while (head1 != NULL)
    {
        if (head1 == head2)
            return head1;
        head2 = head2->next;
        head1 = head1->next;
    }
    return head1;
}

Node *optimal(Node *head1, Node *head2)
{
    Node *d1 = head1;
    Node *d2 = head2;

    while (d1 != d2)
    {
        if (d1 == NULL)
        {
            d1 = head2;
        }
        else
        {
            d1 = d1->next;
        }

        if (d2 == NULL)
        {
            d2 = head1;
        }
        else
        {
            d2 = d2->next;
        }
    }

    return d1;
}

int main()
{
    Node *head1 = nullptr;
    Node *head2 = nullptr;
    Node *tail1 = nullptr;
    Node *tail2 = nullptr;
    vector<int> v1 = {1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> v2 = {9, 10, 11};

    basicoperation bo;
    bo.tolist(v1, head1, tail1);
    bo.tolist(v2, head2, tail2);
    creatinglink(head1, tail2);
    bo.print(head2);
    return 0;
}