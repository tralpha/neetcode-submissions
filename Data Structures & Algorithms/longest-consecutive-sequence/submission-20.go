func longestConsecutive(nums []int) int {
    numSet := make(map[int]bool)
    longest := 0
    for _, n := range nums {
        numSet[n] = true
    }
    for n := range numSet {
        if numSet[(n - 1)] == false {
            length := 1
            for numSet[(n + length)] {
                length++
            }
            longest = max(longest, length)
        }
    }
    return longest
}
