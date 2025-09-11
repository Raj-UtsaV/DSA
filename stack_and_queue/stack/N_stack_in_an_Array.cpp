#include <thread>
#include <chrono>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class NStack
{
public:
    int size;
    int numStacks;
    std::vector<std::stack<int>> N_stack; 


    NStack(int N, int S)
    {
        N_stack.resize(N);
        size = S;
        numStacks = N; 
    }


    bool push(int x, int m)
    {
        if (m-1 >= numStacks)
            return false; 
        N_stack[m-1].push(x);
        return true;
    }

    int pop(int m)
    {
        if (m-1 >= numStacks || N_stack[m-1].empty())
        {
            return -1; 
        }
        int top = N_stack[m-1].top();
        N_stack[m-1].pop();
        return top;
    }
};

int main()
{
    system("cls");

    
    NStack N_Stack(3,6);

    cout << N_Stack.pop(2) << endl;
    cout << N_Stack.push(8,2) << endl; 
    cout << N_Stack.push(1,2) << endl; 
    cout << N_Stack.push(25,2) << endl; 
    cout << N_Stack.push(41,3) << endl; 
    cout << N_Stack.push(20,2) << endl; 
    cout << N_Stack.push(17,2) << endl; 
    cout << N_Stack.pop(2) << endl;      
    cout << N_Stack.pop(2) << endl;      
    cout << N_Stack.pop(2) << endl;      

    this_thread::sleep_for(chrono::seconds(10));
    system("cls");

    return 0;
}
