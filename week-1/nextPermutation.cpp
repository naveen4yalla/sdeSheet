/* #include <algorithm>
#include<iostream>
//#include<bits/stdc++.h>
#include<vector>
using namespace std;

int main()
{  
    int arr[] = {1,3,2};
    next_permutation(arr,arr+3);
    for(int i=0;i<3;i++){
        cout<<arr[i];
    }
    return 0;

}
 */
#include<vector>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void nextPermutationInTheSeries(vector<int>& nums){
    int n = nums.size();
    int i,l;
    for( i = n-2 ; i>=0 ;i--)
    {
         if(nums[i]<nums[i+1])
         {
             break;         
         }
    }
    if(i<0){
        reverse(nums.begin(),nums.end());

    }
    else
    {
        for(l = n-1 ; l>i; l--)
        {
            if(nums[l]>nums[i])
            {
                break;
            }

        }
        swap(nums[i],nums[l]);
        reverse(nums.begin()+i+1,nums.end());
    }
    for (int m =0;m<nums.size(); m++)
    {
        cout << nums[m];
    }


}
int main()
{
    vector <int> arr {1,2,3};
    
   nextPermutationInTheSeries(arr); 
   return 0;
}