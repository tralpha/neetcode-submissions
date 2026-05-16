func maxSubArray(nums []int) int {
    maxSub, curr := nums[0], 0
    for _, num := range nums {
        if curr < 0 {
            curr = 0
        }
        curr += num
        maxSub = max(maxSub, curr)
    }
    return maxSub
}
