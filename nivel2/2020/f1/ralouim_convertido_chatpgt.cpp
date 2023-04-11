// questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
// nota: 10/100
// Código reescrito de um código python para c++ pelo chatgpt
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

vector<pair<int, int>> ENTRADAS;
int N;

vector<tuple<int, pair<int, int>, pair<int, int>>> calcular_todas_distancias() {
    vector<pair<int, int>> lista_pos = ENTRADAS;
    lista_pos.push_back(make_pair(0, 0));
    vector<tuple<int, pair<int, int>, pair<int, int>>> retorno;
    map<pair<int, int>, vector<int>> retorno2;
    map<pair<int, int>, vector<int>> retorno3;
    map<pair<int, int>, int> retorno4;

    for (int i = 0; i < N; i++) {
        pair<int, int> curr = lista_pos.front();
        lista_pos.erase(lista_pos.begin());
        retorno2[curr] = vector<int>();
        retorno3[curr] = vector<int>();
        retorno4[curr] = 0;
        for (pair<int, int> j : lista_pos) {
            int distancia = pow(curr.first - j.first, 2) + pow(curr.second - j.second, 2);
            retorno.push_back(make_tuple(distancia, curr, j));
        }
    }

    sort(retorno.rbegin(), retorno.rend());
    return retorno;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        ENTRADAS.push_back(make_pair(x, y));
    }

    vector<tuple<int, pair<int, int>, pair<int, int>>> DISTANCIAS = calcular_todas_distancias();
    map<pair<int, int>, vector<int>> contador;
    map<pair<int, int>, vector<int>> distancia;
    map<pair<int, int>, int> quantidade;
    vector<int> resultado = {1};

    for (tuple<int, pair<int, int>, pair<int, int>> percurso : DISTANCIAS) {
        int distancia_atual = get<0>(percurso);
        pair<int, int> local1 = get<1>(percurso);
        pair<int, int> local2 = get<2>(percurso);
        if (local1 == make_pair(0, 0)) {
            contador[local2].push_back(1);
            distancia[local2].push_back(distancia_atual);
            quantidade[local2]++;
        } else if (local2 == make_pair(0, 0)) {
            contador[local1].push_back(1);
            distancia[local1].push_back(distancia_atual);
            quantidade[local1]++;
        } else {
            int quantidadeAgora = quantidade[local1];
            for (int index = 0; index < quantidadeAgora; index++) {
                if (distancia_atual != distancia[local1][index]) {
                    int c = contador[local1][index] + 1;
                    contador[local2].push_back(c);
                    resultado.push_back(c);
                    distancia[local2].push_back(distancia_atual);
                    quantidade[local2]++;
                }
            }
            quantidadeAgora = quantidade[local2];
            for (int index = 0; index < quantidadeAgora; index++) {
                if (distancia_atual != distancia[local2][index]) {
                    int c = contador[local2][index] + 1;
                    contador[local1].push_back(c);
                    resultado.push_back(c);
                    distancia[local1].push_back(distancia_atual);
                    quantidade[local1]++;
                }
            }
        }
    }
    cout << *max_element(resultado.begin(), resultado.end()) << endl;
    return 0;
}