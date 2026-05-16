func threeSum(nums []int) [][]int {
    // SORT --> FIX --> 2Sum --> DEDUPE
    sort.Ints(nums)
    n := len(nums)
    res := [][]int{}
    for i := 0; i < n - 2; i++{
        if i > 0 && nums[i] == nums[i - 1] {
            continue
        }
        target := -nums[i]
        l, r := i + 1, n - 1
        for l < r {
            total := nums[l] + nums[r]
            if total < target {
                l++
            } else if total > target {
                r--
            } else {
                res = append(res, []int{nums[i], nums[l], nums[r]})
                l++
                r--
                for l < r && nums[l] == nums[l - 1] {
                    l++
                }
            }
        }
    }
    return res
}
