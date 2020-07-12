#include <iostream>
#include <queue>
#include <stack>
#include <cstdio>
using namespace std;
int matrix[1002][1002] = {0,};
int visit[1001] = {0,};
int vertex;

void dfs(int start){
    visit[start] = 1;
    printf("%d ", start);
    for(int i=1; i<=vertex; i++){
        if(matrix[start][i] == 1 && visit[i] == 0) dfs(i);
    }
}

void bfs(int start){
    int visit[1001] = {0,};
    int a = start;
    queue<int> q;
    visit[start]=1;
    q.push(start);
    while(!q.empty()){
        for(int j=1; j<=vertex; j++){
            if(matrix[a][j]==1 && visit[j] == 0) {
                q.push(j);
                visit[j] = 1;
            }
        }
        printf("%d ", q.front());
        q.pop();
        a = q.front();
    }
    printf("\n");
}

int main() {
    int n,weight;
    int weight1,weight2;
    scanf("%d %d %d", &vertex, &weight, &n);
    for(int i=0; i<weight; i++){
        scanf("%d %d", &weight1, &weight2);
        matrix[weight1][weight2] = 1;
        matrix[weight2][weight1] = 1;
    }
    // matrix 확인
    // for(int i=1; i<=vertex; i++){
    //     printf("Matrix : ");
    //     for(int j=1; j<=vertex; j++){
    //         printf("%d", matrix[i][j]);
    //     }
    //     printf("\n");
    // }
    dfs(n);
    printf("\n");
    bfs(n);
    return 0;
}
