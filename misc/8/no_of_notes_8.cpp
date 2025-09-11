#include<iostream>
using namespace std;

int main(){
    int ammount;
    cout<<"Enter the ammount : ";
    cin>>ammount;

    cout<<endl;

    int RS500,RS100,RS50,RS20,RS10,RS5,RS2,RS1;

    switch(1){
        case 1: RS500=ammount/500;
                ammount=ammount%500;
                cout<<"500 rupees notes : "<<RS500<<endl;

        case 2: RS100=ammount/100;
                ammount=ammount%100;
                cout<<"100 rupees notes : "<<RS100<<endl;

        case 3: RS50=ammount/50;
                ammount=ammount%50;
                cout<<"50 rupees notes : "<<RS50<<endl;

        case 4: RS20=ammount/20;
                ammount=ammount%20;
                cout<<"20 rupees notes : "<<RS20<<endl;

        case 5: RS10=ammount/10;
                ammount=ammount%10;
                cout<<"10 rupees notes : "<<RS10<<endl;

        case 6: RS5=ammount/5;
                ammount=ammount%5;
                cout<<"5 rupees coins : "<<RS5<<endl;

        case 7: RS2=ammount/2;
                ammount=ammount%2;
                cout<<"2 rupees coins : "<<RS2<<endl;

        case 8: RS1=ammount/1;
                ammount=ammount%1;
                cout<<"1 rupees coins : "<<RS1<<endl;

    }

    return 0;
}