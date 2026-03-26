#include<iostream>
#include<vector>

using namespace std;

class DisjointSet{
        vector<int> rank,parent,size;

    public:
        DisjointSet(int n){
            rank.resize(n+1,0);
            parent.resize(n+1);
            size.resize(n+1,1);

            for (int i=0;i<=n;i++){
                parent[i] = i;
            }
        }

        int find_Ultimate_parent(int node){
            if(parent[node] == node) return node;
            return parent[node] = find_Ultimate_parent(parent[node]);
        }

        void union_by_rank(int u, int v){
            int ulp_u = find_Ultimate_parent(u);
            int ulp_v = find_Ultimate_parent(v);

            if (ulp_u == ulp_v){
                return;
            }

            if(rank[ulp_u] < rank[ulp_v]){
                parent[ulp_u] = ulp_v;
            }
            
            else if(rank[ulp_u] > rank[ulp_v]){
                parent[ulp_v] = ulp_u;
            }

            else {
                parent[ulp_v] = ulp_u;
                rank[ulp_u]++;
            }
        }


        void union_by_size(int u, int v){
            int ulp_u = find_Ultimate_parent(u);
            int ulp_v = find_Ultimate_parent(v);

            if (ulp_u == ulp_v){
                return;
            }

            if (size[ulp_u] < size[ulp_v]){
                parent[ulp_u] = ulp_v;
                size[ulp_v] += size[ulp_u];
            }

            else {
                parent[ulp_v] = ulp_u;
                size[ulp_u] += size[ulp_v];
            }
        }
};

int main(){
    DisjointSet ds(7);
    ds.union_by_rank(1,2);
    ds.union_by_rank(2,3);
    ds.union_by_rank(4,5);
    ds.union_by_rank(6,7);
    ds.union_by_rank(5,6);

    if(ds.find_Ultimate_parent(3) == ds.find_Ultimate_parent(7)){
        cout<<"Same Component\n";
    }
    else{
        cout<<"Different Component\n";
    }

    ds.union_by_rank(3,7);

    if(ds.find_Ultimate_parent(3) == ds.find_Ultimate_parent(7)){
        cout<<"Same Component\n";
    }
    else{
        cout<<"Different Component\n";
    }



    DisjointSet ds1(7);
    ds1.union_by_size(1,2);
    ds1.union_by_size(2,3);
    ds1.union_by_size(4,5);
    ds1.union_by_size(6,7);
    ds1.union_by_size(5,6);

    if(ds1.find_Ultimate_parent(3) == ds1.find_Ultimate_parent(7)){
        cout<<"Same Component\n";
    }
    else{
        cout<<"Different Component\n";
    }

    ds1.union_by_size(3,7);

    if(ds1.find_Ultimate_parent(3) == ds1.find_Ultimate_parent(7)){
        cout<<"Same Component\n";
    }
    else{
        cout<<"Different Component\n";
    }

    return 0;



}