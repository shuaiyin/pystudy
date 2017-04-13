package Topic;

import java.util.HashMap;

public class HashTableTopic {

	
	
	
	
	/*
	 * leetcode 299. Bulls and Cows   0413  beats 14.7%
	 * 浪费空间的做法
	 */
    public String getHintBad(String secret, String guess) {
    	int bullCnt = 0,allCnt = 0;
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        for(int i=0;i<secret.length();i++){
        	if(secret.charAt(i) == guess.charAt(i)) bullCnt++;
        	char schar = secret.charAt(i);
        	if(!hm.containsKey(schar)) hm.put(schar,1);
        	else hm.put(schar,hm.get(schar) + 1);
        }
        for(int i=0;i<guess.length();i++){
        	char gchar = guess.charAt(i);
        	if(hm.containsKey(gchar) && hm.get(gchar) > 0){
        		hm.put(gchar,hm.get(gchar)-1);
        		allCnt++;
        	}
        }
        int cowCnt = allCnt - bullCnt;
        StringBuffer sb = new StringBuffer();
        sb.append(bullCnt);
        sb.append('A');
        sb.append(cowCnt);
        sb.append('B');
        return sb.toString();
    }
    
    /**
     * 使用数组这种简易hashtable来代替HashMap
     */
    public String getHintGood(String secret, String guess){
    	int[] hashTab = new int[10];
    	int bullCnt=0,allCnt=0,cowCnt;
    	for(int i=0;i<secret.length();i++){
    		char schar = secret.charAt(i);
    		if(schar == guess.charAt(i)) bullCnt++;
    		hashTab[schar-'0']++;
    	}
    	for(int i=0;i<guess.length();i++){
    		char gchar = guess.charAt(i);
    		if(hashTab[gchar-'0'] > 0){
    			hashTab[gchar-'0']--;
    			allCnt++;
    		}
    	}
    	cowCnt = allCnt - bullCnt;
    	return bullCnt + "A" + cowCnt + "B";
    }
    
    
    public void getHintTest(){
    	String res = this.getHintGood("1123","0111");
    	System.out.println(res);
    }
    
    
    //----- leetcode  219. Contains Duplicate II  0413  ac 
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
        	if(!hm.containsKey(nums[i])) hm.put(nums[i],i);
        	else{
        		if(i - hm.get(nums[i]) <= k) return true;
        		hm.put(nums[i],i);//focus  on
         	}
        }
        return false;
    }
    
    

    /*
     * ----------leetcode 387 beats 67.72%-------------------------
     */
    public int firstUniqChar(String s) {
       int[] char_set = new int[256];
       for(int i=0;i<s.length();i++){
    	   char_set[s.charAt(i)]++;
       }
       for(int i=0;i<s.length();i++){
    	   if(char_set[s.charAt(i)] == 1)
    		   return i;
       }
       return -1;
    }
    
    
    
	
	/**
	 * page108 ensure if all char is different 
	 * @param {@code str} (only contains char in 'a'~'z')
	 * @return {@code true} if all char is different 
	 * 		   {@code false} otherwise
	 */
	public static boolean isUniqueChars(String str){
		if(str.length() > 26) return false;
		int checker = 0;
		for(int i=0;i<str.length();i++){
			int val = str.charAt(i) - 'a';
			if((checker & (1 << val)) > 0)
				return false;
			checker |= (1 << val);
		}
		return true;
	}
	
	/**
	 * page108 ensure if all char is different 
	 * @param {@code str} {only contains ascii char}
	 * @return {@code true} if all char is different 
	 * 		   {@code false} otherwise 
	 */
	public static boolean isUniqueChars2(String str){
		if(str.length() > 256) return false;
		boolean[] char_set = new boolean[256];
		for(int i=0;i<str.length();i++){
			int val = str.charAt(i);
			if(char_set[val])
				return false;
			char_set[val] = true;
		}
		return true;
	}
	
	public static void isUniqueCharsTest(){
		boolean res = isUniqueChars("abcdef5678.,//");
		System.out.println(res);
	}
	
    
    
    
    public static void main(String[] args) {
		
	}
    
    
    
    
    
}
