//Leetcode 344. Reverse String
#include<bits/stdc++.h>
#include<vector>
using namespace std;
class Solution {
public:
    void rev(vector<char>& s, int left, int right)
    {
        if(left>=right)                             
            return;
        swap(s[left++],s[right--]);                         
        rev(s,left,right);
    }
    void reverseString(vector<char>& s) {
        rev(s,0,s.size()-1);
    }
};