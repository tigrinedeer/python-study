# labyrinth
Task description
Write a program that generates and draws a simple labyrinth in ASCII mode. The labyrinth should consist of 6 different tiles (3x3 symbols) represented as string as follows 
 
NO = '###
      ###
      ###' # No path
 
LR = '###
        
      ###' # Path from left to right
 
LT = '# #
        #
      ###' # Path from left to top 
 
BR = '###
      #
      # #' # Path from bottom to right 
 
LB = '###
        #
      # #' # Path from left to bottom 
 
TR = '# #
      #
      ###' # Path from top to right 
 
Write a function that draws any given combination of tiles as 2-dimensional array. For example 
 
`render([ 
 
    [NO, BR, LR, LB, NO], 

    [LR, LT, NO, TR, LR] 
 
])`