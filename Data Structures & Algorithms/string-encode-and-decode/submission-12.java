class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String s : strs) {
            res.append(s.length()).append('#').append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        // return null if str is empty 
        //first character will be a number
        // read the string up to the number
        // store the read string in the list
        // then read next number
        // stop at the end of the string
        // return the list


        List<String> res = new ArrayList<>();
        int strLength = 0;
        int i = 0;
        int j = 0;

        while(i < str.length()) {
            
            while(str.charAt(j) != '#'){
                ++j;
            }
            strLength = Integer.parseInt(str.substring(i,j));
            ++j;

            int count = 0;
            String resStr = "";
            while(count < strLength) {
                resStr += str.charAt(j);
                ++count;
                ++j;
            }
            res.add(resStr);
            i = j;
        }

        return res;
    }
}
