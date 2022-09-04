
for algorithm in "BFS" "DFS" "ASTAR_DIFFCOLORS" "ASTAR_SMANHATTAN" "LGREEDY_DIFFCOLORS" "LGREEDY_SMANHATTAN" "GGREEDY_DIFFCOLORS" "GGREEDY_SMANHATTAN"
do
    mkdir -p out/$algorithm
    for scramble in 2 6 9
    do
        echo "seed, visited nodes, depth, border nodes, time" > out/$algorithm/out_$scramble.csv
        for seed in 1 2 3 4 5 6 7 8 9 10
        do
            python3 -u solver.py -n=3 --timeout=90 --algorithm=$algorithm --scramble=$scramble --seed=$seed --csv=True >> out/$algorithm/out_$scramble.csv
        done
    done
    echo "Done $algorithm"
done
