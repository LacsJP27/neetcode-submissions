class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            // adding a and b without carry
            a = a ^ b;
            System.out.println(a);
            b = carry;
            //4 and 7
            // 0100 ^ 0111 = 0011

        }
        return a;
    }
}
