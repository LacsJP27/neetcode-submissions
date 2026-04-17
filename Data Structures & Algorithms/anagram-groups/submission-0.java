class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for(String str : strs) {
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sortedStr = new String(charArr);
            result.putIfAbsent(sortedStr, new ArrayList<>());
            result.get(sortedStr).add(str);
        }

        return new ArrayList<>(result.values());
    }
}
