//! #include <iostream>
//! #include <map>
//! using namespace std;

//! class DLL
//! {
//! public:
//!     int key;
//!     int data;
//!     DLL *next;
//!     DLL *prev;

//!     DLL(int key, int data) : key(key), data(data), next(NULL), prev(NULL) {}
//! };

//! int capacity;
//! map<int, DLL *> mpp;
//! DLL *head = new DLL(-1, -1);
//! DLL *tail = head;

//! void put(int key1, int data1,int used = 0)
//! {

//!     if (mpp.size() == capacity && mpp.find(key1) == mpp.end())
//!     {

//!         DLL *temp = tail->prev;
//!         tail->prev = tail->prev->prev;
//!         tail->prev->next = tail;
//!         mpp.erase(temp->key);
//!         delete temp;
//!     }

//!     if (mpp.find(key1) != mpp.end() && used==0)
//!     {

//!         mpp[key1]->data = mpp[key1]->data + data1;
//!     }

//!     else
//!     {
//!         DLL *new_node = new DLL(key1, data1);
//!         head->next->prev = new_node;
//!         new_node->next = head->next;
//!         head->next = new_node;
//!         new_node->prev = head;
//!         mpp[key1] = new_node;
//!     }
//! }

//! void get(int key1)
//! {
//!     if (mpp.find(key1) != mpp.end())
//!     {
//!         cout << mpp[key1]->data << endl;
//!         int x = mpp[key1]->data;
//!         mpp[key1]->prev->next = mpp[key1]->next;
//!         mpp[key1]->next->prev = mpp[key1]->prev;
//!         delete mpp[key1];
//!         put(key1, x, 1);
//!     }
//!     else
//!     {
//!         cout << "Key not found" << endl;
//!     }
//! }

//! void print()
//! {
//!     DLL *temp = head->next;
//!     while (temp != tail)
//!     {
//!         cout << temp->key << " " << temp->data << " " << endl;
//!         temp = temp->next;
//!     }
//!     cout << endl;
//! }
//! int main()
//! {
//!     capacity = 1;
//!     {
//!         head->next = tail;
//!         tail->prev = head;
//!     }
//!     put(2, 1);
//!     get(2);
//!     print();
//!     return 0;
//! }

#include <iostream>
#include <list>
#include <map>

using namespace std;

list<pair<int, int>> ls;
map<int, list<pair<int, int>>::iterator> mpp; // Adjusted to use correct iterator type
int capacity = 1;

void addnode(int key, int value)
{
    ls.push_front({key, value});
    mpp[key] = ls.begin();
}
int get(int key)
{
    if (mpp.find(key) != mpp.end())
    {
        int value = mpp[key]->second;
        ls.erase(mpp[key]);
        addnode(key, value);
        return value;
    }
    return -1;
}

void put(int key, int value)
{
    if (mpp.find(key) != mpp.end())
    {
        ls.erase(mpp[key]);
        mpp.erase(key);
    }
    if (mpp.size() == capacity)
    {
        int lastkey = ls.back().first;
        mpp.erase(lastkey);
        ls.pop_back();
    }
    addnode(key, value);
}

void print()
{
    for (auto it = ls.begin(); it != ls.end(); ++it)
    {
        cout << it->first << " " << it->second << endl;
    }
    cout << endl;
}

int main()
{
    capacity = 2;
    put(2, 1);
    put(2, 2);
    cout<<get(2)<<endl;
    print();
    put(1, 1);
    put(4, 1);
    get(2);
    print();
    return 0;
}
