#include <thread>
#include <chrono>
#include <iostream>
#include <stack>

void insertAtBottom(std::stack<int> &s, int x)
{
    if (s.empty())
    {
        s.push(x);
        return;
    }
    int temp = s.top();
    s.pop();
    insertAtBottom(s, x);
    s.push(temp);
}

// Function to reverse the stack
void reverseStack(std::stack<int> &s)
{
    if (!s.empty())
    {
        int x = s.top();
        s.pop();
        reverseStack(s);
        insertAtBottom(s, x);
    }
}

void print(std::stack<int> &s)
{
    while (!s.empty())
    {
        std::cout << s.top() << " ";
        s.pop();
    }
    std::cout << std::endl;
}

int main()
{
    {
        system("cls");
    }

    //! In this block write your code
    {
        std::stack<int> s;
        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        // std::cout<<"Original Stack: ";
        // print(s);
        reverseStack(s);
        std::cout << "Reversed Stack: ";
        print(s);
    }

    {
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }
    return 0;
}