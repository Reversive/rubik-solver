
for index in {0..7}
do
    python3 -u main.py --index=$index -n=2 > out$index.txt
done