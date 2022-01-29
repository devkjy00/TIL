
// 3. 지네릭 올바른 사용

public class Pr_12 {
    public static void main(String[] args) {
        // 1.
        // -> a, b, c

        // 2. 
        // -> c, d            

        // 3.
        // -> a(x), c, d, e(x), g
        // -> 지네릭 클래스를 원시타입으로 생성해도 괜찮다
        // -> 지네릭 참조변수로 원시타입을 가리킬수 있다
        // -> 원시타입을 가리키는 지네릭 참조변수의 타입변수는 의미가 없다
        // -> <?>는 <? extends Object>가 아니라 선언된 지네릭의 가장 조상타입이다 
        // -> 원시타입 참조변수로 지네릭인스턴스를 가리킬수 있지만 바람직하지 않다 
        // 원시타입과 지네릭타입은 완전히 호환된다
        
    }
}
