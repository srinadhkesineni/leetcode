class Solution {
    public int[] twoSum(int[] k, int target) {
        int l=0;
        int r=k.length-1;
        while(l<r)
        {
          int curSum=k[l]+k[r];
            if(curSum>target)
            {
                r--;
            }
            else if(curSum<target)
            {  
                l++;
            }
            else
            {
                return new int[]{l+1,r+1};
                }
    }
                    return new int[]{};
}
}