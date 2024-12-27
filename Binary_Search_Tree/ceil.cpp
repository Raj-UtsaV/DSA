#include <iostream>
#include <vector>

using namespace std;

#define N -1

class Node {
public:
    int data;
    Node* left;
    Node* right;
    Node(int data) : data(data), left(nullptr), right(nullptr) {}
};

class construct {
private:
    static Node* insert(Node* root, int data) {
        if (data == N) {
            return root;
        }
        if (root == nullptr) {
            return new Node(data);
        }
        if (data < root->data) {
            root->left = insert(root->left, data);
        } else {
            root->right = insert(root->right, data);
        }
        return root;
    }

public:
    static Node* constructBST(const vector<int>& values) {
        Node* root = nullptr;
        for (int value : values) {
            root = insert(root, value);
        }
        return root;
    }
};


int ceil(Node* root,int val,int *ceiL ){
    if(!root) return *ceiL;
    if(root->data == val) return val;

    if(root->data > val) {
        *ceiL = root->data;
        return ceil(root->left,val,ceiL);
    }

    if(root->data < val){
        return ceil(root->right,val,ceiL);
    }

    return *ceiL;

    
}


int main(){
    vector<int> values = {8, 3, 10, 1, 6, N, 14, N, N, 4, 7, N, N, 13, N};
    Node* root = construct::constructBST(values);

    int ceiL = -1;
    cout << "Ceil of 5: " << ceil(root, 5,&ceiL) << endl;
    cout << "Ceil of 11: " << ceil(root, 11,&ceiL) << endl;
    cout << "Ceil of 6: " << ceil(root, 6,&ceiL) << endl;
    cout << "Ceil of 15: " << ceil(root, 15,&ceiL) << endl;
    return 0;
}