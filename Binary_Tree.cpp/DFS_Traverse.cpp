// ? ? Inorder traversal (left,root,right)
// ? ? preorder traversal (root,left,right)
// ? ? postorder traversal (left,right,root)

#include "main.cpp"
print_Tree print;
to_BT BT;

class preorder
{
public:
    void print(BT_Node *root)
    {
        if (root == nullptr)
            return;
        cout << root->data << " ";
        print(root->left);
        print(root->right);
    }

    void vec(BT_Node *root, vector<int> &res)
    {
        if (root == nullptr)
            return;
        res.push_back(root->data);
        vec(root->left, res);
        vec(root->right, res);
    }


    
};

class postorder
{
public:
    void print(BT_Node *root)
    {
        if (root == nullptr)
            return;
        print(root->left);
        print(root->right);
        cout << root->data << " ";
    }

    void vec(BT_Node *root, vector<int> &res)
    {
        if (root == nullptr)
            return;
        vec(root->left, res);
        vec(root->right, res);
        res.push_back(root->data);
    }
};

class inorder
{
public:
    void print(BT_Node *root)
    {
        if (root == nullptr)
            return;
        print(root->left);
        cout << root->data << " ";
        print(root->right);
    }

    void vec(BT_Node *root, vector<int> &res)
    {
        if (root == nullptr)
            return;
        vec(root->left, res);
        res.push_back(root->data);
        vec(root->right, res);
    }
};

int main()
{

    system("cls");
    BT_Node *root;
    vector<int> v{1, 2, 3, -1, -1, -1, 6, -1, -1};
    root = BT.Queue(v);

    preorder pre;
    postorder pos;
    inorder in;

    pre.print(root);
    cout << endl;
    vector<int> ans;
    pre.vec(root, ans);
    print.printvector(ans);
    ans.clear();
    cout << endl;

    pos.print(root);
    cout << endl;
    pos.vec(root, ans);
    print.printvector(ans);
    ans.clear();
    cout << endl;

    in.print(root);
    cout << endl;
    in.vec(root, ans);
    print.printvector(ans);
    ans.clear();
    cout << endl;


}
