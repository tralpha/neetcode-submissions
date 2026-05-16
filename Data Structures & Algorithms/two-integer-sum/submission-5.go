func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int)

    for i, n := range nums {
        diff := target - n

        if idx, ok := hmap[diff]; ok {
            return []int{idx, i}
        }

        hmap[n] = i
        
    }
    return []int{}
}
