#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <vector>
#include <limits>

enum class Color {
    WHITE = 0,
    GRAY = 1,
    BLACK = 2
};

struct Vertex {
    std::string name;
    Color color = Color::WHITE;
    float d = std::numeric_limits<float>::infinity();
    float f = 0; // Finish time
    Vertex *p = nullptr; // Predecessor

    Vertex(std::string n) : name(n) {}
};
class Graph {
    private:
        float time = 0;
        std::map<Vertex*, std::vector<Vertex*>> adj;

        void dfs_visit(Vertex* u) {
            time += 1;
            u->d = time;
            u->color = Color::GRAY;

            for (Vertex* v : adj[u]) {
                if (v->color == Color::WHITE) {
                    v->p = u;
                    dfs_visit(v);
                }
            }

            u->color = Color::BLACK;
            time += 1;
            u->f = time;
        }

    public:
        Graph(std::map<Vertex*, std::vector<Vertex*>>& adj_map) : adj(adj_map) {}

        void BFS(Vertex* s) {
            for(auto const& [u, neighbors] : adj) {
                u->color = Color::WHITE;
                u->d = std::numeric_limits<float>::infinity();
                u->p = nullptr;
            }
            s->color = Color::GRAY;
            s->d = 0;
            s->p = nullptr;

            std::queue<Vertex*> Q;
            Q.push(s);
            while(!Q.empty()) {
                Vertex* u = Q.front();
                Q.pop();
                for(Vertex* v : adj[u]) {
                    if(v->color == Color::WHITE) {
                        v->color = Color::GRAY;
                        v->d = u->d + 1;
                        v->p = u;
                        Q.push(v);
                    }
                }
                u->color = Color::BLACK;
            }
        }

        void DFS() {
            for (auto const& [u, neighbors] : adj) {
                u->color = Color::WHITE;
                u->p = nullptr;
            }

            time = 0;

            for (auto const& [u, neighbors] : adj) {
                if (u->color == Color::WHITE) {
                    dfs_visit(u);
                }
            }
        }
};

int main() {
    Vertex a("A"), b("B"), c("C"), d("D"), e("E"), f("F"), h("H"), x("X");

    std::map<Vertex*, std::vector<Vertex*>> adj = {
        {&a, { &b, &c }},
        {&b, {&a}},
        {&c, {&a,&f,&h}},
        {&d, {&e,&f}},
        {&e, {&d}},
        {&f, {&c,&d}},
        {&h, {&c}},
        {&x, {&a}}
    };

    Graph g(adj);

    g.BFS(&b);
    g.DFS();

    std::cout<<x.d<<std::endl;
    std::cout << "A finish time: " << a.f << std::endl;
    return 0;
}