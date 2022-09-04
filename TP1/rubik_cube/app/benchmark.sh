
for algorithm in "BFS" "DFS" "ASTAR1" "LGREEDY1" "GGREEDY1"
do
    mkdir -p out/$algorithm
    for scramble in 2 6 9
    do
            echo "visited nodes, depth, border nodes, time" > out/$algorithm/out_$scramble.csv
        for seed in {1..10}
        do
            python3 -u solver.py -n=2 --timeout=90 --algorithm=$algorithm --scramble=$scramble --seed=$seed --csv=True >> out/$algorithm/out_$scramble.csv
        done
    done
    echo "Done $algorithm"
done
