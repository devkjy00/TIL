// 1. 매달 2번째 일요일 날짜 출력하기
// 2. 입력받은 날짜 사이에 특정날짜 몇번나오는지 세기
// 3. 숫자문자열을 파싱해서 다른 포맷으로 출력하기
// 4. 입력받은 날짜데이터로 요일 출력하기
// 5. 입력받는 두 날짜간에 차이 계산하기
// 6. 입력한 날로 부터 오늘까지 몇일, 몇달 지났는지 출력
// 7. 4번째 주 화요일 날짜 출력하기
// 8. 서울, 뉴욕 시차 계산하기

import java.text.*;
import java.time.*;
import java.time.format.*;
import java.time.temporal.*;
import java.util.*;

public class Pr_10 {
    public static void main(String[] args){
        // 1. 매달 2번째 일요일 날짜 출력하기
        // Calendar cal = Calendar.getInstance();
        // cal.set(2010, 0, 1);

        // for (int i=0; i<12; i++){
        //     int weekday = cal.get(Calendar.DAY_OF_WEEK);

        //     // 시작이 일요일(1) 이면 8일, 아니면 16일 - 시작일 
        //     int secondSunday = (weekday==1) ? 8 : 16 - weekday;     
                   
        //     cal.set(Calendar.DAY_OF_MONTH, secondSunday);
        //     Date d = cal.getTime();
        //     System.out.println(new SimpleDateFormat("yyyy-MM-dd은 F번째 E요일입니다").format(d));

        //     cal.add(Calendar.MONTH, 1);
        //     cal.set(Calendar.DAY_OF_MONTH, 1);
        // }
        


        // 2.
        // Calendar fromCal = Calendar.getInstance();
        // Calendar toCal   = Calendar.getInstance();
 
        // fromCal.set(2010, 0, 1);
        // toCal.set(2010, 0, 1);
        // printResult(fromCal, toCal);

        // fromCal.set(2010, 0, 21);
        // toCal.set(2010, 0, 21);
        // printResult(fromCal, toCal);

        // fromCal.set(2010, 0, 1);
        // toCal.set(2010, 2, 1);
        // printResult(fromCal, toCal);

        // fromCal.set(2010, 0, 1);
        // toCal.set(2010, 2, 23);
        // printResult(fromCal, toCal);
        
        // fromCal.set(2010, 0, 23);
        // toCal.set(2010, 2, 21);
        // printResult(fromCal, toCal);

        // fromCal.set(2011, 0, 22);
        // toCal.set(2010, 2, 21);
        // printResult(fromCal, toCal);

        // 3. 문자열을 파싱해서 다른 포맷으로 출력하기
        // String data = "123,456,789.5";
        // System.out.println(data);
        // // #,### 패턴은 몇글자를 나눌지 한번만 작성하면 된다
        // DecimalFormat df1 = new DecimalFormat("#,###.#");
        // DecimalFormat df2 = new DecimalFormat("#,####");

        // try {
        //     int parNum  = df1.parse(data).intValue();
        //     parNum = Math.round(parNum/10f)*10;
        //     System.out.println("반올림:"+parNum);
        //     // DecimalFormat().format()에서 소수는 double형을 써야한다
        //     System.out.println("만단위:"+df2.format(parNum));
        // } catch (ParseException e) {
        //     // TODO Auto-generated catch block
        //     e.printStackTrace();
        // }

        // 4. 입력받은 날짜데이터로 요일 출력하기
        // while(true){
        //     Scanner s = new Scanner(System.in);
            
        //     System.out.println("날짜를 yyyy/MM/dd의 형태로 입력해주세요");
        //     String input = s.nextLine();
            
        //     SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd");
        //     SimpleDateFormat sdf1 = new SimpleDateFormat("입력하신 요일은 E요일입니다");

        //     try {
        //         Date d = sdf.parse(input);
        //         System.out.println(sdf1.format(d));

        //     } catch (ParseException e) {
        //         // TODO Auto-generated catch block
        //         continue;
        //     }
        //     break;
        // }

        // 5. 입력받는 두 날짜간에 차이 계산하기
        // System.out.println(getDayDiff("20010103", "20010101"));
        // System.out.println(getDayDiff("20010103", "20010103"));
        // System.out.println(getDayDiff("20010103", "200103"));

        // 6. 태어난 날부터 현재까지 day 계산
        // getDaysFromBirth("1996-04-18");

        // 7. 2016/12 네번째 화요일 출력하기
        // LocalDate d = LocalDate.parse("2016-12-01");
        // int week = 4;
        // if (d.get(ChronoField.DAY_OF_WEEK) <= 2) {
        //     week --;
        // }
        // d = d.plusWeeks(week).with(ChronoField.DAY_OF_WEEK, 2);
        // System.out.println(d);

        // 8. 서울과 뉴욕의 시차 계산하기
        // ZonedDateTime zdt = ZonedDateTime.now();
        // ZoneId nyId = ZoneId.of("America/New_York");
        
        // // withZoneSameInstant(ZoneId)로 zdt객체의 시간대를 변경할 수있다
        // ZonedDateTime zdtNy = ZonedDateTime.now().withZoneSameInstant(nyId);
        
        // // zdt.getOffset은 ZoneOffset을 반환
        // long sec1 = zdt.getOffset().getTotalSeconds();
        // long sec2 = zdtNy.getOffset().getTotalSeconds();
        // long diff = (sec1 - sec2)/3600;

        // System.out.println("sec1="+sec1);
        // System.out.println("sec2="+sec2);   
        // System.out.printf("diff= %d hrs%n", diff);
    }   
    

    // 2.
    static int paycheckCount(Calendar from, Calendar to) {
        if (Objects.isNull(from) || Objects.isNull(to)) return 0;
        if (from.equals(to) || from.get(Calendar.DAY_OF_MONTH)==21) return 1;


        int monDiff = to.get(Calendar.MONTH) - from.get(Calendar.MONTH);
        int yearDiff = to.get(Calendar.YEAR) - from.get(Calendar.YEAR); 
        if (monDiff < 0 || yearDiff < 0){
            return 0;
            
        }
        
        if (from.get(Calendar.DAY_OF_MONTH)<= 21 && to.get(Calendar.DAY_OF_MONTH)>= 21) {
            monDiff ++;
        }else if (from.get(Calendar.DAY_OF_MONTH) > 21 && to.get(Calendar.DAY_OF_MONTH) < 21 ) {
            monDiff --;
        }
        return monDiff;
    }

    static void printResult(Calendar from, Calendar to) {
        Date fromDate = from.getTime();
        Date toDate = to.getTime();

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");

        System.out.print(sdf.format(fromDate)+"~~"+sdf.format(toDate)+":");
        System.out.println(paycheckCount(from, to));

    }
    
    // 6.
    static int getDayDiff(String yyyymmdd1, String yyyymmdd2) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyyMMdd");

        TemporalAccessor ta1 = null;
        TemporalAccessor ta2 = null;

        try {
            ta1 = dtf.parse(yyyymmdd1);
            ta2 = dtf.parse(yyyymmdd2);
            
        } catch (Exception e) {
            //TODO: handle exception
            return 0;

        } 
        //from(TemporalAccessor) 파싱한 문자열을 객체로 만들어준다
        LocalDate d1 = LocalDate.from(ta1);
        LocalDate d2 = LocalDate.from(ta2);
        
        int dayDiff = d1.getDayOfYear() - d2.getDayOfYear();

        return dayDiff;
    }

    static void getDaysFromBirth(String birth) {
        LocalDate d1 = LocalDate.parse(birth);
        LocalDate d2 = LocalDate.now();

        // until로 두 날짜,시간의 차이를 상수값 단위로 반환
        long days = d1.until(d2, ChronoUnit.DAYS);
        long months = d1.until(d2, ChronoUnit.MONTHS);
        

        System.out.println("birth day = "+d1);
        System.out.println("today     = "+d2);
        System.out.println(days + "  days");
        System.out.println(months+ " months");
        
        

    }
}
