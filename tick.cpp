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
    void randomPopulate(){
        vector<vector<int>> newvec;
        uniform_real_distribution<double> uni(0, 1);
        default_random_engine engine;
        for(int i=0;i<10;++i){
            vector<int> line;
            for(int j=0;j<10;++j){
                uni(engine)<0.1 ? line.push_back(1) : line.push_back(0);
            }
            newvec.push_back(line);
        }
        alive = newvec;
        cout<<endl<<"size: "<<alive.size()<<"x"<<alive[0].size()<<endl;
        for(int i=0;i<10;++i){
            for(int j=0;j<10;++j){
                cout<<alive[i][j]<<" ";
            }
            cout<<endl;
        }
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
        cnpy::npy_save("field.npy", &alive[0][0], {alive.size(),alive[0].size()}, "w");
    }
};


extern "C" {
    grid* grid_new(){ return new grid(); }
    void grid_randomPopulate(grid* field){ field->randomPopulate(); }
    void grid_tick(grid* field){ field->tick(); }
    void grid_save(grid* field){ field->save(); }
}
