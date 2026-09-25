# Part 1 Quiz 1

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/g9rki/part-1-quiz-1
- Item type: staffGraded
- Grading status: GRADED, earned grade 1
- Score: latest 7, highest 7, max 7

## Questions

### Q1 (1/1 pts) ✅ correct

Today’s cloud computing systems are similar to previous generations of distributed systems in that they involve (select the best answer):  (1 point)

- ( ) On-demand access to cloud resources, with pay-as-you-go pricing
- ( ) New paradigms for computation like Hadoop
- (x) Servers coordinating with each other  ← your answer, CORRECT
- ( ) New programming paradigms

### Q2 (1/1 pts) ✅ correct

A datacenter run by an upstart company called Zahoo! consumed about 750 kWh in 2014. If only 500 kWh of this total power was used in running IT equipment (servers, routers, etc.), then the PUE of Zahoo’s datacenters is: (1 point)

- ( ) 0.0
- (x) 1.5  ← your answer, CORRECT
- ( ) 1.25
- ( ) 1.0

> Feedback: PUE = Power Usage Efficiency = Total power consumed divided by power consumed for running IT equipment.

### Q3 (1/1 pts) ✅ correct

The Hadoop Capacity Scheduler runs at: (1 point)

- ( ) Reduce
- ( ) None of these
- ( ) AM
- (x) RM  ← your answer, CORRECT

### Q4 (1/1 pts) ✅ correct

Someone in your company decides to run Hadoop on a cluster of eight machines, out of which seven machines are each quad core 2.2 GHz, 16 GB RAM, 1 TB hard disk, and the eighth machine is single core 2.2 GHz, 2 GB RAM, 1 TB hard disk. Further, this person has initialized the cluster with the setting where each of the eight machines is configured to run at most four containers (Map or Reduce tasks) at any time – the containers at each machine equally split all the resources at the machine. For a job that contains 32 Map tasks, you claim that this will result in: (1 point)

- ( ) No scheduling at all
- ( ) Long job completion time due to straggler tasks at the 16 GB nodes
- ( ) None of these options
- (x) Long job completion time due to straggler tasks at the 2 GB node  ← your answer, CORRECT

### Q5 (1/1 pts) ✅ correct

In MapReduce, a difference between the Map and Reduce functions is: (1 point)

- ( ) None of these options
- ( ) Map processes a set of all key-value pairs sharing the same key, while Reduce processes each input line separately.
- ( ) Both Map and Reduce process a set of all key-value pairs sharing the same key.
- (x) Reduce processes a set of all key-value pairs sharing the same key, while Map processes each input line separately.  ← your answer, CORRECT

### Q6 (1/1 pts) ✅ correct

Which of the following is a private cloud? (1 point)

- ( ) Google Cloud
- ( ) Amazon Web Services Simple Storage Service
- ( ) EMC’s data-hosting services
- (x) Yahoo’s internal Grid clusters, accessible to only Yahoo employees  ← your answer, CORRECT

### Q7 (1/1 pts) ✅ correct

The Hadoop locality-aware scheduler is trying to assign a map task T to the best server. The cluster has 3 racks R1, R2, and R3. Each rack Ri has 3 servers Si1, Si2, Si3. Right now, the only servers that have free containers are: S13, S31, and S32. The input file (or block) for map task T has three replicas, which HDFS has replicated at the following servers: S12, S21, and S23. Then the map task T will be scheduled at: (1 point)

- (x) S13  ← your answer, CORRECT
- ( ) S23
- ( ) S32
- ( ) S31
