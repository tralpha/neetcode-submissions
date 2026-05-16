func groupAnagrams(strs []string) [][]string {
    hmap := make(map[[26]int][]string)
    for _, s := range strs {
        count := [26]int{}
        for _, c := range s {
            count[c - 'a']++
        }
        hmap[count] = append(hmap[count], s)
    }
    res := [][]string{}
    for _, anagrams := range hmap {
        res = append(res, anagrams)
    }
    return res
}
