func topKFrequent(nums []int, k int) []int {
    counts := make(map[int]int)
    freqs := make([][]int, len(nums) + 1)

    for _, num := range nums {
        counts[num] ++
    }

    for k := range counts {
        freqs[counts[k]] = append(freqs[counts[k]], k)
    }

    results := []int{}
    for i := len(nums); i > 0; i-- {
        for _, n := range freqs[i] {
            results = append(results, n)
            if len(results) == k {
                return results
            }
        }
    }
    return results
}
