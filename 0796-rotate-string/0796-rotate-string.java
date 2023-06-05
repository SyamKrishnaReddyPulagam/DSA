class Solution {
    public boolean rotateString(String s, String goal) {
        if(s.length()!=goal.length()){
            return false;
        }
        if(s.equals(goal)){
            return true;
        }
        for(int i=1;i<s.length();i++){
            String ts = (s.substring(i)+s.substring(0,i));
            if(ts.equals(goal)){
                return true;
            }
        }
        return false;
    }
}