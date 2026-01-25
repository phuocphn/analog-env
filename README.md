# Analog Circuit Synthesis Tool



```
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/thirdparty_libs/gecode-release-6.2.0"
export PYTHONPATH=/mnt/home/pham/code/maga/build/src/pymaga:$PYTHONPATH
```


```
valgrind --leak-check=full \
         --show-leak-kinds=all \
         --track-origins=yes \
         --verbose \
         --log-file=valgrind-out.txt \
         ./executable exampleParam1

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/thirdparty_libs/gecode-release-6.2.0"
export PYTHONPATH=/mnt/home/pham/code/maga/build/src/pymaga:$PYTHONPATH
```




# References
- inga000/acst: acst - Analog Circuit Synthesis Tool https://github.com/inga000/acst
- AugustUnderground/circus: Analog CIrcuit Sizing Gym Environment (GACE 2.0) https://github.com/AugustUnderground/circus/