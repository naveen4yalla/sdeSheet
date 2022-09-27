def mergeTwoSortedLists(self,arr1,arr2):
        lenArr1 = len(arr1)
        lenArr2 = len(arr2)
        self.status = False
        for f in range(0,len(arr1)):
            #COMPARE WITH THE FIRST ELEEMNT in the Array2 
            if arr2[0]<=arr1[f]:
                arr1[f],arr2[0] = arr2[0],arr1[f]
                self.status = True
            temp = 1
            #Sort the second array when change happens 
            while temp<lenArr2 and self.status:
                if arr2[temp-1] > arr2[temp]:
                    arr2[temp-1],arr2[temp] = arr2[temp] , arr2[temp-1]
                    temp = temp+1
                else:
                    self.status = False
                    break
