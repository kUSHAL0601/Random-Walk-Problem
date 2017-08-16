Libraries used:random => Used to generate random float between 0 and 1 using random() method
			  :matplotlib.pyplot => Used to plot graph

Variables used:trials => Denotes no of experiments
			  :steps => Max number of steps
			  :count => Maintains count(key) of positions(value) and how many times they meet 
			  :man1,man2 => To keep track of position of the two drunkards
			  :i,j => Iterators
			  :x,y => Values for x and y axis

Logic: If the random number generated is greater than 0.5 we move corresponding man 1 step backward otherwise we move him forward
	 : If their positions are same we note the position where they meet and store it in count dictionary