#include <iostream>
using namespace std;

char convert(char c)
{
    if (c >= 'a' && c <= 'z')
        return c;
    else
    {
        char temp = c - 'A' + 'a';
        return temp;
    }
}

string palindrom(string c){
    int e = c.size() - 1;
    for(int i = 0;i<c.size();i++ ){
        if(c[i] != c[e--]) return "NO"; 
    }
    return "YES";
}


string convert1(string c )
{   
    int i = 0;
    //? until the string doesn't end
    while (c[i] != '\0')
    {
        
        if (c[i] >= 'a' && c[i] <= 'z')
           i++;
        else if((c[i] >= 'A' && c[i] <= 'Z'))
        {
            char temp = c[i] - 'A' + 'a';
            c[i] = temp;
            i++;
        }
        
         
    }
    return palindrom(c);
}



int main()
{
    string c;
    cin >> c;
    cout<<convert1(c);
    return 0;
}