#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .

sed -e "s,{urlExpression},https://osf.io/qjvhd/download,g" -e "s,{urlClinical},https://osf.io/g2jz8/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

