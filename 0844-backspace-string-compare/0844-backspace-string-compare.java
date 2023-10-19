class Solution {
    public static boolean backspace(String s, String t) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '#' && !stack.isEmpty()) {
                stack.pop();
            } else if (Character.isLetter(c)) {
                stack.push(c);
            }
        }

        Stack<Character> stack1 = new Stack<>();
        for (char c : t.toCharArray()) {
            if (c == '#' && !stack1.isEmpty()) {
                stack1.pop();
            } else if (Character.isLetter(c)) {
                stack1.push(c);
            }
        }

        StringBuilder sbStack = new StringBuilder();
        while (!stack.isEmpty()) {
            sbStack.insert(0, stack.pop());
        }

        StringBuilder sbStack1 = new StringBuilder();
        while (!stack1.isEmpty()) {
            sbStack1.insert(0, stack1.pop());
        }

        return sbStack.toString().equals(sbStack1.toString());
    }
    public boolean backspaceCompare(String s, String t) {
        return backspace(s, t);
    }
}