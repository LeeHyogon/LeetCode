class Solution {
    public int missingNumber(int[] nums) {
        int N = nums.length;
        int total = (N*(N+1))/2 ;
        int total2 = 0;
        
        for (int i = 0; i< N; i++) {
            total2 += nums[i];
        }
        return total-total2;

    }
}