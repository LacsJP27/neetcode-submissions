class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> smap = new HashMap<>();
        Map<Character, Integer> tmap = new HashMap<>();

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        for(char letter : sArr){
            smap.put(letter, smap.getOrDefault(letter, 0) + 1);
        }
        for(char letter : tArr){
            tmap.put(letter, tmap.getOrDefault(letter, 0) + 1);
        }

        // for(char letter : smap.keySet()){
        //     if(tmap.size() != smap.size() || tmap.get(letter) != smap.get(letter)){
        //         return false;
        //     }
        // }

        if(sArr.length != tArr.length){
            return false;
        }
        return smap.equals(tmap);
    }
}
