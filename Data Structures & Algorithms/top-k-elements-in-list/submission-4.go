func topKFrequent(nums []int, k int) []int {
    counts := make(map[int]int)
    freqs := make([][]int, len(nums) + 1)

    for _, n := range nums {
        counts[n] ++
    }

    for k := range counts {
        freqs[counts[k]] = append(freqs[counts[k]], k)
    }

    var results = []int{}
    for i := len(nums); i >= 1; i-- {
        for _, num := range freqs[i] {
            results = append(results, num)
            if len(results) == k {
                return results
            }
        }
    }
    return results
}
