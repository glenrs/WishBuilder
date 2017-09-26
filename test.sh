#!/bin/bash

#module load python/3/5

#cd $1
#chmod +x ./download.sh
#chmod +x ./parse.sh
#./download.sh
#./parse.sh
#gzip -d data.tsv.gz
#cd ..
python test.py $1
#cd $1
#rm data.tsv
#rm $(tail -n 1 .gitignore)
#cd ..
