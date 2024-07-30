# Names of files
HT_SRC="test_ht.c"
HT_EXEC="prog"
HT_OUT="output.txt"
PLOT_SCR="scripts/plot.py"

# If in scripts/, prefix with ./../, else just ./
DIR_PREFIX="./"
if [ ! -s "./${HT_SRC}" ]; then 
  DIR_PREFIX="${DIR_PREFIX}../"
fi 

# Compile and link HT source file 
# * On my laptop, GSL is installed in /usr/local/, instead of /usr/
gcc -o ${DIR_PREFIX}${HT_EXEC} ${DIR_PREFIX}${HT_SRC} -I/usr/local/include -L/usr/local/lib -lgsl -lgslcblas -lm

# Run HT executable and overwrite output file with program output
${DIR_PREFIX}${HT_EXEC} > ${DIR_PREFIX}${HT_OUT}

# Run plotting script on output
python3 ${DIR_PREFIX}${PLOT_SCR} ${DIR_PREFIX}${HT_OUT}
