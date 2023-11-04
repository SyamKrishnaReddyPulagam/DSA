class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        if (right.length != 0 && left.length != 0) {
            int a1 = Integer.MIN_VALUE;
            for (int i : left) {
                a1 = Math.max(a1, i);
            }
            
            int a2 = Integer.MAX_VALUE;
            for (int i : right) {
                a2 = Math.min(a2, i);
            }
            
            return Math.max(n - a2, a1);
        } else if (right.length == 0) {
            int a1 = Integer.MIN_VALUE;
            for (int i : left) {
                a1 = Math.max(a1, i);
            }
            return a1;
        } else {
            int a2 = Integer.MAX_VALUE;
            for (int i : right) {
                a2 = Math.min(a2, i);
            }
            return n - a2;
        }
    }
}