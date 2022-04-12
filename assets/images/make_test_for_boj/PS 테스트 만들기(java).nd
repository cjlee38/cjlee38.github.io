# PS 테스트 만들기
코딩테스트를 준비하는 여러분 중 대부분은 아마 백준이나 프로그래머스를 많이 사용하실텐데요.
해당 사이트에서 주어지는 환경 날 것을 그대로 사용하기는 아무래도 어렵고, IDE 에서 코드를 작성한 뒤 복사 붙여넣기 하는 경우가 대부분일 것 같습니다.

저는 자바를 좋아하는데, 프로그래머스에서는 클래스 내의 함수를 작성하는 형태로 문제가 주어지기 때문에, 그닥 어렵지 않게 코드를 작성하고, 또 그 결과를 확인할 수 있는 반면, 표준 입출력을 활용하는 백준은 코드 작성이 조금 귀찮은 편입니다.

상대적으로 코드가 (조금 더) 긴 `BufferedReader` 클래스를 활용해야 조금 더 빠른 입출력이 가능하다는 점이나 , 코드가 올바르게 작성됐는지 확인하기 위해 표준 입력에 매번 테스트케이스를 복사해서 넣어주어야 한다는 점이 그렇죠.

제가 지금까지 작업해왔던 방식을 생각해보면 다음과 같습니다.

1. 문제를 읽어본다.
2. 어떻게 문제를 풀지 생각하면서, IDE 내에 코드를 작성한다.
3. 완성된 코드를 실행한다.
4. 예제 입력을 클립보드에 복사하고, 이를 표준 입력에 붙여 넣는다.
5. 결과가 올바른지 확인한다.

이 과정을 조금 간소화하고자, `Live Template` 그리고 `Junit` 을 이용하기로 했습니다.

## 1. Live Template
Live Template은, 코드의 템플릿을 저장해두면, 코드의 작성을 편리하게 사용할 수 있도록 해주는 intellij의 기능 중 하나입니다. 지금까지 코드를 작성하면서, `sout` , `psvm`, `main`, `iter` 등 다양한 축약을 이용해왔는데, 이 녀석들이 바로 Live Template 이었습니다.

해당 설정은 다음에서 확인할 수 있습니다.
> Preferences -> Editor -> Live Template  

![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/6ED8497E-E56E-42D6-B328-20A2E951F1BC.png)
Java 부분을 살펴보니, 지금껏 사용했던 것들 이외에도 여러 유용한 것들이 있는 것을 볼 수 있습니다. 이것은 나중에 천천히 살펴보기로 하고, 우선 우측 상단의 + 버튼부터 눌러봅시다.

	1. Live Template
	2. Template Group
 
의 두 가지 항목이 있을텐데요. 템플릿 그룹을 먼저 만든 뒤, 해당 그룹에 내가 만든 템플릿을 넣어보도록 하겠습니다.
템플릿 그룹은 간단하게 이름만 지어주면, 해당 그룹이 생긴것을 볼 수 있는데요. 저는 좀 눈에 띄게 `-*- custom-*-` 이라고 만들었습니다.

![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/1AF185DE-D861-43E9-BE8C-458631B45551.png)

기존에 제가 만들어둔 템플릿도 보이네요. 해당 내용은 잠시 후에 보여드리는 것으로 하고, 손댈 부분만 살펴보면 다음과 같습니다.

> 1. Abbreviation : 사용할 축약어를 의미합니다. 가령 `sout`, `psvm` 정도가 되겠네요.  
> 2. Description : 일종의 주석입니다. 해당 축약어의 설명 정도로 표현할 수 있겠네요.  
> 3. Template Text : 실제 나타날 코드가 작성될 부분입니다.   
> 4. Edit Variables : 템플릿에서 사용할 변수에 대한 상세한 내용을 작성할 수 있습니다.  

1, 2번이야 쉽게 쓸 수 있지만, 3,4 번은 조금 난해하게 다가옵니다. 이럴 때엔 남에꺼 보고 베끼는게 최고입니다.
다시 Java 탭으로 돌아가서, 대충 `iter` 를 한번 살펴봅시다.


![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/A18827F6-638B-4EC3-AF79-9662E3965D89.png)

더더욱 모르겠습니다. 방금 했던 말은 취소하고, 역시 공식 문서를 봅시다.

[Live template variables | IntelliJ IDEA](https://www.jetbrains.com/help/idea/template-variables.html)

공식 문서를 보고 오니 대충 알 것 같습니다.
$ $ 기호로 묶어서 변수를 정의할 수 있고, 이에 대한 내용은 predefined functions 를 활용해서 좀 더 편하게 작성할 수 있다는 것처럼 보이네요. 본 포스팅에서의 핵심은 Live template이 아니니 대충 이정도만 알고 넘어가도 될 것 같습니다.

앞서 생성했던 템플릿으로 돌아와서, 마저 작성해봅니다. Abbreviation 은 temp, Description은 생략하고, Template text에 다음과 같이 입력했습니다.

```java
import java.io.*;
import java.util.StringTokenizer;

public class bj$NUMBER$ {

    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));) {

            // == do == //


            // == done //
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static StringTokenizer tokenize(BufferedReader br) throws IOException {
        return new StringTokenizer(br.readLine());
    }

    private static int bInt(BufferedReader br) throws IOException {
        return Integer.parseInt(br.readLine());
    }

    private static int sInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

    static class Solution {

        public int run() {

            return -1;
        }

    } // end of class
}

```

제가 기존에 주로 사용하던 형태는 이와 같습니다. 몇 가지 편의를 위해 tokenize, bInt 와 같은 함수도 추가했습니다.
클래스 이름쪽도 한번 살펴보면, bj$NUMBER$ 와 같은 형태로 구성되어 있습니다. 해당 bj부분에 문제 번호를 입력할 예정입니다.

이렇게 작성하고나서, `No applicable contexts` 옆의 Define 을 눌러서, Java 를 체크해줍시다.

그리고, java 파일을 하나 생성해서, temp 입력 후 tab 을 눌러 잘 동작하는지 확인해봅니다.

![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/6B847F79-7FC2-444E-9770-545BC428C64E.png)


한 단계만 더 나가보겠습니다. 저는 각 문제마다 주석을 다는데, 예시는 다음과 같습니다.

```java
/**
 * uri = https://www.acmicpc.net/problem/2573
 * name = 빙산
 * tier = gold 4
 * date = 2021-07-29, 목, 20:3
 */
```

따라서, 템플릿 텍스트는 다음과 같이 써주었는데요.
```java
/**
 * uri = https://www.acmicpc.net/problem/$NUMBER$
 * name = $NAME$
 * tier = $TIER$
 * date = $DATE$
 */

public class bj$NUMBER$ { 
...
}
```

여기서 다른 부분은 어쩔 수 없이 수기로 입력해야 하지만, 날짜는 아무래도 현재시각으로 자동으로 입력되면 좋겠죠.
아까 보았던 Edit variables 버튼을 눌러봅시다.

저는 [Live template variables | IntelliJ IDEA](https://www.jetbrains.com/help/idea/template-variables.html#predefined_functions) 에서 다음과 같은 내용을 확인했기 때문에, 이를 활용해서 작성했습니다.

![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/C4DDBDC0-A399-4EB2-B8EE-CFCE8D887A40.png)

![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/70A2E005-A6C6-4502-8887-D500912848EF.png)
이렇게 까지 해주면, 크게 불편함 없이 템플릿을 활용할 수 있습니다.
```java
package BOJ;

import java.io.*;
import java.util.StringTokenizer;

/**
 * uri = https://www.acmicpc.net/problem/TEMP
 * name =
 * tier =
 * date = 2021-07-30, 금, 7:53
 */

public class Temp {
...
}

```

## 2. JUnit
JUnit은 스프링을 공부하면서 손쉽게 사용할 수 있었는데요. Gradle 혹은 Maven 기반의 프로젝트로 생성되다 보니, 의존성만 추가하면 사용하는데에 큰 무리가 없었습니다. 문제는 지금까지 PS 로 사용하고 있던 프로젝트가 일반적인 Java 프로젝트 였다는 것입니다. 찾아보니, Intellij에서 Maven 프레임워크를 추가할 수 있는 기능을 제공하고 있었습니다. 


![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/CCF4BB0C-64DB-48AF-8F0D-13E137665080.png)


좌측 프로젝트 탭에서, 최상위 경로인 PS를 우클릭하면, 위와 같이 Add Framework Support 를 볼 수 있습니다. 클릭하고, Maven을 추가하면 됩니다. 그리고 역시, pom.xml 에 Junit 의존성을 추가해주었습니다.

```xml
<dependencies>
    <!-- https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-api -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.7.0</version>
        <scope>test</scope>
    </dependency>

    <!-- https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-engine -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.7.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

다음 문제는, "어떻게 테스트 케이스를 작성할 것인가?" 입니다. 기존에 터미널에 입력하던 표준 입출력을, 문자열로 다룰 수 있어야 하는데요.
`BufferedReader` 클래스의 인자로 넘겨주는 `Reader` 추상 클래스를 구현하는 클래스를 넘겨줄 수도 있겠습니다만, 문제는 `Writer` 입니다. 기존의 코드를 수정하지 않고 표준 출력을 문자열로 받아내고 싶었습니다. 찾아보니, `System.setOut()` 혹은 `System.setIn()` 메소드를 통해, 적절하게 입출력 스트림 자체를 제어할 수 있었습니다.

그리고 여기에 `ByteArrayInputStream`과 `ByteArrayOutputStream` 을 세팅해서, ByteArray로부터 읽고, ByteArray로 쓸 수 있도록 해봅시다.

```java
ByteArrayInputStream inputStream = new ByteArrayInputStream(inputExample.getBytes(StandardCharsets.UTF_8));
ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
System.setOut(new PrintStream(outputStream));
System.setIn(inputStream);
```

잘 동작하는지 확인하기 위해, 가장 쉬운 1000번 문제인 A + B 를 테스트해보겠습니다.

```java
@Test
public void test() throws Exception {
    // given
    String inputExample = "3 4"; // 예제 입력

    ByteArrayInputStream inputStream = new ByteArrayInputStream(inputExample.getBytes(StandardCharsets.UTF_8));
    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    System.setOut(new PrintStream(outputStream));
    System.setIn(inputStream);

    // when
    Temp.main(new String[]{}); // 테스트 실행

    // then
    String outputExample = outputStream.toString();
    assertEquals(outputExample, "8"); // 결과 확인
}
```

3 + 4 는 8이 아니니, 에러가 발생해야 합니다. 결과는 다음과 같습니다.

![](PS%20%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5(java)/674EB982-9AA2-46F9-AF8A-80DCF5A3377D.png)

마지막으로, 해당 테스트는 IDE 에서만 사용할 것이므로, 반복되는 코드를 제거하고자 해당 Input / Output Stream 을 하나의 클래스로 만들겠습니다.

```java
public class StreamHandlerForTest {

    private ByteArrayInputStream inputStream;
    private ByteArrayOutputStream outputStream;

    public StreamHandlerForTest(String input) {
        inputStream = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        outputStream = new ByteArrayOutputStream();
        System.setIn(inputStream);
        System.setOut(new PrintStream(outputStream));
    }

    public String get() {
        return outputStream.toString();
    }
}
```

그리고, 테스트는 여러개가 들어갈 수 있으니, Parameterized Test를 사용해서 다음과 같이 깔끔하게 정리하겠습니다.
```java
class TempTest {

    private StreamHandlerForTest handler;

    @ParameterizedTest
    @MethodSource("provideParameters")
    public void test(String input, String output) throws Exception {
        // given
        handler = new StreamHandlerForTest(input);

        // when
        Temp.main(new String[]{}); // 테스트 실행

        // then
        assertEquals(output, handler.get());
    }

    private static Stream<Arguments> provideParameters() {
        return Stream.of(
                Arguments.of("3 4", "7"),
                Arguments.of("1 9", "10")
        );
    }
}
```

마찬가지로, 이 녀석 또한 Live Template에 적용시켰습니다. 하는 방법은 위에서 다뤘으니 여기선 다루지 않겠습니다.
삶이 조금 더 윤택해진 것 같습니다.

> 해당 템플릿은 [여기](https://github.com/cjlee38/PS/blob/master/live_template_boj.xml) 에 업로드 했습니다.   