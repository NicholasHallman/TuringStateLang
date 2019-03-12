# TuringStateLang

## Description

Turing state lang turns the source code and generates a turing machine and executes the program

## Example

A machine that does addition

| M1      | 0        | 1         |\( \lambda \ \Lambda \)|
| --------|:--------:|:---------:| --------:|
| Q0      | Q0,0,R   |  Q0,1,R   |  Q1,\( \lambda \ \Lambda \),L| 
| Q1      |  !,1,-   |   !,1,-   |   !,1,-  |