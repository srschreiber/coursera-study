# Part 1 Quiz 2

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/O5yL1/part-1-quiz-2
- Item type: staffGraded
- Grading status: GRADED, earned grade 1
- Score: latest 6, highest 6, max 6

## Questions

### Q1 (1/1 pts) ✅ correct

Given that there is at most one failure at a time in the system, which of the following protocols does NOT satisfy completeness? (1 point)

- (x) Central heartbeating  ← your answer, CORRECT
- ( ) Ring-style heartbeating
- ( ) All-to-all heartbeating
- ( ) Gossip-style heartbeating

### Q2 (1/1 pts) ✅ correct

Which of the following is faster? (1 point)

- (x) Pull gossip  ← your answer, CORRECT
- ( ) Push gossip

### Q3 (1/1 pts) ✅ correct

Someone designs a new failure detector where processes are organized in a binary tree. In a binary tree, there is one node (process) at the root (level 1), which has 2 children (nodes or processes) at level 2, which in turn each have 2 children at level 3, and so on. If node A is a child of node B, then B is a parent of A (and vice-versa). In this heartbeat protocol, every process sends heartbeats to its parent in the tree. Heartbeats are not relayed or gossiped. This protocol is: (1 point)

- ( ) Complete
- (x) Neither complete nor accurate  ← your answer, CORRECT
- ( ) Accurate

> Feedback: No heartbeat protocol is accurate (as heartbeats from a healthy node can be dropped). In this case, there is no one to detect the failure of the root of the tree.

### Q4 (1/1 pts) ✅ correct

A startup in your home garage is designing a new gossip-style failure detection similar to that discussed in lecture. In this new protocol, at a node (process or server) A, at local time = 140, its local entry for a node C is (address, counter, time) = (C, 340, 133). Tfail = 40. A receives a gossip message from node B containing one heartbeat as (sender-id, heartbeat counter), as shown below. Select the choice below where in all (four) cases, the left entry (heartbeat) leads to the right entry (updated heartbeat at A for C after receiving this heartbeat). (1 point)

-
(C, 349). ____________

-
(C, 123). ____________

-
(C, 60). _____________

-
(C, 355). ____________

- (x) -
 = (C, 349), A: (C, 349, 140)

-
 = (C, 123), A: (C, 340,133)

-
 = (C, 60), A: (C, 340, 133)

-
 = (C, 355), A: (C, 355, 140)  ← your answer, CORRECT
- ( ) -
 = (C, 349), A: (C, 349, 133)

-
 = (C, 123), A: (C, 340,133)

-
 = (C, 60), A: (C, 340, 133)

-
 = (C, 355), A: (C, 355, 133)
- ( ) -
 = (C, 349), A: (C, 349, 140)

-
 = (C, 123), A: (C, 340,133)

-
 = (C, 60), A: (C, 340, 133)

-
 = (C, 355), A: (C, 340, 133)
- ( ) -
 = (C, 349), A: (C, 349, 140)

-
 = (C, 123), A: (C, 340,140)

-
 = (C, 60), A: (C, 340, 140)

-
 = (C, 355), A: (C, 355, 140)

### Q5 (1/1 pts) ✅ correct

In a heartbeat protocol for failure detection, increasing the timeout (used for declaring a member as failed), without changing any other protocol parameter, results in which of the following? (Select multiple correct answers.)  (1 point)

- [x] Decreases false positive rate  ✅ correct answer
- [ ] Increases false positive rate  (not a correct answer)
- [x] Increases detection time  ✅ correct answer
- [ ] Increase in bandwidth  (not a correct answer)

### Q6 (1/1 pts) ✅ correct

In
a datacenter with 10,000 machines, the MTTF (mean time to failure) of a single
server is 36 months. You can assume each month has 30 days. The MTTF (mean time
to failure) until the next server fails in the data center is approximately: (1
point)

- ( ) 0.1 hours
- (x) 2.5 hours  ← your answer, CORRECT
- ( ) 0.1 months
- ( ) 2.5 months

> Feedback: MTTF
(mean time to failure) until next failure = MTTF of each machine divided by
total number of machines in data center.
