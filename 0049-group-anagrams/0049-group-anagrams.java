import java.util.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> dicti = new HashMap<>();
        for(int i=0;i<strs.length;i++){
            String temp=strs[i];
            char[] charArray = temp.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            
            if (dicti.containsKey(sortedStr)){
                dicti.get(sortedStr).add(strs[i]);
            }
            else{
                dicti.put(sortedStr, new ArrayList<>());
                dicti.get(sortedStr).add(strs[i]);
            }
        }
        Collection<List<String>> values = dicti.values();
        List<List<String>> ans = new ArrayList<>();
        for (List<String> value : values) {
            ans.add(value);
        }
        return ans;
    }
}