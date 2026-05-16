func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int) // diff --> idx
    for i := 0; i < len(nums); i++ {
        diff := target - nums[i]
        if idx, exists := hmap[diff]; exists {
            return []int{idx, i}
        }
        hmap[nums[i]] = i
    }
    return []int{}
}
