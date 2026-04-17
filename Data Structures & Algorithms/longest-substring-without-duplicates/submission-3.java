class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int r = 1;
        int count = 1;
        int maxLen = 1;
        Set<Character> charSet = new HashSet<>();
        if(s.length() == 0) return 0;
        if(s.length() == 1) return 1;
        while(r < s.length()) {
            if(s.charAt(l) == s.charAt(r) || charSet.contains(s.charAt(r))) {
                ++l;
                r = l + 1;
                charSet.clear();
            } else {
                count = r - l + 1;
                maxLen = Math.max(count, maxLen);
                charSet.add(s.charAt(r));
                ++r;
            }
        }
        return maxLen;
    }
}
