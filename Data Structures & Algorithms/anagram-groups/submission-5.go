func groupAnagrams(strs []string) [][]string {
    hmap := make(map[[26]int][]string)

    for _, s := range strs {
        s_key := [26]int{}
        for _, c := range s {
            s_key[c - 'a'] += 1
        }
        hmap[s_key] = append(hmap[s_key], s)
    }
    values := [][]string{}
    for _, v := range hmap{
        values = append(values, v)
    }

    return values

}
