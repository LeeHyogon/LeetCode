class Pair {
    int val;
    int idx;
    Pair(int v, int i) {
        val = v;
        idx = i;
    }
}
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Pair[] arr = new Pair[nums.length];
        for (int i = 0; i < nums.length; i++) {
            arr[i] = new Pair(nums[i], i);
        }

        Arrays.sort(arr, (a, b) -> Integer.compare(a.val, b.val));

        int start = 0;
        int end = nums.length-1;


        while (start < end) {
            int sum = arr[end].val + arr[start].val;

            if (sum == target) {
                return new int[]{arr[start].idx, arr[end].idx};
            }
            else if (sum > target) {
                end-=1;
            }
            else {
                start+=1;
            }
        }
        return new int[]{arr[start].idx, arr[end].idx};
    }
}