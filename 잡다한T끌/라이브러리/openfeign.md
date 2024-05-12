
## issue
- 401 응답이 왔을때 에러 메시지를 받아야 되는데 exception을 던진다... 왜?..?


## implement
- build.gradle
	``` groovy
	
	plugins {
		id 'java'
		id 'org.springframework.boot' version '3.2.0'
		id 'io.spring.dependency-management' version '1.1.4'
	}
	
	group = 'jy'
	version = '0.0.1-SNAPSHOT'
	
	ext {
	    set('springCloudVersion', "2023.0.1")
	}
	
	dependencyManagement {
	    imports {
	        mavenBom "org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}"
	    }
	}
	
	java {
		sourceCompatibility = '17'
	}
	
	repositories {
		mavenCentral()
	}
	
	dependencies {
		implementation 'org.springframework.boot:spring-boot-starter-web'
		testImplementation 'org.springframework.boot:spring-boot-starter-test'
		implementation 'org.springframework.cloud:spring-cloud-starter-openfeign'
	}
	
	tasks.named('test') {
		useJUnitPlatform()
	}
	```

- code
	``` java
	
	@EnableFeignClients
	@SpringBootApplication
	public class FeigntestApplication {
	
		public static void main(String[] args) {
			SpringApplication.run(FeigntestApplication.class, args);
		}
	
		@Bean
		public CommandLineRunner run(MyFeignClientService myFeignClientService) {
			return args -> {
				System.out.println(myFeignClientService.getHelloMessage(Map.of("prompt", "hey")));
			};
		}
	}
	```
	
	
	``` java
	@FeignClient(name = "myFeignClient", url = "http://southoftheriver.synology.me:8080")
	public interface MyFeignClient {
	    @PostMapping(value = "/refactoring", consumes = "application/json")
	    @Headers("Content-Type: application/json")
	    String getHello(@RequestBody Map<String, String> prompt);
	}
	
	```
	
	```java
	@Service
	public class MyFeignClientService {
	    private final MyFeignClient myFeignClient;
	
	    @Autowired
	    public MyFeignClientService(MyFeignClient myFeignClient) {
	        this.myFeignClient = myFeignClient;
	    }
	
	    public String getHelloMessage(Map<String, String> prompt) {
	        return myFeignClient.getHello(prompt);
	    }
	}
	
	```


