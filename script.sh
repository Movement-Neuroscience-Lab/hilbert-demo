gcc -o prog test_ht.c -I/usr/include -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
./prog > output.txt
python3 plot.py
