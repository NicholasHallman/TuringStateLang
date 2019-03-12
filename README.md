# TuringStateLang

## Description

Turing state lang turns the source code and generates a turing machine and executes the program

## Example

### Turing Machine

A machine that adds one to the given string

| M1      | 0        | 1         | λ        |
| --------|:--------:|:---------:| --------:|
| Q0      | Q0,0,R   |  Q0,1,R   |  Q1,λ,L  | 
| Q1      |  !,1,-   |   !,1,-   |   !,1,-  |

### Code
```
[0001]
{01}

START
    READ 0 > START
    READ 1 > START
    READ   < SECOND

#SECOND
    READ 0 = 1 END
    READ 1 = 0 < SECOND
    READ   = 1 END
```

Each state is described with a keyword.
There are three given states

START: the program always begins here
END:   the program reached the accepted state
FAIL:  the program reached the fail state

Users can create their own keywords like this
```
#STATENAME
```

You can read a line of code like this 
```
READ 1 = 0 < SECOND
```

If 1 is read, replace with 0, move left, goto SECOND

# Language

The programs languages is between {}

# String

The string on the tape

## But Why?

Created for my Foundations of Computing class to quickly test different turing machines made for assignments

## More Examples

