#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;

int visited[100][100], moveY[4]={0,1,0,-1}, moveX[4]={1,0,-1,0};
int check_point = 0;

pair<int, int> find_start(vector<string> maps){
    for(int y=0; y<maps.size(); y++){
        for(int x=0; x<maps[0].size(); x++){
            if (maps[y][x] == 'S') return make_pair(y, x);
        }
    }
}

pair<int, int> find_checkpoint(int start_y, int start_x, vector<string> maps){
    queue<pair<int, int> > q;
    q.push(make_pair(start_y, start_x));
    visited[start_y][start_x] = 1;
    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second; q.pop();
        for(int d=0; d<4; d++){
            int ny = y + moveY[d];
            int nx = x + moveX[d];
            if (ny >=0 && ny < maps.size() && nx >=0 && nx < maps[0].size()){
                if (maps[ny][nx] != 'X' && visited[ny][nx] == 0){
                    if (maps[ny][nx] == 'L'){
                        check_point = visited[y][x];
                        return make_pair(ny, nx);
                    }
                    else{
                        q.push(make_pair(ny, nx));
                        visited[ny][nx] = visited[y][x] + 1;
                    }
                }
            }
        }
    }
    return make_pair(-1, -1);
}

int find_exit(int startY, int startX, vector<string> maps){
    memset(visited, 0, sizeof(visited));
    queue<pair<int, int > > q;
    q.push(make_pair(startY, startX));
    visited[startY][startX] = 1;
    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second; q.pop();
        for(int d=0; d<4; d++){
            int ny = y + moveY[d];
            int nx = x + moveX[d];
            if (ny >=0 && ny < maps.size() && nx >=0 && nx < maps[0].size()){
                if (maps[ny][nx] != 'X' && visited[ny][nx] == 0){
                    if (maps[ny][nx] == 'E'){
                        return visited[y][x];
                    }
                    else {
                        q.push(make_pair(ny, nx));
                        visited[ny][nx] = visited[y][x] + 1;
                    }
                }
            }
        }
    }
    return -1;
}

int solution(vector<string> maps) {
    int answer = 0;
    pair<int, int> start = find_start(maps);
    pair<int, int> lever = find_checkpoint(start.first, start.second, maps);
    if (lever.first == -1 && lever.second == -1) return -1;
    answer = find_exit(lever.first, lever.second, maps);
    if (answer == -1) return answer;
    return answer + check_point;
}