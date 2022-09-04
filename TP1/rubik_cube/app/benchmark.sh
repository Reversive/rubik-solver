
for algorithm in "BFS", "DFS", "ASTAR1", "ASTAR2", "LGREEDY1", "LGREEDY2", "GGREEDY1", "GGREEDY2"
do
    for scramble in 2, 5, 8
    do
        python3 -u solver.py --algorithm=$algorithm --scramble=$scramble -n=2 > out/out_$algorithm$moves_qty.txt
    done
done