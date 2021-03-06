---
layout: post
title:  "# Hash 맛보기"
date:   2020-09-25 22:52:00 +0900
categories: btb
tags: 
author: cjlee
cover: /assets/covers/coding.png
---
<script type="text/javascript" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML">
</script>

# 0. 들어가며
: Hash 라는 용어는 주로 암호학에서 많이 사용되지만,  
개발자라면 오며가며 한 번쯤은 주워 듣는 용어이기도 하다.

특히, 블록체인을 한 번이라도 공부해봤다면,  
Hash 라는 것이 이 블록체인의 핵심 기술 중 하나라는 것을 배웠을 것이다.

동작 원리를 안다고 해도 복호화(Decryption)가 불가능하므로,  
암호학을 전공하지 않는 한 깊게 파고들 이유는 없다고 생각하지만,  

그렇다고 아예 모르는 것은 개발자에겐 죄악에 가까우므로,  
이번 포스팅을 통해 가볍게 ~~혓바닥 한 번 대서 맛이라도 보자는 느낌으로~~ 건드려보자.

# 1. Hash 에 대한 이론
## 1) What is Hash?
: Hash란, Hash 함수를 이용하여, "어떤 값을 넣더라도" 고정된 길이의 문자열로 바꿔버리는 것을 의미한다.

Wikipedia에서 설명하는 Hash 함수는 다음과 같이 설명하고 있다.

---

>A hash function is any function that can be used to map data of arbitrary size to fixed-size values.

---

즉, 임의의 크기의 데이터가 고정된 크기의 값으로 mapping 시켜버리는 함수를 의미한다.

극단적으로 쉬운 Hash function은, 짝홀수를 만드는 함수다.

다음을 보자.

```java
public int myHash(int value) {
    int hashValue;
    if (value % 2 == 0) {
        hashValue = 0;
    } else {
        hashvalue = 1;
    }
    return hashValue;
}

```
사실, 한 줄로도 작성할 수 있는 코드지만, 일부러 위와 같이 작성했다.  
각설하고, 위와 같은 코드가 하는 일은,   
<u>입력된 숫자가 짝수면 0을, 홀수면 1을 return하는 것이다.</u>

이 myHash() 라는 hash 함수에,   
1을 집어넣든, 1억을 집어넣든, 1조를 집어넣든,   
결국 0 혹은 1의 **고정된 값**이 나온다.

고정된 길이의 값을 출력하므로, 이 함수는 *일단은* Hash 함수라고 이야기 할 수 있다.

## 2) Hash 함수의 특징
: 이러한 Hash 함수는, 다음과 같은 특성을 가진다.

1. 어떠한 값을 입력하더라도, **"고정된 길이"**의 값을 출력한다.
2. 입력값이 조금이라도 바뀌면, 출력값은 달라진다.
3. 복호화가 불가능하다.

여기서 핵심이라고 볼 수 있는 부분은 2번인데,  
주로 암호화 Hash의 경우, Hash 값만 같으면 본래의 값도  
동일하다고 취급하는 것이 주 목적이기 때문에,   
**최대한 Hash 충돌이 일어나지 않도록** 해야 한다.

일례로, 강의를 들었을 때 교수님께서 재미난 비유를 하나 해주셨는데,  
책이 100만 권이 있는 도서관에서, 책의 내용이 단 한 글자라도  
바뀌었는지 알기 위해서는, 모든 책을 다 조사할 필요 없이  
**책들의 내용을 Hash 값으로 보관**해서 그것만 들고 있기만 한다면 된다는 이야기를 하셨다.

물론, 바뀌었을 때 **"어디가 바뀌었는지?"** 에 대해서는 절대 알 수 없다.

## 3) Hash 함수의 성질
: 또한, Hash 함수는 다음을 만족해야 한다.   
(정확히는, Cryptographic Hash. 즉 암호화 Hash는 다음을 만족해야 한다.)

　1\. 원상 회피(Pre-image resistance)
   - 주어진 해시 값 h에 대해, 다음을 만족하는 메시지 m을 찾는 것은 불가능하다.  

$$h = H(m)$$


　2\. 두 번째 원상 회피(Pre-image resistance)
   - 주어진 메시지 m에 대해, 다음을 만족하는 또 다른 메시지 m'을 찾는 것은 불가능하다.    

$$m \neq m' 이면서 H(m) = H(m')$$

　3\. 충돌 회피(Collision resistance)
   - 다음을 만족하는 두 메시지 m과 m'를 찾는 것은 불가능하다.  

$$m \neq m' 이면서 H(m) = H(m')$$

말이 좀 어려우므로, 바꿔서 설명하면 다음과 같다

1. Hash의 결과값을 보고, 본래의 값을 찾는 것은 어렵다.
2. 입력값을 보고, 이 입력과 같은 해쉬값을 출력하는 다른 입력값을 찾는 것이 어렵다.
3. Hash의 결과값이 같은 두 입력값을 찾는 것이 어려워야 한다. 즉, **Hash 충돌**에 안전해야 한다.

이 세 가지를 만족시켜야, 비로소 **"진정한"** 암호화 Hash 함수라고 일컬을 수 있다.

아까 작성했던 짝홀수로 만든 Hash 함수를 보자.   

우리는 0 혹은 1이라는 값을 보고, 본래의 값이 무엇이었는지 알 수 없다. 따라서, 원상회피의 조건을 만족한다.

두 번째로, 우리가 3이라는 값이 주어졌을 때, 5라는 값으로 바꿔 넣으면   
같은 Hash 값인 1이 출력된다는 것을 **쉽게** 알 수 있다.  
따라서, 짝홀수 Hash 함수는 두 번째 원상회피를 만족하지 못한다고 볼 수 있다.

마찬가지로, 0 혹은 1이라는 결과값을 내뱉는 본래의 값은 1,3,5... 임을 **쉽게** 알 수 있다.  
이는 충돌회피 또한 만족하지 못한다고 볼 수 있다.

## 4) Hash 충돌
: 위 짝홀수 Hash 함수가 가장 대표적인 Hash 충돌의 예시가 된다.  
세상 모든 정수는 짝홀수로 구분할 수 있고, 따라서 Hash 값은 무조건 0 혹은 1이 된다.

1과 3은 1이라는 같은 값을 출력하므로 충돌이고,  
1과 5 또한 1이라는 같은 값을 출력하므로 충돌이다.

암호화 Hash 에서는 이 충돌을 막기 위해 다양하고 복잡한 방법을 사용한다.

# 2. Hash에 기반한 공격과 수비
## 1) SHA-256
: 위 Hash 함수의 성질을 지키기 위해, 여러 Hash 알고리즘들이 고안되었다.

당장, [해쉬 생성기](https://www.convertstring.com/ko/Hash/SHA256) 사이트로 이동해서,   
아무런 값이나 입력해보면   
**F03B8A4D721D828D8C972CC84C023EA67022CE5D0F8E650FB59D22E4B187DA6E**  
이러한 알 수 없는 숫자가 튀어나오는 것을 볼 수 있다.

지금 예시로 보여준 Hash 값은 SHA-256의 결과인데, 이름처럼  
256 bit(64글자 * 16진수(4 bit)) 로 생성된 결과임을 알 수 있다.

단순히 생각해보더라도, 256 bit 라면, **2<sup>256</sup>** 이고,  
이는 지수표기법으로는  
**1.1579208923731619542357098500869e+77**   
이라는 말도안되게 거대한 숫자가 나온다.

즉, 단순하게 생각하면 위 숫자의 개수만큼 데이터를 집어넣지 않는 이상, 충돌이 나지 않는다는 이야기다.  
(물론 비둘기집의 원리를 고려하면, 실제로는 그렇지 않겠지만)

---

> 여담으로, Firefox를 이용해서 학교 홈페이지에 로그인 해보니, Firefox의 비밀번호를 저장하겠냐는 질문과 함께 원본 데이터를 볼 수 있었다.  
> 숫자가 뭔가 낯이 익다 싶어서 보니 16진수인 것을 확인할 수 있었고,   
> 위 Hash 생성기에 내 비밀번호를 SHA-512에 넣어보니 같은 값임을 확인할 수 있었다.  
>    
> 이 때, 정말 신기하면서도 "Hash ... 라서 괜찮겠지?" 하고 넘겼던 기억이 난다.  

---

## 2) Rainbow Table
: 결국, 이 Hash 함수는 복호화가 불가능하므로,   
있는대로 때려 맞춰보는 **brute force** 가 Hash 를 뚫는 기본적인 방법이 되시겠다.  

어떤 해커가, 철수라는 사람의 비밀번호의 Hash 값을 알아냈는데,  
이 원본 값을 찾기 위해 가능한 모든 입력값들을 다 때려박아서 비밀번호를 찾아냈다.

그렇다면, 이 철수라는 사람과 같은 Hash 값을 갖고 있는  
다른 모~든 사람들의 원본 값도 다 똑같은 값일 것임은 자명하다.  
그렇다면, **모든 입력값과 모든 Hash 값을 다 저장**해놓는다면 어떨까?

Hash 함수가 취약하다면, 어지간한 Hash의 원본 값은 다 찾을 수 있을 것이다.  
그리고, 매 번 찾을 필요가 없이, 그냥 새로운 해킹 대상이 들어올 때마다  
**미리 저장해놓은 곳**에서 Hash 값을 보고 원본 값을 찾아내서 입력하기만 하면 된다.

**이렇게 저장해놓은 Table을 Rainbow Table**이라 한다.  
(실제로는 이보다 좀 더 복잡한 방식으로 저장한다고 한다.)

## 3) Salting
: Salting. 말 그대로 소금을 치는 것이다.  
Rainbow Table에 맞서 나온 대응책이다.  

원리는 간단하다.   

만약 김철수가 "hello" 라는 값을 비밀번호로 저장하려고 했다면,  
거기에 "Kim" 이라는 값을 추가해서 Hash 함수를 적용한다.

다음으로, 홍길동이 똑같이 "hello" 라는 값을 비밀번호로 저장하려고 했다면,  
거기에 "Hong" 이라는 값을 추가해서 Hash 함수를 적용한다.

즉, "Kim" 혹은 "Hong" 이라는 소금을 치는 것이다.

이렇게 하면, 같은 비밀번호를 사용하더라도 다른 Hash 값이 저장되고,  
**"값이 조금이라도 달라지면 출력값은 완전히 달라지므로"** Rainbow Table에 대응할 수 있게 된다.



# 3. 마치며
: Hash에 대한 개념은, 암호학, 컴퓨터공학을 넘어서 IT에 발가락 하나라도 담그고 있는 사람이라면 반드시 알아야 하는 개념이라고 생각한다.

나중에 정말 여유가 되면, 교수님께 배웠던 블록체인 시리즈도 꼭 다뤄보고 싶다.





# Reference
- 한국외대 이병욱 교수님, 정보보안 강의교안.
- [Hash function](https://en.wikipedia.org/wiki/Hash_function)

