import java.util.*;

// 4. sleep, join, wait은 interrupt로 실행대기로 만들 수 있다
// 5,6. sleep 은 스태틱메서드로 실행할 수 있다
// 9. InterruptedException을 캐치하면 다시 interrupt를 호출해서 interrupted를 true로 만들어줘야 한다
public class Pr_13 {
    public static void main(String[] args) throws Exception {
        // 4. sleep, join, wait은 interrupt로 실행대기로 만들 수 있다
        
        // 5. 
        // Thread3 th1 = new Thread3();
        // th1.start();

        // try {
        //     Thread.sleep(5*1000);
        // } catch(Exception e) { }
        // throw new Exception("꽝");

        // 6.
        // Thread3 th1 = new Thread3();
        // th1.setDaemon(true);
        // th1.start();

        // try {
        //     Thread.sleep(5*1000);
        // } catch(Exception e) { }

        // throw new Exception("꽝");

        // 7.
        // Thread3 th1 = new Thread3();
        // th1.start();

        // try {
        //     Thread.sleep(6*1000);
        // } catch(Exception e) {}

        // stopped = true;
        // th1.interrupt();
        // Thread.yield();

        // System.out.println("stopped");

        // 8.
        // Pr_13 game = new Pr_13();
        
        // game.wg.start();

        // Vector words = game.words;

        // while(true) {
        //     System.out.println(words);
        //     System.out.print(">>");

        //     Scanner s = new Scanner(System.in);
        //     String input = s.nextLine().trim();

        //     int index = words.indexOf(input);

        //     if(index!=-1) {
        //         words.remove(index);
        //     }
        // }

        // 9.

    }// end of main
    
    // 7.
    static boolean stopped = false;

    // 8.
    Vector words = new Vector();
    String[] data = {"태연","유리","윤아","효연","수영","서현","티파니","써니","제시카"};

    int interval = 2 * 1000; 

    WordGenerator wg = new WordGenerator();

    class WordGenerator extends Thread {
        public void run() {
            while(true) {
                
                int rand = new Random().nextInt(data.length);
                words.add(data[rand]);
                
                try {
                    Thread.sleep(interval); 
                } catch(Exception e) { }
            }
        }
    }
} // class Pr_13

class Thread3 extends Thread {
    public void run() {
        // for (int i=0; i < 10; i++) {
        for (int i=0; !Pr_13.stopped; i++) {
            System.out.println(i);
            try {
                Thread.sleep(3*1000);
            } catch (Exception e) { }
        }
    }
} // class Thread3 
    
