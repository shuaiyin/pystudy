package Topic;

public class HighAccuracyTopic {
    //----- leetcode 445 ac  04-10
    public ListNode addTwoNumbers1(ListNode l1, ListNode l2) {
    	if(l1 == null) return l2;
    	if(l2 == null) return l1;
    	ListNode newL1 = reverse(l1);
    	ListNode newL2 = reverse(l2);
    	////辅助节点,这个辅助节点很重要，因为它可以节省下新链初始节点为空的判定
    	ListNode dummy = new ListNode(-1);
    	ListNode resultL = dummy;//
    	int carry = 0;
    	while(newL1 != null || newL2 != null){
    		int val1 = newL1 == null ? 0 : newL1.val;
    		int val2 = newL2 == null ? 0 : newL2.val;
    		int val = (val1 + val2 + carry)%10;
    		carry = (val1 + val2 + carry)/10;
			resultL.next = new ListNode(val);
			resultL = resultL.next;
    		if(newL1 != null) newL1 = newL1.next;
    		if(newL2 != null) newL2 = newL2.next;
    	}
    	if(carry > 0) resultL.next = new ListNode(carry);///
        return reverse(dummy.next);
    }
    
    	//反转也是有门道的
        public ListNode reverse(ListNode head){
    	if(head == null || head.next == null) return head;
    	ListNode preNode = head;
    	ListNode nextNode = head.next;
    	while(nextNode != null){
    		ListNode temp = nextNode.next;
    		nextNode.next = preNode;
    		preNode = nextNode;
    		nextNode = temp;
    	}
    	head.next = null;
    	return preNode;
    }
        
    //leetcode 2  ac 0410 beats19%
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	int carry = 0;
    	ListNode dummy = new ListNode(-1);//定义存储新的结果
    	ListNode sumNode = dummy;//临时缓存
        while(l1 != null || l2 != null){
        	int listOneVal = l1 != null ? l1.val : 0;
        	int listTwoVal = l2 != null ? l2.val : 0;
        	int sum = listOneVal + listTwoVal + carry;
        	sumNode.next = new ListNode(sum%10);
        	sumNode = sumNode.next;
        	carry = sum/10;
        	if(l1 != null) l1 = l1.next;
        	if(l2 != null) l2 = l2.next;
        }
        if(carry != 0) sumNode.next = new ListNode(carry);
        return dummy.next;
    }
    
    //leetcode 67 add binary beats 14.38%
    public String addBinary(String a,String b){
    	StringBuffer sb = new StringBuffer();//可以直接使用上String的索引,String不可变
    	int carry = 0;//
    	for(int ai = a.length()-1,bi = b.length()-1;ai >= 0 || bi >= 0;){
    		int aval = ai >= 0 ? a.charAt(ai) - '0' : 0;//记得转换
    		int bval = bi >= 0 ? b.charAt(bi) - '0' : 0;
    		int sum  = aval + bval + carry;
    		sb.append(sum%2);
    		carry = sum/2;//更新carry
    		if(ai >= 0) ai--;
    		if(bi >= 0) bi--;
    	}
    	if(carry > 0) sb.append(carry);
    	return sb.reverse().toString();
    }
    
    //---- leetcode 415   ac  beats 92.80% very good solution 
    //充分利用索引，以避免reverse
    public String addStrings(String num1, String num2) {//
    	StringBuffer sb = new StringBuffer();
    	int carry = 0;
    	for(int i= num1.length()-1,j=num2.length()-1;i >= 0 || j >= 0;){
    		int nums1Val = i >=0 ? num1.charAt(i) - '0' : 0;
    		int nums2Val = j >= 0 ? num2.charAt(j) - '0' : 0;
    		int sum = nums1Val + nums2Val + carry;
    		sb.append(sum%10);
    		carry = sum/10;
    		if(i >= 0) i--;
    		if(j >= 0) j--;
    	}
    	if(carry > 0) sb.append(carry);
    	return sb.reverse().toString();
    }
    
    
    //--------高精度加法 leetcode 66  plus one  ac 0410
    //数组的索引性质可以避免转置  beats 49.%
    public int[] plusOne(int[] digits) {
    	int carry = 1;//carry还是必须的
    	for(int i= digits.length-1;i >=0 && carry > 0;i--){
    		int sum = carry + digits[i];
    		digits[i] = sum%10;
    		carry = sum/10;
    	}
    	if(carry == 0) return digits;
		//java中的数组是定长的，无法动态增加长度。如果要扩充数组，只能通过重新定义数组，
		//把旧数组内容拷贝到新数组中。但是这里并没有拷贝，因为plus1的特殊性
		int[] newArr = new int[digits.length + 1];
		newArr[0] = carry;
		return newArr;
    }

    public void plusOneTest(){
    	int[] digits = {9,9,9,9};
    	int[] res = this.plusOne(digits);
    	for(int val:res)
    		System.out.println(val);
    }
    
}