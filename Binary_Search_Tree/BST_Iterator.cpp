#include "main.h"
#include <stack>

using namespace std;

class BSTIterator
{
private:
   stack<TreeNode *> st;

   void pushALL(TreeNode *node)
   {
      while (node != NULL)
      {
         st.push(node);
         node = node->left;
      }
   }

public:
   BSTIterator(TreeNode *root)
   {
      pushALL(root);
   }

   int next()
   {
      TreeNode *node = st.top();
      st.pop();
      pushALL(node->right);
      return node->val;
   }

   bool hasNext()
   {
      return !st.empty();
   }
};

int main()
{
   vector<int> v{7, 3, 15, 9, 20};
   TreeNode *root = vectorToBST(v);

   BSTIterator iterator(root);
   cout << iterator.next() << endl;
}
