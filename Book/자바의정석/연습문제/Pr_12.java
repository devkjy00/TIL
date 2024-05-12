import java.util.*;

// 3. 지네릭 올바른 사용
// 4. 지네릭 타입변수를 사용한 메서드 지네릭메서드로 변환하기
public class Pr_12 {
    public static void main(String[] args) {

        // 3.
        // -> a(x), c, d, e(x), g
        // -> 지네릭 클래스를 원시타입으로 생성해도 괜찮다
        // -> 지네릭 참조변수로 원시타입을 가리킬수 있다
        // -> 원시타입을 가리키는 지네릭 참조변수의 타입변수는 의미가 없다
        // -> <?>는 <? extends Object>가 아니라 선언된 지네릭의 가장 조상타입이다 
        // -> 원시타입 참조변수로 지네릭인스턴스를 가리킬수 있지만 바람직하지 않다 
        // 원시타입과 지네릭타입은 완전히 호환된다

        // 4. 지네릭 타입변수를 사용한 메서드 지네릭메서드로 변환하기
        // -> 지네릭 메서드의 타입변수는 메서드의 반환타입, 매개변수타입의 지네릭, 구현블럭에 사용된다
        
        // 5. 
        // Deck d = new Deck();
        // Card c = d.pick(0);
        // System.out.println(c);

        // d.shuffle();
        // c = d.pick(0);
        // System.out.println(c);


    } // end of main    

    // 4.
    // public static <T extends Product> ArrayList<T> merge(
    //     ArrayList<T> list1, ArrayList<T> list2) {
    //         ArrayList<T> newList = new ArrayList<>(list1);
    //         newList.addAll(list2);
    //         return newList;
    // }

} // class Pr_12

class Deck{
    final int CARD_NUM = Card.Kind.values().length 
                * Card.Number.values().length;

    Card cardArr[] = new Card[CARD_NUM];

    Deck(){
        int i=0;
        for(Card.Kind kind : Card.Kind.values()) { 
            for(Card.Number num : Card.Number.values()) {
                cardArr[i++] = new Card(kind, num); 
}
}
    }

    Card pick(int index) {
        return cardArr[index];
    }

    Card pick() {
        int index = new Random().nextInt(CARD_NUM);
        return pick(index);
    }

    void shuffle() {
        for(int i=0; i<cardArr.length; i++) {
            int r = new Random().nextInt(CARD_NUM);
            Card temp = cardArr[i];
            cardArr[i] = cardArr[r];
            cardArr[r] = temp;
        }
    }
} // Deck class

class Card {
    enum Kind {CLOVER, HEART, DIAMOND, SPADE}
    enum Number {
        ACE, TWO, THREE, FOUR, FIVE,
        SIX, SEVEN, EIGHT, NINE, TEN,
        JACK, QUEEN, KING 
    }

    Kind kind;
    Number num;

    Card() {
        this(Kind.SPADE, Number.ACE);
    }

    Card(Kind kind, Number num) {
        this.kind = kind;
        this.num = num;
    }

    public String toString() {
        return "[" + kind.name() + "," + num.name() + "]";
    }
}
