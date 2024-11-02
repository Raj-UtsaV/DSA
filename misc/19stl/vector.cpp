#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> v;

    //! assign a vector of length 5 and all element 1 initially
    vector<int> a(5,1);
    for(int i:a){
        cout<<i<<" ";
    }
    cout<<endl;




    cout<<"capacity--> "<<v.capacity()<<endl;

    //! push_back command use to take input in vector
    v.push_back(10);
    cout<<"capacity--> "<<v.capacity()<<endl;
    v.push_back(20);
    cout<<"capacity--> "<<v.capacity()<<endl;

    //* here capacity will double because  of no space left in the vector  so it will call reallocate to 
    //* allocate more (aka doble of prev one)
    v.push_back(30);

    // ! capacity  is the  size of the memory allocated by allocator::allocate
    // * and size is number of elements for which memory has been allocated
    // * So when we push back an element, size increases but not capacity
    cout<<"capacity--> "<<v.capacity()<<endl;

    // ! size  is number of elements present till now and not the memory allocated for them
    cout<<"size---> "<<v.size()<<endl;

    //* at,front,back operation can be use in vector also as used in array


    //! pop_back use to remove last element in a vector

    cout<<"before pop "<<endl;
    for(int i:v){
        cout<<i<<" ";
    }
    cout<<endl;

    v.pop_back();

    cout<<"after pop "<<endl;
    for(int i:v){
        cout<<i<<" ";
    }
    cout<<endl;


    //* to clear the vector we use clear command 
    //* this command only set the size=0 and does not deallocate the memory
    //* if you want to free up the memory then you have to use swap with empty vector or assign empty vector to your vector
    

    cout<<"befor clear size "<<v.size()<<endl;
    v.clear();
    cout<<"after clear size "<<v.size()<<endl;
    v.empty();
    cout<<"capacity--> "<<v.capacity()<<endl;

}