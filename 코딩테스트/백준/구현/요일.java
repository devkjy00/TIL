import java.util.stream.*;
import java.util.*;
import java.time.*;
import java.time.temporal.ChronoField;

public class A {
	public static void main(String[] arvs) {
		long startTime = System.currentTimeMillis();

		// 2007/1/1 월요일
		// 2007/x/y 는 무슨 요일인가

		Scanner sc = new Scanner(System.in);
		String[] inputStrings = sc.nextLine().split(" ");
		int[] inputInts = Arrays.stream(inputStrings)
							.map(String::trim)
							.mapToInt(Integer::parseInt)
							.toArray();

		sc.close();

		LocalDate ld = LocalDate.of(2007,inputInts[0],inputInts[1]);
		String[] dayName = {"MON", "TUE", 
					"WED", "THU", "FRI", "SAT", "SUN"};
		
		int index = ld.get(ChronoField.DAY_OF_WEEK);
		System.out.println(dayName[index-1]);

		long endTime = System.currentTimeMillis();
		System.out.println((endTime-startTime)/1000.0);
	}
}
 
