
for algorithm in "ASTAR_DIFFCOLORS" "ASTAR_SMANHATTAN" "BFS" "IDDFS" "LGREEDY_DIFFCOLORS" "LGREEDY_SMANHATTAN" "GGREEDY_DIFFCOLORS" "GGREEDY_SMANHATTAN" "DFS" 
do
    mkdir -p out/$algorithm
    for scramble in 2 6 9
    do
        echo "seed, visited nodes, depth, border nodes, time" > out/$algorithm/out_$scramble.csv
        for seed in 1 3 5 6 7 8 9 10 12 13 16 18 20 21 22 23 24 25 28 29 30
        do
            python3 -u solver.py -n=2 --timeout=90 --algorithm=$algorithm --scramble=$scramble --seed=$seed --csv=True >> out/$algorithm/out_$scramble.csv
        done
    done
    echo "Done $algorithm"
done
