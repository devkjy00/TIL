
public class ClientInfo{
    private static int clientCount = 0;
    private int num;
    private String id;
    private String contact;
    public ClientInfo(String id, String contact){
        this.num = ++clientCount;
        this.id = id;
        this.contact = contact;
        System.out.println(this.id+this.contact+num);
    }
}