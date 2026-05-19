# Analog Circuit Synthesis Tool

Before runing any example/script in this README file, please execute the following two export commands first


```bash
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/thirdparty_libs/gecode-release-6.2.0"
export PYTHONPATH=/mnt/home/pham/code/maga/build/src/pymaga:$PYTHONPATH
```



## Topology Generation

Build the executable `cmd_toplibgen` first (`Shift + Command + P` $\to$ CMake: Set Build Target $\to$ enter `cmd_toplibgen`, then continue to select CMake: Build).

```bash
mkdir -p outputs/TopologyGen
```


## Python Binding
Build the Python lib `pymaga` first (`Shift + Command + P` $\to$ CMake: Set Build Target $\to$ enter `pymaga`, then continue to select CMake: Build).

Use this command to obtain the structural recognition and paritioning results for a format-compatible FUBOCO SPICE netlist.
```bash
python src/pymaga/examples/recognition.py -f tests/example3.ckt 
```

A format-compatible FUBOCO SPICE netlist should defined inside `subckt` block, with `vdd!` and `gnd!` terminals for power rail 

```
.suckt  FD_Symmetry ibias in1 in2 out1 out2 vdd! gnd! vcm
m1  net1  net1  vdd!  vdd  pmos
m2  net2  net1  vdd!  vdd  pmos
m3  ibias ibias gnd!  gnd!  nmos
m4  net1  ibias gnd!  gnd!  nmos
m5  net4  ibias gnd!  gnd!  nmos
m6  net5  in1 net4  gnd!  nmos
...
.end FD_Symmetry
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