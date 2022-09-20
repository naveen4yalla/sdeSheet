def nMeetingsInOneRoom(n,start,end):
    meetingStack = []
    if n == 0:
        return []
    if n == 1:
        return [1]
    for i in range(n):
        temp = [i+1,start[i],end[i]]
       # temp.append(i+1)
       # temp.append(start[i])
       # temp.append(end[i])
        meetingStack.append(temp)
    meetingStack.sort(key=lambda x:x[2])
    print(meetingStack)
    ans= [ ]
    ans.append(meetingStack[0][0])
    temp = meetingStack[0][2]
    meetingStack.pop(0)
    for i in meetingStack:
        if temp<i[1]:
            ans.append(i[0])
            temp = i[2]
    return ans

            
            
print(nMeetingsInOneRoom(6,[1,3,0,5,8,5],[2,4,5,7,9,9]))