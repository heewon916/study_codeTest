# 배열 정렬 
1. 2차원 배열 
- 2차원 배열의 [0]번째 값을 기준으로 오름차순 정렬: 
```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[][] arr = { {3, 4}, {1, 9}, {2, 7} };

        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        for (int[] row : arr) {
            System.out.println(Arrays.toString(row));
        }
    }
}
```

- 2차원 배열의 [1]번째 값을 기준으로 오름차순 정렬 
```java
Arrays.sort(arr, (a, b) -> Integer.compare(a[1], b[1]));

```

2. 1차원 배열
→ List로 변환 후 Collections.sort() 또는 Arrays.sort()
→ Comparator<String>을 사용해 길이 + 사전순 기준 지정

```java
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        String[] arr = {"apple", "dog", "banana", "cat", "elephant"};

        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return Integer.compare(s1.length(), s2.length());
            }
        });

        // 결과 출력
        System.out.println(Arrays.toString(arr));
    }
}

```

3. 길이 -> 사전순 정렬
```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 중복 제거를 위한 Set
        Set<String> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }

        // List로 변환해서 정렬
        List<String> list = new ArrayList<>(set);

        // 정렬 기준 적용
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.length() != s2.length()) {
                    return s1.length() - s2.length(); // 길이 오름차순
                    // s1.length() - s2.length()가 음수면 s1이 앞으로, 양수면 s2가 앞으로 감
                    // 내림차순 정렬: return s2.length() - s1.length(); 
                }
                return s1.compareTo(s2); // 사전순
            }
        });

        // 결과 출력
        for (String s : list) {
            System.out.println(s);
        }
    }
}

``` 

4. Comparator.reversed() 
- 기존 Comparator를 내림차순으로 바꿔주는 메소드 
- Comparator 객체 뒤에 .reversed()를 붙이면 정렬 순서가 반대로 적용됨 

사전순 내림차순
```java
List<String> list = Arrays.asList("apple", "dog", "banana");

list.sort(Comparator.naturalOrder().reversed()); // 기본 오름차순을 뒤집음

System.out.println(list); // [dog, banana, apple]

```

길이기준 정렬 + reversed()
```java
list.sort(Comparator.comparingInt(String::length).reversed());

```

복합 조건 정렬 (길이 내림차순, 사전 오름차순)
- reversed 붙이면 내림차순 정렬 
- String::length s -> s.length()와 같음 
```java
list.sort(
    Comparator.comparingInt(String::length).reversed() // 1. 길이 내림차순
              .thenComparing(Comparator.naturalOrder()) // 2. 사전순 오름차순
);

```