//? this file contain basic tree opetations

#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <algorithm>

using namespace std;

class BT_Node
{
public:
    int data;
    BT_Node *left, *right;
    BT_Node(int data)
    {
        this->data = data;
        this->left = nullptr;
        this->right = nullptr;
    }
};

// todo: print out the tree structure
class print_Tree
{
public:
    void printBinaryTreeWithArrows(BT_Node *root, int space = 0, int height = 10)
    {
        if (root == NULL)
            return;

        space += height;

        printBinaryTreeWithArrows(root->right, space);
        cout << endl;

        for (int i = height; i < space; i++)
            cout << " ";

        cout << root->data;

        if (root->left != nullptr || root->right != nullptr)
        {
            if (root->left != nullptr)
                cout << " <-";
            if (root->right != nullptr)
                cout << " ->";
        }

        cout << "\n";

        printBinaryTreeWithArrows(root->left, space);
    }

    void printBinaryTreeHorizontally(BT_Node *root, int space = 0, int height = 10)
    {
        if (root == NULL)
            return;
        space += height;
        printBinaryTreeHorizontally(root->right, space);
        cout << endl;
        for (int i = height; i < space; i++)
            cout << " ";
        cout << root->data << "\n";
        printBinaryTreeHorizontally(root->left, space);
    }

    void printTree(BT_Node *root)
    {
        if (!root)
        {
            return;
        }
        printTree(root->left);
        cout << root->data << " ";

        printTree(root->right);
    }

    void printLevelOrder(BT_Node *root)
    {
        if (!root)
            return;

        queue<BT_Node *> q;
        q.push(root);

        while (!q.empty())
        {
            BT_Node *node = q.front();
            q.pop();

            if (node)
            {
                std::cout << node->data << " ";
                q.push(node->left);
                q.push(node->right);
            }
            else
            {
                std::cout << "null ";
            }
        }
    }
    void printvector(vector<int> v)
    {
        for (int i = 0; i < v.size(); i++)
        {
            cout << v[i] << " ";
        }
        cout << endl;
    }
    void print2dvector(vector<vector<int>> v){
        for(auto &v1 : v){
            for(auto &i : v1){
                cout << i << " ";
            }
            cout << "\n";
        }
    }


};

// todo: create binary representation
class to_BT
{
public:
    BT_Node *Queue(vector<int> &v)
    {
        if (v.empty())
            return nullptr;
        queue<BT_Node *> q;
        BT_Node *root = new BT_Node(v[0]);
        q.push(root);
        int i = 1;
        while (i < v.size())
        {
            BT_Node *temp = q.front();
            q.pop();
            if (i < v.size() && v[i] != -1)
            {
                temp->left = new BT_Node(v[i]);
                q.push(temp->left);
            }
            i++;
            if (i < v.size() && v[i] != -1)
            {
                temp->right = new BT_Node(v[i]);
                q.push(temp->right);
            }
            i++;
        }
        return root;
    }

    BT_Node *List(vector<int> &v)
    {
        if (v.empty())
            return nullptr;

        list<BT_Node *> ls;
        BT_Node *root = new BT_Node(v[0]);
        ls.push_back(root);
        int i = 1;
        while (i < v.size())
        {
            BT_Node *temp = ls.front();
            ls.pop_front();

            if (i < v.size())
            {
                temp->left = new BT_Node(v[i++]);
                ls.push_back(temp->left);
            }
            if (i < v.size())
            {
                temp->right = new BT_Node(v[i++]);
                ls.push_back(temp->right);
            }
        }
        return root;
    }
};

// todo: DFS traversal for tree
class DFS
{
public:
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

        void iterative_1(BT_Node *root)
        {
            if (!root)
                return;
            stack<BT_Node *> st;
            auto curr = root;
            while (curr || !st.empty())
            {
                if (curr)
                {
                    st.push(curr);
                    curr = curr->left;
                }
                else
                {
                    auto temp = st.top()->right;
                    if (!temp)
                    {
                        temp = st.top();
                        st.pop();
                        cout << temp->data << " ";
                        while (!st.empty() && temp == st.top()->right)
                        {
                            temp = st.top();
                            st.pop();
                            cout << temp->data << " ";
                        }
                    }
                    else
                        curr = temp;
                }
            }
        }

        void iterative_2(BT_Node *root)
        {
            if (!root)
                return;
            stack<BT_Node *> st1, st2;
            st1.push(root);
            while (!st1.empty())
            {
                root = st1.top();
                st1.pop();
                st2.push(root);
                if (root->left)
                    st1.push(root->left);
                if (root->right)
                    st1.push(root->right);
            }
            while (!st2.empty())
            {
                cout << st2.top()->data << " ";
                st2.pop();
            }
        }

        vector<int> iterative_vec_1(BT_Node *root)
        {
            vector<int> ans;
            if (!root)
                return ans;
            stack<BT_Node *> st;
            auto curr = root;
            while (curr || !st.empty())
            {
                if (curr)
                {
                    st.push(curr);
                    curr = curr->left;
                }
                else
                {
                    auto temp = st.top()->right;
                    if (!temp)
                    {
                        temp = st.top();
                        st.pop();
                        ans.push_back(temp->data);
                        while (!st.empty() && temp == st.top()->right)
                        {
                            temp = st.top();
                            st.pop();
                            ans.push_back(temp->data);
                        }
                    }
                    else
                        curr = temp;
                }
            }
            return ans;
        }

        vector<int> iterative_vec_2(BT_Node *root)
        {
            vector<int> ans;
            if (!root)
                return ans;
            stack<BT_Node *> st1, st2;
            st1.push(root);
            while (!st1.empty())
            {
                root = st1.top();
                st1.pop();
                st2.push(root);
                if (root->left)
                    st1.push(root->left);
                if (root->right)
                    st1.push(root->right);
            }
            while (!st2.empty())
            {
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
};

// todo: BFS traversal
class BFS
{
public:
    vector<vector<int>> vec(BT_Node *root)
    {
        vector<vector<int>> result;
        queue<BT_Node *> q;
        if (root == NULL)
            return result;
        q.push(root);
        while (!q.empty())
        {
            int size = q.size();
            vector<int> level;
            while (size--)
            {
                BT_Node *temp = q.front();
                q.pop();
                if (temp->left)
                    q.push(temp->left);
                if (temp->right)
                    q.push(temp->right);
                level.push_back(temp->data);
            }
            result.push_back(level);
        }
        return result;
    }
};