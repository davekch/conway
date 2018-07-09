#include<random>
#include<iostream>
#include<vector>
#include"cnpy.h"
using namespace std;

class grid{
private:
    vector<vector<int>> alive;
    int step = 0;
public:
    void randomPopulate(int density){
        vector<vector<int>> newvec;
        uniform_real_distribution<double> uni(0, 1);
        default_random_engine engine;
        for(int i=0;i<500;++i){
            vector<int> line;
            for(int j=0;j<500;++j){
                uni(engine)<density/100. ? line.push_back(1) : line.push_back(0);
            }
            newvec.push_back(line);
        }
        alive = newvec;
    }

    int countLiveNeighbours(int i,int j){
        int liveNeighbours=0;
        for(int di=-1;di<2;++di){
            for(int dj=-1;dj<2;++dj){
                if(!(di==0&&dj==0) && !(i+di>=alive.size()||j+dj>=alive[0].size())){
                    if(alive[i+di][j+dj]==1) liveNeighbours++;
                }
            }
        }
        return liveNeighbours;
    }

    void tick(){
        int liveCells = 0;
        vector<vector<int>> updated(alive);
        for(int i=0;i<alive.size();++i){
            for(int j=0;j<alive[0].size();++j){
                int liveNeighbours = countLiveNeighbours(i,j);
                if(alive[i][j]==1){
                    liveCells++;
                    if(liveNeighbours<2) updated[i][j]=0;
                    else if(liveNeighbours>3) updated[i][j]=0;
                } else {
                    if(liveNeighbours==3) updated[i][j]=1;
                }
            }
        }
        alive = updated;
        step++;
        // cout<<step<<": Found "<<liveCells<<" live cells      "<<endl;
    }

    void save(){
        size_t N = alive.size();
        size_t M = alive[0].size();
        vector<int> raw(N*M);

        for(int row = 0;row < N; row++) {
           for(int col = 0;col < M; col++) {
              raw[row*M+col] = alive[row][col];
           }
        }

        cnpy::npy_save("field.npy",&raw[0],{N,M},"w");
    }
};


extern "C" {
    grid* grid_new(){ return new grid(); }
    void grid_randomPopulate(grid* field, int d){ field->randomPopulate(d); }
    void grid_tick(grid* field){ field->tick(); }
    void grid_save(grid* field){ field->save(); }
}
