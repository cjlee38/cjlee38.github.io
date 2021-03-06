---
layout: post
title:  "# 백준[No.1748] - 수 이어 쓰기 1 ( Python )"
date:   2020-08-23 23:58:00 +0900
categories: problem-solving
tags: baekjoon
author: cjlee
cover: /assets/covers/coding.png
---

[문제 링크](https://www.acmicpc.net/problem/1748)

# PROBLEM

![1](/assets/images/2020-08-27-09-21-28_2020-08-27-ps_3.md.png){: .alignCenter}
# SOLVE

: 이번 문제는 이해 하기에 그리 어렵지 않으므로, 바로 해결 방법으로 진행한다.

###  1) 첫 번째 방법 ( feat. Out of Memory )

: 첫 번째 잘못된 접근은, 모든 숫자를 다 구해서 String으로 캐스팅해서 리스트에 담은 뒤, 이를 모두 concatenate 하는 것이다. 문제를 그대로 이해하고 그대로 해결하고자 하는 것이다. 

```python
N = int(input())
numbers = [str(i) for i in range(1, N+1)]
print(len(''.join(numbers)))
```

그러나, 입력의 최대 값이 1억이므로, 이를 모두 이어 붙이게 되면 굉~장히 긴 String이 등장할 것이다.

---

> 여담으로, python의 String 크기에 대해서 구글링 해보니, 메모리 상의 String의 크기는 "Overhead + 실제 String"으로 구성되고, 직접 확인해보니 Overhead는 Python version 3.7.4 기준 49로 나타났다. 실제 String이 차지하는 bytes의 크기는 character의 종류에 따라 다르고 ( 가령, 알파벳은 1, 한자는 2, 이모지는 4를 차지한다고 한다. ) 숫자의 문자열의 크기는 1 임을 확인할 수 있었다. 
>
> 입력이 1억일 때의 숫자의 길이는 788888898이고, 따라서, 788888898 + 49 = 788888947 약 752메가로 나타났다. 간단한 문제를 해결하기엔 너무 큰 메모리 소모다.
>
>이에 더해, Python의 String은 immutable 객체다. 1억 번의 메모리를 할당하는 것은 잠깐만 생각해도 비효율적으로 느껴진다.

---

###  2) 두 번째 방법 ( feat. Time Complexity )

: 두 번째 잘못 된 접근법은, 곧바로 하나하나 계산해서 더하는 것이다.

예제의 입력이 120이므로, 1부터 120까지 loop를 돌면서

'1의 자릿수의 길이(1)' + '2의 자릿수의 길이(1)' + ... + '10의 자릿수의 길이(2)' + '11의 자릿수의 길이(2)' + ... + '119의 자릿수의 길이(3)' + '120의 자릿수의 길이(3)' = 252

를 구하게 되면, 아주 간단해 보인다.

``` python
N = int(input())
result = 0
for i in range(1, N + 1):
    result += len(str(i))
print(result)
```

But, 역시 입력의 최대 값은 1억이다. 따라서, 이를 모두 계산하게 되면 매우 긴 시간이 걸릴 것은 자명하다. 

이 역시 한번 실제로 테스트를 해보니, **1억번 연산하는데 약 50초 가량**이 걸렸다. 

###  3) 세 번째 방법 

: 이 문제의 아주 자명하면서도 간단한 사실은 바로 **"특정 자릿수의 길이"를 갖고 있는 숫자의 범위를 파악하기가 매우 쉽다**는 것이다.

 1 - 9 까지의 숫자의 자릿수의 길이는 1이다.

 10 - 99 까지의 숫자의 자릿수의 길이는 2이다.

 100 - 999 까지의 숫자의 자릿수의 길이는 3이다.

따라서, 다음과 같이 해결하면 된다.

-   입력값의 '최대 자릿수의 길이 미만'의 '자릿수의 길이'를 계산할 때는, 최종 값에 **'해당 자릿수의 길이 \* 해당 자릿수의 개수'**를 더해준다.
-   '최대 자릿수의 길이'를 계산할 때에는, **'최대 자릿수의 길이 \* 나머지 자릿수의 개수'**를 더해준다.

말로 설명하니 무슨 말인지 헷갈린다. 문제의 예시를 통해 풀어서 설명하면 다음과 같다.

-   "최대 자릿수의 길이"는 3이다.
-   따라서, 그 미만의 길이일 때에는 ( 즉, 1, 2 일 때에는 각 자릿수의 개수인 9와 90을 각각 곱한 뒤 더해준다 ) 
-   따라서, 처음 1부터 9까지를 더하면, 1(길이) \* 9(개수)이므로,  result는 9다.
-   10부터 99까지를 더하면, 2(길이) \* 90(개수) 인 180이 더해지므로, result는 189다.
-   마지막으로 100부터 120까지를 더하면, 3(길이) \* 21(개수) 인 63이 더해지므로, result는 252이다.

이를 코드로 구현하면 다음과 같다.

```python
N = int(input())
nines = [int('9'+'0'*i) for i in range(0, len(str(N)))] # if 120 --> [9, 90, 900]
result = 0

for i, s in enumerate(nines):
    if s == nines[-1]: # 마지막 자릿수를 계산할 때
        result += len(str(s)) * (N - sum(nines[:-1])) # result += 3 * 21
    else :
        i += 1
        result += i*s

print(result)
```

252번의 iteration이 발생하는 첫 번째 방법이나, 두 번째 방법과 달리, **단 3번의 iteration**만으로 답을 구할 수 있다. 1**억까지 계산하더라도 9번의 연산**으로 끝낼 수 있다.

# 마치며

아직도 부족한 점이 느껴진다. 머릿속으로 세 번째 방법에 대해서 떠올리고 설계하는 데에는 오래 걸리지 않았지만, 이를 코드로 구현함에 있어서 손가락이 자꾸 멈추니 스스로가 답답하게 느껴진다.