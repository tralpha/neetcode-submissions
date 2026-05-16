func maxSubArray(nums []int) int {
    res, curSum := nums[0], 0
    for _, num := range nums {
        curSum = max(num, curSum+num)
        res = max(curSum, res)
    }
    return res
}
