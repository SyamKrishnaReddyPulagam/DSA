class Solution {
    public boolean checkRecord(String s) {
        if(s.contains("LLL")){
            return false;
        }	
        int x=s.length();
        s = s.replaceAll("A", "");
        if ((x- s.length()) > 1)
        {
            return false;
        }
    	return true;
    }
}