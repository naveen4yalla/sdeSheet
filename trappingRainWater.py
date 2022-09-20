def trappingRainWater(heights):
    for f in range(0,len(heights)):
      leftmax , heightmax,waterTrapped= 0 , 0,0
      while(leftmax>=0):
          leftmax = max(leftmax,heights[f])
      while(rightmax<len(heights)):
          rightmax = max(rightmax,heights[f])
      waterTrapped = min(leftmax,rightmax) - heights[f]
    return waterTrapped

def trappingRainWater(heights):
    n = len(heights)
    prefix[n]
    suffix[n]
    waterTrapped = 0 
    prefix[0] = heights[0]
    for f in range(1,n):
        prefix[f] = max(heights[f],prefix[f-1])
    suffix[n] = heights[n-1]
    for f in range(n-2,-1,-1):
        suffix[f] = max(heights[f],suffix[f+1])
    for f in range(0,n):
        waterTrapped = min(suffix[f],prefix[f]) - heights[f]
    return waterTrapped
    
