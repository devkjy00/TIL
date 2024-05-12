import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Pr_9 {

	public static void main(String[] args) {
		// 1.
	//	SutdaCard c1 = new SutdaCard(3,true);
	//	SutdaCard c2 = new SutdaCard(3,true);
	//
	//	System.out.println("c1="+c1);
	//	System.out.println("c2="+c2);
	//	System.out.println("c1.equals(c2):"+c1.equals(c2));
		
		// 2. 
		// point3D p1 = new Point3D(1,2,3);
		// Point3D p2 = new Point3D(1,2,3);
		
		// System.out.println(p1);
		// System.out.println(p2);
		// System.out.println("p1==p2?"+(p1==p2));
		// System.out.println("p1.equals(p2)?"+(p1.equals(p2)));
		
		// 3. 
		// String fullPath = "TIL/study/Test.java";
		// String path = "";
		// String fileName = "";

		// StringTokenizer t = new StringTokenizer(fullPath, "/", true);
		// while(t.hasMoreTokens()) {
		// 	if (t.countTokens() > 1) {
		// 		path += t.nextToken();
		// 	}else {
		// 		fileName += t.nextToken();
		// 	}

		// }

		// System.out.println("fullPath:"+fullPath);
		// System.out.println("path:"+path);

		// System.out.println("fileName:"+fileName);

		// 4. 
		// printGraph(new int[]{3,7,1,4},'*');
		
		// 5.
		// System.out.println(count("12345AB12AB345AB", "AB"));
		// System.out.println(count("12345", "AB"));

		// 6. 
		// String src = "12345";
		// System.out.println(fillZero(src, 10));
		// System.out.println(fillZero(src, -1));
		// System.out.println(fillZero(src, 3));

		// 7. 
		// System.out.println(contains("12345","23"));
		// System.out.println(contains("12345","67"));

		// 8.
		// System.out.println(round(3.1415,1));
		// System.out.println(round(3.1415,2));
		// System.out.println(round(3.1415,3));
		// System.out.println(round(3.1415,4));
		// System.out.println(round(3.1415,5));

		// 9.
		// System.out.println("(1!2@3^4~5)"+" -> "
		// 		+ delChar("(1!2@3^4~5)","~!@#$%^&*()"));
		
		// System.out.println("(1 2   3  4/t5"+" -> "
		// 		+ delChar("(1 2   3  4/t5)"," /t"));
				
		// 10.
		// String str = "가나다";
		// System.out.println(format(str,7,0)); 	//왼쪽 정렬
		// System.out.println(format(str,7,1));	//가운데 정렬
		// System.out.println(format(str,7,2));	//오른쪽 정렬

		// 11.
		// if (args.length != 2){
		// 	System.out.println("2 개의 수를 입력하세요");
		// 	return;
		// }
		// if (args[0].charAt(0) >= args[1].charAt(0)) {
		// 	System.out.println("0~9까지의 숫자를 오름차순으로 입력하세요");
		// 	return;
		// }
		// int x = Integer.parseInt(args[0]);
		// int y = Integer.parseInt(args[1]);
		
		// for (;x<=y; x++) {
		// 	for (int i=0; i<10; i++) {
		// 		System.out.println(x+"*"+i+"="+x*i);
		// 	}
		// 	System.out.println();
		// }

		// 12.
		// for (int i=0; i<20; i++) 
		// 	System.out.print(getRand(1, -3)+",");

		// 13.
		// String src = "aabbccAABBCCaa";
		// System.out.println(src);
		// System.out.println("aa를 " + stringCount(src, "aa") +"개 찾았습니다.");

		// 14.
		String[] phoneNumArr = {
			"012-2345-7890",
			"099-2345-7980",
			"088-2346-9870",
			"013-3456-7890"
		};

		Vector list = new Vector();
		Scanner s = new Scanner(System.in);

		while(true) {
			System.out.print(">>");
			String input = s.nextLine().trim();

			if (input.equals("")) {
				continue;
			}else if (input.equalsIgnoreCase("Q")){
				System.exit(0);
			}
		
			String pattern = ".*"+input+".*";
			Pattern p = Pattern.compile(pattern);

			for (String str:phoneNumArr){
				String tmp = str.replace("-","");

				Matcher m = p.matcher(tmp);
				
				if (m.find()){
					list.add(str);	
				}
			}

			if (list.size() > 0) {
				System.out.println(list);
				list.clear();
			}else {
				System.out.println("일치하는 번호가 없습니다.");
			}
		}
	}
	// 4. 
	static void printGraph(int[] dataArr, char ch) {
		for(int i:dataArr) {
			for (int j=0; j<i; j++){
				System.out.print(ch);
			}
			System.out.print(i);
			System.out.println();
		}
	
	}

	public static int count(String src, String target) {
		int count = 0;
		int pos = 0;
		
		while(true) {
			int i = src.indexOf(target, pos);
			if (i == -1) break;
			pos += i;
			count ++;			
		}
		return count;
	}

	// 6.
	public static String fillZero(String src, int length) {
		if (Objects.isNull(src) || src.length() == length) {
			return src;
		}
		
		if (length <= 0) {
			return "";
		}
		
		if (src.length() > length) {
			return src.substring(0, length);
		}

		char[] result = new char[length];
		Arrays.fill(result, '0');
		System.arraycopy(src.toCharArray(), 0, result, 0, src.length());


		// 문자배열을 문자열로 바꾸기
		return String.valueOf(result);
		
	}

	// 7.
	public static boolean contains(String src, String target) {
		return src.contains(target);
	}

	// 8. n제곱, n이 1이면 현재자릿수에서 소수점 1자리만,,,
	public static double round(double d, int n) {
		d = Math.round(d*Math.pow(10, n));
		return d/Math.pow(10, n);
	
	}

	// 9. 
	public static String delChar(String src, String delCh) {
		StringBuffer sb = new StringBuffer(src.length());

		for (int i=0; i<src.length(); i++) {
			char ch = src.charAt(i);
			// 검사할 문자열에서 문자를 빼서
			// 삭제할 데이터에 있는지 비교
			if (delCh.indexOf(ch)==-1)
				sb.append(ch);
		}
		return sb.toString();
	}

	// 10.
	static String format(String str, int length, int alignment) {
		if(str.length() > length) {
			return str.substring(0, length);
		}

		char[] aliArr = new char[length];
		
		Arrays.fill(aliArr, ' ');
		int n = 0;
		switch(alignment){
			 case(1):{
				n = length/2-(str.length()/2);
				break;
			} case(2):{
				n = length - str.length();
				break;
			}
			// break 문 꼭 쓰기!
		}
		System.arraycopy(str.toCharArray(),0,aliArr,n,str.length());

		return String.valueOf(aliArr);
	}

	// 12.
	static int getRand(int from, int to){
		int min = Math.min(from, to);
		int max = Math.max(from, to);
		if (min < 0) {
			max += Math.abs(min);
		}else if(min > 0) {
			max -= min;
		}

		int rand = new Random().nextInt(max+1);
		return rand+min;
		

		
	}

	// 13.
	static int stringCount(String src, String key) {
		return stringCount(src, key, 0);
	}

	static int stringCount(String src, String key, int pos) {
		int count = 0;

		if (key == null || key.length() == 0)
			return 0;
		
		Pattern p = Pattern.compile(key);
		Matcher m = p.matcher(src);
		
		while(m.find()) {
			count ++;
		} 

		return count;
	}

}

// 1. 
class SutdaCard {
	int num;
	boolean isKwang;

	SutdaCard() {
		this(1, true);
	}

	SutdaCard(int num, boolean isKwang) {
		this.num = num;
		this.isKwang = isKwang;
	}

	public String toString(){
		return num + (isKwang ? "K" : "");
	}

	public boolean equals(SutdaCard obj) {
		if (this.num == obj.num && this.isKwang == obj.isKwang) {
			return true;
		} else {
			return false;
		}
	}
}

// 2. 
class Point3D {
	int x, y, z;

	Point3D(int x, int y,int z) {
		this.x=x;
		this.y=y;
		this.z=z;
	}
	
	Point3D() {
		this(0, 0, 0);
	}

	public boolean equals(Object obj) {
		if (obj instanceof Point3D){
			Point3D o = (Point3D)obj;
			if (x == o.x && y == o.y && z == o.z){
				return true;
			}
		} 
		return false;
	}

	public String toString() {
		return ""+x+y+z;
	}
}

