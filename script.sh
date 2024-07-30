# compile and link test_ht.c 
gcc -o prog test_ht.c -I/usr/include -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
# run prog and overwrite output.txt with prog output
./prog > output.txt
# run plotting script
python3 plot.py
