#include<iostream>
#include<vector>

#define N -1

using namespace std;


class Node{
    public:
    int data;
    Node* left;
    Node* right;
   Node(int data) : data(data), left(nullptr), right(nullptr) {}
};


class construct{
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


bool find(Node* root, int value){
    if(!root) return false;
    if(root->data == value) return true;
    if(root->data > value)  return find(root->left, value);
    if(root->data < value)  return find(root->right, value);
    
}


int min (Node* root){
    if(!root) return -1;
    if(!root->left) return root->data;
    return min(root->left);
}

int max(Node* root){
    if(!root) return -1;
    if(!root->right) return root->data;
    return max(root->right);
}

int main(){
    vector<int> v{5, 4, 6, 3, N, N, 7, 1};
    Node* root = construct::constructBST(v);

    int value = 1;

    cout<<"find value: "<<find(root,value)<<endl;


    cout<<"min value: "<<min(root)<<endl;
    cout<<"max value: "<<max(root)<<endl;


    return 0;



}