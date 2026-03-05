import time
""" EXPECTED OUTPUT
           *
           *
           *
        *******
       *       *
      * ******* *
     * ********* *
    * ***     *** *
*** * ***     *** * ***
     * ********* *
* * * * ******* * * * *
     * ********* *
*** * ***     *** * ***
    * ***     *** *
     * ********* *
      * ******* *
       *       *
        *******
           *
           *
		   *
"""

"""
1:
           *
           *
           *
2:
        ****
3:
       *    
4:
      * ****
     * *****
5:
    * ***   
*** * ***   
6:
     * *****
7:
* * * * ****
"""

should_animate = input("input 1 to animate, else skip: ") == "1"

segment_height = 11
segment_width = 12

for i in range(1, segment_height * 2):
	y = abs((i - segment_height))

	for j in range(1, segment_width * 2):
		x = abs((j - segment_width))
		
		if y >= 8:#1
			print(" " if x!=0 else "*", end="", flush=should_animate)
		elif y == 7:#2
			print(" " if x>=4 else "*", end="", flush=should_animate)
		elif y == 6:#3
			print(" " if x!=4 else "*", end="", flush=should_animate)
		elif y >= 4:#4
			print(" " if x!=5-y+5 and x >= 4-y+5 else "*", end="", flush=should_animate)
		elif y >= 2:#5
			print(" " if x!=7 and not 2<x<6 and (y!=2 or (y==2 and x<9)) else "*", end="", flush=should_animate)
		elif y == 1:#6
			print(" " if x!=6 and not x<5 else "*", end="", flush=should_animate)
		elif y == 0:#7
			print(" " if not x<4 and x%2 == 0 else "*", end="", flush=should_animate)
		
		if should_animate: time.sleep(0.01)

	print("")
