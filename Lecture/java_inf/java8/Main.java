import java.security.Provider;
import java.util.function.Function;
import java.util.function.IntFunction;
import java.util.function.Supplier;

public class Main{
    public static void main(String[] args) {
    
        Supplier s = () -> "abc";
        System.out.println(s.get());

        Function f = (Object st) -> st;
        System.out.println(f.apply("string"));
        
    }
}
