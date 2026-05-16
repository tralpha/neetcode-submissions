func groupAnagrams(strs []string) [][]string {
    hmap := make(map[[26]int][]string)

    for _, s := range strs {
        var count [26]int
        for _, c := range s {
            count[c-'a']++
        }
        hmap[count] = append(hmap[count], s)
    }
    var groups [][]string
    for _, group := range hmap {
        groups = append(groups, group)
    }
    return groups
}
