# compile and link test_ht.c 
# - on my laptop, gsl is installed in /usr/local/, instead of /usr/
gcc -o prog test_ht.c -I/usr/local/include -L/usr/local/lib -lgsl -lgslcblas -lm
# run prog and overwrite output.txt with prog output
./prog > output.txt
# run plotting script
python3 plot.py
