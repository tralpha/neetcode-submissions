type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    res := ""
    for _, str := range strs {
        res = res + strconv.Itoa(len(str)) + "#" + str
    }
    return res
}

func (s *Solution) Decode(encoded string) []string {
    i, j := 0, 0
    res := []string{}
    for i < len(encoded) {
        for encoded[j] != '#' {
            j++
        }
        length, _ := strconv.Atoi(encoded[i:j])
        i = j + 1
        j = i + length
        str := encoded[i:j]
        res = append(res, str)
        i = j
    }
    return res
}
