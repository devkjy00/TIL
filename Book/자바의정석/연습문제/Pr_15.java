// 1. 커맨드라인으로 파일입력을 받아서출력
// 2. 이진 파일을 16진수로 보기
// 3. 파일의 개수, 디렉토리의 개수, 파일의 총 크기를 계산
// 4. 커맨드라인으로 입력받은 파일을 합쳐서 새로운 파일 만들기
// -> SequenceInputStream 사용
// 5. 파일에서 태그만 빼고 출력하기
import java.io.*;
import java.util.*;

import javax.lang.model.util.AbstractAnnotationValueVisitor6;

import java.awt.*;
import java.awt.event.*;
import java.beans.EventHandler;

public class Pr_15 {
    public static void main(String[] args) {
    
        // 1. 커맨드라인으로 파일입력을 받아서출력
        // try {
        //     int line = Integer.parseInt(args[0]);
        //     String fileName = args[1];

        //     FileReader fr = new FileReader(fileName);
        //     BufferedReader br = new BufferedReader(fr);
        //     for (int i=0; i<line; i++){
        //         System.out.println(i+":"+br.readLine());
        //     br.close();
        //     }
        // } catch (Exception e) { }

        // 2. 이진 파일을 16진수로 보기
        // try {
        //     String fileName = args[0];
        //     BufferedInputStream bis = new BufferedInputStream(new FileInputStream(fileName));

        //     int data;
        //     while((data = bis.read()) != -1){
        //         System.out.printf("%02X ", data);
        //     }

        //     } catch (Exception e) { }

        // 3. 파일의 개수, 디렉토리의 개수, 파일의 총 크기를 계산
        
        // if (args.length != 1) {
        //     System.out.println("USAGE : java DirectoryInfoTest DIRECTORY");
        //     System.exit(0);
        // }

        // File dir = new File(args[0]);

        // if (!dir.exists() || !dir.isDirectory()) {
        //     System.out.println("유효하지 않은 디렉토리입니다.");
        //     System.exit(0);
        // }
            
        // countFiles(dir);

        // System.out.println();
        // System.out.println("총 " + totalFiles + "개의 파일");
        // System.out.println("총 " + totalDirs + "개의 디렉토리");
        // System.out.println("총 " + totalSize + "bytes");
        
        // 4. 커맨드라인으로 입력받은 파일을 합쳐서 새로운 파일 만들기
        // -> SequenceInputStream 사용

        // if (args.length < 2) {
        //     System.out.println("USAGE : java FileName MERGE_FILENAME FILENAME1 FILENAME2");
        //     System.exit(0);
        // }

        // try {

        //     Vector data = new Vector();
            
        //     for(int i=1; i < args.length; i++) {
        //         File f = new File(args[i]);

        //         if (f.exists()) {
        //             data.add(new FileInputStream(args[i]));
        //         } else {
        //             System.out.println(args[i] + " - 존재하지 않는 파일입니다.");
        //             System.exit(0);
        //         }
        //     }

        //     SequenceInputStream input = new SequenceInputStream(data.elements());
        //     FileOutputStream output = new FileOutputStream(args[0]);

        //     int info;
        //     while((info = input.read()) != -1 ) {
        //         output.write(info);
        //     }
        //     output.close();
            
        // } catch (Exception e) {}
            
        // 5. 파일에서 태그만 빼고 출력하기
        
        // if (args.length != 2) {
        //     System.out.println("USAGE : java name File File");
        //     System.exit(0);
        // }

        // String inputFile = args[0];
        // String outputFile = args[1];

        // try {
        //     BufferedReader input 
        //         = new BufferedReader(new FileReader(inputFile));
            
        //     HtmlTagFilterWriter output 
        //         = new HtmlTagFilterWriter(new FileWriter(outputFile));
            
        //     int ch = 0;

        //     while ((ch=input.read()) != -1) {
        //         output.write(ch);
        //     }

        //     input.close();
        //     output.close();
        // } catch (Exception e) { }

        // 6.
        // Scanner s = new Scanner(System.in);

        // while(true) {
        //     try {
        //         String prompt = curDir.getCanonicalPath()+">>";
        //         System.out.print(prompt);

        //         String input = s.nextLine();

        //         input = input.trim();
        //         argArr = input.split(" +");

        //         String command = argArr[0].trim();

        //         if("".equals(command)) continue;

        //         command = command.toLowerCase();

        //         if(command.equals("q")) {
        //             System.exit(0);
        //         } else if(command.equals("cd")) {
        //             cd();
        //         } else {
        //             for(int i=0; i<argArr.length; i++) {
        //                 System.out.println(argArr[i]);
        //             }
        //         }
        //     } catch (Exception e) {
        //         e.printStackTrace();
        //         System.out.println("입력오류입니다.");
        //     }
        // } //while(true)

    } // main

    static int totalFiles = 0;
    static int totalDirs = 0;
    static int totalSize = 0;

    public static void countFiles(File dir) {
        File[] fileList = dir.listFiles();
        
        for(File f : fileList){
            if (f.isFile()) {
                totalFiles++;
                totalSize += f.length();
            }else if (f.isDirectory()) {
                totalDirs++;
            }
        }
    } // countFiles

    static String[] argArr;
    static File curDir;

    static {
        try {
            curDir = new File(System.getProperty("user.dir"));
        } catch (Exception e) { }
    }

    public static void cd() {
        if (argArr.length==1) {
            System.out.println(curDir);
            return;
        } else if (argArr.length>2) {
            System.out.println("USAGE : cd directory");
            return;
        }
        
        String subDir = argArr[1];

        if ("..".equals(subDir)) {
            File newDir = curDir.getParentFile();

            if (newDir==null) {
                System.out.println("유효하지 않은 디렉토리입니다");
            } else {
                curDir = newDir;
            }
        } else if(".".equals(subDir)) {
            System.out.println(curDir);
        } else {
            File newDir = new File(curDir, subDir);
            if(newDir.exists() && newDir.isDirectory()) {
                curDir = newDir;
            } else {
                System.out.println("유효하지 않은 디렉토리입니다.");
            }

        }
        
    } // cd

} // calss Pr_15


class HtmlTagFilterWriter extends FilterWriter {

    StringWriter tmp = new StringWriter();
    boolean inTag = false;

    HtmlTagFilterWriter(Writer out) {
        super(out);
    }

    public void write(int c) throws IOException {
        if (c == '<') {
            inTag = true;
        } else if(c == '>' && inTag) {
            inTag = false;
            tmp = new StringWriter();
            return;
        }

        if (inTag) {
            tmp.write(c);
        }else {
            out.write(c);
        }
    }

    public void close() throws IOException {
        out.write(tmp.toString());
        super.close();
    }
} // class HtmlTagFilterWriter 

