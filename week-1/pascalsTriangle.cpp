#include<bits/stdc++.h>
#include<vector>
using namespace std;

vector < vector < int > > generate(int numOfRows){
     vector < vector < int > > s(numOfRows);
     for(int i =0 ;i<numOfRows;i++){
        s[i].resize(i+1);
        s[i][0] = s[i][i] = 1;

        for(int j =1;j<i;j++){

            s[i][j] = s[i-1][j-1] + s[i-1][j];
        }
     }
return s;
}
int  main()
{    
    vector < vector < int > > result  = generate(5);
   for (unsigned int i = 0; i < result.size(); ++i)
{
    for (unsigned int j = 0; j < result[i].size(); ++j)
    {
        cout << result[i][j];
    }
    cout << std::endl;
}
    return 0;
}