func topKFrequent(nums []int, k int) []int {
    n := len(nums)
    freqs := make(map[int]int)
    buckets := make([][]int, n+1)
    for _, num := range nums {
        freqs[num]++
    }
    for num, freq := range freqs {
        buckets[freq] = append(buckets[freq], num)
    }
    res := []int{}
    for i := n; i > 0; i-- {
        for _, num := range buckets[i] {
            res = append(res, num)
            if len(res) == k {
                return res
            }
        }
    }
    return res
}
