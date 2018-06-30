#include<iostream>
#include<vector>
#include"cnpy.h"
using namespace std;

class grid{
private:
    vector<vector<int>> alive;
public:
    void randomPopulate(){
        for(int i=0;i<1000;++i){
            vector<int> line;
            int odd=0;
            if(i%2==0) odd=1;
            for(int j=0;j<1000;++j){
                line.push_back(odd);
            }
            alive.push_back(line);
        }
    }

    int countLiveNeighbours(int i,int j){
        int liveNeighbours=0;
        for(int di=-1;di<2;++di){
            for(int dj=-1;dj<2;++dj){
                if(!(i==0&&j==0) && !(i+di>alive.size()||j+dj>alive.size())){
                    if(alive[i+di][j+dj]==1) liveNeighbours++;
                }
            }
        }
        return liveNeighbours;
    }

    void tick(){
        vector<vector<int>> updated = alive;
        for(int i;i<alive.size();++i){
            for(int j;j<alive[0].size();++j){
                int liveNeighbours = countLiveNeighbours(i,j);
                if(alive[i][j]==1){
                    if(liveNeighbours<2) updated[i][j]=0;
                    else if(liveNeighbours>3) updated[i][j]=0;
                } else {
                    if(liveNeighbours==3) updated[i][j]=1;
                }
            }
        }
        alive = updated;
    }

    void save(){
        cnpy::npy_save("field.npy", &alive[0][0], {alive.size(),alive[0].size()}, "w");
    }
};


extern "C" {
    grid* grid_new(){ return new grid(); }
    void grid_randomPopulate(grid* field){ field->randomPopulate(); }
    void grid_tick(grid* field){ field->tick(); }
    void grid_save(grid* field){ field->save(); }
}