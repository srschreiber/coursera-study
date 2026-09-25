# Part 1 Quiz 3

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/EpzdZ/part-1-quiz-3
- Item type: staffGraded
- Grading status: GRADED, earned grade 1
- Score: latest 14, highest 14, max 14

## Questions

### Q1 (1/1 pts) ✅ correct

Napster servers, as discussed in lecture, do not store which of the following? (1 point)

- ( ) File pointers, i.e., (filename, peer address) pairs
- ( ) Addresses of other Napster servers
- ( ) Addresses of some of the peers (clients)
- (x) Files  ← your answer, CORRECT

### Q2 (1/1 pts) ✅ correct

Which of the following Gnutella messages are flooded out and TTL restricted? (1 point)

- (x) Query  ← your answer, CORRECT
- ( ) Giv
- ( ) OK
- ( ) QueryHit

### Q3 (1/1 pts) ✅ correct

In BitTorrent, a new leecher is downloading a file with 5 blocks (B1 through B5). The leecher has 3 neighbors X, Y, and Z. These neighbor peers have the following blocks: X: (B1, B2, B3, B4). Y: (B1, B3, B4, B5). Z: (B1, B3, B5). Which of the following blocks does the leecher prefer downloading first? (1 point)

- ( ) B4
- ( ) B5
- (x) B2  ← your answer, CORRECT
- ( ) B1

> Feedback: BitTorrent uses Local Rarest First policy (see lecture for more information).

### Q4 (1/1 pts) ✅ correct

A Pastry DHT has a peer P with the following neighbors. P currently has to route a query to key 101001011010. Which of the following neighbors is the best next-hop for this query? (1 point)

- ( ) 101101011010
- ( ) 111111100000
- (x) 101001011000  ← your answer, CORRECT
- ( ) 111001011010

> Feedback: Pastry uses longest-prefix match to determine next hop for a Query.

### Q5 (1/1 pts) ✅ correct

In the Chord DHT when a peer P fails from the system, which of the following will not happen? (1 point)

- ( ) Before the failure is detected, some queries passing through P may be dropped or rerouted.
- ( ) Some files will need to move (assuming replication).
- (x) The entire ring will have to be reorganized from scratch.  ← your answer, CORRECT
- ( ) Some other peers will need to change their finger table entries.

### Q6 (1/1 pts) ✅ correct

A Gnutella topology looks like a balanced ternary tree with 4 levels of nodes, i.e., peers, as shown in the picture below. Thus, there is 1 root at Level 1, which has 3 children at Level 2, which each have 3 children at Level 3, which in turn each have 3 children at Level 4 – thus, there are a total of 40 nodes.

If the root node (Level 1) sends a Query message with TTL=2, then what are the number of nodes receiving the Query message, not including the originating node? Enter your answer as a numeric value in the text box below. (1 point)
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/hw1_sample.png]

- Your answer: `12`  ✅ (correct)

### Q7 (1/1 pts) ✅ correct

A Gnutella topology looks like a balanced ternary tree with 4 levels of nodes, i.e., peers, as shown in the picture below. Thus, there is 1 root at Level 1, which has 3 children at Level 2, which each have 3 children at Level 3, which in turn each have 3 children at Level 4 – thus, there are a total of 40 nodes.

If one of the leaf nodes (Level 4 nodes in the tree) sends a Query message with TTL=3, then what are the number of nodes receiving the Query message, not including the originating node? Enter your answer as a numeric value in the text box below. (1 point)
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/hw1_sample.png]

- Your answer: `7`  ✅ (correct)

> Feedback: The Query is received by the root (1), the Level 2 ancestor and its children (1+2), the Level 3 parent and all its descendants (1+2).

### Q8 (1/1 pts) ✅ correct

A Gnutella topology looks like a balanced ternary tree with 5 levels of nodes, i.e., peers. Thus, there is 1 root at Level 1, which has 3 children at Level 2, which each have 3 children at Level 3, which in turn each have 3 children at Level 4, which in turn each have 3 children at Level 5 – thus, there are a total of 121 nodes.

If a child of the root (i.e., a Level 2 node) sends a Query message with TTL=5, then what are the number of nodes receiving the Query message, not including the originating node? Enter your answer as a numeric value in the text box below. (1 point)

- Your answer: `120`  ✅ (correct)

> Feedback: All nodes in the overlay receive this Query.

### Q9 (1/1 pts) ✅ correct

A Gnutella topology looks like a balanced ternary tree with 5 levels of nodes, i.e., peers. Thus, there is one root at Level 1, which has 3 children at Level 2, which each have 3 children at Level 3, which in turn each have 3 children at Level 4, which in turn each have 3 children at Level 5 – thus, there are a total of 121 nodes.

 What is the minimum TTL required for any node’s Query to reach every other node? Enter your answer as a numeric value in the text box below. (1 point)

- Your answer: `8`  ✅ (correct)

> Feedback: Feedback: In the worst case the Query takes 4 hops to get to the Level 1 node and 4 further hops to get down to another Level 4 node.

### Q10 (1/1 pts) ✅ correct

In a Chord ring using m = 9, nodes with the following peer ids (or node ids) join
the system: 1, 12, 123, 234, 345, 456, 501.

What node id is the file with id 120 stored at (assuming only one replica)? Enter your answer as a numeric value in the text box below. (1 point)

- Your answer: `123`  ✅ (correct)

> Feedback: The ith finger table entry (i = 0 and upwards) at node n is the first node at or clockwise to n+2i. A Query is forwarded, at each step, to the farthest clockwise neighbor which is still to the anticlockwise of the key, or failing that it is forwarded to the successor.

### Q11 (1/1 pts) ✅ correct

In a Chord ring using m = 9, nodes with the following peer ids (or node ids) join
the system: 1, 12, 123, 234, 345, 456, 501. Which of the following nodes is not present as a finger table entry or successor of 234? (1 point)

- ( ) 501
- (x) 1  ← your answer, CORRECT
- ( ) 456
- ( ) 345

> Feedback: The ith finger table entry (i = 0 and upwards) at node n is the first node at or clockwise to n+2i. A Query is forwarded, at each step, to the farthest clockwise neighbor which is still to the anticlockwise of the key, or failing that it is forwarded to the successor.

### Q12 (1/1 pts) ✅ correct

In a Chord ring using m = 8, nodes with the following peer ids (or node ids) join the system: 45, 32, 132, 234, 99, 199. What is the comma-separated list of 8 finger table entries at node 45?

Use the text box below to enter your answer as a sequence of numeric values with each numeric value separated by a comma. Please ensure you enter one number for each finger table id i (you do not need to enter i, but only the node id's). (1 point)

- Your answer: `99,99,99,99,99,99,132,199`  ✅ (correct)

> Feedback: The ith finger table entry (i = 0 and upwards) at node n is the first node at or clockwise to n+2^i. A Query is forwarded, at each step, to the farthest clockwise neighbor which is still to the anticlockwise of the key, or failing that it is forwarded to the successor.

### Q13 (1/1 pts) ✅ correct

In a Chord ring using m = 9, nodes with the following peer ids (or node ids) join
the system: 1, 12, 123, 234, 345, 456, 501. If node 234 fails, which of the following nodes will not update any of their finger table entries or successors? (1 point)

- (x) 501  ← your answer, CORRECT
- ( ) 123
- ( ) 12
- ( ) 456

> Feedback: (1+128) mod 512 is 129, so 1 has 234 in its FTs

(12+128) mod 512 is 140, so 12 has 234 in its FTs

123’s successor is 234

(456+256) mod 512 is 200, so 456 has 234 in its FTs.

(501+128) mod 512 = 117 and (501+256) mod 512 = 245. So 501 does not have 234 in its FTs.

### Q14 (1/1 pts) ✅ correct

In a Chord ring using m = 9, nodes with the following peer ids (or node ids) join
the system: 1, 12, 123, 234, 345, 456, 501. The successor of  node 501 is: (1 point)

- ( ) 12
- ( ) 456
- ( ) 123
- (x) 1  ← your answer, CORRECT
- ( ) Nothing – 501 does not have a successor since it is the end of the ring

> Feedback: The ith finger table entry (i = 0 and upwards) at node n is the first node at or clockwise to n+2i. A Query is forwarded, at each step, to the farthest clockwise neighbor which is still to the anticlockwise of the key, or failing that it is forwarded to the successor.
