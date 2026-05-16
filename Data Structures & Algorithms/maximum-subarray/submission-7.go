func maxSubArray(nums []int) int {
    currSum, maxSub := 0, nums[0]
    for _, num := range nums {
        currSum = max(num, currSum + num)
        maxSub = max(currSum, maxSub)
    }
    return maxSub
}
