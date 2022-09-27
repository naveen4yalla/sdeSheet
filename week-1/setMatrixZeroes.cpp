#include<bits/stdc++.h>
#include<vector>
using namespace std;
void setZeros(vector < vector< int> > &arr){
     int rows = arr.size();
     int cols = arr[0].size();
     for(int i =0;i<rows;i++)
     {
        for(int j=0 ;j<cols;j++){
            if(arr[i][j]==0){
                //check for left side of the row
                int index = i-1;
                while(index>=0){
                    if(arr[index][j]!=0){
                        arr[index][j] = -1;
                    }
                    index--;
                }
                index = i+1;
                while(index<rows){
                    if(arr[index][j]!=0){
                        arr[index][j] = -1;
                    }
                    index++;
                }
                index = j-1;
                while(index>=0){
                    if(arr[i][index]!=0){
                        arr[i][index] = -1;
                    }
                    index--;
                }
                index = j+1;
                 while(index<cols){
                    if(arr[i][index]!=0){
                        arr[i][index] = -1;
                    }
                    index++;
                }


            }
        }
     }

    for(int i =0;i<rows;i++){
        for(int j=0;j<cols;j++){
            if(arr[i][j]<=0){
                arr[i][j] = 0;
            }
        }
    }
}

void setZeros1(vector < vector <int> > &arr)
{
    bool colo0 = true;
    int rows = arr.size();
    int cols= arr[0].size();
    for(int i = 0; i<rows; i++){
        if(arr[i][0] == 0){
            colo0 = false;
        }
        for (int j = 1; j<cols ; j++){
           if(arr[i][j] == 0){
            arr[i][0] = 0;
            arr[0][j] = 0;
           }
        }
    }
    for(int i =rows-1 ; i>=0 ;i--){
        for(int j = cols-1;j>=1; j--){
            if(arr[i][0] == 0 || arr[0][j] == 0){
                arr[i][j] = 0;
            }
        }
        if (colo0 == false){
            arr[i][0] = 0;
        }
    }
}




int main()
{
   // vector < vector <int>> arr {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
    vector <vector<int>> arr;
    arr = {{1,1,1,1}, {1,0,1,1}, {1, 1, 0,1},{0,0,0,1}}; 
   // setZeros(arr);
     setZeros1(arr);
    cout<<"The final Matrix is "<<endl;
    for(int i = 0; i<arr.size(); i++){
        for(int j = 0 ; j<arr[0].size();j++)
        {
            cout<<arr[i][j];
        }
        cout<<"\n";
    }
    return 0;
}