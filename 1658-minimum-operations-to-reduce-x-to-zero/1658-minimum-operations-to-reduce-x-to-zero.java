class Solution {
    public int minOperations(int[] nums, int x) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int target = totalSum - x;
        if (target < 0) {
            return -1; 
        }
        if (target == 0) {
            return nums.length; 
        }
        int n=nums.length;
        int left = 0;
        int right = 0;
        int currentSum = 0;
        int minOperations = Integer.MAX_VALUE;

        while (right < nums.length) {
            currentSum += nums[right];
            right++;

            while (currentSum > target) {
                currentSum -= nums[left];
                left++;
            }

            if (currentSum == target) {
                minOperations = Math.min(minOperations,n-( right - left));
            }
        }

        return minOperations != Integer.MAX_VALUE ? minOperations : -1;
    }
}