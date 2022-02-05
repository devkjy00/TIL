// 1. 서브넷 마스크로 네트워크주소, 호스트주소 계산하기
// -> split("[.]")

import java.util.*;
import java.io.*;
import java.net.*;
import java.awt.*;
import java.awt.event.*;

public class Pr_16 {
    public static void main(String[] args) {
        
        // 1. 서브넷 마스크로 네트워크주소, 호스트주소 계산하기
        
        // String[] ip = "192.168.10.100".split("[.]");
        // String[] subnet = "255.255.255.0".split("[.]");

        // StringBuffer netIp = new StringBuffer();
        // StringBuffer userIp = new StringBuffer();
        // for(int i=0; i<ip.length; i++) {
        //     if ("255".equals(subnet[i])) {
        //         netIp.append(ip[i]+".");        
        //         userIp.append("0.");
        //     }else {
        //         userIp.append(ip[i]+".");
        //         netIp.append("0.");
        //     }
        // }
        // System.out.println("네트워크 주소: " + netIp);
        // System.out.println("호스트 주소: " + userIp);

        // 3.
        SourceViewer mainWin = new SourceViewer("Source Viewer");


        
    }    
}

class SourceViewer extends Frame {
    TextField tf = new TextField();
    TextArea ta = new TextArea();

    SourceViewer(String title) {
        super(title);

        add(tf, "North");
        add(ta, "Center");

        tf.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                displaySource();
            }
        });

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                System.exit(0);
            }
        });
        setBounds(500, 200, 500, 300);
        setVisible(true);
    }

    void displaySource() {
        URL url = null;
        BufferedReader input = null;
        String address = tf.getText().trim();
        String line = "";

        ta.setText("");

        try {
            if( !address.startsWith("http://"))
                address = "http://"+address;

                url = new URL(address);
                input = new BufferedReader(
                    new InputStreamReader(
                        url.openStream(), "UTF-8"
                    )
                );

                while((line=input.readLine()) != null) {
                    ta.append(line);
                    ta.append("\n");
                }

                input.close();
        } catch (Exception e) {
            ta.setText("유효하지 않은 URL입니다");
        }
    }
}