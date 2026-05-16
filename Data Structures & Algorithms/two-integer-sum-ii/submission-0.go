func twoSum(numbers []int, target int) []int {
    n := len(numbers)
    l, r := 0, n - 1
    res := []int{}
    for l < r {
        total := numbers[l] + numbers[r]
        if total < target {
            l++
        } else if total > target {
            r--
        } else {
            res = append(res, l + 1)
            res = append(res, r + 1)
            l++
            r--
        }
    }
    return res
}
