class Solution {
    public boolean isPalindrome(String s) {
        String strNoSpace = s.replaceAll("[^a-zA-Z0-9]", "");
        String backwardsStr = "";
        for (int i = strNoSpace.length() - 1; i >= 0; --i){
            backwardsStr += strNoSpace.charAt(i);
        }
        System.out.print(backwardsStr);
        if(backwardsStr.equalsIgnoreCase(strNoSpace)){
            return true;
        }
        return false;
    }
}
