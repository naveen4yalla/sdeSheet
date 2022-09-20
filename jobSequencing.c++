#include<bits/stdc++.h>
using namespace std;
struct job{
    int id;
    int deadline;
    int profit;
};
class Solution{
public:
    bool static comparsion(job a,job b){
        return(a.profit > b.profit);
    }


pair <int,int> jobScheduling(job jobsequence[],int n){
    sort(jobsequence,jobsequence+n,comparsion);
    int maxDeadline = jobsequence[0].deadline;
    for(int i = 1;i<n;i++){
        maxDeadline = max(maxDeadline,jobsequence[i].deadline);
    }
    int slots[maxDeadline+1];
    for(int i=0;i<=maxDeadline;i++){
         slots[i] = -1;
    }
    int countJobs = 0; 
    int jobProfit = 0;
    for(int i=0;i<n;i++){
        for(int j = jobsequence[i].deadline; j>0 ;j--)
        {
            if(slots[j]==-1)
            {
                slots[j] = i;
                countJobs++;
                jobProfit = jobProfit + jobsequence[i].profit;
                break;
                
            }
        }
    }


}
};
int main()
{
    int n = 4;

   job arr[n] = {{1,4,20},{2,1,10},{3,2,40},{4,2,30}};
    Solution obj;
    pair <int,int> ans = obj.jobScheduling(arr,n);
    cout << ans.first << " " << ans.second << endl;
    return 0;
}
