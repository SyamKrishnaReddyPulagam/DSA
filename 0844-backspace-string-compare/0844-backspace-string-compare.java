class Solution {
    public boolean backspaceCompare(String s, String t) {
        String s1 = "";
        for (char i : s.toCharArray()) {
            if (Character.isLetter(i)) {
                s1 += i;
            } else {
                if (!s1.isEmpty()) {
                    s1 = s1.substring(0, s1.length() - 1);
                }
            }
        }

        String t1 = "";
        for (char i : t.toCharArray()) {
            if (Character.isLetter(i)) {
                t1 += i;
            } else {
                if (!t1.isEmpty()) {
                    t1 = t1.substring(0, t1.length() - 1);
                }
            }
        }

        return s1.equals(t1);
    }
}