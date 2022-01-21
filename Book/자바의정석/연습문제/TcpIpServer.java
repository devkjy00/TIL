import java.net.*;
import java.io.*;
import java.util.Scanner;



public class TcpIpServer {
    public static void main(String[] args){
        ServerSocket serverSocket = null;
        Socket socket = null;

        try {
            serverSocket = new ServerSocket(7777);            
            System.out.println("서버가 준비되었습니다");
            
            socket = serverSocket.accept();

            Sender sender = new Sender(socket);
            Receiver receiver = new Receiver(socket);

            sender.start();
            receiver.start();

        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}

class Sender extends Thread {
    Socket socket;
    DataOutputStream out;
    String name;

    Sender(Socket socket) {
        this.socket = socket;
        try {
            out = new DataOutputStream(socket.getOutputStream());
            name = "["+socket.getInetAddress()+":"+socket.getPort()+"]";

        } catch (Exception e) {}
    }
        
    public void run() {
        Scanner sc = new Scanner(System.in);
        while(out != null) {
            try {
                out.writeUTF(name + sc.nextLine());
            } catch(IOException e) {}
            }
        }
        
    } //run


class Receiver extends Thread {
    Socket socket;
    DataInputStream in;
    String name;

    Receiver(Socket socket) {
        this.socket = socket;
        try {
            in = new DataInputStream(socket.getInputStream());
        } catch (IOException e) {}
    }
    public void run() {
        while(in != null) {
            try {
                System.out.println(in.readUTF());
            }catch(IOException e) {

            }
        }
    }
}
        