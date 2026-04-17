class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0) return false;

        Stack<Character> openCharStack = new Stack<Character>();
        Stack<Character> closedCharStack = new Stack<Character>();

        // Stack<Character> closedChars = new Stack<Character>();
        /**
        **(){}[]
            open (, {, [,
            closed ), }, ]
            ([{[]}])
            open ([{[
            closed )]}]
        */
        if(s.charAt(0) == '}' || s.charAt(0) == ')' || s.charAt(0) == ']') return false;
        for(char c : s.toCharArray()){
            if(c == '(' || c == '{' || c == '[' ){
                openCharStack.push(c);
            }
            else if(openCharStack.isEmpty()) return false;
            else{
                closedCharStack.push(c);

                if(openCharStack.peek() == '(' && c  != ')'){

                    return false;
                } 
                if(openCharStack.peek() == '{' && c  != '}'){
                    return false;
                } 
                if(openCharStack.peek() == '[' && c  != ']'){
                    return false;
                }
                openCharStack.pop();
            }
        }
        if(closedCharStack.isEmpty()){
            return false;
        }
        return openCharStack.isEmpty();
    }
}
