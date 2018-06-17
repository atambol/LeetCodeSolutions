func groupAnagrams(strs []string) [][]string {
    l := len(strs)
    var result = make(map[string][]string)
    
    for i:=0; i<l; i++ {
        str := strings.Split(strs[i], "")
        sort.Strings(str)
        key := strings.Join(str, "")
        result[key] = append(result[key], strs[i])
    }
    
    var groups [][]string
    for _,v := range(result) {
        groups = append(groups, v)
    }
    return groups
}
