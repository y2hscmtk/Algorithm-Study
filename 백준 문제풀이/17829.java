import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static int n;
    static int num[][];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        num = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                num[i][j] = sc.nextInt();
            }
        }

        System.out.println(deep(0, 0, n));
    }


    static int deep(int x,int y,int deepth){
        // 깊이가 2가 되면, 비교해서 2번째로 큰 값을 반환할 수 있도록
        if(deepth == 2){
            int temp[] = new int[4];
            int k = 0;
            for(int i = x; i<x+deepth;i++){
                for (int j = y; j < y + deepth; j++) {
                    temp[k++] = num[i][j];
                }
            }
            Arrays.sort(temp); // 오름차순 정렬
            return temp[2]; // 2번째로 큰 값 반환
        }

        // 각자 크기가 2x2 크기가 될때까지 쪼갠다음 원하는 값을 가져오도록 명령
        int length = deepth / 2;
        int temp[] = new int[4];
        temp[0] = deep(x+length, y, length);
        temp[1] = deep(x, y+length, length);
        temp[2] = deep(x+length, y+length, length);
        temp[3] = deep(x, y, length);
        Arrays.sort(temp);
        return temp[2];
    }
}
