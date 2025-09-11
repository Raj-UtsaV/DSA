#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class StockSpannerbrute
{
    vector<int> prices;

public:
    //! Function to calculate the number of consecutive days with a price less than or equal to the current price
    int next(int price)
    {
        prices.push_back(price); //! Add the current price to the list of prices
        int count = 1;           //! Initialize count to 1 (includes the current day)

        //! Traverse the list of prices in reverse order (excluding the current day)
        for (int i = prices.size() - 2; i >= 0 && prices[i] <= price; i--)
        {
            count++; //! Increment the count for each day with a price less than or equal to the current price
        }

        return count; //! Return the total count
    }
};

class StockSpanneroptimal
{
    int index = 1;

public:
    stack<pair<int, int>> st;  //!store price and index of the current price
    
    int next(int price)
    {
        //! Remove elements from the stack while the stack is not empty and the top element's price is less than or equal to the current price
        while (!st.empty() && st.top().first <= price)
        {
            st.pop();
        }

        //! Calculate the number of days
        //! If the stack is empty, set x to the current index
        //! Otherwise, set x to the difference between the current index and the index of the top element on the stack
        int x = (st.empty()) ? index : index - st.top().second;

        //! Push the current price and index onto the stack
        st.push({price, index});

        //! Increment the index for the next call
        index++;

        //! Return the calculated number of days
        return x;
    }
};
int main()
{
    vector<int> v = {100, 80, 60, 70, 60, 75, 80};
    StockSpannerbrute stockSpannerbrute;
    for (int price : v)
    {
        cout << stockSpannerbrute.next(price) << " ";
    }
    cout << endl;
    StockSpanneroptimal stockSpanneroptimal;
    for (int price : v)
    {
        cout << stockSpanneroptimal.next(price) << " ";
    }
    return 0;
}