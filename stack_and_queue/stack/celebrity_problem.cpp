#include<iostream>
#include<vector>
using namespace std;

int brute(vector<vector<int>> v){
    vector<int> knowme(v.size(),0);
    vector<int> iknow(v.size(),0);
    for (int i = 0;i<v.size();i++){
        for(int j = 0;j<v[i].size();j++){
            if(v[i][j] == 1){
                iknow[i]++;
                knowme[j]++;
            }
        }
    }

    for (int i = 0;i<v.size();i++){
        if(knowme[i] == v.size()-1 && iknow[i] == 0){
            return i;
        }
    }
    return -1;
}

int optimal(vector<vector<int>> v){
    int top = 0;
    int bottom = v.size() - 1;
    while(top<bottom){
        
        if(v[bottom][top]==1)
        {
            bottom--;
        }
        else
            top++;
    }

    if(top>bottom)
        return -1;
    for (int i = 0; i < v.size();i++){
        if(i== top)
            continue;
        if(v[top][i] == 0 && v[i][top]==1){
            continue;
        }
        else
            return -1;
    }
    return top;
}

int main(){
    vector<vector<int>> v = {{0, 0, 1, 0},{0, 0, 1, 0},{0, 0, 0, 0},{0, 0, 1, 0}};
    cout << brute(v) << endl;
    cout<<optimal(v) << endl;
    return 0;
}