## 모놀리스 아키텍쳐
- 하나의 프로세스, 하나의 DB endpoint, 한줄 수정 -> 전부 재배포
	- 멀티모듈로 구성하더라도 CI의 단위만 달라질 뿐 CD의 범위는 전체

- 장점
	- 배포가 간단하고 유지보수가 비교적 쉽다
		- 공통 모듈등을 활용하기 쉽다
	- 리소스사용이 효율적
		- 과거 일반적이었던 IDC(Server, DB)는 비싼 자원이었다
		- 비싼 서버 리소스를 최적화해서 사용 가능
- positive use case
	- 새로운 서비스, 소수의 팀원, 빠른 초기 구현, 금융/보안 중요성, DevOps 역량 부족

- 단점
	- Scale Out이 어렵다
		- 단일 DB 의존성이 크다
	- 배포가 오랜 시간 걸린다
	- 장애 시 전체 서비스 다운
- negative use case
	- DevOps 역량 충분, 보안보다는 빠른 기능 개발과 배포가 중요, 많은 서비스를 동시 다발적으로 개발

## SOA(Service Oriented Architecture)
"서비스" 단위로 개발, 서비스 간 규격화된 인터페이스로 통신
- 보통 같은 기술 스택으로 개발
- ESB(Enterprise Service Bus)를 사용해서 요청에 대한 로직을 캡슐화한 Layer 존재
	- MSA에 반하는 개념
	- ESB <-통신-> (Service, Service...)

- 서비스 간 통합을 강조
	- Shared DB 사용
- 동일 플랫폼에서 서비스 간 호출로 성능 이슈 존재

## MSA(Micro services Architecture)
"서비스" 단위로 개발, 서비스 마다 독립적으로 개발/배포 가능
- 비즈니스 로직(서비스)의 재사용 지양..
	- 서비스 간 결합도를 낮추는 것이 근본적인 목표이다
- 최적의 기술 스택을 독립적으로 선택 가능
- 서비스 간 자유로운 방식으로 통신 가능
- Business Capa : 요구사항 변화에 따른 빠른 대처
	- 빌드 / 배포  : CI/CD, 자동화, API Gateway

#### 핵심원칙
- ***Business Capabillties : 조직이 얼마나 빠르고 유연하게 변화에 대응할 수 있는지에 대한 능력***
	- Conway's Law : 시스템이 설계되면, 그 시스템의 구조는 설계한 조직의 구조와 유사해진다
		- 빠른대처가 가능한 msa로 설계하면 그에 맞는 조직구조로 변화한다, 선순환
		- 일반적인 조직구조 : (백엔드), (프런드엔드), (DBA)
		- 변화하는 조직구조 : (business/domain(백엔드, 프런트엔드, DBA)), (business/domain(백엔드, 프런트엔드, DBA)),...
			- 하나의 역할이 아닌 여러 역할을 할 수 있는 사람 필요.. ~~backend engineer~~가 아닌 software engineer
	> ***빠른 대처가 필요한 비즈니스 모델 == 빠른 대처가 가능한 MSA***

- Products, not Projects 
	- project는 1회성..(SI 방식, 개발 따로 유지보수 따로, 저렴..)
	- 직접개발한 사람이 유지보수를 하는게 가장 빠르다..

- Smart endpoints and dumb pipes : 단순한 방식의 프로토콜 사용
- Decentralized Data Management / Governance
	- 데이터 유연성, 탄력성의 확보
	- 비즈니스 필요성에 따른 최적의 기술스택 사용해야 한다
		- 닭 잡는데 소 잡는 칼 쓰지 말자
- Infrastructure Automation : 자! 동! 화!

- Design for Failrue : 시스템 에러를 예상한 설계 필요
	1. 감지(Circuit Breaker) 
		- 서킷 브레이커 : 특정 시스템이 정상동작 하지 않을 때 트래픽을 다른 정상 노드로 옮기는 등의 역할(장애 감지, 차단, 복구)
			- 모놀리식에는 없던 기능(if문으로 처리하던 기능)
			- 특정 레이어 안에서는 K8S 보다 세밀한 조절 가능
	2. 복구(K8s) 
		- K8S : Deployment, Replica set
			- Rediness probe(준비 상태 검사), liveness probe(활성 상태 검사)등으로 어플리케이션 상태 검사및 처리
			-  서킷 브레이커보다 위층 레이어, 인프라 측면에서 동작
	3. 의도치 않은 결과 방지(Transaction, Event Driven) 
		- Event Driven Architecture (EDA) : 시스템 구성 요소가 이벤트를 통해 서로 통신하는 방식
			- message broker를 사용해서 이벤트를 감지
			- 각 노드에서 로직의 특정부분이 실패하더라도 이벤트가 제대로 처리됬다면 트랜잭션을 성공으로 처리할 수 있다.. 이러한 로직등을 관리
	4. 서비스 간의 영향도(Chaos Test)
		- Chaos Engineering 
			- 응답 속도를 늦추는 등... 통신에 부하를 주는 등의 테스트를 통해 각 노드의 영향도를 테스트 할 수 있다

#### 분산 시스템이 어려운 이유
- **IPC(Inter Process Communication)**
	- 출처: [https://jwprogramming.tistory.com/54](https://jwprogramming.tistory.com/54) [개발자를 꿈꾸는 프로그래머:티스토리]
	- MSA 환경에서 서비스 간 통신은 HTTP/gRPC등을 활용
		- Keepalive? Connection Pool? Connection/Business Logic Timeout의 차이등의 이해 필요
	- CI/CD 측면에서 Devops, SRE 가 책임질 수 있는 부분들에 한계가 존재
		- 로깅, 모니터링 등 각 서비스 간 동작 방식을 알아야 트러블 슈팅이 가능하다(서비스간의 결합도가 낮기 때문)

- **Transactions**
	- 분산환경 트랜잭션에 대한 이해 -> 2PC, 보상 트랜잭션 - Saga
		- 보상 트랜잭션 : 다른 프로세서간의 트랜잭션 공유할 수 없기 때문에 트랜잭션 실패 시 해당 메시지를 다시 던진다
	- 분산환경에서는 트랜잭션관련 구현이 어렵다.. 트랜잭션이 없는 게 베스트
	- Data Query의 어려움
		- ***API 조합 패턴*** : 여러 프로세스의 API를 조합해서 원하는 결과를 얻는 것
			- DB가 여러개이기 때문에 연관있는 데이터가 여러 DB에 나뉘어 져있다... 원하는 데이터를 얻기 위해 여러 DB를 뒤져야 함

- **Monitoring**
	- 하나의 요청에 대한 모니터링(레이턴시등)이 각 서비스에 나뉘어져 있기 때문에 단번에 파악이 어렵다
	- 어떤 트랜잭션이 어느 구간에서 왜 문제가 발생했는지...
