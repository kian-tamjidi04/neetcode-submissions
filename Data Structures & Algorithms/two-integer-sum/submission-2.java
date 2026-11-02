class Solution {
    public int[] twoSum(int[] nums, int target) {
        boolean flag = false;
        int[] returnList = new int[2];
        for (int i=0; i<nums.length-1; i++) {
            if (flag == true) {
                break;
            }
            for (int j=i+1; j<nums.length; j++) {
                if (flag == true) {
                    break;
                }
                if (nums[i] + nums[j] == target) {
                    returnList[0] = i;
                    returnList[1] = j;
                    flag = true;
                } else {
                    continue;
                }
            }
        }
        return returnList;
    }
}
