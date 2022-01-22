// 1. 교집합, 차집합, 합집합
// 5. Comparable 정렬기준 정의
// 6. TreeSet의 생성자 매개변수로 Comparator익명클래스(Student객체의 점수로정렬) 지정

import java.util.*;
class pr_11{
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
        TreeSet<Student> set = new TreeSet<>(new Comparator<Student>(){
            public int compare(Student s1, Student s2) {
                if (s1 instanceof Student && s2 instanceof Student) {
                    return (int)(s1.getAverage() - s2.getAverage());
                }
                return -1;
            }
        });

        set.add(new Student("홍길동", 1,1,100,100,100));
        set.add(new Student("남궁성", 1,2,90,70,80));
        set.add(new Student("김자바", 1,3,80,80,90));
        set.add(new Student("이자바", 1,4,70,90,70));
        set.add(new Student("안자바", 1,5,60,100,80));

        Iterator<Student> it = set.iterator();
        
        while(it.hasNext()){
            System.out.println(it.next());
        }

        System.out.println("[60~69] :"+getGroupCount(set, 60, 70));
        System.out.println("[70~79] :"+getGroupCount(set, 70, 80));
        System.out.println("[80~89] :"+getGroupCount(set, 80, 90));
        System.out.println("[90~100] :"+getGroupCount(set, 90, 100));
    }

    // 6.
    static int getGroupCount(TreeSet<Student> tset, int from, int to) {
        Student s1 = new Student("", 0, 0, from, from, from);
        Student s2 = new Student("", 0, 0, to, to, to);

        return tset.subSet(s1,s2).size();
    }

}

// 5. 
class Student implements Comparable {
    String  name;
    int     ban;
    int     no;
    int     kor, eng, math;

    Student(String name,int ban, int no, int kor, int eng, int math) {
        this.name   = name;
        this.ban    = ban;
        this.no     = no;
        this.kor    = kor;
        this.eng    = eng;
        this.math   = math;  
    }

    int getTotal() {
        return kor+eng+math;
    }

    float getAverage() {
        return (int)((getTotal()/3f)*10+0.5)/10f;
    }

    public String toString() {
        return name+","+ban+','+no+','+kor+','+eng+','+math+','+getTotal()+'.'+getAverage();
    }

    @Override
    public int compareTo(Object st) {
        // Override 한 메서드의 매개변수는 바꿀수 없기때문에
        // 특정 메서드를 쓰려면 형변환은 꼭 해줘야한다 
        return this.name.compareTo(((Student)st).name);
    }


}
