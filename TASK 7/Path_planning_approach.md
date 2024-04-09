For the path planning I have used brute force method to first find all the possible paths,
and then from all those possible paths I have taken the path with the shortet length which gives us our desired output.


First I have defined a function 'fun(i, j, a, goal, path, c)', which has five parameters,
i: the row of the block which the function is evaluating
j: the column of the block which the function is evaluating
a: this represents a 2D matrix in which traverseable blocks(yellow coloured) have value 1 and non-traveseable blocks(blue coloured) blocks have 0 value.
goal: this represents the end block (the block we need to reach)
path: this list contains all possible paths from start to end
c: this list contains the last recorded path which takes us from start to end

First in the function we append the block that is being visited i.e. (i, j) th block to the list c
if (i, j) th block is the end block then append c to path list.
for us to travese to a block on the row i needs to be less than 4 and i+1 needs to be traverseable in that column
and same goes for the column...
then I have used recursion to recursively call the function and get the path which is traveseable.
