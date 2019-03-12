
[10001#10001]

{10#}

START
    READ 0 < START
    READ 1 < START
    READ # < START
    READ   > TWO

#TWO 
    READ 0 = > THREE
    READ 1 = > FIVE
    READ #   < SEVEN
    READ       FAIL

#THREE
    READ 0 > THREE 
    READ 1 > THREE
    READ # > FOUR
    READ     FAIL

#FOUR
    READ 0 = # < START
    READ 1 = # > FAIL
    READ #     > FOUR
    READ         FAIL

#FIVE
    READ 0 > FIVE 
    READ 1 > FIVE
    READ # > SIX
    READ     FAIL

#SIX 
    READ 0       FAIL
    READ 1 = # < START
    READ # >     SIX
    READ         FAIL

#SEVEN 
    READ 0 FAIL
    READ 1 FAIL
    READ # > SEVEN
    READ END