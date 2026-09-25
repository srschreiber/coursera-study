# Part 1 Quiz 4

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/ICyLP/part-1-quiz-4
- Item type: staffGraded
- Grading status: GRADED, earned grade 1
- Score: latest 25, highest 25, max 25

## Questions

### Q1 (1/1 pts) ✅ correct

A Cassandra deployment with 6 (N1 through N6) nodes across three racks: N1 and N2 are in rack 1; N3 and N4 in rack 2; N5 and N6 in rack 3. The Cassandra ring has the nodes in the following clockwise order: N1, N2, N3, N4, N5, N6. The NetworkTopologyStrategy is attempting to place 2 replicas of a given key. The first replica is placed by the partitioner at N3. The second replica will be placed at node: (1 point)

- (x) N5  ← your answer, CORRECT
- ( ) N4
- ( ) N6
- ( ) N2

> Feedback: To find the second replica the NetworkTopologyStrategy goes clockwise around the ring starting from the first replica, until it hits a node in a different rack than the first replica.

### Q2 (1/1 pts) ✅ correct

A Cassandra deployment uses the RackInferringSnitch. Two addresses 1.2.3.4 and 1.2.4.5: (1 point)

- ( ) Belong to different datacenters
- (x) Belong to the same datacenter but different racks  ← your answer, CORRECT
- ( ) Belong to the same rack but are different machines
- ( ) Are the same machine

> Feedback: The RackInferringSnitch treats node addresses as
x.<DC octet>.<rack octet>.<node octet>

### Q3 (1/1 pts) ✅ correct

A Cassandra-like key-value store system uses write consistency level of size W and read level of size R. There are N replicas of each key, and N is an even integer that is large enough. You are told that to maintain the strong consistency needed by your application, all conflicting writes must be detected by at least one replica (i.e., any two sets of written replicas must overlap) and a read must return the value of the latest acknowledged write (i.e., a read replica set must overlap with every written replica set). Which of the following combinations does NOT maintain strong consistency? (1 point)

- ( ) W=3N/4, R=N/4+1
- (x) W=N/2+1, R=N/2-1  ← your answer, CORRECT
- ( ) W=N/2+2, R=N/2-1
- ( ) W=N-1; R=2

> Feedback: The stated conditions require both W > N/2 and W+R > N.

### Q4 (1/1 pts) ✅ correct

A BASE system implements implies: (1 point)

- ( ) Sequential consistency
- ( ) Meaningful consistency
- (x) Eventual consistency  ← your answer, CORRECT
- ( ) No consistency

> Feedback: BASE stands for Basically Available Soft State Eventually Consistent.

### Q5 (1/1 pts) ✅ correct

The best definition of eventual consistency says that: (1 point)

- ( ) A read from a client will be answered eventually
- (x) If writes stop to a key, then all replicas of the key will eventually reflect the same value  ← your answer, CORRECT
- ( ) All replicas of a key will eventually reflect the same value
- ( ) A write from a client will be answered eventually

### Q6 (1/1 pts) ✅ correct

In HBase, which of the following entities is stored in-memory? (1 point)

- (x) MemStore  ← your answer, CORRECT
- ( ) HRegion
- ( ) HLog
- ( ) StoreFiles

### Q7 (1/1 pts) ✅ correct

In Cassandra, when a write comes in at a replica, it is immediately: (1 point)

- ( ) Stored on disk into an SSTable
- ( ) Stored on disk into a Memtable
- (x) Stored in memory into a Memtable  ← your answer, CORRECT
- ( ) Stored in memory into an SSTable

### Q8 (1/1 pts) ✅ correct

Someone gives you an arbitrary run (execution) trace from a system that implements eventual consistency. It is impossible that this run: (1 point)

- ( ) Returns an answer for a read from a write that was issued by a client after the read was issued by the client
- ( ) Returns an answer for a read from a write which was acknowledged at a client after the read result was received at the client
- ( ) Satisfies causal consistency
- (x) Returns an answer for a read from a write which was issued by a client after the read result was received at the client  ← your answer, CORRECT

> Feedback: Eventual consistency may return stale answers, but it cannot go back in time!

### Q9 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L1.png]
Answer the following question. (1 point)

-
In this run (execution), the total number of events summed across all processes is:

- Your answer: `25`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L1feedback.png]
There are 10 messages (each with a send and receive), and 5 instructions. This gives a total of 10+10+5=25 events.

### Q10 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2.png]
Answer the following question. (1 point)

-
The Lamport timestamp carried by the first message sent from P0 to P2 is:

- Your answer: `1`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2feedback.png]

### Q11 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2.png]
Answer the following question. (1 point)

-
The Lamport timestamp of the only process instruction at P3 is:

- Your answer: `8`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2feedback.png]

### Q12 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2.png]
Answer the following question. (1 point)

-
The ending Lamport timestamp at process P1 is:

- Your answer: `7`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2feedback.png]

### Q13 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2.png]
Answer the following question. (1 point)

-
The process with the highest Lamport timestamp at the end of this run is:

- ( ) P3
- ( ) All of the processes have the same timestamp at the end.
- ( ) P1
- (x) P0  ← your answer, CORRECT

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2feedback.png]

### Q14 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2.png]
Answer the following question. (1 point)

-
The number of events with a Lamport timestamp of 9 is:

- Your answer: `1`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2feedback.png]

### Q15 (1/1 pts) ✅ correct

A system using Lamport timestamps executes the following run shown in below. Initially, all four processes start with sequence numbers containing all zeros. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L2.png]
Answer the following question. (1 point)

-
The comma-separated list of Lamport timestamps to the last 3 events at P3 is:

Please ensure you enter answers in increasing order of integers.

- Your answer: `8,12,13`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/qbnpBux1EeWTZAooSlqjlw_19232de2f8b08f2cd79dfa188155a23a_HW4Q15V2.png?expiry=1790442396585&hmac=9SJ8KqVebwWo74HMy8ERUB-pUNjiPf5b1wvsexJ01Mg]

### Q16 (1/1 pts) ✅ correct

A system using vector timestamps executes the following run. Initially, all four processes start with vectors containing all zeros, i.e., each process starts at 0,0,0,0. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L4.png]
Answer the following question. Note: Please represent your vector timestamps as a comma-separated list (without the brackets). (1 point)

-
The ending vector timestamp at P1 is:

- Your answer: `5,8,6,5`  ✅ (correct)

> Feedback: Please see the picture below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L4feedback.png]

### Q17 (1/1 pts) ✅ correct

A system using vector timestamps executes the following run. Initially, all four processes start with vectors containing all zeros, i.e., each process starts at 0,0,0,0. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L4.png]
Answer the following question. Note: Please represent your vector timestamps as a comma-separated list (without the brackets). (1 point)

-
The vector timestamp of the only process instruction at P2 is:

- Your answer: `1,0,4,0`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L4feedback.png]

### Q18 (1/1 pts) ✅ correct

A system using vector timestamps executes the following run. Initially, all four processes start with vectors containing all zeros, i.e., each process starts at 0,0,0,0. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L3.png]
Answer the following question. Note: Please represent your vector timestamps as a comma-separated list (without the brackets). (1 point)

-
The receipt vector timestamp of the last message received at P2 is:

- Your answer: `4,3,9,1`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L3feedback.png]

### Q19 (1/1 pts) ✅ correct

A system using vector timestamps executes the following run. Initially, all four processes start with vectors containing all zeros, i.e., each process starts at 0,0,0,0. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L3.png]
Answer the following question. Note: Please represent your vector timestamps as a comma-separated list (without the brackets). (1 point)

-
The receipt timestamp of the last message received at P0 is:

- Your answer: `7,3,8,6`  ✅ (correct)

> Feedback: Please see the picture in below to check your answers.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L3feedback.png]

### Q20 (1/1 pts) ✅ correct

A system using vector timestamps executes the following run. Initially, all four processes start with vectors containing all zeros, i.e., each process starts at 0,0,0,0. An arrow shows a message, and each darkened circle shows a process instruction.
 [image: https://d396qusza40orc.cloudfront.net/cloudcomputing/images/Homework%202/HW2_L3.png]
Answer the following question. (1 point)

-
The number of events concurrent with the send event of the only message sent from P1 to P2 is:

- Your answer: `8`  ✅ (correct)

> Feedback: Concurrent events are sendM1, eventP0, recvM1, sendM5, eventP2, recvM4, recvM5, eventP3.

### Q21 (1/1 pts) ✅ correct

Your boss loves Bloom filters. To impress her, you start implementing one. Your Bloom filter uses m=32 bits and 3 hash functions h1, h2, and h3, where hi(x) = ((x2 +x3)*i) mod m.

In this case, answer the following question. (1 point)

-
Starting from an empty Bloom filter, you’ve inserted the following two elements: 2010, 2013. Note the bits in the Bloom filter have positions numbered 0 through 31. At the end of these insertions, which of the following bits IS NOT set to 1?

- (x) 16  ← your answer, CORRECT
- ( ) 24
- ( ) 28
- ( ) 12

> Feedback: Please see the following list to check your answers.

-
After inserting 2010 (h1(2010) = 12, h2(2010) = 24, h3(2010) = 4): Bits set: 12, 24, 4

-
After inserting 2013 (h1(2013) = 14, h2(2013) = 28, h3(2013) = 10): Bits set: 4, 10, 12, 14, 24, 28

### Q22 (1/1 pts) ✅ correct

Your boss loves Bloom filters. To impress her, you start implementing one. Your Bloom filter uses m=32 bits and 3 hash functions h1, h2, and h3, where hi(x) = ((x2 +x3)*i) mod m.

In this case, answer the following question. (1 point)

-
Starting from an empty Bloom filter, you’ve inserted the following three elements: 2010, 2013, 2007. Now some bits are set. Now, you insert the fourth element 2004. Note the bits in the Bloom filter have positions numbered 0 through 31. The bits whose values will change when the fourth element 2004 is inserted INCLUDE:

- ( ) 28
- ( ) 24
- (x) 0  ← your answer, CORRECT
- ( ) 8

> Feedback: Please see the following list to check your answers.

-
After inserting 2010 (h1(2010) = 12, h2(2010) = 24, h3(2010) = 4): Bits set: 12, 24, 4

-
After inserting 2013 (h1(2013) = 14, h2(2013) = 28, h3(2013) = 10): Bits set: 4, 10, 12, 14, 24, 28

-
After inserting 2007 (h1(2007) = 24, h2(2007) = 16, h3(2007) = 8): Bits set: 4, 8, 10, 12, 14, 16, 24, 28

-
After inserting 2004 (h1(2004) = 16, h2(2004) = 0, h3(2004) = 16): Bits set: 0, 4, 8, 10, 12, 14, 16, 24, 28 (0 is the only new bit set).

### Q23 (1/1 pts) ✅ correct

Your boss loves Bloom filters. To impress her, you start implementing one. Your Bloom filter uses m=32 bits and 3 hash functions h1, h2, and h3, where hi(x) = ((x2 +x3)*i) mod m.

In this case, answer the following question. (1 point)

-
Starting from an empty Bloom filter, you’ve inserted the following elements: 2010, 2013, 2007, 2004. If someone checks for membership of the element 2004, it will be found to be:

- (x) In the Bloom filter and not a false positive  ← your answer, CORRECT
- ( ) A false negative
- ( ) In the Bloom filter and hence a false positive
- ( ) Indeterminate since it was never inserted into the Bloom filter

> Feedback: Checking for membership of an already-inserted element always returns true, i.e., there are no false negatives.

### Q24 (1/1 pts) ✅ correct

Your boss loves Bloom filters. To impress her, you start implementing one. Your Bloom filter uses m=32 bits and 3 hash functions h1, h2, and h3, where hi(x) = ((x2 +x3)*i) mod m.

In this case, answer the following question. (1 point)

-
Starting from an empty Bloom filter, you’ve inserted the following elements: 2013, 2010, 2007, 2004, 2001, 1998. If someone checks for membership of the element 3200, it will be found to be:

- ( ) A false negative
- ( ) Indeterminate since it was never inserted into the Bloom filter
- ( ) Not in the Bloom filter
- (x) In the Bloom filter and hence a false positive  ← your answer, CORRECT

> Feedback: Please see the following list to check your answers.

-
After inserting 2013 (h1(2013) = 14, h2(2013) = 28, h3(2013) = 10): Bits set: 10, 14, 28

-
After inserting 2010 (h1(2010) = 12, h2(2010) = 24, h3(2010) = 4): Bits set: 4, 10, 12, 14, 24, 28

-
After inserting 2007 (h1(2007) = 24, h2(2007) = 16, h3(2010) = 8): Bits set: 4, 8, 10, 12, 14, 16, 24, 28

-
After inserting 2004 (h1(2004) = 16, h2(2004) = 0, h3(2004) = 16): Bits set: 0, 4, 8, 10, 12, 14, 16, 24, 28

-
After inserting 2001 (h1(2001) = 18, h2(2001) = 4, h3(2001) = 22): Bits set: 0, 4, 8, 10, 12, 14, 16, 18, 22, 24, 28

-
After inserting 1998 (h1(1998) = 28, h2(1998) = 24, h3(1998) = 20): Bits set: 0, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28

-
3200 will be a false positive since all of its hashes will map to the zeroth bit which has already been set by 2004.

### Q25 (1/1 pts) ✅ correct

Calibrations on a recent version of a (slow) operating system showed that on the client side, there is a delay of at least 5.0 ms for a packet to get from an application to the network interface and a delay of 4.0 ms for the opposite path (network interface to application buffer). The corresponding minimum delays for the server are 2.0 ms and 3.0 ms respectively.

What would be the accuracy of a run of the Cristian's algorithm between a client and server, both running this version of Linux, if the round trip time measured at the client is 26 ms?

- (x) 6 ms  ← your answer, CORRECT
- ( ) 2 ms
- ( ) 12 ms
- ( ) 14 ms

> Feedback: The earliest point at which the server could have placed the time in message mt was min1 = 5.0 + 3.0 = 8.0 ms after the client dispatched message mr. The latest point at which the server could have done this was min2 = 4.0 + 2.0 = 6.0 ms before message mt arrived at the client. The time by the server's clock when mt arrives at the client is therefore in the range: [t + min2, t + RTT - min1], where t is the time placed by the server in mt. The width of this range is (RTT - min1 - min2) = 12 ms. Thus, the accuracy = (RTT - min1 - min2)/2 = 6 ms.
