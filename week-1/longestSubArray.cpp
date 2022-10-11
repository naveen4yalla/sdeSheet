#include<iostream>
#include<vector>
using namespace std;
int longestSubArray(vector <int>& arr){
    int maxSizeSofar = -99999;
    int maxEnding = 0;
    int start = 0;
    int end = 0;
    int s = 0;
    for(int i =0; i<=arr.size(); i++)
    {
        maxEnding = maxEnding + arr[i];
        if(maxEnding>maxSizeSofar){
            start = i;
            end  = i;
            maxSizeSofar = maxEnding;
        }
        if (maxSizeSofar<0)
        {
            maxEnding = 0;
            s = i + 1;
        }
    }
    return maxSizeSofar;

}
int main()
{
    vector <int> arr;
    arr = {-2,1,-3,4,-1,2,1,-5,4};
    cout<<longestSubArray(arr);
    return 0;
}