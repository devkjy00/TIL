import java.util.*;
import java.util.stream.*;

import javax.swing.text.Style;

import java.util.function.*;

// 4. 스트림생성을 중첩하면 반복문을 중첩하는 것과 같다 
// -> 스트림을 중첩하면 flatMap의 안에서 중첩해야 결과가 제대로 나온다

public class Pr_14 {
    public static void main(String[] arvs){
        // 1. 메서드를 람다식으로 변환
        // BiFunction<String, Integer, Integer>
        // lam1 = (name, i) -> System.println(name+"="+i);

        // UnaryOperator<Integer> 
        // lam2 = x -> x * x;

        // Supplier<Integer> 
        // lam3 = () -> new Random().nextInt(6);

        // Function<int[], Integer> 
        // lam4 = {arr -> 
        //         int sum = 0;
        //         for (int i:arr){
        //             sum += i;
        //         }
        //         return sum;}

        // Supplier<Integer>
        // lam5 = () -> new int[]{};

        // 2. 람다식을 메서드참조로 변환
        // - String::length
        // - int[]::new
        // - Arrays::stream
        // - String::equals
        // - Integer::compare
        // - Card::new
        // - System.out::println
        // - Math::random
        // - String::toUpperCase
        // - NullPoiinterException::new
        // - Optional::get
        // - StringBuffer::append
        // - System.out::println
        
        // 3. d
        
        // 4. 스트림생성을 중첩하면 반복문을 중첩하는 것과 같다 
        // -> 스트림을 중첩하면 flatMap의 안에서 중첩해야 결과가 제대로 나온다
        // Stream<Integer> die = IntStream.range(1,6).boxed();

        // die.flatMap(i -> Stream.of(1,2,3,4,5,6).map(i2 -> new int[]{i, i2}))
        //    .filter(iArr -> iArr[0]+iArr[1]==6)
        //    .forEach(iArr -> System.out.println(Arrays.toString(iArr) ));

        // 5.
        // String[] strArr = {"aaa", "bb", "c", "dddd"};
        // System.out.println(Stream.of(strArr)
        //                     .map(str -> str.length())
        //                     .reduce((x,y) -> x+y)
        //                     .get());

        // 6. 
        // String[] strArr = {"aaa", "bb", "c", "dddd"};
        // System.out.println(Stream.of(strArr)
        //                     .map(str -> str.length())
        //                     .reduce((x, y) -> x > y ? x : y)
        //                     .get());

        // 7.
        // new Random().ints(5, 1, 45)
        //             .boxed()
        //             .sorted()
        //             .forEach(System.out::println);
    
        // 8~9.
        Student[] stuArr = {
            new Student("나자바", true, 1, 1, 300),
            new Student("김지미", false, 1, 1, 250),
            new Student("김자바", true, 1, 1, 200),
            new Student("이지미", false, 1, 2, 150),
            new Student("남자바", true, 1, 2, 100),
            new Student("인지미", false, 1, 2, 50),
            new Student("황지미", false, 1, 3, 100),
            new Student("강지미", false, 1, 3, 150),
            new Student("이자바", true, 1, 3, 200),

            new Student("나자바", true, 2, 1, 300),
            new Student("김지미", false, 2, 1, 250),
            new Student("김자바", true, 2, 1, 200),
            new Student("이지미", false, 2, 2, 150),
            new Student("남자바", true, 2, 2, 100),
            new Student("인지미", false, 2, 2, 50),
            new Student("황지미", false, 2, 3, 100),
            new Student("강지미", false, 2, 3, 150),
            new Student("이자바", true, 2, 3, 200)
        };

        // 8.
        // Map<Boolean, Map<Boolean, Long>> failedStuBySex = 
        //     Stream.of(stuArr)
        //         .collect(Collectors.partitioningBy(st -> st.score < 150,
        //         Collectors.partitioningBy(st -> st.isMale, 
        //         Collectors.counting())));

        // long failedMaleStuNum = failedStuBySex.get(true).get(true);
        // long failedFemaleStuNum = failedStuBySex.get(true).get(false);

        // System.out.println("불합격[남자]:"+ failedMaleStuNum +"명");
        // System.out.println("불합격[여자]:"+ failedFemaleStuNum +"명");

        // 9.
        Map<Integer, Map<Integer, Long>> totalScoreByHakAndBan =
        Stream.of(stuArr)
        .collect(Collectors.groupingBy(st -> st.hak, 
        Collectors.groupingBy(st -> st.ban,
        Collectors.summingLong(st -> st.score))));

        for(Object e : totalScoreByHakAndBan.entrySet()) {
            System.out.println(e);
        }


        

    } // end of main
} // class Pr_14

// 8.
class Student {
    String name;
    boolean isMale;
    int hak;
    int ban;
    int score;

    Student (String name, boolean isMale, int hak, int ban, int score) {
        this.name = name;
        this.isMale = isMale;
        this.hak = hak;
        this.ban = ban;
        this.score = score;
    }

    Stirng  getName() {return name;}
    boolean isMale() {return isMale;}
    int     getHak() {return hak;}
    int     getBan() {return ban;}
    int     getScore() {return score;}
    
    public String toString() {
        return String.format("[%s, %s, %d학년 %d반, %3d점]",
                         name, isMale ? "남":"여", hak, ban, score);
    }

    enum Level {HIHG, MID, LOW}
}





