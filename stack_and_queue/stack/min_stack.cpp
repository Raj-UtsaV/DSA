#include <iostream>
#include<stack>

using namespace std;

class stack1{
    public:
    stack<pair<int, int>> st;

    void push(int x){
        if(st.empty()){
            st.push({x, x});
            return;
        }
        else{
            int p =st.top().second;
            st.push({x, min(x, p)});
        }
    }

    int pop(){
        if(st.empty()){
            cout<<"Stack is empty\n";
            return -1;
        }
        int x = st.top().first;
        st.pop();
        return x;
    }

    int getmin(){
        if(st.empty()){
            cout<<"Stack is empty\n";
            return -1;
        }
        return st.top().second;
    }
    
    int size(){
        return st.size();
    }
};

class MinStack
{
    vector<pair<int, int>> st;

public:
    MinStack()
    {
    }

    void push(int val)
    {
        if (st.empty())
        {
            st.push_back(make_pair(val, val));
        }
        else
        {
            int x = st.back().second;
            st.push_back(make_pair(val, min(x, val)));
        }
    }

    void pop()
    {
        if (st.empty())
        {
            return;
        }
        st.pop_back();
    }

    int top()
    {
        if (st.empty())
            return -1;
        return st.back().first;
    }

    int getMin()
    {
        if (st.empty())
            return -1;
        return st.back().second;
    }
};
int main() {
    stack1 st;
    st.push(5);
    st.push(2);
    st.push(3);
    st.push(1);
    cout << "Minimum element is " << st.getmin() << endl;
    st.pop();
    cout << "Minimum element is " << st.getmin() << endl;
    st.push(4);
    cout << "Minimum element is " << st.getmin() << endl;
    st.pop();
    cout << "Minimum element is " << st.getmin() << endl;
    cout << "Size of stack is " << st.size() << endl;
    return 0;
}