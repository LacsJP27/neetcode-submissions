class Solution {
    public boolean isValidSudoku(char[][] board) {
       Map<Integer, HashSet<Character>> rows = new HashMap<>();
       Map<Integer, HashSet<Character>> cols = new HashMap<>();
       Map<String, HashSet<Character>> squares = new HashMap<>();

       for(int r = 0; r < board.length; ++r) {
        for(int c = 0; c < board[r].length; ++c) {
            if(board[r][c] == '.') continue;
            if(rows.computeIfAbsent(r, k -> new HashSet<>()).contains(board[r][c]) ||
                cols.computeIfAbsent(c, k -> new HashSet<>()).contains(board[r][c]) ||
                squares.computeIfAbsent((r/3) + "," + (c/3), k -> new HashSet<>())
                .contains(board[r][c])){
                    return false;
            }

            rows.get(r).add(board[r][c]);
            cols.get(c).add(board[r][c]);
            squares.get((r/3) + "," + (c/3)).add(board[r][c]);
        }
       }

       return true;
    }
}
