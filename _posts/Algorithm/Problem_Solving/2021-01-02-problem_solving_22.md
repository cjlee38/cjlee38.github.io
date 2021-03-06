---
layout: post
title:  "# 백준[No.1676] - 팩토리얼 0의 개수 ( Java )"
date:   2021-01-02 22:17:00 +0900
categories: problem-solving
tags: baekjoon
author: cjlee
cover: /assets/covers/coding.png
---

[문제링크](https://www.acmicpc.net/problem/1676)

# Problem

![](/assets/images/2021-01-02-22-16-45_2021-01-02-problem_solving_22.md.png)

# Solve

## 접근 방법
: 문제를 푸는 원리만 이해하면, 구현은 쉽게 할수 있는 문제다.

우선, 주어진 문제의 이해를 위해 `factorial(10)` 을 구해보면, 3628800 이라는 숫자가 나온다. 그리고 가장 뒤쪽에서부터 0의 개수를 세보면, 2개 라는 정답을 얻을 수 있다.

그러나, 이를 직접 계산해서 0의 개수를 세는, 즉 **시뮬레이션**을 하게 되면 아주 치명적인 문제가 발생하는데, 문제의 입력 조건에서도 보이듯이 최대 `factorial(500)`까지 갈 수 있고, 이는 

122013682599111006870123878542304692625357434280319284219241358838584537315388
199760549644750220328186301361647714820358416337872207817720048078520515932928
547790757193933060377296085908627042917454788242491272634430567017327076946106
280231045264421887878946575477714986349436778103764427403382736539747138647787
849543848959553753799042324106127132698432774571554630997720278101456108118837
370953101635632443298702956389662891165897476957208792692887128178007026517450
776841071962439039432253642260523494585012991857150124870696156814162535905669
342381300885624924689156412677565448188650659384795177536089400574523894033579
847636394490531306232374906644504882466507594673586207463792518420045936969298
102226397195259719094521782333175693458150855233282076282002340262690789834245
171200620771464097945611612762914595123722991334016955236385094288559201872743
379517301458635757082835578015873543276888868012039988238470215146760544540766
353598417443048012893831389688163948746965881750450692636533817505547812864000
000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000 


라는 아주 말도안되게 큰 숫자가 나온다.

물론 BigInteger 과 같은 클래스를 활용하는 방법이야 있겠지만, 문제의 본질에서 한참을 어긋나게 된다. 그렇다면 어떻게 해결해야 할까? 조금만 고민을 해보면, 두 자리수 이상의 숫자에서, 0 이라는 숫자로 끝난다는 것은, 이 숫자가 **5 라는 숫자를 반드시 인수로 갖고 있다**는 뜻이 된다.

즉, 10 이라는 숫자는 2 * 5 로 구성되어 있으며, 20 이라는 숫자는 4 * 5 라는 숫자로 구성되어 있다. 그렇다면 단순히 5 의 개수를 세면 되는가? 정답은 그렇다 이긴 한데, 여기에 근거를 조금 더 붙여보자.

가령, 25 라는 숫자는, 5 * 5 로 구성되어 있으므로, 5를 인수로 갖고 있음에도 불구하고 0 이 등장하지 않는다. 15 라는 숫자 또한 마찬가지로, 3 * 5 로 구성되어 있으므로, 5 를 인수로 갖고 있음에도 불구하고, 뒤에 0 이 붙지 않는다. 

그 이유는, 바로 2 라는 숫자의 부재 때문이다. 2 가 없는 5 는, 10 이라는 숫자를 구성할 수 없다. 그리고 그 기저를 한 단계 더 파고들어보면, 짝수와 홀수가 갖는 곱셈의 성질에 대해서도 생각해 볼 수 있다.

무슨 말인가 하면, 짝/홀수의 곱셈에서, 곱셈은 or 로, 짝수는 true 로 비유해볼 수 있다는 것이다. 즉,

- 짝수 * 짝수 = 짝수
- 짝수 * 홀수 = 짝수
- 홀수 * 짝수 = 짝수
- 홀수 * 홀수 = 홀수

그렇기에, 0 이라는 숫자로 끝나기 위해서는 반드시 짝수가 하나 이상 포함되어 있어야 하며, 그 짝수의 최소(즉, 소인수) 인 2 가 5와 쌍을 이루어주어야, `~0` 이라는 형태의 숫자를 만들어낼 수 있는 것이다.

그러나 우리가 해결하고자 하는 문제인 팩토리얼은, 연속된 자연수를 곱하는 것이고, 따라서 당연하게도 2 의 배수에 해당하는 숫자는 5의 배수에 해당하는 숫자보다 훨씬 더 많이 존재한다. 바꿔 말해, **재료는 충분하다**는 이야기다.

다시 본론으로 돌아와서, 주어진 팩토리얼의 계산 결과가 10 이라면, 이는 2 * 5 로 구성되어 있기에, 즉 하나의 쌍이 적절하게 주어져있기 때문에 하나의 0 이 붙는다.

절대 그럴수는 없지만, 만약 팩토리얼의 계산 결과가 50 이라면 ? 2 * 5 * 5 로 구성되어 있고, 2 라는 재료가 하나 부족하기 때문에, 0 의 개수는 하나가 된다.

문제의 예시로 돌아가서 생각해보자. `factorial(10)` 은 3628800 인데, 여기에는 5 가 두 번 들어간다. 그리고 그 재료가 되는 2의 배수는 [2, 4(2 * 2), 6(2 * 3), 8(2 * 2 * 2), 10(2 * 5)] 의 총 8개로, 주어진 5를 모두 사용하고도 남는다.

조금 더 연장해보자.

`factorial(15)` 는, 5 가 세 번 들어가니, 0 이 총 세 개 붙을 것이라 예상해볼 수 있다. 그리고 이 결과값은 1307674368000 로, 0 이 세 개 붙는다.

그렇다면 `facotrial(25)`는 어떨까? 단순하게 쳐다보면 5 가 다섯 번 들어간다고 생각할 수 있지만, 사실은 마지막에 25 를 곱하는 과정에서 5 가 두 번 들어가기에, 총 여섯 개의 5 가 들어가게 된다. 그리고 다시 말하지만, 2 의 재료 또한 충분하기 때문에, 여섯 개의 5 에 모두 쌍을 맞추어줄 수 있다. 실제 계산 결과값 또한 15511210043330985984000000 이다.

## 구현
: 여기까지 이해했다면, 구현하는데에는 전혀 어려움이 없다. 1부터 주어진 숫자까지 반복하는 과정 속에서, 현재 숫자가 5 로 나누어진다면, 또 5 를 곱해서 나눠보고.. 를 그 내부에서 반복하면 된다.

전체 코드는 다음과 같다.

```java
package BOJ.clazz.lv3;

import java.io.*;

/**
 * uri = https://www.acmicpc.net/problem/1676
 * name = 팩토리얼 0의 개수
 */

public class bj1676 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int ans = 0;

        for (int i = 1; i <= n; i++) {
            int div = 5;
            while (i % div == 0) {
                ans++;
                div *= 5;
            }
        }

        bw.write(ans + "");
        bw.flush();
        bw.close();
    }
}

```
