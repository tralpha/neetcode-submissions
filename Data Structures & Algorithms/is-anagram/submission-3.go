func isAnagram(s string, t string) bool {
    countS := [26]int{}
    countT := [26]int{}
    for _, c := range s {
        countS[c - 'a'] += 1
    }
    for _, c := range t {
        countT[c - 'a'] += 1
    }
    return countS == countT
}
