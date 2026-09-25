# Prerequisite Quiz

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/YRJDz/prerequisite-quiz
- Item type: ungradedAssignment
- Grading status: GRADED, earned grade 0.96
- Score: latest 24, highest 24, max 25

## Questions

### Q1 (1/1 pts) ✅ correct

The value of 5 + 3 + 77 is _____.

- ( ) 77
- ( ) 100
- (x) 85  ← your answer, CORRECT
- ( ) 80

### Q2 (1/1 pts) ✅ correct

The value of 5*3*2 is ____.

- ( ) 35
- ( ) 50
- ( ) 15
- (x) 30  ← your answer, CORRECT

### Q3 (1/1 pts) ✅ correct

The value of $$5^2$$ + $$3^2$$ + $$77^2$$ + $$10^2$$ is _____.

- ( ) 7700
- (x) 6063  ← your answer, CORRECT
- ( ) 190
- ( ) 95

### Q4 (1/1 pts) ✅ correct

The value of 1+2+3+4+5+6+7+8+9+10 is _____.

- ( ) 44
- (x) 55  ← your answer, CORRECT
- ( ) 11
- ( ) 66

> Feedback: The fastest way to calculate the answer is to use an arithmetic
progression. The rule of thumb is that the addition of integers 1
through N is equal to N*(N+1)/2. That’s 10*11/2 = 55. If your approach
was to manually add up the numbers, then please look up arithmetic
progressions.

### Q5 (1/1 pts) ✅ correct

The value of 21+22+23+24+25 is _____.

- ( ) 32
- ( ) 65
- (x) 62  ← your answer, CORRECT
- ( ) 64

> Feedback: The fastest way to calculate the answer is to use a geometric
progression. The rule of thumb is that the addition of numbers a, a*r,
a*r2,… through a*rN is equal to a*(rN+1-1)/(r-1). In this case a=2, r=2, N=4. That’s 2*(25-1)/(2-1) = 2*31 = 62. If your approach was to manually add up the numbers, then please look up geometric progressions.

### Q6 (1/1 pts) ✅ correct

In a queue data structure, the following items are inserted in the
following order: Bob, Alice, Charlie, Eve, Zebra. Then an item is
removed from the queue. That item will be _____.

- (x) Bob  ← your answer, CORRECT
- ( ) None - this will be an error
- ( ) Charlie
- ( ) Eve

> Feedback: A queue is a first in first out datastructure.

### Q7 (1/1 pts) ✅ correct

In a queue data structure, the following items are inserted in the
following order: Bob, Alice, Charlie, Eve, Zebra. Then three items are
removed from the queue. Then two further items are inserted: Yelp,
Pinion. Then two more items are removed from the queue. The next item
removed will be _____.

- ( ) Pinion
- ( ) Eve
- (x) Yelp  ← your answer, CORRECT
- ( ) Zebra

> Feedback: A queue is a first in first out datastructure. After the first five
items are inserted, the queue is (from head to tail): <Bob, Alice,
Charlie, Eve, Zebra>. After the first removal of three items, the
queue is:<Eve, Zebra>. After the next two insertions, the queue
is: <Eve, Zebra, Yelp, Pinion>. After the next two removals, the
queue is: <Yelp, Pinion>. That means Yelp will be the next item
removed.

### Q8 (1/1 pts) ✅ correct

In a stack data structure, the following items are inserted in the
following order: Bob, Alice, Charlie, Eve, Zebra. Then an item is
removed from the stack. That item will be _____.

- ( ) None - this will be an error
- ( ) Alice
- (x) Zebra  ← your answer, CORRECT
- ( ) Eve

> Feedback: A stack is a first in last out datastructure.

### Q9 (1/1 pts) ✅ correct

In a stack data structure, the following items are inserted in the
following order: Bob, Alice, Charlie, Eve, Zebra. Then three items are
removed from the stack. Then two further items are inserted: Yelp,
Pinion. Then two more items are removed from the stack. The next item
removed will be _____.

- ( ) Eve
- ( ) Charlie
- (x) Alice  ← your answer, CORRECT
- ( ) Pinion

> Feedback: A stack is a first in last out datastructure. After the first five
insertions, the stack is (from top to bottom): <Zebra, Eve, Charlie,
Alice, Bob>. The next three items are moved are Zebra, Eve, and
Charlie, leaving the stack as <Alice, Bob>. After the next two
insertions, the stack is <Pinion, Yelp, Alice, Bob>. The next two
removals will be Yelp and Pinion, leaving the stack as <Alice,
Bob>. The next item removed will thus be Alice.

### Q10 (1/1 pts) ✅ correct

You write a C++ program and it’s in two files: myprogram.h, and myprogram.cpp. Then a “process” is _____.

- ( ) Any object (.o) files created when this program is compiled
- ( ) The two C++ files myprogram.h and myprogram.cpp
- (x) The compiled version (executable) of this program in action, with stack, heap, registers, code, program counter, etc.  ← your answer, CORRECT
- ( ) The executable file created when this program is compiled

### Q11 (1/1 pts) ✅ correct

Which of the following in a process typically DOES NOT change its value or contents over the lifetime?

- ( ) Registers
- ( ) Program counter
- ( ) Stack
- (x) Code  ← your answer, CORRECT

> Feedback: Most programs are not written to change the code itself (which is
static). Program counter changes as it always points to the line number
currently being executed. Heap changes as new variables are created or
garbage collected. Stack changes as methods/functions are called or
return. The register changes as variables are accessed by the process’
running code.

### Q12 (1/1 pts) ✅ correct

For an executing process, which of the following actually executes the instructions of the process?

- (x) CPU  ← your answer, CORRECT
- ( ) Cache
- ( ) Memory
- ( ) Disk

### Q13 (0/1 pts) ❌ incorrect

The CPU can access data stored in different levels of the memory hierarchy. Which of these is the fastest to access?

- ( ) Main Memory (RAM)
- ( ) SSD
- (x) Cache  ← your answer, incorrect
- ( ) Registers

_Correct option not revealed for this attempt._

### Q14 (1/1 pts) ✅ correct

In an executing process, the program counter points __________.

- (x) To the currently-being-executed line number of low-level (e.g.,
machine-level) program derived by compiling the C++ program you wrote  ← your answer, CORRECT
- ( ) To the program or process that is currently being executed (among the many processes that are running in the Operating System)
- ( ) To the top of the stack
- ( ) To the bottom of the stack

> Feedback: A program written in a high level language like C++ is compiled down to a
 low-level language (e.g., machine language, or intermediate language in
 Java. The CPU keeps track of this as it executes. The Program Counter
points to the instruction number in this compiled executable that is
currently running in the CPU.)

### Q15 (1/1 pts) ✅ correct

Searching for an element in an unsorted array (or vector) of N elements takes time _____.

- ( ) O(N/2)
- ( ) O(1)
- ( ) O(N2)
- (x) O(N)  ← your answer, CORRECT

> Feedback: This was discussed in lecture. The only potentially confusing answer is
O(N/2). We NEVER write O(N/2), because the constant (in this case ½) is
used up in the “c” that goes into the O() notation, e.g., here c=2. For
more information on c, see the video lecture.

### Q16 (1/1 pts) ✅ correct

Insertion sorting of an unsorted array of size N takes time _____.

- ( ) O(N)
- ( ) O(N3)
- (x) O(N2)  ← your answer, CORRECT
- ( ) O(1)

> Feedback: This was discussed in lecture.

### Q17 (1/1 pts) ✅ correct

You are given an array (vector) of N integers that is sorted in
increasing order. You are asked to create a sorted list of the same
integers but in decreasing order. You can use any extra arrays, and
creating extra arrays takes O(1) time. The most efficient algorithm to
achieve this takes time ______.

- ( ) O(N/2)
- ( ) O(N2)
- ( ) O(1)
- (x) O(N)  ← your answer, CORRECT

> Feedback: While one could have executed insertion sort on this array (takes time O(N2)),
 one can do better! Create a new empty array, and start with the
original array but from the last element and work your way to the front
of the old array. Each encountered element is inserted into the new
array (starting from the front of the new array). Since there are N
elements in the array and each is processed exactly once, that’s an
O(N) algorithm.

### Q18 (1/1 pts) ✅ correct

An algorithm to process a set of N elements takes time (in microseconds) = f(N) = 0.03*N3+1000*N+3. This algorithm is _____.

- ( ) O(N/2) because 1000 is the highest constant
- (x) O(N3)  ← your answer, CORRECT
- ( ) O(N) because 1000 is the highest constant
- ( ) O(1) because 3 is the highest constant

### Q19 (1/1 pts) ✅ correct

You are given a bag with 10 balls, of which 3 are red, 3 are blue, 1 is
yellow,  2 are black, and 1 is white. You pick one ball at random from the bag. The
probability that this ball is black is _____.

- (x) 1/5  ← your answer, CORRECT
- ( ) 1/10
- ( ) 0
- ( ) 1

> Feedback: Since there are 2 black balls out of 10, the probability of picking a black ball at random is = 2/10 = 1/5.

### Q20 (1/1 pts) ✅ correct

You are given a bag with 10 balls, of which 3 are red, 3 are blue, 1 is
yellow, 2 are black, and 1 is white. You pick one ball, note its color, put the ball
 back in the bag, and then pick another ball. The probability that it
was the case that the first ball was black and the second ball was red
is _____.

- ( ) None of these
- ( ) 2
- (x) 0.06  ← your answer, CORRECT
- ( ) 0.5

> Feedback: The probability that the first ball was black is 2/10 = 1/5. The
probability that the second ball was red is 3/10. Since these two events
 are independent of each other (remember – you put the first ball back
in the bag before picking the second ball out), we can obtain the joint
probability by multiplying the two probabilities. That’s 1/5*3/10 = 3/50
 = 0.06.

### Q21 (1/1 pts) ✅ correct

Someone claims that the big O notation does not make sense at all, and
they give the following example. An algorithm A that processes an input
set of N elements takes time, in seconds, given by T(N) = 10000*N +
0.00001*N^3. They say that the large constant (10000) associated with the
 N will always dominate over the small constant (0.00001) associated
with the N^3. You say that this algorithm A is _____.

- ( ) O(N)
- ( ) Confusing
- ( ) O(1)
- (x) O(N3)  ← your answer, CORRECT

> Feedback: Big O notation tries to calculate the asymptotic cost of an algorithm,
i.e., what would happen if the input set were really (really) large!
This is important for “Big Data” kinds of applications. When N is more
than one billion, for instance,  0.00001*N3 is much larger
than 10000*N. Thus, in calculating Big O notation, you must always take
the “highest power” (or the fastest growing function), independent of
the constants.

### Q22 (1/1 pts) ✅ correct

Someone writes the following piece of code. What is its Big O complexity?
int k=0;
for (i = 0; i < N; i++) {
       for (j = 0; j < N; j++) {
               k++;
       }
}

- ( ) O(N)
- ( ) O(1)
- ( ) None of these
- (x) O(N2)  ← your answer, CORRECT

> Feedback: The outermost loop executes N times. For each of the iterations, the
second inner loop (with j) executes N times. Thus the total number of
times “some statements” will be execute is N*N = N2 times. You can also verify this by calculating the value of k when the nested loops complete.

### Q23 (1/1 pts) ✅ correct

You are given the following graph. In this graph, each edge has a
weight that denotes the time taken to move between those cities (in
hours). A “path” is defined as a sequence of edges that can be joined
together to create, well, a path from a source node to a destination
node. For instance, one path from node E to node D goes like: E to B to C
 to D. The “path cost” is obtained by adding up the costs of all its
constituent edges – for the above example, the path’s cost is 9 + 2 + 4 =
 15. There might be multiple paths between a pair of source, destination
 nodes. Among all these paths, we say that “shortest path” between a
source and destination node pair is that path which has the lowest path
cost.

Answer the following question: the shortest path that goes from node A to node C passes via which sequence of nodes?
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/orientation/q23.PNG]

- ( ) None of these
- ( ) Direct edge from A to C
- (x) A to B to C  ← your answer, CORRECT
- ( ) A to D to C

> Feedback: There are three paths from A to C. The direct path (edge) has a cost of
10, the second path via E and B has a cost of (3+9+2) = 14, while the
third path via B has the lowest cost of (5+2)=7.

### Q24 (1/1 pts) ✅ correct

In the following graph, the shortest path that goes from node D to node E has what cost?
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/orientation/q24.PNG]

- (x) 14  ← your answer, CORRECT
- ( ) 15
- ( ) None of these
- ( ) 17

> Feedback: The shortest path from D to E is D-C-B-A-E. This has a total cost of
(4+2+5+3) = 14. All other paths are longer (e.g., D-C-A-E has a cost of
17, D-C-B-E has a cost of 15, and so on).

### Q25 (1/1 pts) ✅ correct

In a graph containing N nodes, an edge can only join a pair of nodes.
The maximum number of edges that can be present in this graph is best
described as _____.

- (x) O(N2)  ← your answer, CORRECT
- ( ) O(N3)
- ( ) O(N)
- ( ) O(N4)

> Feedback: The maximum number of edges is reached when every pair of nodes is
connected. To calculate this number, first assign the N nodes unique
integer ids 1, 2, … N (the order does not matter). The node with id 1
has N-1 edges to the other N-1 nodes with higher ids than itself.
Similarly, the node with id 2 has N-2 edges (excluding the one edge to
node 1 that was already accounted for), the node with id 3 has N-3
edges, and so on. The total number of edges is: (N-1)+(N-2)+(N-3)+…1+0.
This is a sum you’ve seen in lecture and in this quiz. Its sum is
N*(N-1)/2, which is < 2*N2. This is O(N2). For those of you who know combinatorics, this can also be calculated as N-choose-2.
