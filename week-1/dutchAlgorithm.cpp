#include<vector>
#include<iostream>
using namespace std;
void dutchAlgorithm(vector <int> &arr){
    int low,mid = 0;
    int high = nums.size() -1;
    while(high>=mid){
        switch(nums[mid]){
            case 0:
                 swap(nums[low++],nums[mid++]);
                  break;
            case 1:
                  mid++;
                  break;
            case 2:
                  swap(nums[mid],nums[high--]);
                  break;
        }
    }
}
int main(){
    vector<int> arr;
    arr = {2,0,2,1,1,0}; 

dutchAlgorithm(arr);
for(auto itr : arr)
    cout << itr << "\n";
}