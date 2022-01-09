import java.util.*;

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
		System.out.println(round(3.1415,1));
		System.out.println(round(3.1415,2));
		System.out.println(round(3.1415,3));
		System.out.println(round(3.1415,4));
		System.out.println(round(3.1415,5));
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

	// 8.
	public static double round(double d, int n) {
		d = Math.round(d*Math.pow(10, n));
		return d/Math.pow(10, n);

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

