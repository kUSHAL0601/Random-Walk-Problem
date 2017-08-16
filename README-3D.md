Libraries used: random => Used to generate random float between 0 and 1 using random() method
			  : matplotlib.pyplot => Used to plot graph

Variables used:men => Denotes no of men starting from centre
			  : steps => Max number of steps
			  : posn => To keep track of position of man every time
			  : count => Maintains count(key) of positions(value) and how many times they meet 
			  : i,j => Iterators
			  : x,y => Values for x and y axis
			  : add => Keeps track corresponding to random value if man moves forward or backward

Assumption: I have assumed that the men move simultaneously forward or backward by 1 unit radius

Logic: If the random number generated is greater than 0.5 we move corresponding man 1 step backward otherwise we move him forward
	 : Corresponding to men we store the positions
	 : Again corresponding to position count stores people who came to that position