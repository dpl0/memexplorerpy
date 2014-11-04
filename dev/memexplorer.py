# N = # Data structures
# M = # Mem Banks
# Si = Size of DS i
# Cj = Capacity of MV
# Ei = Access cost if in memory bank
# Ei*p = access cost if in external mem
# O = # conflicts
# Dk = cost of conflict k
# Dk*p cost of conflict if in external memory
# Yk = State of conflict can be:
#		0 - If a and b DA are in different MB
#		1 - If a and b DA are in the same MB
#		p - If one is in EM
#		2p - If both are in EM
# Xij = Boolean 1 if i in MB j

# Data:
#	DataStructure = {'size', 'pos'}
#	MemoryBank = {'capacity', 'pos'}
#	Conflict = {'cost', 'state', 'a', 'b'}
#	X = [[]]


##### ******* BOTAS PICUUDAS WOOOOOOOOOOO *************

              _           ... and growing
                  H|| 
        __________H||___________
       [|.......................|
       ||.........## --.#.......|                       - A-B -
       ||.........   #  # ......|            @@@@
       ||.........     *  ......|          @@@@@@@       - C -
       ||........     -^........|   ,      - @@@@        
       ||.....##\        .......|   |     '_ @@@        - D-F -
       ||....#####     /###.....|   |     __\@ \@       
       ||....########\ \((#.....|  _\\  (/ ) @\_/)____  - G-I -
       ||..####,   ))/ ##.......|   |(__/ /     /|% #/ 
       ||..#####      '####.....|    \___/ ----/_|-*/   - J-L -
       ||..#####\____/#####.....|       ,:   '(          
       ||...######..######......|       |:     \        - M-O -
       ||.....""""  """"...b'ger|       |:      )      
       [|_______________________|       |:      |       - P-R -
              H||_______H||             |_____,_|       
              H||________\|              |   / (         - S - 
              H||       H||              |  /\  )        
              H||       H||              (  \| /         - T -
             _H||_______H||__            |  /'=.        
           H|________________|           '=>/  \        - U-W -   
                                        /  \ /|/
                                      ,___/|            - X-Z -

#******************************************************************


