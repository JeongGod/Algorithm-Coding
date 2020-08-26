#include <cstdio>
#include <map>
using namespace std;
map<int,int> card;
int main() {
    int n,m,ans;
    int temp;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d", &temp);
        card[temp]++;
    }
    scanf("%d", &m);
    map<int,int>::iterator iter;
    for(int i=0; i<m; i++) {
        ans = 0;
        scanf("%d", &temp);
        iter = card.find(temp);
        if(iter != card.end()) {
            printf("%d", iter->second);
        } else {
            printf("0");
        }
        if(i==m-1) break;
        printf(" ");
    }
    printf("\n");
    return 0;
}

/*
Map으로 이용한 operator [] 연산으로 해볼라했지만, 시간초과가 난다.
왜냐하면 []연산을 하면 만약 해당 key가 없을 경우에 key:default값이 삽입이 된다.
그래서 50만개를 입력받고, 50만개를 비교하는 이 문제에서는 worst case가 100만개를
삽입하게 되는 경우가 있다. 그래서 시간초과가 난다.
find를 사용한다면, 50만개로 줄어들어 성공하겠지만, 이 방법도 시간이 많이 소모한다.

그래서 counting sort를 이용한다면 시간은 단축되지만, 메모리소모는 map보다는 많이 된다.
*/