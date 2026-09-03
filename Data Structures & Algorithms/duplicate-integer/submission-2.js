class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hs = new Set(nums);
        if (nums.length !== hs.size) {
            return true;
        }
        return false;
    }
}
