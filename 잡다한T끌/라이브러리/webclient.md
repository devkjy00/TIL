### impl
``` java
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.BodyInserters;
import reactor.core.publisher.Mono;

public class WebClientPostExample {
    public static void main(String[] args) {
        // Create a WebClient instance
        WebClient webClient = WebClient.create("YOUR_BASE_URL_HERE");

        // Define the request body as a Map
        Map<String, Object> requestBodyMap = new HashMap<>();
        requestBodyMap.put("key1", "value1");
        requestBodyMap.put("key2", "value2");

        // Send the POST request with the Map as the body
        Mono<String> responseMono = webClient.post()
                .uri("/your-endpoint")
                .body(BodyInserters.fromValue(requestBodyMap))
                .retrieve()
                .bodyToMono(String.class);

        // Block and get the response
        String response = responseMono.block();
        System.out.println(response);
    }
}

```