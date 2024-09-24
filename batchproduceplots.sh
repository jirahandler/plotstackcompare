setupATLAS -q
#lsetup "root 6.28.08-x86_64-centos7-gcc11-opt"
lsetup "root 6.32.02-x86_64-el9-gcc13-opt"
for f1 in `ls plotConfigs/*.py`; do python3 Compare.py -l $f1 ; done
