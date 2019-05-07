#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include "BTree.hpp"
#include <vector>
using std::cin;
using std::cout;
using std::string;
using std::endl;

sjtu::bptree <int, int> tree;
std::map <int, int> mp;
std::vector <int> v1;
std::vector <int> v2;
const int n = 10000;

long long aa=13131,bb=5353,MOD=(long long)(1e9+7),now=1;
int rand()
{
    for(int i=1;i<3;i++)
        now=(now * aa + bb) % MOD;
    return now;
}

void make_vector() {
    for (int i = 0; i < n; ++i) {
        v1.push_back(rand());
        v2.push_back(rand());
    }
}

void test_insert() {
    puts("Test: insert");
    //insert even number
    for (int i = 0; i < n; i += 2) {
        tree.insert(i, -i);
    }
    //insert odd number
    for (int i = n; i > 0; i -= 2) {
        tree.insert(i, -i);
    }

    puts("Test insert passed!");
}

void test_insert_random() {
    puts("Test: insert randomly");
    for (int i = 0; i < n; ++i) {
        tree.insert(v1[i], v2[i]);
        mp[v1[i]] = v2[i];
    }
    puts("Test insert passed!");
}

void test_count() {
    puts("Test count");
    for (int i = 0; i < n; i += 2) {
        if (!tree.count(i)) {
            puts("count error!");
            return;
        }
    }

    puts("Test count passed!");
}


void test_find() {
    puts("Test: find");
    for (int i = 0; i <= n; i++) {
        if (tree.find(i) != -i) {
            puts("find error!");
            return;
        }
    }
    for (int i = n; i > 0; i -= 2) {
        if (tree.find(i) != -i) {
            puts("find error!");
            return;
        }
    }
    puts("Test find passed!");
}

void test_find_random() {
    puts("Test: find");
    for (int i = 0; i <= n; ++i) {
        if (tree.find(v1[i]) != mp[v1[i]]) {
            puts("find error!");
            return;
        }
    }
    puts("Test find passed!");
}

void test_erase() {
    puts("Test erase");
    for (int i = 0; i < n; ++i) {
        tree.erase(v1[i]);
//        tree.view_root();
    }

    puts("Test erase passed!");
}



int main() {
//    test_insert();
//    test_count();
//    test_find();

    make_vector();
    test_insert_random();
    test_find_random();
//    tree.view_root();
    test_erase();
    tree.view_root();

    puts("Test Over");
}