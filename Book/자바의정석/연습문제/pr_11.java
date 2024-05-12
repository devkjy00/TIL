import java.util.*;
import java.util.concurrent.SynchronousQueue;

import javax.swing.text.PlainDocument;

// 1. 교집합, 차집합, 합집합
// 5. Comparable 정렬기준 정의
// 6. TreeSet의 생성자 매개변수로 Comparator익명클래스(Student객체의 점수로정렬) 지정
// 10. HashSet은 순서를 유지하지 않고 임의의 순서도 제대로 구현하지 못한다
// 11. 클래스를 HashSet에 저장하고 출력, hashCode 오버라이딩
    
public class Pr_11{
    public static void main(String[] args) {
        // 1.
        // ArrayList<Integer> list1 = new ArrayList<>();
        // ArrayList<Integer> list2 = new ArrayList<>();
        // ArrayList<Integer> kyo = new ArrayList<>();
        // ArrayList<Integer> cha = new ArrayList<>();
        // ArrayList<Integer> hap = new ArrayList<>();
        
        // list1.add(1);
        // list1.add(2);
        // list1.add(3);
        // list1.add(4);

        // list2.add(3);
        // list2.add(4);
        // list2.add(5);
        // list2.add(6);


        // kyo.addAll(list1);
        // kyo.retainAll(list2);
        // cha.addAll(list1);
        // cha.removeAll(list2);
        // hap.addAll(list1);
        // hap.addAll(list2);

        // System.out.println("list1="+list1);
        // System.out.println("list2="+list2);
        // System.out.println("kyo="+kyo);
        // System.out.println("cha="+cha);
        // System.out.println("hap="+hap);

        // 2. 
        // -> 7\n 6\n 3\n 2\n

        // 3.
        // -> a : 첫번째 요소 삭제

        // 4.
        // -> 6번째 인덱스

        // 5.
        // ArrayList<Student> list = new ArrayList<>();
        // list.add(new Student("홍길동", 1,1,100,100,100));
        // list.add(new Student("남궁성", 1,2,90,70,80));
        // list.add(new Student("김자바", 1,3,80,80,90));
        // list.add(new Student("이자바", 1,4,70,90,70));
        // list.add(new Student("안자바", 1,5,60,100,80));

        // Collections.sort(list);

        // for(Student st:list) {
        //     System.out.println(st);
        // }

        // 6. 
        // Tree~ 의 생성자 매개변수로 Comparator익명클래스(Student객체의 점수로정렬) 지정
//        TreeSet<Student> set = new TreeSet<>(new Comparator<Student>(){
//            public int compare(Student s1, Student s2) {
//                if (s1 instanceof Student && s2 instanceof Student) {
//                    return (int)(s1.getAverage() - s2.getAverage());
//                }
//                return -1;
//            }
//        });
//
//        set.add(new Student("홍길동", 1,1,100,100,100));
//        set.add(new Student("남궁성", 1,2,90,70,80));
//        set.add(new Student("김자바", 1,3,80,80,90));
//        set.add(new Student("이자바", 1,4,70,90,70));
//        set.add(new Student("안자바", 1,5,60,100,80));
//
//        Iterator<Student> it = set.iterator();
//        
//        while(it.hasNext()){
//            System.out.println(it.next());
//        }
//
//        System.out.println("[60~69] :"+getGroupCount(set, 60, 70));
//        System.out.println("[70~79] :"+getGroupCount(set, 70, 80));
//        System.out.println("[80~89] :"+getGroupCount(set, 80, 90));
//        System.out.println("[90~100] :"+getGroupCount(set, 90, 100));
//    }

	// 7.  객체의 변수를 기준으로 정렬하기
//	ArrayList<Student> list = new ArrayList<>();
//	
//	list.add(new Student("이자바", 2, 1, 70, 90, 70));
//	list.add(new Student("홍길동", 2, 2, 60, 100, 80));
//	list.add(new Student("남궁성", 1, 3, 100, 100, 100));
//	list.add(new Student("안자바", 1, 1, 90, 70, 80));
//	list.add(new Student("김자바", 1, 2, 80, 80, 90));
//
//	Collections.sort(list, new BanNoAscending());
//:w

//	for(Object st:list){
//		System.out.println((Student)st);
//	}

	// 8. 정렬기준으로 객체변수, 순서를 객체의 변수에 저장
		
	// ArrayList<Student> list = new ArrayList<>();
	
	// list.add(new Student("이자바", 2, 1, 70, 90, 70));
	// list.add(new Student("홍길동", 2, 2, 60, 100, 80));
	// list.add(new Student("남궁성", 1, 3, 100, 100, 100));
	// list.add(new Student("안자바", 1, 1, 90, 70, 80));
	// list.add(new Student("김자바", 1, 2, 80, 80, 90));

	// calculateSchoolRank(list);

	// for(Student st:list){
	// 	System.out.println(st);
	// }
    
    // 9.
    // ArrayList<Student> list = new ArrayList<>();
	
	// list.add(new Student("이자바", 2, 1, 70, 90, 70));
	// list.add(new Student("홍길동", 2, 2, 60, 100, 80));
	// list.add(new Student("남궁성", 1, 3, 100, 100, 100));
	// list.add(new Student("안자바", 1, 1, 90, 70, 80));
	// list.add(new Student("김자바", 1, 2, 80, 80, 90));

	// calculateSchoolRank(list);
    // calculateClassRank(list);

	// for(Student st:list){
	// 	System.out.println(st);
	// }
    
    // 10. 1~30까지의 숫자 섞기(Set을 List쓰기) 
    // Set<Integer> set = new HashSet<>();
    // int[][] board = new int[5][5];

    // for(int i=0; set.size() < 25; i++) {
    //     set.add(new Random().nextInt(30)+1);
    // }
    // ArrayList list = new ArrayList(set); // hashSet은 순서와 관련된 작업을 하지 못하기 때문에
    // Collections.shuffle(list);  // shuffle로 다시 섞기

    // Iterator<Integer> it = list.iterator();
    // for(int i=0; i<board.length; i++) {
    //     for(int j=0; j<board[i].length; j++){
    //         board[i][j] = it.next();
    //         System.out.print((board[i][j] < 10 ? "  " : " ")
    //                             + board[i][j]);  
    //     }
    //     System.out.println();
    // }

    // 11.
    // SutdaCard c1 = new SutdaCard(3, true);
    // SutdaCard c2 = new SutdaCard(3, true);
    // SutdaCard c3 = new SutdaCard(1, true);

    // HashSet set = new HashSet();
    // set.add(c1);
    // set.add(c2);
    // set.add(c3);

    // System.out.println(set);

    // 12. 임의의 값으로 HashMap의 값 가져오기
    // SutdaDeck deck = new SutdaDeck();

    // deck.shuffle();
    // Player p1 = null;
    // Player p2 = null;
    // try {
    //     p1 = new Player("타짜", deck.pick(), deck.pick());
    //     p2 = new Player("고수", deck.pick(), deck.pick());
    // } catch (Exception e) {
    //     e.printStackTrace();
    // }

    // System.out.println(p1+" "+deck.getPoint(p1));
    // System.out.println(p2+" "+deck.getPoint(p2));

    // 13. 클래스 멤버를 기준으로 정렬하기
    // SutdaDeck deck = new SutdaDeck();

    // deck.shuffle();

    // Player[] pArr = new Player[5];
    // String[] names = {"타짜", "고수", "물주", "중수", "하수"};

    // for (int i=0; i<pArr.length; i++) {
    //     Player tempP = null;
    //     try {
    //         tempP = new Player(names[i], deck.pick(), deck.pick());
    //     } catch(Exception e) {
    //         e.printStackTrace();
    //     }
    //     pArr[i] = tempP;
    // }

    // TreeMap rank = new TreeMap(new Comparator<Player>(){
    //     public int compare(Player p1, Player p2) {
    //             return p2.point - p1.point;
    //         }
    //     });
    
    // for (int i=0; i<pArr.length; i++){
    //     Player p = pArr[i];
    //     rank.put(p, deck.getPoint(p));
    //     System.out.println(p+" "+deck.getPoint(p));
    // }

    // System.out.println();
    // System.out.println("1위는 "+rank.firstKey()+"입니다. ");
    
    // 14. 성적처리 프로그램
    while(true) {
        switch(displayMenu()) {
            case 1:
                inputRecord();
                break;
            case 2:
                displayRecord();
                break;
            case 3:
                System.out.println("프로그램을 종료합니다.");
                System.exit(0);
        }
    } // while(true)


}// end of main 

// 6.
static int getGroupCount(TreeSet<Student> tset, int from, int to) {
	Student s1 = new Student("", 0, 0, from, from, from);
	Student s2 = new Student("", 0, 0, to, to, to);

	return tset.subSet(s1,s2).size();
}

// 8.
public static void calculateSchoolRank(List list) {

	Collections.sort(list);

	int prevRank = -1;
	int prevTotal = -1;
    int length = list.size();

    for(int i=0; i<length; i++) {
            Student st = (Student)list.get(i);
            if(st.total == prevTotal) {
                st.schoolRank = prevRank;
            } else {
                st.schoolRank = i + 1; 
            }
            prevRank = st.schoolRank;
            prevTotal = st.total;
            }
	}

// 9.
public static void calculateClassRank(List<Student> list) {
    Collections.sort(list, new Comparator<Student>(){
        public int compare(Student s1, Student s2) {
            int result = s1.ban - s2.ban;
            if (result == 0) {
                result = s2.total - s1.total;
            }
            return result;
        }
    });

    int prevBan = -1;
    int prevRank = -1;
    int prevTotal = -1;
    int length = list.size();

    // for문의 변수를 선언부에 추가해서 사용하면 편하다
    for(int i=0, n=0; i<length; i++, n++) {
        Student tmp = list.get(i);
        
        if(tmp.ban != prevBan) {
            prevTotal = -1;
            prevRank = -1;
            n = 0;
        }
        if(tmp.total == prevTotal) {
            tmp.classRank = prevRank;
        } else {
            tmp.classRank = n+1;
        }
        prevBan = tmp.ban;
        prevRank = tmp.classRank;
        prevTotal = tmp.total;
    }
}

// 14
static ArrayList record = new ArrayList();
static Scanner s = new Scanner(System.in);

static int displayMenu() {
    System.out.println("**************************************************");
    System.out.println("* 성적 관리 프로그램 *"); 
    System.out.println("**************************************************");
    System.out.println();
    System.out.println(" 1. 학생성적 입력하기 "); 
    System.out.println();
    System.out.println(" 2. 학생성적 보기"); 
    System.out.println();
    System.out.println(" 3. 프로그램 종료 "); 
    System.out.println();
    
    int menu = 0;
    // 14.
    while(true){
        System.out.print("원하는 메뉴를 선택하세요.(1~3) : ");
        menu = s.nextInt();
        if(1<=menu&&menu<=3) {
            break;
        }else {
            System.out.println("메뉴를 잘못 선택했습니다, 다시 입력해주세요");
        }
    }
    //  
    return menu;
} // public static int displayMenu

static void inputRecord() {
    System.out.println("1. 학생성적 입력하기"); 
    System.out.println("이름,반,번호,국어성적,영어성적,수학성적'의 순서로 공백없이 입력하세요."); 
    System.out.println("입력을 마치려면 q를 입력하세요. 메인화면으로 돌아갑니다.");    

    while(true) {
        System.out.print(">>");
        String info = s.nextLine();
        if (info.equalsIgnoreCase("q")) {
            return;
        }
        try {
            String[] s = info.split(",");
            int[] nums = new int[s.length];
            for (int i=1; i<s.length; i++) {
               nums[i] = Integer.parseInt(s[i]);
            }
            Student st = new Student(s[0], nums[1], nums[2], nums[3], nums[4], nums[5]);
            record.add(st);
            
        } catch (Exception e) {
            System.out.println("입력오류입니다.");
            continue;
        }
        System.out.println("입력되었습니다");
    }   
}

static void displayRecord() {
    int koreanTotal = 0;
    int englishTotal = 0;
    int mathTotal = 0;
    int total = 0;

    int length = record.size();

    if(length > 0) {
        System.out.println();
        System.out.println("이름 반 번호 국어 영어 수학 총점 평균 전교등수 반등수");
        System.out.println("====================================================");
        for (int i = 0; i < length ; i++) {
            Student student = (Student)record.get(i); 
            System.out.println(student);
            koreanTotal += student.kor;
            mathTotal += student.math;
            englishTotal += student.eng;
            total += student.total;
        }
        System.out.println("===================================================="); 
        System.out.println("총점: "+koreanTotal+" "+englishTotal+" "+mathTotal+" "+total);
        System.out.println(); 
    } else {
        System.out.println("===================================================="); 
        System.out.println(" 데이터가 없습니다.");
        System.out.println("===================================================="); 

}
}
} // class Pr_11.java 


// 5. 
class Student implements Comparable {
    String  name;
    int     ban;
    int     no;
    int     kor, eng, math;

	int total;
	int schoolRank;
    int classRank;

    Student(String name,int ban, int no, int kor, int eng, int math) {
        this.name   = name;
        this.ban    = ban;
        this.no     = no;
        this.kor    = kor;
        this.eng    = eng;
        this.math   = math;  
		
		total = kor+eng+math;
    }

    int getTotal() {
        return total; 
    }

    float getAverage() {
        return (int)((getTotal()/3f)*10+0.5)/10f;
    }

    public String toString() {
        return name+","+ban+','+no+','+kor+','+
        eng+','+math+','+total+','+getAverage()
       +','+schoolRank+','+classRank;
    }

//    @Override
//    public int compareTo(Object st) {
//        // Override 한 메서드의 매개변수는 바꿀수 없기때문에
//        // 특정 메서드를 쓰려면 형변환은 꼭 해줘야한다 
//        return this.name.compareTo(((Student)st).name);
//    }

//  8.
	public int compareTo(Object o) {
        // 내림ㅏ
        if (o instanceof Student) {
            Student tmp = (Student)o;
            return tmp.total - this.total;
        }else {
            return -1;
        }
	}


} // class student

// 7.
class BanNoAscending implements Comparator {
	public int compare(Object o1, Object o2) {
		Student s1 = (Student)o1;
		Student s2 = (Student)o2;
		Integer s1_ban = s1.ban;
		Integer s2_ban = s2.ban;
		Integer s1_no = s1.no;
		Integer s2_no = s2.no;
		
		if(s1_ban == s2_ban) {
			return s1_no.compareTo(s2_no);
		}else {
			return s1_ban.compareTo(s2_ban);
		}

	}
} // class BanNoAscendign

// 11.
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

    public boolean equals(Object obj) {
        if(obj instanceof SutdaCard) {
            SutdaCard c = (SutdaCard)obj;
            return num==c.num && isKwang == c.isKwang;
        } else {
            return false;
        }
    }

    public String toString() {
        return num + (isKwang ? "K":"");
    }

    public int hashCode() {
            String thisStr = ""+num+isKwang;
            return thisStr.hashCode();
        }
    
} // class Sutdacard

class SutdaDeck {
    final int CARD_NUM = 20;
    SutdaCard[] cards = new SutdaCard[CARD_NUM];

    int pos = 0;
    HashMap jokbo = new HashMap();

    SutdaDeck() {
        for(int i=0; i<cards.length; i++){
            int num = i%10 + 1;
            boolean isKwang = i < 10 && (num==1 || num==3 || num==8);

            cards[i] = new SutdaCard(num, isKwang);
        }
        registerJokbo();
       }    


    void registerJokbo() {
        jokbo.put("KK", 4000);
        jokbo.put("1010",3100); 
        jokbo.put("99", 3090);
        jokbo.put("88", 3080);
        jokbo.put("77", 3070);
        jokbo.put("66", 3060);
        jokbo.put("55", 3050);
        jokbo.put("44", 3040);
        jokbo.put("33", 3030);
        jokbo.put("22", 3020);
        jokbo.put("11", 3010);

        jokbo.put("12", 2060);
        jokbo.put("21", 2060);
        jokbo.put("14", 2050);
        jokbo.put("41", 2050);
        jokbo.put("19", 2040);
        jokbo.put("91", 2040);
        jokbo.put("110", 2030);
        jokbo.put("101", 2030);
        jokbo.put("104", 2020);
        jokbo.put("410", 2020);
        jokbo.put("46",  2010);
        jokbo.put("64", 2010);
    }

    int getPoint(Player p) {    
        if(p==null) return 0;
        SutdaCard c1 = p.c1; 
        SutdaCard c2 = p.c2;

        Integer result = 0;  
        String tempJokbo = ""+c1.num+c2.num;
        
        if (c1.isKwang==true && c2.isKwang==true) {
            result = (int)jokbo.get("KK");
        }else if(jokbo.containsKey(tempJokbo)){
            result = (int)jokbo.get(tempJokbo);
        }else{
            result = (c1.num + c2.num) % 10 + 1000;
        }
        p.point = result;
        return result;
    }

    SutdaCard pick() throws Exception {
        SutdaCard c = null;
        if (0 <= pos && pos < CARD_NUM) {
            c = cards[pos];
            cards[pos++] = null; 
        } else {
            throw new Exception("남아있는 카드가 없습니다");
        }

        return c;
    }

    void shuffle() {
        for (int x=0; x<CARD_NUM*2; x++) {
            Random random = new Random();
            int i = random.nextInt(CARD_NUM);
            int j = random.nextInt(CARD_NUM);

            SutdaCard tmp = cards[i];
            cards[i] = cards[j];
            cards[j] = tmp;

        }
    }
} // class SutdaDeck
        
class Player {
    String name;
    SutdaCard c1;
    SutdaCard c2;

    int point;

    Player(String name, SutdaCard c1, SutdaCard c2) {
        this.name = name;
        this.c1 = c1;
        this.c2 = c2;
    }

    public String toString() {
        return "["+name+"]"+c1.toString()+","+c2.toString();
    }
}   // class Player