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

    void iterative(BT_Node *root)
    {
        stack<BT_Node *> st;
        if (root == nullptr)
            return;
        st.push(root);
        while (!st.empty())
        {
            BT_Node *temp = st.top();
            st.pop();
            cout << temp->data << " ";
            if (temp->right)
                st.push(temp->right);
            if (temp->left)
                st.push(temp->left);
        }
    }

    vector<int> iterative_vec(BT_Node *root)
    {
        vector<int> ans;
        if (!root)
            return ans;
        stack<BT_Node *> st;
        st.push(root);
        while (!st.empty())
        {
            root = st.top();
            st.pop();
            ans.push_back(root->data);
            if (root->right)
                st.push(root->right);
            if (root->left)
                st.push(root->left);
        }
        return ans;
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

    void iterative_1(BT_Node *root){
        if(!root) return;
        stack<BT_Node *> st;
        auto curr = root;
        while(curr ||!st.empty()){
            if(curr){
                st.push(curr);
                curr = curr->left;
            }
            else{
                auto temp = st.top()->right;
                if(!temp){
                    temp=st.top();
                    st.pop();
                    cout << temp->data << " ";
                    while(!st.empty() && temp ==  st.top()->right){
                        temp = st.top();
                        st.pop();
                        cout << temp->data << " ";
                    }
                }
                else curr = temp;
            }
        }
    }

    void iterative_2(BT_Node *root)
    {
        if(!root) return;
        stack<BT_Node *> st1,st2;
        st1.push(root);
        while(!st1.empty()){
            root = st1.top();
            st1.pop();
            st2.push(root);
            if(root->left) st1.push(root->left);
            if(root->right) st1.push(root->right);
        }
        while(!st2.empty()){
            cout << st2.top()->data << " ";
            st2.pop();
        }
    }

    vector<int> iterative_vec_1(BT_Node *root){
        vector<int> ans;
        if(!root) return ans;
        stack<BT_Node *> st;
        auto curr = root;
        while(curr ||!st.empty()){
            if(curr){
                st.push(curr);
                curr = curr->left;
            }
            else{
                auto temp = st.top()->right;
                if(!temp){
                    temp=st.top();
                    st.pop();
                    ans.push_back(temp->data);
                    while(!st.empty() && temp ==  st.top()->right){
                        temp = st.top();
                        st.pop();
                        ans.push_back(temp->data);
                    }
                }
                else curr = temp;
            }
        }
        return ans;
    }

    vector<int> iterative_vec_2(BT_Node *root)
    {
        vector<int> ans;
        if (!root)
            return ans;
        stack<BT_Node *> st1,st2;
        st1.push(root);
        while(!st1.empty()){
            root = st1.top();
            st1.pop();
            st2.push(root);
            if(root->left) st1.push(root->left);
            if(root->right) st1.push(root->right);
        }
        while(!st2.empty()){
            ans.push_back(st2.top()->data);
            st2.pop();
        }
        return ans;
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

    void iterative(BT_Node *root)
    {
        if (!root)
            return;
        stack<BT_Node *> st;
        BT_Node *temp = root;
        while (true)
        {
            while (temp != nullptr)
            {
                st.push(temp);
                temp = temp->left;
            }
            if (st.empty())
                break;
            temp = st.top();
            st.pop();
            cout << temp->data << " ";
            temp = temp->right;
        }
    }

    vector<int> iterative_vec(BT_Node *root)
    {
        vector<int> ans;
        if (!root)
            return ans;
        stack<BT_Node *> st;
        BT_Node *temp = root;
        while (true)
        {
            while (temp != nullptr)
            {
                st.push(temp);
                temp = temp->left;
            }
            if (st.empty())
                break;
            temp = st.top();
            st.pop();
            ans.push_back(temp->data);
            temp = temp->right;
        }
        return ans;
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
    vector<int> ans;

    //? preorder
    {
        cout << "Recursive : ";
        pre.print(root);
        cout << endl;
        cout << "Recursive Vector : ";
        pre.vec(root, ans);
        print.printvector(ans);
        ans.clear();
        cout << "iterative : ";
        pre.iterative(root);
        cout << endl;
        cout << "iterative Vector : ";
        ans = pre.iterative_vec(root);
        print.printvector(ans);
        ans.clear();
        cout << endl;
    }

    //? postorder
    {
        cout << "Recursive : ";
        pos.print(root);
        cout << endl;
        cout << "Recursive Vector : ";
        pos.vec(root, ans);
        print.printvector(ans);
        ans.clear();
        cout << "iterative using 1 stack : ";
        pos.iterative_1(root);
        cout << endl;
        cout << "iterative using 2 stack : ";
        pos.iterative_2(root);
        cout << endl;
        cout << "iterative Vector using 1 stack : ";
        ans = pos.iterative_vec_1(root);
        print.printvector(ans);
        ans.clear();
        cout << "iterative Vector using 2 stack : ";
        ans = pos.iterative_vec_2(root);
        print.printvector(ans);
        ans.clear();
        cout << endl;
    }

    //? inorder
    {
        cout << "Recursive : ";
        in.print(root);
        cout << endl;
        cout << "Recursive Vector : ";
        in.vec(root, ans);
        print.printvector(ans);
        ans.clear();
        cout << "iterative : ";
        in.iterative(root);
        cout << endl;
        cout << "iterative Vector : ";
        ans = in.iterative_vec(root);
        print.printvector(ans);
        ans.clear();
        cout << endl;
    }
}
