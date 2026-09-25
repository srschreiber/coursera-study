# Week 03 - Week 3 Gossip, Membership, and Grids

Contents: 2 readings, 14 lectures, 1 quizzes/assignments.

## Readings

### Week 3 Overview

- Coursera: https://www.coursera.org/learn/cs-425/supplement/490TF/week-3-overview
- Lesson: Week 3 Overview

# Week 3: Gossip, Membership, and Grids

## Overview

 This week’s video lectures cover the topics of Grids, Membership, and Gossip. With this, you have all the concepts you need to complete the Programming Assignment in this course.

## Time

This week should take **approximately ****10 - 15 hours (this estimate excludes time spent on the programming assignment, which varies based on your background)** of dedicated time to complete, with its videos and assignments.

## Lessons

The lessons for this module are listed below :

|

**Lesson Title** |

**Time Estimated** |
|

**Lesson 1: Gossip** |

 |
|

Lecture 1.1. Multicast Problem |

10 minutes |
|

Lecture 1.2. The Gossip Protocol |

6 minutes |
|

Lecture 1.3. Gossip Analysis  |

16 minutes |
|

Lecture 1.4. Gossip Implementations |

5 minutes |
|

**Lesson 2: Membership** |

 |
|

Lecture 2.1. What Is Group Membership List? |

9 minutes |
|

Lecture 2.2. Failure Detectors |

10 minutes |
|

Lecture 2.3. Gossip-Style Membership |

8 minutes |
|

Lecture 2.4. What Is the Best Failure Detection? |

5 minutes |
|

Lecture 2.5. Another Probabilistic Failure Detector |

10 minutes |
|

Lecture 2.6. Dissemination and Suspicion |

9 minutes |
|

**Lesson 3: Grids** |

 |
|

Lecture 3.1. Grid Applications |

7 minutes |
|

Lecture 3.2. Grid Infrastructure |

12 minutes |
|

**Interview** |

 |
|

Interview with William Gropp |

20 minutes |
|

**_Part 1 Quiz 2_** |

1 - 2 hours |
|

**_Part 1 Programming Assignment_** |

30 - 45 hours |

## Goals and Objectives

After you actively engage in the learning experiences in this module, you should be able to:

-

Analyze various gossip/epidemic protocols.
-

Design and analyze various distributed membership protocols.
-

Know what grid computing is.

## Key Phrases/Concepts

Keep your eyes open for the following key terms or phrases as you interact with the lectures. These topics will help you better understand the content in this module.

-

Failure detectors
-

Membership protocols
-

Gossip/epidemic protocols
-

Grid computing

## Guiding Questions

Develop your answers to the following guiding questions while completing the activities throughout the week.

-

Why are gossip and epidemic protocols fast and reliable?
-

What is the most efficient way for cloud computing systems to detect failures of servers?
-

How is grid computing related to cloud computing?

## Readings

-

[Gossip-style FD](http://dl.acm.org/citation.cfm?id=1659238)
-

[SWIM](http://ieeexplore.ieee.org/document/1028914/?reload=true&arnumber=1028914)

## Tips for Success

To do well this week, I recommend that you do the following:

-

Review the video lectures a number of times to gain a solid understanding of the key questions and concepts introduced this week.
-

When possible, provide tips and suggestions to your peers in this class. As a learning community, we can help each other learn and grow. One way of doing this is by helping to address the questions that your peers pose. By engaging with each other, we’ll all learn better.
-

Refer to the video lectures and chapter readings we've read during this week and reference them in your responses. When appropriate, critique the information presented.
-

Take notes while you read the materials and watch the lectures for this week. By taking notes, you are interacting with the material and will find that it is easier to remember and to understand. With your notes, you’ll also find that it’s easier to complete your assignments. So, go ahead, do yourself a favor; take some notes!

### Part 1 Quiz 2 Instructions

- Coursera: https://www.coursera.org/learn/cs-425/supplement/cKFFG/part-1-quiz-2-instructions
- Lesson: Quiz

**Topics: **Gossip, Membership, and Grids

## Instructions

-

The quiz must be done individually.
-

 You can use any of the course resources, the course staff, or the Piazza forum to complete this assignment.
-

 However, when using the Piazza forum, you cannot post solutions on it! You can only use it to discuss ideas and concepts.
-

 For multiple choice, please note whether the question says there are MULTIPLE correct answers. For questions with MULTIPLE answers, you must specify ALL the correct answers and no wrong answers.

## Evaluation

Each quiz question is worth 1 point in Coursera. But the point value will be scaled down to 0.25 pts per question to calculate the grade of the quiz in this course.

## Important Dates

For deadline, refer to Course Deadlines, Late Policy and Academic Calendar page.

## Lectures

### 01 - Week 3 Introduction

#### Transcript

[MUSIC] In the second week of the course, we are
going to first start off by studying some building blocks for distributed
systems as they are used in the cloud. We'll see first gossip or
epidemic protocols, which are a very important building block. Then we'll see failure detection and
membership protocols. These building blocks will be used
in the coming weeks as we see more examples of distributed systems. The programming assignment,
if you are choosing to do that in this first part of cloud computing concepts,
is an implementation of one of these building blocks,
specifically the membership protocol. You'll be implementing your
own membership protocol inside the programming assignment. So it's very important for
you to go through these lectures. Then we'll see grid computing which
is another precursor to clouds. We'll see it in a little bit more
detail than we have seen before. That also appears in
the second week of the course. [MUSIC]

### 02 - 1.1. Multicast Problem

Slides: `C3_Gossip_A_CSRAfinal.pdf`

#### Slide text

```
•   Build a spanning tree among the processes of the
    multicast group
•   Use spanning tree to disseminate multicasts
•   Use either acknowledgments (ACKs) or negative
    acknowledgements (NAKs) to repair multicasts not
    received
•   SRM (Scalable Reliable Multicast)
      • Uses NAKs
      • But adds random delays, and uses exponential
         backoff to avoid NAK storms
•   RMTP (Reliable Multicast Transport Protocol)
      • Uses ACKs
      • But ACKs only sent to designated receivers, which
         then re-transmit missing multicasts
•   These protocols still cause an O(N) ACK/NAK overhead
```

#### Transcript

Hi there, uh, so, uh, in this, uh,
next series of lectures we'll be looking at, uh, this, uh, interesting
class of protocols, called gossip protocols
or epidemic protocols. But first, let's start
from the problem statement and slightly far away from,
uh, where we want to be. Uh, the problem that gossip
is trying to solve is called, uh, the multicast, uh, problem. So what is multicast? Suppose you have
a group of, uh, processes or a group of nodes. Uh, again, each
of these processes or each of these nodes is potentially a process
at some host on the Internet or connected to the network. And essentially, weh-uh,
all we need is that these processes or nodes need to
be able to talk with each other by being able to send
and receive messages. So here I have, uh, a red node, which has a particular
piece of information, um, and they have, I have other blue nodes
in the group that want to receive
this piece of information. For instance,
these might be computers on the floor
of the New York Stock Exchange, and this red computer
might have, uh, or the red node might have information about a latest, uh, stock trade which it wants to get out to the other brokers, on the floor. This is the multicast
problem, okay. So this is the problem where, you want to get information out to other members in your group and, of course, here I'm showing only one multicast message, there might be multiple multicast messages going around at the same time, each of them from potentially,
a different sender. Now multicast is
as opposed to broadcast, where you have
a piece of information that you want to
send out to the, uh, entire network
where everyone, all the computers or all the nodes on the, uh, network, uh, want to receive
that piece of information. That's broadcast. Uh, multicast on the other
hand, is more restricted. It's only within
a particular group of nodes or group of processes. So what are the requirements
for multicast protocol? Well, two of the most
important requirements, uh, as far as cloud computing
is concerned, are fault tolerance
and scalability. Uh, the nodes themselves
may crash, because processes, after all, are failure prone, as we know. Uh, the packets may be dropped
by the underlying network. They might also be delayed
by the underlying network. And so, uh, you want your
multicast to be reliable and have all
the non-faulty recipients receive ah the multicast in spite of these failures and delays that might happen
in the underlying network. You also want to your multicast
protocol to be scalable, uh, and have
an overhead, per node, that does not grow very quickly, as the number of nodes
grows into the thousands maybe even, uh, much higher,
into tens of thousands or hundreds of thousands. So, the protocol that is executed at the individual nodes as well as, the senders, uh, uh, is, uh, what is known
as the multicast protocol. The multicast protocol typically
sits at the application level, meaning that it does not deal
with the underlying network, but this is not a given,
because oftentimes, the application level
multicast protocols also talk with the underlying network level, um, um, uh, techniques, uh,
such as IP multicast. Ah, again, IP multicast is what's available in the underlying, uh, network itself. Um, uh, typically
this is implemented in routers and switches. Um, it's not necessarily
an attractive alternative because even though
it's available it may not be enabled in many
of the routers and switches, and so, uh, most of the multicast protocols that are, uh, deployed out there today, even though some of them may leverage wha-IP multicast where it's, uh, uh, available, all of them,
most of them today, uh, are application level, meaning that, they involve processes
talking with each other, without really worrying
about what's, uh, going on
in the network underneath. So one of the simplest ways
of doing multicast, is a centralized approach. You have the sender,
it has a list of recipients, it simply goes through
those recipients, in say, a for- or while-loop and it sends each
of these recipients either, a UDP or a TCP packet
that contains the information. Uh the multicast message itself. UDP stands for
User Datagram Protocol. It is a, um, uh, uh
connectionless and unreliable way
of transporting messages, but it's cheap
and it's low overhead. TCP is
Transmission Control Protocol, which is a, uh,
connection oriented way and a more reliable way
of sending, uh, messages. You could choose
either one of these. This is, of course,
the simplest implementation. Now, uh, one of the problems
with this implementation is, uh, when it comes
to fault tolerance. If the sender fails when it's
halfway through its "4" loop, essentially,
only half the receivers, uh, would have received
the multicast. Also, the overhead
on the sender is very high. Imagine a group where you have thousands of, uh, nodes in the group and, uh, in that particular case, uh, the sender has, uh, to go through, uh, has to send
a lot of messages. And this also increases
the latency, uh, the average time for a receiver to receive a multicast, could be as high as, um, O(N), which is, linear in the size
of the group itself. So to address that, the Tree-based Multicast Protocols have been developed, essentially, all of these, uh, uh, protocols develop a spanning tree among the, uh, nodes or the processes in the group. Uh, these include,
network level protocols, such as, IP multicast, where the spanning tree's among the routers and switches, in the underlying network, but also application
level multicast protocols, such as, SRM, RMTP, TRAM, TNTP, and a whole bunch of others. Uh, so, m, first of all,
this is attractive because, uh, the, uh, if you build a tree,
uh, well enough, if it is say, a balanced tree, then with N,
uh, nodes in your group, the height of the tree
is O(log(N)) and this means that the latency for a message to reach, any of the nodes
in the group is O(log(N)) as opposed to centralized, where the latency might have been, as high as, O(N) Also, the overhead
on each member in the group, both the sender, uh, as well as, any
of the receivers, is constant, especially if, the number
of children is constant. Uh, essentially, you recieve one copy of the multicast message and you send it out- send out as many copies
as you have children. However, one of the problems
here is that you need to, um, uh, set up
and maintain the tree. When, uh, load failures happen,
uh, the uh, um, nodes in the system might actually not receive multicast, for a while. For instance, if, uh, if this node at-at the leaf fails, then, uh, that's the only node that's affected, when that node rejoins the tree, uh, it will start
to recieve multicast. However, if this node that's
closer to the root fails, then essentially,
you have a situation where, none of its descendants
will receive any of the multicasts
that are sent, uh, before, uh, this part
of the tree is repaired. Perhaps it is replaced
by another node or it recovers and rejoins the tree
at that particular position. So, uh, because, as you know, failures are the norm
rather than the exception, you're always
going to have situations where nodes are failing
all the time and you have to spend some amount of bandwidth and resources in co-continuously repairing the tree, all the time. So, a little bit more on the
Tree-based Multicast Protocols. Essentially, these, uh,
build a spanning tree among the processes
of the multicast group. They use a spanning tree
to disseminate the multicast. They might prefer IP multicast
where its available-available to, uh, do this
initial dissemination. Thereafter, they use
either acknowledgements, positive acknowledgements
or negative acknowledgements, uh, to repair the multicasts that are not received by the, uh, receivers. Positive acknowledgements
are often called as ACKs and negative acknowledgements are called as NACKs, Uh, for instance, the Scalable
Reliable Multicast protocol, the SRM, uses NACKs. Essentially, um, uh, when
a receiver has not received, uh, multicast messages that it is expecting or for a while, it sends a repair request
up towards, uh, the root of the tree, and when these repair requests are received, uh, nodes closer to the root
of the tree send, uh, the latest multicasts
that they have or the missing multicasts as far as the receiver is concerned. One of the issues with
tree-based protocols is that, uh, the, uh, ACKs
and NACKs might implode, meaning that there might be very large numbers of ACKs and NACKs. For instance, for multicast
where the initial dissemination was not very successful
and was received at very few, uh, nodes in the group. To avoid this, the SRM protocol
adds random delays, uh, at the receiver. So receivers when they realize
they need to send out a NACK, they don't send out
the NACK immediately. They wait for a little bit of
time and then they send it out. Uh, If they need to send
a NACK multiple times, uh, then they might use
an exponential backoff, meaning that, uh, they, uh,
wait for, uh, a period of time that doubles every time
they wait. Uh, also, the messages
that are sent out might also be subject
to exponential backoff. The RMTP, the Reliable Multicast
Transport Protocol, uh, ha-is similar,
but it's slightly different. Instead of using
negative acknowledgements, it uses
positive acknowledgements. So, uh, the receivers
periodically send a digest or a collection
of acknowledgements for all the multicasts
that they received so far, uh, and, uh, if any of the messages are missing from this, uh, from these ACKs, then those messages are sent downwards towards the receivers. Now once again, you can have
ACK storms here and, uh, to avoid these
ACK storms, uh, there are certain receivers marked as designated receivers and, uh, the ACKs are sent only to these designated receivers and then these designated receivers forward, uh, the, uh, corresponding multicast messages down the tree. However, there have been
studies that have, uh, analyzed the scalability
of these protocols and even, in spite,
of the random delays and en-and exponential backoff, uh, both these, uh, uh, clas-uh, both these types of protocols, both, uh, NACK based
and ACK based protocols still suffer from, uh, uh, uh, a large number of NACKs
and ACKs that are sent out and the number of these
NACKs and ACKs typically grows
linearly with the, uh, size of the group itself. So these protocols are not as
scalable as they were intended, uh, to be. So this motivates
the development, um, or the introduction
of our gossip based or epidemic based protocol.

### 03 - 1.2. The Gossip Protocol

Slides: `C3_Gossip_B_CSRAfinal.pdf`

#### Slide text

```
•   So that was “Push” gossip
     • Once you have a multicast message, you start
         gossiping about it
     • Multiple messages? Gossip a random subset
         of them, or recently-received ones, or higher
         priority ones
•   There’s also “Pull” gossip
     • Periodically poll a few randomly selected
         processes for new multicast messages that you
         haven’t received
     • Get those messages
•   Hybrid variant: Push-Pull
     • As the name suggests
```

#### Transcript

In this lecture, we will see what the gossip protocol
actually looks like. So once again,
you have a group of, uh, nodes in your
multicast group and you have one
multicast sender. Again, we consider
only one multicast message and only one multicast sender, but the same protocol
can be applied, uh, to multiple mulst-multicast messages being sent out, each by a separate sender. So you want to get
the multicast across to all the nodes in the group. So, uh, what happens through
the-eh-the sender is that periodically, say once every
five seconds or so, uh, the period can be adjusted but let's say five seconds. Uh, the sender picks b, uh,
targets at random and sends them copies
of the multicast message using what is known
as a gossip message. This gossip message
can be transmitted using the connectionless, uh, undereliable protocol, UDP, uh, and this works, uh, because gossip by itself, the overall protocol has a lot of reliability,
as you will see soon. Okay, so this b again-again
is, uh, is a gossip parameter. B, typically,
is a very small number, say b equals two is a typical, uh, value for, uh,
the, uh, gossip fan out. B is called a gossip fan out. Uh, and it does this periodly. So every five seconds, a sender
will send out, will select b, uh, nodes at random
from the group, and sends them copies
of the gossip. Uh, these are, uh,
these nodes are picked, uh, uh, with replacements so, uh, it's potentially possible that, uh, the same nodes
are picked multiple times to receive the gossip. What do receivers do? so once, uh, uh, a node
receives its gossip, it is said to be infected
by the gossip. And after it doe-after it
receives the gossip, after it's infected
by the gossip, it does the same thing,
uh, as the sender, meaning that periodically,
every say five seconds, it sends out, um,
uh, b copies of the gossip, of the multicast message, to, uh, each, to a randomly selected, um, gossip target. So here you notice that, uh,
the two red nodes that received the gossip
in the previous round, uh, are sending out gossips now and there might be nodes
that receive, uh, multiple, duplicate gossips that contain the same
multicast message. So, there is some amount
of wastage, over here. Finally, in this particular run, all the, uh, nodes in the group get infected by this uh, uh, gossip, uh, spread and they receive
the multicast message. So, in a sense, gossip is using a slightly higher
number of messages, i-in order to get
the gossip across but this has certain amount of, uh, benefit as
you will see soon. Uh, and the amount
of overhead involved- the increased overhead involved is not that much. So this is the epidemic or
the gossip multicast protocol, uh, in a nutshell. When a, uh, node, eh, receives, uh, the, uh, gossip
or the multicast message, it's said to be infected. Otherwise, it's uninfected. When a node turns from
uninfected into infected it starts periodically
sending out, uh, copies of, uh, this gossip, uh, message, uh, to b t-targets,
uh, selected at random. Once again, the gossip, uh, protocol itself is not synchronized across different, uh, nodes so each node would essentially be running
its periods of gossip completely independent of
the other nodes in the system. However, when it comes
to analysis, uh, typically we assume that the nodes run in, uh, synchrony, uh, because this helps to make the analysis, uh, um, easier and more tractable. However, that analysis
also applies when nodes are
completely unsynchronized and are running gossip,
uh, periods, uh, completely independently
of each other. So that protocol,
that I described, was actually a push,
uh, gossip protocol, where, once a node has received a multicast message, it then, turns infected and starts to gossip that message. If you have multiple messages
essentially, uh, you can gossip, uh, either each
message separately or you can gossip uh,
a set of messages together, perhaps a random subset
of the messages you received, or you could gossip
recently received ones, recently rec-recently
received multicasts, uh, because they are
more important. Or multicast messages might be
marked with a priority, and you always prefer
the higher priority messages and put those in the gossip, uh, uh, rather than
the lower priority messages. Again, there are variants of the gossip protocol
that I described that have each of these, um, uh, implemented in them. Now the reverse of the push,
is the pull based, uh, gossip protocol, where essentially instead of, uh, sending out gossips
only when you turn infected, you send out gossips
all the time, and the gossips don't necessarily contain messages, instead they contain, um,
uh, queries, uh, for, uh, messages that might
have been received, uh, since the last time
you gossiped. So, essentially, periodically you send out a gossip message, uh, to a few randomly selected nodes in the group asking, "Hey, have you heard
of any multicasts "since this last multicast
that I heard?" If they have, then they send you
copies of the multicast message. That's called a, uh,
pull based, uh, um, protocol. There are also, uh,
hybrid, uh, variants, uh, hybrid push-pull variants
of gossip where, in the initial query
when you have the pull, uh, message going out, um, the pull query going out, you also include some
of the recent gossip messages that you received, that makes it
a push-pull hybrid protocol. In the next lecture,
we'll be analyzing, uh, how the push
and the pull protocol, uh, work, how fast they are, how fault tolerant they are.

### 04 - 1.3. Gossip Analysis

Slides: `C3_Gossip_C_CSRAfinal.pdf`

#### Slide text

```
•
•
•

From old mathematical branch of Epidemiology [Bailey 75]
• Population of (n+1) individuals mixing homogeneously
• Contact rate between any individual pair is 
• At any time, each individual is either uninfected
  (numbering x) or infected (numbering y)
• Then, x0  n, y0  1
    and at all times   x  y  n 1
• Infected–uninfected contact turns latter infected, and it
  stays infected
                                                              3

•
•
    dx
         xy
    dt

           n(n  1)               (n  1)
       x      ( n 1) t
                          ,y
          ne                 1  ne   ( n1)t

   b

   n

                    1
y  (n  1)        cb  2
                n

•
•

    •
           1
        n cb  2

    •

•
•

•
    •
    •
    •
    •

•
    •

    •

•
    •

    •

•

•
    •

    •

•

•   In all forms of gossip, it takes O(log(N)) rounds
    before about N/2 gets the gossip
      • Why? Because that’s the fastest you can
         spread a message – a spanning tree with
         fanout (degree) of constant degree has
         O(log(N)) total nodes
•   Thereafter, pull gossip is faster than push gossip
•   After the ith, round let p i be the fraction of non-
    infected processes. Then

                 p  p 
                                k 1

                   i 1     i
•   This is super-exponential
•   Second half of pull gossip finishes in time
    O(log(log(N))

•Network topology is                          N/2 nodes in a subnet
hierarchical
•Random gossip target
selection => core routers
face O(N) load (Why?)
•Fix: In subnet i, which
contains ni nodes, pick
gossip target in your subnet
with probability 1/ni
•Router load=O(1)
•Dissemination
time=O(log(N))                 N/2 nodes in a subnet
     •Why?

          b
       
          n

            n 1                  n 1
y         b
                              
           ( n 1) c log(n )         1
   1  ne  n                    1  cb 1
                                    n         1
                               (n  1)(1  cb 1 )
                                            n
                                            1
                               (n  1)  cb 2
                                          n
```

#### Transcript

So, in this, uh, lecture, we'll analyze the push-based
gossip protocol that we discussed
in the previous lecture, uh, and I'll also touch a little bit on the analysis of the pull-based
gossip protocol. This analysis willshow
three claims. The first that, uh, the, uh,
gossip protocol is lightweight, even when the groups
are very large, meaning they contain
a large number of nodes, uh, it spreads a multicast
quickly, even in large groups, and it is highly fault tolerant in spite of, uh, node failures and in spite
of packets being dropped. So, the analysis here is, uh, derived from an old branch of mathematics called epidemiology, and this is taken from a, uh, well-known textbook on epidemiology by Bailey,
published in 1975. Um, essentially, epidemiology
was a old branch of mathematics that studied the spread
of epidemic diseases among prison populations and among human populations
in society. Uh, the-the traditional, uh,
classical version of epidemi-epidemiology analysis has a population
of n+1 individuals mixing homogenously. Essentially, each
of these individuals is one of the nodes
in our system and consider these individuals or these molecules being inside a jar and you're
constantly shaking the jar and these molecules
are moving around and hitting each other
all the time. The contact rate per time unit between any pair
of individuals is beta. So, beta's typically
a number between 0 and 1. Uh, this is the probability that two individuals will come
in to contact with each other during a given time unit. At any time, each individual
is either uninfected and there are
x such uninfected individuals, or once it turns infected, it stays infected and the
number of infected is y. Initially, only one infected, uh, individual is present. This is the multicast center,
so y_0=1 and the remaining, of, uh, the remaining n individuals
are all uninfected at time zero. Of course, at all times, because a-an individual is either uninfected or infected, the sum of x+y at any given
point of time should be n+1, the number of individuals
in the group. When an uninfected individual
comes into contact with any infected individual, uh, the uninfected individual
turns into infected and it stays
infected thereafter. So, this sort of models, uh,
the, uh, gossip-based protocol that we have seen so far. So, how do you analyze this? Well, this is
a continues time process and you can essentially write this as a differential equation where you write
the rate of change of, uh, x, which is the, uh, uh, uh,
uninfected, uh, number in the-in the system, um,
as -beta*x*y. First of all, it's negative
because the number of uninfected is obvious going
down over time. Uh, now, why is it, uh,
-beta*x*y? Well, x*y is the, uh, total number of potential infected/uninfected contacts per time unit, and among those, um, uh, all possible x*y contacts, only a fraction, beta, happen because beta is, after all,
the contact rate, and for each of those contacts, one uninfected
turns into infected. So, essentially that's gives you
the rate of change of x, and this is
a differential equation which you can replace y,
ah, uh, using x+y=n+1 and it becomes
a differential equation in just one variable and it
has the following solution. Uh, if you have your differential equation
charts with you, you might actually be able
to derive the solution. I encourage you to do this if you're familiar with differential equations. One of the things for you
to notice here is that, uh, x over here, the equation for x, uh, has, um, a t in it,
which is the time, which is the number of rounds since the gossip-based
protocol has started. Remember again that here we are
using a synchronous, uh, model where all the processes or nodes
proceed in lock step, uh, from one round to another. Uh, this is the only for the,
uh, ease of analysis. The analysis holds even if, the, uh, processes
are all unsynchronized. So, you notice
that as t goes to infinity, as t becomes very large, the denominator is going
to become extremely large and x is gonna go down to zero. Similarly, here,
when t becomes very large, this second, uh, uh, factor
in the denominator, uh, is, uh, going to go to zero,
and so y is gonna go to n+1. So, eventually
the number of uninfected becomes very close to zero and the number of infected
becomes very close to n+1, which is the total
number of nodes in the group. So, eventually gossip converges and everyone receives
the gossip. That's not surprising. Well, what we want to show is that gossip actually
converges fairly fast. So, this is our epidemic
multicast protocol and essentially,
this is what we're analyzing. So, in the gossip based and
epidemic multicast protocol, the value beta is actually b/n. Well, why is this? Consider a, uh,
an-an infected, uh, node and consider one particular uninfected node. The probability that
this infected node picks this particular uninfected node as a gossip target during the round is essentially the probability
that it is one of the b targets picked by the infected
node during that round. So, since there are n possible,
um, uh, uh, targets, uh, per round and the probability
that this uninfected node is picked as a gossip target, simply b/n. So, you substitute
this value beta into the equation
that we derived and you substitute
the value of t=clog(n) this essentially says that you
have, uh, n- uh, log(n) rounds that have happened so far and actually
all the log(n) rounds that have happened so far. And you substitute
in the previous equations, you get the number, uh,
of infected nodes in the system is n+1, the total number of nodes,
minus this quantity 1/n^(cb-2) This c comes
from the clog(n) here, and the b comes from, uh,
the fan out of the gossip. Now, if I set c to be some small
number like 2 and b to be
a small fan out like 2, this, uh, term becomes
1/n^(4-2), or 1/n^2. That's a very small number
that's very close to zero. Essentially what that's-
what that is saying is that after 2log(n) rounds, as long as I'm using
a gossip fan out of 2, the, ah, number of infected nodes in the system will be n+1 minus
a very small number, 1/n^2, which is very close to 0,
and in fact, as n increases, this number goes
even closer to 0. Essentially this is saying
that the gossip converges within a logarithmic
number of rounds and it gets very close to n+1
infected being in the system. So, as l- as long as you set c
and b to be small numbers that are independent of n, they are constants,
within clog(n) rounds. This means low latency,
all but a very small fraction of number of nodes receive,
uh, the multicast. This means that the multicast
is highly reliable and it gets to almost everyone with high probability within a logarithmic
number of rounds. And since only clog(n) rounds
have happened, um, nodes in the worst case
are sent out, uh, each node is sent out c*b*log(n) copies of the gossip message. So, the order, the, ah, overhead on each node
is also logarithmic. So, essentially this shows
the three claims that I have, uh, that I, uh, that I showed in the beginning of this lecture. It's reliable, it's low
latency, and it's lightweight. Now, I hope that
some of you are thinking, "Well, it's log(n),
it's not constant," right? Um, the latency is O(log(n)),
it's not constant, um, the overhead is O(log(n)),
it's not constant. But, why is O(log(n))
so sacrosanct? Well, log(n) is really not
constant in theory, but when it comes, uh,
to practice, uh, it is a very slowly
growing number. A log base 2(1000) = 10,
log base 2(1M) = 20, log base 2 (1B)~30, and if you consider the IP before address space, uh, log base 2(all IPv4 address)=32. So, these are
fairly small, uh, numbers, and as far as practitioners
are concerned, many practitioners
consider log(n) to be a fairly small, uh, number and a constant
for practical purposes. So, that was the push-based
gossip protocol, um, and, uh, the next thing that we need to show is, uh, the, uh, fault tolerance of the push-based
gossip protocol. What happens when
you have packet loss? Suppose 50% of the packets
get dropped, uh, from the network. Again, we can analyze
the protocol by simply replacing b by b/2 because, after all, uh, the gossip targets
are selectived at random, so even if you have,
um, uh, uh, uh, packet losses all over the network, uh, these packet losses
will be distributed uniformly at random among
the gossip messages. So, you simply analyze b by,
uh, nah, this, do the same analysis as before
by replacing b by b/2 because half the gossip messages get dropped, and it turns out, and you can check this
for yourself, uh, that to achieve the same
reliability as 0% packet loss, you only need to wait
for twice as many rounds. So, instead
of using clog(n) rounds, you wait for 2clog(n) rounds and you get the same reliability
as, uh, with a 50- as with the 0% packet loss rate. With node failure,
50% of the nodes fail, uh, you replace n by n/2 because there are
only half the nodes that are alive in the system, you care only about
the reliability at them, and you replace b
by b/2, ah, again, again, half the gossips
get dropped because they are sent
to one of the failed nodes. And once again, ah, you get
a similar, um, a result as, uh, before by increasing
the number of log- uh, the-the rounds by only
a constant factor- um, uh, multiplicative, constant multiplicative factor, you get the same reliability as if you had no node failures
in the system. So, with failures, one of the things that could
happen with the gossip is that it could die
out very quickly and this, uh, if it does happen, typically happens
very early in the gossip. Very early in the gossip,
if the sender, uh, before it sends out a copy of the gossip dies, then obviously you're not gonna get the gossip spread out anywhere. The sender might send out one
copy of the gossip, uh, to a few nodes in the system, just one round, and then all these, uh,
first round recipients and the sender byte might die. Okay, the probability
of this happening is very low because these
are selected at random, so even if you have gossip
running in a data center and an entire rack goes out, as long as one, um, er, process outside the rack got the gossip, you'd still have the gossip spread and it is very resilient. So, once the gossip has infected
a small amount of nodes in the system,
just a few rounds, after that it's very hard
to kill the gossip. And this is kinda,
should be familiar to you because this is uh, paralleling uh, the way in which
disease is spread in, uh, human populations or
rumors spread in society. Once a rumor of the disease gets
out, uh, a little bit farther, it's very hard to contain. Okay, so, all the analysis
that we've seen in the previous slides
is with high probability, and this has been shown
in another book, uh, by Galey and Dani, uh, which also analyzed, uh, gossip. Here again, um, here we are
using gossip or epidemics for a good purpose. Um, uh, the same behavior
is seen when rumors spread in society, infections diseases
spread in populations, or viruses and worms, uh,
spread, uh, on the internet. So, what about the
pull-gossip protocol? So far we have looked
at the push-gossip protocol, what about pull? Uh, in all forms of gossip,
whether it's push or pull, it takes O(log(n)) rounds
before the, uh, before, uh, about half the nodes
in the system get the gossip. Why is this? Well, uh, the best you can do is essentially build
a spanning tree among the nodes in the system, and if you have
a constant fan out, constant number of children per node in
f-in the spanning tree, it takes O(log(n)) rounds for
about half the nodes to get, uh, this, uh, uh, gossip message
in the best case. However, thereafter, after about half the nodes
have received the gossip, pull is faster than push. Yeah, how-to see this,
let's look at the following: After the ith round, let p_i be the fraction of noninfected or uninfected
processes in the system, then in the i+1 round, uh, the value of p_(i+1) is essentially (p_i)/(k+1) where k is the, um,
number of, um, k is the number
of, uh, gossip targets. K=b in this particular case. Why is this? Well, the probability that you
stay infected- uh, noninfected at the end of the i+1 round is the probability
that you were uninfected at the beginning
of the i+1 round, so that's p_i by itself, and also the probability that each of the k or b,
um, uh, targets that you contacted at random were all also uninfected
by the gossip, and that's, uh, times (p_i)^k, and that's how you get
(p_i)^(k+1). So, this goes around
very quickly, and in fact this goes around, uh, super exponentially, faster than exponential, and it can show
that this is O(log(log(n)), not just O(log(n)),
but it's O(log(log(n)), so it's much faster
than logarithmic. So, overall the pull gossip
protocol is still O(log(n)), but, ah, uh, it's much faster
in the second half. So, this should give you
an idea of getting, b-of designing, perhaps,
a push-pull hybrid protocol where you use push
in the beginning portion to get the gossip out
very quickly and then use pull, uh,
in the later rounds, uh, to, uh, um, uh, to-to get it out to everyone else
in-in the system very quickly. Finally, uh,
the gossip protocols that we've discussed
so far are not topology aware, so, uh, when it comes
to a hierarchical topology, whether it's, uh,
on the internet using subnets or whether it's on-in a data
center using, uh, racks, uh, the core switches
and routers might get overloaded
quite a bit. So, for instance,
consider a scenario where I have two subnets, perhaps two racks; uh, the top subnet
and the bottom subnet each with n/2 nodes, uh,
from the group. Since each node selects a gossip
target uniformly at random, about half the gossips are gonna go across from one subnet to the other, okay, and also from the bottom to the top. This means that
the router sees, uh, n/2, actually b*(n/2) gossips
go out per, uh, gossip period and so the load on the router is going to be O(n),
which is very, very high. So, the fix to this
is to do the following. You have gossip that, uh,
prefers nodes in your own subnet with a high probability and nodes outside your subnet
with a lower probability. If your subnet contains ni
or n_i, uh, nodes, you, uh, gossip, uh, um, uh, outside your
subnet with probablity 1/(n_i). With probability 1-(1/(n_i)), you gossip
within your own subnet. So, this means
that within your own subnet, because the probability
of gossiping is still very close to one, ah, it's gonna spread
in O(log(n)) time, and this is true
for any one of these subnets. And then after a subnet
has been completely infected, uh, since everyone gossips
outside with probability 1/(n_i) and there is n_i such nodes
gossiping outside, it takes O(1), uh,
rounds on expectation for the gossip to go across the
router to the other, uh, subnet and for someone in the other
subnet to get infected. After that, again, it's gonna take O(log(n)) rounds to spread within
that subnet itself. So, overall it's still O(log(n)) +, uh, O(1) + O(log(n)), uh, for it to get across and so it's still O(log(n))
rounds dissemination time, and instead what we have done is that we have re-reduced the
load on the router to be O(1). Why is it O(1)? Well, uh, because essentially
you have n_i nodes in the- in one subnet
and since each of them sends a gossip out
with probability 1/(n_i), the, uh, expected number of
gossips going through the router is (n_i*1)/(n_i),
which is O(1). So, that concludes our, uh,
analysis of, uh, gossip. Uh, in the next lecture
we'll see, uh, some practical permutations
of, uh, gossip. Uh, now, for those of you who
have been trying to analyze, uh, the push analysis, here is an addendum where the
analysis is actually shown out. Uh, I encourage you
to go through this, uh, and make sure that your analysis was, in fact, correct.

### 05 - 1.4. Gossip Implementations

Slides: `C3_Gossip_D_CSRAfinal.pdf`

#### Slide text

```
•
•

•
                ‘
•           ‘
•                   ‘
•                           ‘
        ‘
•                       ‘
•

•
    ‘

•
•
•

•
•
```

#### Transcript

In this, uh, lecture
we'll see a little bit and just take a peek into some
of the, uh, uh, implementations of gossip that exist out there. I'll give you a list and I'll give you a peek
into one of them. So, uh, we have discussed a lot
of theories so far for gossip, and I'm sure some of you are
wondering, uh, is this all a bunch of equations or are there
implementations yet. Well, there's a bunch of
implementations out there starting from the 1980s when, um, Xerox used, uh, um, gossip in their, um, uh, email and
database transactions systems. Uh, the Clearinghouse and
Bayou projects, uh, had, um, gossip-based protocols
running inside of them where essentially the servers, uh, would talk with ea- the e-mail servers would talk with each other and exchange
gossip messages, uh, which then they would,
uh, help, uh, to make sure that every one-every one of the servers received all the emails
that had been sent out. Um, this is sort of similar
to the NNTP protocol that I'll describe
on the next slide. The refDBMS system
also used gossip. Bimodal Multicast, uh, um, uh,
which was published in the late '90s, uh, a-and has continued, uh,
were from Cornell University, um, uh, brought back gossip, uh, to be used in fast
multicast implementations. Sensor networks
and wireless networks have also used,
uh, uh, uh, gossip. Uh, the Amazon web services
cloud infrastructure is rumored to use, uh, gossip,
uh, to, uh, uh, uh, to exchange messages
among the servers in both the EC2
and the S3 cloud. Again, this is rumored: none of the, uh, none of the,
uh, design details have actually been
published at all, but this is rumored and actually if you look
at the, um, uh, the postmortems from Amazon web
services outages, you will, uh, see that
some of the outages refer to gossip messages
and the use, uh, thereof. Uh, key-value stores
such as Cassandra, uh, also use gossip
for maintaining membership lists among the, um, uh, knowns
in the system. And the NNTP, the Network News
Transport Protocol, which is used in news groups, uh, which have been fairly
active for many, many decades, uh, which is a usenet NNTP
protocol, also use gossip. Uh, so essentially
in that NNTP protocol, each client uploads
and downloads news posts from a news server, uh, then the servers talk
with each other and exchange
the latest news posts so that every server
has all the posts. So, an upstream server might,
uh, um, send a message to the downstream server saying
"why don't we check these, uh, "message IDs that I
have received recently." Downstream server checks
the ones that, uh, it has not received and sends
back, uh, a message saying: "Why don't you give me those missing messages." And upstream then server sends a
"take this," uh, uh, message, followed by the action
messages themselves. Then the downstream
server acknowledges. And this is going on all the
time among the servers, in NN-among NNTP servers,
and so eventually, um, all the servers receive, uh,
all the messages. Of course, messages
always keep coming and so essentially the group
of servers is always, uh, in a wave, and that wave
is always, um, uh, lagging behind
the actual wave of messages and is always trying
to catch up. If the messages stop at any
point of time, uh, then, uh, the servers catch up
and they, um, uh, have the same set
of messages as each other, um, and, uh, the servers
and the NNTP implementation also, uh, uh, uh, um, delete
the posts after a while, uh, so, after the, you know,
the-the-after all the clients have in fact downloaded
the posts themselves so the servers are not keeping
the posts around forever. So that concludes our
discussion of, uh, gossip. Uh, gossip is a solution
to the multicast problem in, uh, uh, uh, large groups
of nodes or processes. Um, there are many tree-based
multicast protocols, and also some clients multicast
protocols that are out there, but they don't scale
as well as gossip, they're not as fault tolerant as, uh, gossip. Gossip is also known
as epidemics, essentially this is using, uh, the phenomenon
of rumor-spreading or, uh, disease-spreading or
spreading of worms in internet, uh, for a good purpose here: uh, to spread,
uh, multicast messages among large groups
of processes fairly quickly, fairly, uh, fault tolerantly, fairly reliably, and in a very scalable
and also topology-aware manner.

### 06 - 2.1. What is Group Membership List

Slides: `C3_Member_A_CSRAfinal.pdf`

#### Slide text

```

```

#### Transcript

[MUSIC] Hi everyone, so today we're going to
discuss group membership and its need in datacenters and
in cloud environments. So let's start with a scenario where
you've been put in charge of a datacenter, perhaps that's your new job. And your manager tells you, no, we don't
have any failures in our data center. Would you believe your manager? And if you didn't believe your manager,
what would be your first responsibility? Well, your first responsibility would
be to build a mechanism that detects failures of servers in your datacenter. I encourage you to think at this point
about some of the things that could go wrong if you did not
build a failure detector. And I'll come back to this
question in a couple of minutes. But why would you not
believe your manager? Well, in datacenters, failures
are the norm rather than the exception. And let's see an example
that illustrates this. Suppose the failure rate of one machine,
say the hardware, software, failure rate
is once every 10 years. This is a little bit optimistic, but
let's say it's one every 10 years, and that means it's 120 months on average. When you increase the number of machines
in your datacenter from one to 120, the mean time to failure goes
down by a factor of 120. This means that the average time
between now and the first machine, among those 120 failing, is 120 months
divided by 120 which is 1 month. This is known as the MTTF,
the mean time to failure. Still it's looking fine, but suppose you have a good scale datacenter,
12,000 servers. Then the mean time to failure goes
down by a factor of 12,000, and that turns out to be about 7.2 hours. You can imagine what happens if
I make that a 120,000 servers, it would be 0.72 hours. Essentially this means that failures
are happening almost all the time. And any system that you build that
assumes failures don't happen will not work correctly. So what are the things that could go wrong
if you didn't build a failure detector? Essentially, what you can have is you
could have data loss because some of the servers have gone down. And your software has not
detected this failure and not recovered from that failure. You could also have inconsistency in
your system which could lead to loss of revenue for your customers. And eventual shut down of your datacenter
and the services that it provides. So how do you build a failure detector? You have a couple of options,
the first option is to hire 1,000 people. Each monitoring one or
a few machines in the datacenter and reporting to you when the machine fails. The second option is to write a program or software that in a distributed manner
automatically detects failures and reports to your workstation, or
maybe even takes corrective action. Well, clearly the second approach
is more preferable because, one, it does not require you to spend
money to hire 1,000 people. Second, it's much faster, and third, it might even be able to take
corrective action upon detecting failures. So we won't use the first
option obviously, and we'll go down the path
of the second option. So our target here is any distributed
system that involves multiple members in a group. The group might be a datacenter
where we have groups of servers, the members are servers. It might be a group of servers
replicating one or more files, for instance in a peer-to-peer system. Or it might be a group of
servers running a distributed or a replicated database,
it doesn't matter what these are. The kinds of failures we're dealing with
are crash-stop or fail-stop failures. This essentially means that
once a member of the group, we'll call that member a process. Once a process fails, it basically
stops executing any instructions from its point of failure
until time infinity. It does not recover, also it does not
take any actions which deviate from the original code or
the original algorithm that you coded in. This is different from
a few other failure models, such as a crash recovery failure
model where processes can recover. The fail-stop, crash-stop failure model can be easily
changed to be a crash recovery model. When you have processes rejoin the system
with a slightly different identifier. The failure model where processes fail and
deviate from their actions, that is known as Byzantine failure model. We won't discuss that in this series of
lectures, we might discuss them later on. So essentially what you have at each
process in your group of processes is that you have a membership list here. Which maintains the list of most or all of the other processes that are currently in
your system and that have not yet failed. That means non-faulty processes. This membership list is accessed
by a variety of applications, for instance the application might be,
A gossip-based application, which you will find
elsewhere in this course. Or it might be an overlay or
a distributed hash table application, which you'll find elsewhere
in the course as well. So essentially the membership list or
accessing the membership list or even sampling the membership list is
an important building block of many distributed algorithms. So our goal is to build
the membership protocol which keeps this membership
list up-to-date. As processes join the system, the group, as they fail silently, and as they leave. The difference between failure and
leave is that a process, when it fails, it fails silently without telling anyone. However, a process leave essentially
involves it telling people and giving them time to update their
membership lists before it changes. One of the biggest challenges is that this
membership protocol has to communicate over the unreliable communication medium. Which can drop packets,
which can delay packets quite a bit. The quality of the semantics of this
list might be of different flavors. The list might be a complete list that
is consistent at all times across all the processes in the group, this is
known as strongly consistent membership. For instance, virtual synchrony, which is a well known distributed
computing paradigm, relies on this. There are also algorithms
such as gossip style, algorithms which rely on
an almost complete list. There are a variety of examples of this, some of which you will
see in this lecture. There are also other algorithms
such as SCAMP, T-MAN and Cyclon which you can look up papers for on
the web which make a partial-random list. Our focus here is on almost complete
lists because they are weakly consistent. But they're close enough to the complete
list itself that they're useful to a variety of applications. So you'll notice here that I put
two sub-protocols in the membership protocol place. One is a mechanism that detects failures, the second is a mechanism that
disseminates information about these failures after detection to
the other processes in the system. The dissemination component can also be
used to disseminate information about process joints as well as
process leaves in the system. So that was for one process pi,
however the same algorithm or the same software is running at
all the processes in your group. And this might be thousands of processes, we'll call these as
the members of the group. And remember that they're communicating
over an unreliable communication medium. The goal here is that, just suppose
we have two processes, pi and pj, and we're dealing with
crash-stop failures only. When process pj crashes,
this could be any of the process pj, some process finds out
quickly about this failure. This is the goal of the failure detector
component of the membership protocols. Now multiple processes might find out
about this failure, but we need to ensure that at least one non-faulty process
finds out about this failure. What it does, it can then use
the dissemination component to disseminate this information to
the other processes quickly. So that they get to know about this
failure and update their membership lists. So next we will discuss how to design
group membership protocol that has both the failure detector component and
the dissemination component. [MUSIC]

### 07 - 2.2. Failure Detectors

Slides: `C3_Member_B_CSRAfinal.pdf`

#### Slide text

```

```

#### Transcript

So, in this lecture we will discuss some of the important properties of failure detectors. And we'll see some very simple failure detectors. Just to remind you again, we have a large group of processes and you have the same algorithm or protocols running at each of the processes in this system. We might consider the protocol running at only a given process PI, because the same thing is running at all processes. The communication is over an unreliable network. So once again, if a process PJ crashes, we need a failure detector to detect this failure, at least one process in the system. Perhaps, even multiple processes in the system. So the fact that PJ crashes is inevitable. All processes crash at some point of time. And as we have seen before, and this is a frequent occurrence in a large scale data center. This is the common case and the norm rather than the exception. And the frequency goes up linearly with the size of the data center. The frequency of failures. There are too important correctness properties for failure detectors, they are known as completeness and accuracy. Completeness essentially says that when a process fails, that process is detected eventually by at least one other non faulty process. There are two important terms there. The first is that it is detected by a non faulty process. Detection by a faulty process really doesn't make a difference. The second important term is eventually. This means that there is no time bound as of now at least, of when the process is detected as having failed. The second is kind of the converse but not really. It's known as accuracy which essentially says that, when a process is detected as having failed that process has in fact failed. In other words, it says that there are no mistaken failure detections or there are no false positives. But also, two other performance criteria, we'll discuss that in a little bit, but let's focus on just these two important criteria. The bad news is that achieving both of these properties, completeness and accuracy, over a network which loses packets, which can delay packets quite a bit, is impossible. In other words, over the Internet, all the wireless networks that we have today, or any realistic network, you cannot build a failure detector that is 100 percent complete, meaning, it detects all failures. And is 100 percent accurate, meaning, it never makes any mistakes. Essentially,this boils down to the fact that the failure detector problem is equivalent to another well-known problem in distributed computing known as consensus. In a consensus problem, which you'll see elsewhere in the course. Essentially, you'll have a group of processes that are trying to decide on the value of a single bit and that is a well-known proof that shows that this is impossible to do over lossy and delayed networks. So what happens in real life? In real life, failure detectors always guarantee completeness 100 percent of the time. And so they have to punt on the accuracy. Which means that the accuracy guarantee is either partial or it's a probabilistic guarantee. Always close to 100 percent, but never getting exactly at 100 percent. Why is this trade-off the right trade-off? Well you need completeness because when you have a failure, you definitely want to be able to detect it and recover from it. Make your data consistent again. You don't want to miss any failures. However, if you mistakenly did it go figure, it's fine for you to ask that poor victim process to leave the system and rejoin again perhaps with a different identifier. The overhead of doing that is less than if you did the reverse. All the failure detectors we'll study have this property of 100 percent completeness and less than 100 percent accuracy. There are two of the properties that are important for performance of failure detectors, speed is the first one. The speed basically says that between the time when a failure actually happens, and the first other non faulty process detects this failure, we want that time to first detection of failure to be as small as possible. You want your system to be responsive. A scale is important because you want your system to scale as a number of processes and your group grows. This means that you want to have a low and equally distributed load in terms of number of messages on each process or member in your group. Also, you want low overall network load in terms of the number of messages. Also, you want to avoid single points of failure, you want to avoid bottlenecks. And you want to get into all of these properties in spite of the fact that you might have arbitrary simultaneous process figures. So, it's not given to you that one process fails, your failure detector detects it, and then the next process fails. Multiple processes might fail simultaneously and your failure to vector must capture all of these failures. So let's see very simple failure detector protocol known as centralized heartbeating. The basic concept here is heartbeating. Consider the process PI, which needs to be detected as having failed. Essentially, what it does is that it sends periodic heartbeats to another process, PJ. A heartbeat is basically a message that carries a sequenced number. Every time PI sends a heartbeat to PJ, it increments this local sequence number and sends it over. Heartbeats are sent periodically, say once every pi seconds. PJ keeps track of when the last heartbeat from PI was received. If a new heartbeat has not been received within a specified time out, then it marks PI as having failed. The centralized hardbeating version of this protocol ensures that all of the other n-1 processes in the system sent heartbeats to one central process PJ. So, the nice thing about this is that if any of these other process and management fail, their heartbeat will stop arriving at PJ and PJ will time out and mark that process as having failed. So this protocol, for all the other n-1 processes, other than PJ, it is complete. However, when PJ fails, there is no guarantee about who detects that failure. Also the other disadvantage here is that if you have thousands of proxies in your group, PJ might be highly overloaded with messages. Obedient is the ring heartbeating where all the processes are organized in a virtual ring. And every process sends heartbeats to at least one of its neighbors. In this particular picture, each process sends heartbeats to it's left neighbor, as well as its right neighbor, or its anticlockwise as well as its clockwise neighbor. The quality of the heartbeats is the same. Again, it's a sequence number that is incremented locally and then sent over and the quality of the detection is again the same. If PJ times out are waiting for PIs heartbeats, then it marks PI as having failed. So this is better than a centralized approach because it avoids a hotspot but it's still not good enough because when you have multiple failures, you might have some failures that go undetected. Consider the situation where both of PIs anticlockwise and clockwise neighbors failed. And before the ring is repaired, then PI fails. At this point of time, PIs failure might go undetected because both its neighbors were down when PI failed. Of course, repairing the rings also and other overhead which you have to deal with over here, in the ring heartbeating approach. The third heartbeating approach is called, All-To-All heartbeating. Where each process PI, sends out heartbeats not to one or two other process in the system but to all the other processes in the system. And the processes do likewise they timeout waiting for heartbeats. And if their time are then they mark the corresponding processes having failed. So if PJ times out waiting for PI's heart beats, it marks PI as having failed. This is pretty good. First of all, it has an equal load per member. The load is high. And we'll get to the load later on why this might actually be not so bad. But we'll see that later on. First of all, the load is equal, it's well distributed across all. Second the protocol is complete. If PI fails, then as long as there is at least one other non-faulty process in the group, it will time-out waiting for PI's heartbeats. And it will detect PI as having failed. So it is complete for sure. So next lecture we'll see how to increase the robustness of all-to-all heartbeating. Essentially, the problem with all-to-all heartbeating is that if you have one process PJ that is slow and is receiving packets at longer delay than others, it might end up marking all the other or almost all the other processes as having failed, with higher probability. And so you might have a lower accuracy or a very high rate of false positives in all-to-all heartbeating. You can improve this by using more robust ways of sending out to the hardbeat, rather than just direct messages.

### 08 - 2.3. Gossip-Style Membership

Slides: `C3_Member_C_CSRAfinal.pdf`

#### Slide text

```

```

#### Transcript

In this lecture we will see
how gossip-style, uh, failure detection works. Gossip-style failure detection
is essentially, ah, a variant of
call-to-all heartbeating which is more robust
than all-to-all heartbeating. Once again,
the basic concept is that every process, uh, wants
to send out it-its heartbeats to all the other processes
in the system. The heartbeats are again
incremented sequence numbers that are incremented locally. Processes timeout waiting
for heartbeats and mark the corresponding
sources as having failure. We want really good accuracy
properties here, which was lacking in the all
to all variant of heartbeating. So here is how gossip-style
failure detection works in a nutshell. Here I have an example
with, uh, four processes, uh, marked as 1, 2, 3, and 4. Every process maintains a table. Let's look at the table for 1, and the table for 1
shows, uh, four entries for each of the four processes
in the system. There are, uh, so, four rows. There are three columns. The first column is the address
and the process which is basically the ID. The second is
the heartbeat counter received from that corresponding process. Third is the local time at which that heartbeat counter
was last updated. So, for instance, at process 1, the row for 2 says that the last heartbeat that was received from process 2 at process 1
was numbered 10, 10, 3, and it was received when the
local time at process 1 was 62. The local time
is needed essentially because times
may be unsynchronized across different processes as we have discussed before, and this is an
asynchronous system after all, and so we wanna be using
the local time to mark when the heartbeat
was last updated. Periodically, each process
sends over this entire table to a few of its neighbors
selected at random. Okay, this is known
as, uh, gossip. So nodes are processes periodically gossip
their membership list. So, for instance,
if 1 selects 2 at random and sends it
its membership list, say 2's membership looks
like this, right. What 2 does when it receives
1's membership list is that it merges it
into its own list. It merges it row by row; so for instance,
it looks at row number 1 and it says that hey, my, uh,
latest for heartbeat for, uh, 1 is 10,118, but I am receiving a heartbeat
for 1 which is 10,120, which is later, and so I am going to update
that, uh, heartbeat to be 10,120. Also I am going
to update the, uh, time component of that particular row from 64 to my
current local time which happens to be 70
at this node. For the second row,
it doesn't update it because it has
a low- uh, a later heartbeat. After all it was
in row number 2. Uh, for the third row,
for node number 3, again it does update it, uh, because, uh,
1's incoming heartbeat, uh, table has a-a higher
heartbeat counter, so it becomes
10,098 inherited from 1, and the local time is marked
at 70 over here. Number 4 is not updated
because the heartbeat counters are the same here, uh, both at 1
and 2, so that's not updated. It is kept as is. Essentially this, ah, is
the way, ah, gossip works. Ah, the essential component here
is that, ah, 1, ah, periodically selects, um, uh, a few other members at, uh, random from its membership list and sends it copies of, uh,
its membership list and they do the protocol here. The timeout works the same way. If, ah, there is a threshold
typically for, ah, timing out and, um, when a-a particular row's, um, entry was last updated more than
that timeout, uh, seconds ago you mark that node
as our processes having failed. So the heartbeat
has not increased for more than T failed seconds. Notice that
this is a local time at the, uh, process that
is maintaining the table, then the member is marked
as having failed. However, you don't delete that
particular entry right away from the row, uh,
from the table that you have. Uh, you wait for another
T cleanup seconds. Typically cleanup is also
around the same as a T fail, and only after that
do you delete the member from your list. So why do we have
two different timeouts? Why not delete
the member right away? Well you could have, uh, this
very interesting phenomenon if you delete
the member right away where an entry
might never go away. Consider here
this particular scenario where process 1 has
an entry for 3 marked as, uh, a heartbeat 10,098
with local time 55 and process 2 also has a similar
heart- uh, entry for process 3. Process 1 marks- uh, sorry,
process 2 marks row 3 as having failed because
the current timeout is 75 and the T fail
is 24 seconds ago, so the timeout just elapsed; however, process 1, uh, has not
yet reached that timeout of 24 and so it has not deleted 3 yet, but 2 has gone ahead
and deleted 3. Soon enough 1 sends its
heartbeat list over to 2 and 2 sees the entry 3-
for 3 in there and says, "Oh, this is a new, ah, membership list entry. "I'm gonna add it back in. "And in fact,
I'm gonna add it back in "with the new local time,
uh, at node 2." And so essentially you can see
what's going on here, that after a while 1 will delete
the entry for 3, but 2 might select, uh, 1
as the gossip target and it might send it 3's entry and then 1 will add it back, and so because of this ping pong
behavior that happens, 3's entry might never,
ever go away from the system. So it is to avoid exactly this that you remember, uh, the entry for another T cleanup seconds typically the same
as T fail timeout and if you receive another entry
for the same, uh, process, you don't pay heed to it. You ignore it. So, let's go back
to the discussion of, uh, what happens
if the gossip period, uh, T gossip, is decreased. Um, so once again, uh,
the gossip property says that a single heartbeat, uh, takes
O(log(N)) time to propagate as long as you have
enough bandwidth, uh, to, uh, send out
the entire, uh, membership list, uh, every time, uh, you gossip. Uh, so, uh, N heartbeats take
O(log(N)) time to propagate and the bandwidth
allowed per node, ah, is allowed to be O(N). Uh, however, the bandwidth
allowed is O(1), you're allowed to send out
only a few sampled rows from your membership list, theyn the-then the, um, uh, then the, um, dissemination time might go up to Order(N-log(N)). Essentially this is, uh,
inversely proportionate. In the gossip period,
T gossip is decreased; essentially what happens, ah, is that you have
a higher bandwidth, uh, and that, uh, you spre-you send out gossips, uh, much quicker so you can have
a shorter timeout for the failure
detection itself. So essentially,
the T gossip is a tradeoff between bandwidth
and the detection time. Uh, the bandwidth again,
uh, um, determines, uh, um, the detection timeouts. The lower your bandwidth
limits are, uh, the longer y-y-your
detection time has to be. So I encourage you
to think about what happens if you have O(K) bandwidth
in, uh, this. Once again, if you increase
T_fail and T_cleanup, the timeouts there, what happens to the
false positive, uh, probability? Well essentially what happens is that your detection
time increases, but then at the same time, uh, you have a-a lower
false positive rate because you give,
uh, non-faulty nodes that are mistakenly detected slightly longer for the heartbeats
to make it across. So essentially you have
a bunch of knobs here. Uh, the T_gossip is one
of those knobs and the timeouts, the T_fail and the T_cleanup
are the other knobs, and the bandwidth constraints, uh, um, are the other knobs which help you to trade off between the false positive rate, uh, the detection time,
and the bandwidth that is, uh, used
by your gossip protocol itself. So in the next lecture
we'll see whether or not this in is in fact optimal. Is there an optimal
failure detector? How close d-do
the failure detectors we have discussed so far come
to this optimal, uh, amount?

### 09 - 2.4. Which is the best failure detector

Slides: `C3_Member_D_CSRAfinal.pdf`

#### Slide text

```
L=N/T
```

#### Transcript

In this lecture, we will see,
uh, how close, uh, the failure detectors we have discussed come to the optimal, and in fact what the optimal is. So what does optimal mean? Optimal is derived
from the main properties, the correctness properties: completeness and accuracy, as well as, uh,
the time projection, known as speed, and the scale. Essentially, we wanna
guarantee completeness always. We will denote, uh, the time
projection as T time units, and we'll denote
the accuracy as, um, or rather,
the inaccuracy as PM(T) which is basically a probability
of mistake in time T. Essentially this says that, uh,
this is the probability that a mistaken detection will be
made in, uh, T time units. Given these requirements,
we will then compare the, uh, message load across
all the protocols, and that becomes the, uh, base for comparison across protocols. So let's do this, uh, comparison
for all-to-all heartbeating. Uh, you'll notice, uh,
that essentially, uh, T is the time-out period
or the, um, direction time. Uh, the-the period at which
heartbeats are sent out, uh, typically the time-out period
is, uh, a constant, uh, times, uh, the, uh, period at which
heartbeats are sent out, and so the load essentially is,
uh, N heartbeats sent out every T time units
per process pi. So the load per process
is linear in N, uh, for the all-to-all
heartbeating approach. For, uh, the, uh,
gossip-based approach, uh, this slide should, uh, the time
should be gossip based approach, you have, uh, T equals, um, a log(N) times
some constant times tg. tg is the gossip period, the period at which
gossips are sent out to all the other
members in the group. We're assuming here, uh, th-of
course that the gossip message contains the entire
membership list. So essentially the load on, uh,
each member per gossip period is O(N) because it sends out
N entries from its membership list, so the load is N/tg. But tg we can obtain from
the earlier equation, which essentially says
that gossip takes order log(N) rounds
to propagate, and if you plug it in,
you see that L is N log(N)/T. You'll notice here automatically that the gossip-based heartbeating protocol here has a higher load
than the all-to-all heartbeating we discussed
in the previous slide. That's natural because gossip
is trying to get a slightly better accuracy
by using more messages. So how close are
these to the optimal? What is the optimal? Well, you can, uh, show
that if, um, uh, you're given the values
of T, PM(T), and N, as well as a, uh, probability
of losing a message, called pml, this is an independent message
loss probability applied on every single message
independently of other messages, then, uh, you
need to send out at least
log(PM(T))/log(pml) messages, uh, outside
from every single process so that that is a, uh,
probability that, um, at least one message makes it
across to, uh, the other side, meaning to the other N-1
processes in the system. Essentially, you can show that
the worst case load has to be at least this value, log(PM(T))/log(pml)*1/T, uh, for you to satisfy
the PM(T) requirement. You'll notice that here
this value of L*, the worst case load, is in fact, uh, not dependent on N at all, so it is, uh, scale independent
or scale free. So the all-to-all and
gossip-based heartbeating are in fact suboptimal because they have, uh, at least, um, an O(N),
um, uh, requirement. In fact they are O(N) log(N) for
the gossip-based heartbeating. The, uh, key here is to realize
that these two protocols mix up the failure detection and
the dissemination components. Essentially they are trying
to have all the processes in the system detect
the failure by themselves and not really
using dissemination, uh, component, uh, separately. So the key to getting
closer to this bond is to separate
the two components and to use a failure
detection, uh, component that is not based on heartbeats, in fact is based on the inverse, uh, c-, uh, um, uh, an approach that a lot of you
will be familiar with. We'll discuss that
in the next lecture.

### 10 - 2.5. Another Probabilistic Failure Detector

Slides: `C3_Member_E_CSRAfinal.pdf`

#### Slide text

```

```

#### Transcript

So today we'll see, uh, probabilistic failure detector that comes closer to the optima, as we have discussed
in the previous lecture. So this failure detector
is called the SWIM or Scalable Weekly consistent Infection style
Membership protocol. You'll see, uh, why it is called that in this lecture, as well as the next. Essentially here,
instead of using heart beating we use the reverse
which is, pinging. This is a concept that all
of you are familiar with. Process pi runs
the following protocol, which runs periodically
every T prime time units, that's called
the Protocol period. The beginning
of the Protocol period it picks one other process
at random, wa-call that process pj,
and sends it a ping message. If the process pj
receives a ping messages, it responds back with
a ack message immediately. If pi receives this ack then, it does nothing else for the remainder
of the Protocol period, it's satisfied. However, if it does not hear
back an acknowledgement, which might happen if the
acknowledgement is dropped or the original ping is dropped. Then, it tries to ping pj again, but, instead of using the direct path, it uses indirect path. It does this by sending
indirect pings to K other randomly selected processes. This, third process
is one of them. When it receives this
indirect ping, it then sends a direct ping,
uh, to pj, which responds back
with an acknowledgement, and then, uh,
a direct acknowledgement, and then the third process sends an indirect acknowledgement
back to pi. If pi receives at least one such
indirect acknowledgement, by the end of the protocol,
uh, period, uh, then, uh, it is happy
and is satisfied. If it does not receive either, direct acknowledgement
from the beginning or any indirect acknowledgements then, it marks pj as
having failed. So there're two things
going on here, first of all, pi is giving pj
a second chance to respond back to a ping, maybe the first ping
was dropped. That's why we have
the second stage, uh, also the pi to pj path
in the internet itself might be congested and might be dropping
more packets than other paths. So, pi uses other
internet paths, by using these indirect pingers, bypassing this
potential congestion, uh, and, uh,
giving pj a better chance of responding
with an acknowledgement. So, essentially, you're giving
a temporal chance to pj, uh, ah, by sending a second ping and also spatial chance to pj
by using indirect paths. So, where does SWIM lie with
respect to heart beating, I have two axis here,
on this, uh, plot. The Y axis, the vertical axis
is the first detection time. The X axis is the process load. Here we fix the false positive
rate and the message loss rate. For heart beating,
as you increase, when you have
a very low process load, another words, when you have a, a low bound on the bandwidth that can be used, the detection time
can be very high. If it is constant, a load,
that is your constraint, the detection time could be
as high as order N. On the other hand,
if your process load is order N then, your detection time
could be constant. Swim on the other hand,
gets both, a constant detection time
on expectation, as well as,
a constant process load. We'll see this
on the next few slides. So the detection time in SWIM is on expectation
e/e-1 protocol periods, this is a constant and
it's independent of group size. The load on each process
is a constant per period because each process
is sending out, one ping maybe, uh, another K indirect
ping messages and our expectation
is receiving, uh, one, um, direct ping and our expectation, uh, a few, um, uh, indirect ping messages. You can show by analysis that the load is in fact less than 8 times the optimal load, when you have 15% packet loss. The false positive rate, uh, that this protocol
achieves is tunable, by increasing K, you can lower the false positive rate and, uh, the false positive
also falls exponentially, uh, as the value
of K's increase up. Finally, you get completeness,
uh, when a process fails, it will eventually be detec-be, uh, be selected for pinging, as long as, there are any further processes with, uh, this failed process
in their membership list, this is the nice property about, uh, picking, uh,
ping targets at random. That, uh, when you have
multiple, uh, pingers, uh, eventually one
of them will pick you. Uh, but in fact,
the expectation is even better, uh, y'know, an expectation
you have e-1, e/e-1 protocol periods until at least one
of them pings you. You'll also see that you can deterministically
bound the time, uh, to pinging,
by using a trick, as you will see. So, because you have an expected e/e-1 protocol periods
until detection, you can show that, uh, within log in
protocol periods or order log in
protocol periods, uh, with high probability, uh, at least one, uh, process will ping
the failed process, and will mark it
as having failed. So, the probability mistake
is exponentially in -K, so as you increase
the value of K, uh, the probability
mistake falls. It also, depends on
the message lost rate, which we marked as, pml,
in the previous, uh, lecture. It also depends on the
probability of failure, uh, if you have many failures
in the system, then, the probability of mistake might, uh, go up, uh, essentially, because some of these indirect pingers might get affected. Uh, however, PM(T) stays,
uh, small and, it goes down
as K is increased. You can show that, uh, the load
in the worst case is, uh, 28 times, uh, less than 28 times
the optimal, uh, load, uh, and the expectation, uh, on expectation the load is less than 8 times the optimal load, when you have
15% packet loss rates, which are pretty high
for the internet, uh, but for the analysis,
uh, this is good. So let's see for a moment why it's e/e-1 protocol periods on expectation for being,
uh, for the failure detection. So, consider a process
that has failed, uh, what is the probability,
and assume that all the other, uh, processes in the system,
uh, are, uh, have this failed process
in their membership list. And each one of them
is picking one, uh, ping target, at random. The probability that, um, uh, this process will be,
the failed process will be, uh, picked as, uh, a target
by a given other process, pi, is 1/N. The probability that
it will not be picked as, uh, target by this, one of the process pi is 1-1/N. The probability that
it will not be picked as target by any of this other N-1
processes in the system is simply this quantity
raised to N-1 and the probability that
at least one of these, uh, non-value processes
will ping it, is just 1 minus this quantity. The second part of this
equation, is a well-known, uh, limit, as N goes very high, which is what we expect
in data centers. This value becomes e^-1. Essentially, what we
are seeing is that, in each protocol period, you flip a coin, with heads probability
1-e, uh, ^-1 and the coin turns up heads, then at least one other,
uh, process in the group is going to pick the failed process as a ping target and mark it as having failed. So, um, if you know
your probability theory than, basically, you'll know that it,
uh, takes an expectation, uh, one over... this quantity, 1-e^-1 number
of protocol periods f-on expectation for
the first heads to turn up. And that is why we get e/e-1. Also, as I mentioned before,
you have completeness, eventually, um, once a process fails, uh, um, uh, uh, at least one, uh, process will mark it, uh, will, uh, choose it
as a pinged target and in fact, eventually, every other non-faulty process that has this failed process
in this list, will pick it as a pinged target, because that's what you get with, uh, random picking. You can also remove, uh, you can also reduce
this eventual, uh, completeness to a time order completeness, which is order N rounds
in the worst case, by using a simple trick. The trick is as following, um, whenever you pick
a membership element, uh, you, uh, pick the next membership element in your list, in the linear fashions, so, essentially, you traverse the membership list that you have,
uh, one per around. When you reach the end of the
membership list, you simply, reorder and permute the membership list that you have. So, you essentially do
round robin pinging, along with random permutation after each traversum. So you can see, um, um, uh, if you think
about it, you can, uh, see that, this results
in 2N-1 protocol periods, in the worst case, before, uh, process is,
uh, picked as a pinged target, after it has failed. Uh, the worst case happens if, uh, the process has just been passed, in this round, in this round robin traverser and then after the permutation, uh, the process ends up
at the bottom of the list, uh, the very end of the list, that takes N-1+N,
uh, protocol periods for the pinging process
to get around and, and ping the failed process. Uh, this change of, um, uh, the way in which
ping targets are picked, uh, does not change the failure detection properties, such as, uh,
the false positive rate, and other
scalability properties. So far we've discussed,
uh, failure detection protocols, uh, but, uh, we need to return to the big picture of the group
membership protocol, um, and, uh, see how the dissemination component works, uh, in tandem with
the failure detection, uh, component
that we have seen so far.

### 11 - 2.6. Dissemination and suspicion

Slides: `C3_Member_F_CSRAfinal.pdf`

#### Slide text

```

```

#### Transcript

So today we
are bringing together the dissemination component, and the failure detection
component as well, and we will also discuss
a technique known as suspicion that can improve your, uh, false positive, uh, rate. So, again, to remind you, uh, we
have, um, uh, uh, we have, uh, the dissemination, uh, component
here that is, uh, tasked with the goal
of disseminating out information about
a detected failure. Also this, uh, component can
be used to send out information about, uh, processes that have
joined the group and as, as well as processes that are going
to be leaving the group. There is different
mechanisms you can use. You could use, uh, um, hardware
multicast or IP multicast. Uh, the issue with this is, uh,
that it might be unreliable, it is not guaranteed
to get, uh, the information across to all the recipients. Also IP multicast is not
necessarily enabled in all the routers and, uh,
switches in the network. Also this might result in multiple
simultaneous multicasts, especially if you have, um,
multiple, uh, processes that are detecting the same
failure almost at the same time. Instead you could use, uh,
point-to-point messaging, uh, where the detecting, uh, process
sends out, um, uh, either TCP or UDP, uh, messages to all of the processes
in the system. This can get very expensive, especially when you're talking of thousands of processes in the group. A third option, which is
available to us, especially if you're using
the SWIM style of, uh, uh, failure detection, uh, which we saw
in the last lecture, is, uh, by piggybacking
this information on top of the failure
detection messages. This is known as
infection-style dissemination; this is where the "I"
in SWIM comes from. So you might recall this particular SWIM failure
detector protocol. Essentially what we do is that, uh, we piggyback information about some of the recently
detected failures on top of the ping messages, on top of the ack messages, on top
of the indirect ping messages, and on top
of the indirect ack messages. Whenever processes receive
these messages, they do the same
as they did before, but in addition they also look
at what is being piggybacked and use that to update
their membership lists. So this is known as epidemic
style dissemination because the ping and ack
messages are random messages going around the system, and so essentially
you're using epidemic or gossip style dissemination to disseminate out
the information about the detected
failures as well. So the same properties
that we saw in the gossip style failure detection for detecting failures now holds for disseminating information about the failures. Specifically, after lambda times
log-in protocol periods, where lambda is some constant, uh, N power minus...two lambda
minus two processes would not have heard
about the update, which means that most, uh,
processes in the system hear about the update after all the log-in protocol periods. Essentially, eh, every process
maintains a buffer of recently joined
and evicted processes, or join and, uh,
left or failed processes. You piggyback, uh, uh,
some entries from this buffer on top of every message, ping,
ack, indirect ping, or indirect ack
that you send out, and, uh, if you want to maintain
a constant size buffer, you, uh, prefer recent updates and you garbage college-collect
element that are old. If you really care about, uh,
um, more consistency you can, uh, buffer, uh,
elements, um, uh, for longer and garbage collect them after lambda times
log-in protocol periods. Uh, this ensures that, uh,
with high probability, the information
has already been received at all the, uh, members
or processes in your group. But of course there's always
a small probability that-that it
has not been received. So what the value
of lambda is here, it determines, uh, the level
of consistency that you get. No matter what you choose here, you can always be sure that you have completeness guaranteed because, uh, because
of the SWIM failure detector that ensures that all, uh,
failures are detected in, uh, two N minus one protocol
periods, in the worst case. Now in spite of all of this, your false positive rate
might be too high. Uh, this might be too high, uh, because there are
false detections, uh, that are occurring due
to processes that are perturbed, processes that are facing
quite a bit of jumpiness in their, um, um, uh,
message loss rate. Uh, also, there might be
packet losses that occur due
to, uh, congestion. Indirect pinging may not really
solve the problem because there might just be
a high message loss rate near the, um, uh, faulty-the detected faulty host, the pinged host,
during that period of time. The target here is to give
the process a second chance by suspecting it before declaring it as, uh, failed in the group. In other words,
you use a state machine where Pi maintains
a state machine for a given other process, Pj, which is present
in its membership list. By default this, uh,
state is in, a-alive. Uh, if the failure detector detects the process
as having failed, uh, Pj as having failed, then, uh, you move the process
Pj state to suspected. In addition, you start
disseminating via the SWIM piggyback messages the fact that you're
suspecting process Pj. This, uh, state is, uh,
sustained for a while, which times out after a while,
and after the time out, the process Pj
is marked as having failed, and at that point of time
you start disseminating failed Pj via
your SWIM piggyback messages. When you're in the suspected
state for process Pj, you might receive, uh,
an ack for process Pj or maybe even another direct ping from process Pj, or even a message
from someone else in the group saying, "Hey, process Pj
has not failed, but in fact it is alive." In that case you move
the state back again to alive for process Pj. One of the issues here is that, uh, process Pj might
go back and forth between the alive and the
suspected state multiple times. In order to avoid confusion,
you use incarnation numbers. There is a per-process
incarnation number, uh, this is incremented, uh, the pr-the incarnation number
for a process Pi can only be incremented by Pi. Typically Pi does this when it
receives a suspect Pi message, meaning that someone else
in the group is suspecting process Pi
as having failed. It might receive this via a ping
or an ack, uh, message, or an indirect ping
or an indirect ack message, or it might even be piggyback. Uh, and-but it receives this
and increments this Pi message, its, uh, increment,
its-its incarnation number, and starts disseminating
an alive Pi message, along with
the incarnation number. This is, uh, this mechanism
is similar to some routing protocols that are used in ad hoc networks especially the DSDV
routing protocol. Essentially higher incarnation
number notifications override the notifications
of lower incarnation numbers. So for instance, uh, um, uh,
as we've discussed before, uh, the suspect incarnation,
uh, message when it is received
at a process, um, um, Pk for process Pj, uh,
is, uh, used to override, uh, the, uh, alive, uh, information
for process Pj or Pk. So in other words, if process
Pk knows that Pj is alive in incarnation number 35, it receives a suspect Pj incarnation number 35 message, it will mark Pj
as, uh, suspected, over to the suspected state, and start gossiping, uh, or piggybacking the suspect
Pj incarnation 35 messages. Uh, if an alive message
is received with a higher
incarnation number, 36, then the process Pj is moved
back into the alive state again because this is a more recent,
um, uh, notification. However the failed,
uh, um, incarnation, uh, uh, fail-failed message
for any process Pj, regardless
of incarnation number, overrides everything else. So once a process Pj is marked
as having failed, once it is moved back
to the failed state at-by any other process
in the system, uh, then the process
Pj would be marked as failed at everyone in the group, and if it's not actually failed then it may need to rejoin
the group, uh, once again. So to wrap up our discussion
of, uh, failure detection and membership, uh, failures are the norm
rather than the exception in data centers, uh, because
you have very large number of machines and processes
in a data center. And so every distributed system,
uh, needs a failure detector. Many distributed systems, in fact most use some form
of a membership, uh, service or membership, uh, algorithm running among the processes
or among the servers. Uh, we have seen, uh, how our
ring failure detection works, and this in fact underlies
several, uh, systems including the IBM SP2 and many other similar, uh,
small or medium sized clusters. You've also seen how gossip
style failure detection works, uh, and gossip style
failure detection is, uh, rumored to underlie, uh, Amazon web services
internal infrastructure. Of course this is only a rumor,
but at the least now you know how gossip style
failure detection, uh, works.

### 12 - 3.1. Grid Applications

Slides: `C3_Grids_A_CSRAfinal.pdf`

#### Slide text

```
•
    • “

          ”
    •

    •
•

•

Jobs 1 and 2 can be concurrent
```

#### Transcript

Okay, so in this, uh, next,
uh, series of lectures we'll be looking at the technical details
of grid computing. Uh, in this first lecture
we'll, uh, start with, uh, what grid applications typically look like. Uh, here is a sample application that you might want
to run on top of the grid. This application is called the Rapid Atmospheric Modeling System, uh, or RAMS. It was developed
at Colorado State University. It's kind of a nice name 'cause their sports team
is also called, um, uh, Rams. But in any case, RAMS
is essentially a, uh, meteorological application, which models weather phenomenon. So, in 1998, uh,
when a major hurricane, uh, the hurricane Georges
hit, uh, the U.S., uh, RAMS was used to model, uh, and predict the movement of, uh, the hurricane itself, and, um, uh, the predictions that RAMS had, uh, tallied with the actual, um, uh, occurrence
on the ground itself. And RAMS essentially used, uh,
a, um, uh, a grid spacing, um, a two-dimensional grid spacing with 5 kilometer, uh, spacing instead
of the usual 10 kilometers. It was able to do this because it used a fairly large number of processors. It used more than
256 processors. Essentially, this is an example, of a weather
prediction application, uh, so you know when you see weather forecasts on television, essentially, uh, all of the data that you are seeing, in fact, all
of the, uhwa, visualization and the simulations that
went into the visualization and the prediction, uh, are examples of high-performance
computing applications or computation-intensive computing applications. Uh, these are the kinds
of applications that might be run on the grid. So, HPC is a term that is used,
uh, to denote such applications, uh, which are high-performance
computing applications. Typically high-performance
computing application, uh, uses a lot
of the CPU resource, uh, because essentially, uhm, as compared
to data-intensive computing an HPC application, uh, would have
a lot more computation in compared to the data,
uh, that it transfers. So there is less data compared
to data-intensive computing, but a lot more computation,
uh, compared to data- uh, compared
to data-intensive computing. Now the question, uh, that, uh,
the grid, uh, answers is can you run such a program, such a large parallel, uh, program, uh, without access to a
supercomputer, without actually having access
to a machine that has 256 processors? Can you run it on resources
that are widely available anyway across multiple sites? And that's where
the grid comes into play. So here is what grid
resources might look like. Um, uh, a particular university,
say the University of Wisconsin, uh, -Madison, might have, uh, a
set of work stations which are typically used
by students, but, uhhmma, at certain times
of the day, like at night, for instance, uh, the work stations
are relatively free and they could be harvested
for running, uh, some of these, uh, tasks of your grid job. Um, a different site, MIT,
might have, uh, some work stations
like this, it might also have certain dedicated clusters. The National Center
for Supercomputing Applications at the University of Illinois might also have certain, uh, dedicated clusters to run it. In a sense, you have, uh, computation resources available at these three different sites, and what you want to do is you want to run your application, uh, across these
three different sites, using resources wherever
they're available, potentially using resources at multiple sites at the same time. So, this is what, uh, the resources
in the grid infrastructure, uh, would look like, typically. And again, here,
I've drawn only three sites, but of course, there might be many tens of sites involved in a grid,
uh, infrastructure. So what does an
application, uh, look like? So an application, that might be
quoted by a meteorologist or a physicist or a biologist would look something like this. It would essentially,
consist of several jobs. In this example, I have 4 jobs,
job 0, job 1, job 2, and job 3. Uh, and these jobs are connected
in a Directed Acyclic Graph or a DAG. In this case, you notice that, the output of job 0
serves as input to job 1, and some of the output of job 0 also serves as input to job 2. Similarly, the outputs
of job 1 and job 2, uh, these arrows over here,
uh, serve as inputs to job 3. So you have this
Directed Acyclic Graph. Now in this, uh, DAG,
uh, Directed Acyclic Graph, uh, jobs 1 and 2
can be run concurrently; so for instance, you wa-you might be able to run job 1 on the Wisconsin site and job 2 on the MIT site,
uh, parallely. So, a little bit more
on the details of this job. So, the data that goes
from one job to another, the output of one job, which
is the input of the next job, may be several gigabytes. Typically, it's not
much larger than this. However, the jobs themselves,
uh, may be very long lasting, so each of these jobs,
each of these nodes in this DAG, might take several hours
to several days. Uh, each of these, uh, jobs is computation-
intensive, of course. It uses a lot of the
CPU computing resource. Each job has essentially four,
m-maybe a fifth optional stage. There's the
initialization stage. There is a stage
in the phas-uh-s, uh, phase where it
brings in data from its predecessor jobs
in the DAG. There's execution phase,
which itself lasts for, um, uh, hours, sometimes days. There's a stage out, where it sends out data
to the next jobs in the DAG, and if the user requires, uh, certain, uh,
partial results, uh, intermediate results
from this job, those are published as well. These are computation-intensive
jobs which mean that, um, uh, which means that they are,
embarrassingly parallel, which means, that, essentially, they're processing some amoun-
uh, some amount data and they are doing
quite a bit of computing on it, but this data can be split up, uh, and, the entire compilation can be parallelized into tasks. So each job can, essentially,
be split into tasks, maybe thousands, uh, maybe even more tasks, and these, uh, tasks can be run, so that each task runs on one machine, or on one processor, somewhere. These tasks typically
do not talk with each other, because they are
highly parallelized. When they are done, they return
their results, uh, uh, to the job itself
which then aggregates it. So, the main question here
is a scheduling problem. How do you, given such a,
uh, DAG of, uh, jobs, each job consisting
of certain tasks, how do you schedule this horal-
overall application across, um, uh, the grid resource, which might be distributed out over, uh, the wide area?

### 13 - 3.2. Grid Infrastucture

Slides: `C3_Grids_B_CSRAfinal.pdf`

#### Slide text

```
3

•

•

•
•       ’

•
    •

•

•

•

•
•

•
•
    •
    •

        •
        •

    •

    •

    •

•

•

•

•

•

•

•

•

•

•
    •
```

#### Transcript

Hi. So, in this lecture, uh, we'll,
uh, continue our discussion and start, uh, talking about, uh, how to schedule
such an application, uh, which consists
of essentially a DAG of jobs. Remember that each job is
highly parallelizable into tasks over here so each of these nodes
can be split up into multiple parallel tasks. How do you schedule this, um,
across multiple sites in the grid infrastructure? How do you allocate
resources, uh, to it? So, uh, the grid typically uses a two level
scheduling infrastructure at, um, uh, each site is running
an intrasite protocol. For instance, Wisconsin
might be running a protocol known as HT, uh, Condor,
or High-Throughput Condor; I'll talk about this
in a little bit. Um, and, um, there might be, site might be running some other intra-site protocol. However across sites or
intersite, there is a protocol, uh, typically a standard
protocol like Globus, running, which allows, uh, the
different jobs of an application to be scheduled
at different sites. So essentially, uh,
what happens is that Globus decides which job
gets scheduled at which site and then, uh, the intrasite
protocol at that site decides how to, uh, schedule
the different tasks of that job, uh, at the different machines
in that particular site. So let's look at this
in a little bit more detail. So, uh, the intrasite protocol
that runs inside each, uh, site, uh, is responsible for internal
allocation and scheduling so if it's given, uh,
Job 0 and Job 3 to run, it then decides
which of the tasks of Job 3 run on which machines. Again, same thing
for Job 0 as well. Ah, it's responsible
for monitoring. So if any of these, uh, machines
which are running a task, uh, fail or crash, uh, the, uh,
HT Condor Protocol is then responsible
for, uh, restarting those tasks on another, uh, machine. It's also responsible
for distribution and publishing of files. And so, any of the inputs-
input files that are received from, uh, Globus, um, uh, they need
to be internally stored inside, uh, the Wisconsin cluster, uh, and any of the output files
that are generated by the jobs over here,
run over here, need to then be sent
to Globus as well. That's responsib-
that responsibility lies with the HT Condor Protocol as far as the Wisconsin site
is concerned. So a little bit about
the HT Condor protocol. It's a high-throughput computing
system, uh, developped fro-by the University
of Wisconsin, uh, Madison. It belongs to a cy-class of
Cycle-scavenging systems. Uh, essentially Cycle systems
run on a lot of workstations. These workstations might have
regular users like students, might be using these, uh,
clusters to do their, uh, programming assignments
and homeworks. Uh, however, there are
certain times of day when, uh, work stations
are free. For instance, at night
almost all the workstations might be free. Even during the day time,
there might be some times when certain workstations
are free. So whenever a workstation
is free or idle, the workstation which is running
the-the Condor, uh, daemon, uh, goes and asks the site's central server, the Wisconsin's sites
central server or perhaps Globus,
uh, for, uh, for tasks. Um, and it is given
a task to run. When the task completes, uh,
then it asks for another task, and so on and so forth. However if, uh,
the user comes along and hits a keystroke or
a mouse click on that machine, then the task need to be stopped because essentially the task, uh, is potentially using
a lot of the, uh, CP computing resources
at that particular, uh, machine. So either that task is killed
so that, uh, the central server at that site
can restart it, or, um, uh, the partial results
from that task are sent to the central server so that, uh, the rest
of the work of that task can be completed on some other,
uh, work station. Typically the easiest way is
to just kill the task because, uh, a task
s-can simply be repeated, uh, some other, uh, server. Uh, the HT Condor System
can of course be run on a dedicated set
of machines as well, not just on workstations which have otherwise
regular users. So Condor is an example of an,
uh, intrasite, uh, protocol. Um, the intersite protocol
which is typically Globus, uh, runs, uh, between sites. The internal structure
of the different sites, um, uh, is typically invisible,
uh, to, uh, Globus. So this is known
as transparency, uh, and transparency essentially
means that, uh, the, um, essentially means invisibility, right. So Globus does not necessarily
need to know about what Condor does
inside the Wisconsin site or what MIT's intrasite protocol does inside the MIT site. It has a well-defined API
that it uses to communicate with these intrasite protocols. So Globus protocol
is responsible for external allocation. Um, it's responsible
for the scheduling to the extent that it talks
with the, uh, schedulers, uh, in the, uh,
at the individual sites, but Globus doesn't
necessarily do much of scheduling itself. Uh, so, um, uh,
it is also responsible for staging in and out of files so any of the wide
area files transfers that might be involved,
for instance, when Job 1 is allocated to MIT and Job 3
is allocated to Wisconsin, the output data of Job 1
that needs to go to Job 3, uh, essentially that's data that needs to be transferred
from MIT to Wisconsin, that is transferred
by the Globus protocol. So, uh, Globus's, uh,
there's a Globus alliance which involves universities, several national
US research labs, and, uh, several companies. And they have helped
standardize, uh, several things, especially software tools. Um, there is also
the open grid forum, which is separate
but related to this. The Globus Alliance has
essentially developed the Globus Toolkit,
which is, uh, one of the standard, uh, ways
to run the intersite protocol. The Globus Toolkit
is open source and it consists
of several components. The Grid FTP component of Globus
is responsible for, uh, the wide area transfer
of large amounts of data. For instance, if, uh, a job
sends its output data to another job in the DAG
of the application, then Grid FTP is responsible
for transferring this data across different sites. GRAM, or Grid Resource
Allocation Manager is-is what users use to submit,
locate, cancel and manage jobs. Uh, it's only a job allocator and manager
but it's not a scheduler. Uh, Globus simply communicates
with the intrasite scheduler such as HT Condor, uh,
or the Portable Batch System or other schedulers that, uh,
Globus is compatible with. There's also a replica
location service or RLS which is essentially
a naming service. Uh, so users like us, uh, give
names to files or directories that we deal with or that
jobs need to deal with. These are human readable names, however these files may be stored at one more locations, one or different sites. And the RLS is essentially
a naming service that helps translate
from the user, uh, visible name to the target location itself. Uh, the RLS might also translate
a-a name, uh, s-of a file or directory to another file
or directory name and then you recurse through
the, uh, uh, RLS service itself to eventually find
the target location. Globus also has
several libraries like the-like the XIO library that helps provide
standardized API's for all Grid IO functionalities. And, uh, Globus, uh, spends
a lot of, uh, effort and, uh, uh, infrastructure on,
uh, security, so the Grid Security Infrastructure
or the GSI service of Globus is a very important component
of Globus. Some of the things
that, uh, are related to security appear on the slide. Security is important in grids because grids
are essentially federated. Uh, each of the different, um,
sites in a grid structure such as the Wisconsin site or
the MIT site or the NCSA site is run by
different organizations. There is no central authority that manages
and owns the entire grid. Uh, as a result, uh, uh, things
like security and access control need to be managed
in a way that, uh, may be in security of data but also do not make life,
uh, hard for, uh, the users of the grid. So single sign on are one of
the things that, uh, um, Globus really does care about. Essentially once a user starts,
um, an entire application, uh, they need to sign on only
once in the beginning. They don't need to keep signing
on, uh, at different sites. Um, now the security mechanisms
that are visible to, um, uh, a given user, the policies that
the user wants to implement, uh, might map in different ways
through the mechanisms at different sites. So, for instance,
the Wisconsin site might be, uh, using, uh, a particular
security service like, uh, Kerberos
for authentication. Others might be using simple
UNIX authentication and you need to map, uh,
what the user sees to these different sites in a way that the use does not need to grapple with the different mechanisms at different sites. Delegation is important so, um,
resources that were accessible to, uh, job 0 in an application
should be accessible to, uh, the children of job 0
in that application, instead of cre-basically
graph as well. And of course, a third party
authentication is needed. Uh, this needs to be, uh, done
as, uh, well, uh, and third party authorization of
resources also needs to be done, in a way that is, uh,
transparent, uh, to the user and the user does not need, uh, to grapple with, uh, the different mechanisms
at different sites all at the same time. And all of these , uh, issues, such as single
sign on delegation are all important in clouds but there is less emphasis
in clouds. And the reason for this is
essentially because, uh, most of the times
a cloud-a cloud is run under a single central control. So for instance,
Amazon web services runs a variety of data centers,
uh, but essentially all the data centers are under the control of Amazon. And so, uh, single sign on,
delegation, uh, mapping to local
security mechanisms are relatively easier to solve, eh, in that, uh, single control,
uh, environment than in the federated
environment, uh, of, uh, grids. As a result in clouds the focus
tends to be on failures, scale, and, uh, the on-demand, uh,
access of, uh, resources. That's not to say
that these security issues are not important in, uh,
cloud computing environments such as Amazon web services, they are important, uh, but
because those are not federated, uh, they are, um, uh,
we hear less about them. So in summary, the grid
computing focuses typically on computation
intensive computing. Uh, it offers, uh, a federated
architecture, uh, um, uh, however the architecture
and key concepts have a lot with that of cloud, uh, architectures
and cloud infrastructures. Uh, the typical users
of grid applications today tend to be biologists, uh, physicists, um, and meteorologists, um, who, uh, do weather prediction
and simulation. Now there is an open question
out there, um, uh, which is whether grids and in general high performance
computing are in fact, converging towards
cloud computing and toward data
intensive computing and, uh, this is
an open question. There is a lot of commonalities
among these two different areas but they tend
to be disjoint areas in terms of what the software and the standards
that they develop as well as, uh, the conferences where research gets published. So one of the things
that I would encourage you to do is to compare the architecture of Globus with
the architecture of OpenStack. OpenStack is one of these cloud
computing, uh, open source, um, uh, platforms that has emerged, uh, so that you can draw
your own virtualized, um, cloud computing platform. There is a lot of commonality in the goals
of OpenStack and Globus. The architectures are different, uh, but, um, I encourage you
to look at them and see what
commonalities are there and what differences are there in between these two systems.

### 14 - Interview with William Gropp

#### Transcript

Hi there. So we are here in the, uh, Siebel Center
for Computer Science which is the Department
of Computer Science at the University of Illinois
at Urbana-Champaign. This is the building
where I work and a lot of other, uh, students and a lot of other
faculty work, uh, here, in Computer Science. So, uh, here we are talking with, uh,
Professor William Gropp. And he is gonna tell us some
juicy pieces of information and opinions about, uh, uh,
what he works on and how that relates
to cloud computing, so, thank you for talking
with us, uh, uh, Bill. Uh, why don't you start
by saying a little bit about, uh, yourself? Sure, so, uh,
I am a-a professor here in the Department
of Computer Science. I've been here
for about seven years. Before that, I was a scientist
at Argonne National Lab, and before that I was, uh,
on the faculty at Yale. Uh, I've been doing what we call
high performance computing, uh, since I was a graduate student, and I think it's really cool
and exciting. Uh, one of the, uh, things I got
to do just last year was to be the general chair
of the biggest meeting in the high performance computing field which has a little
over 10,000 people attend. So it was a really exciting time in, uh, the Denver
convention center, and so. Uh, our field is very active,
uh, very vibrant, has a lot of cool opportunities, uh, and has a lot of overlap
with cloud computing, so I'm happy
to talk about it. Alright, so you mention high
performance computing, uh, w-can w-can you say a little about what high performance
computing is? Yeah, it's one of these things
that's sorta hard to define. It's like, you know
it if you see it. Uh, one way to define it is it's computing where performance is important. Uh, and then that's maybe
the broadest definition. Uh, definitions also used is that it's computing that involves supercomputers, or machines
that are like supercomputers. And so you could ask
what a supercomputer is. Uh, the definition of that
has also changed over time, but one way to define it is it's about the most expensive
computer you can buy. [Indy laughs] Um, it was once defined as a
machine that cost $12 million but there's
been inflation since then. Um, but a supercomputer is,
is a computer that, uh, allows you to tackle problems that are just oth-otherwise uh, out of reach, and a typical supercomputer
or computer of that class, is made up of thousands
to hundreds of thousands of the kind of fast processors you might find in a server node. What are the similarities or
the differences between high performance
computing and cloud computing, as you see cloud computing? So the, let me start
with the similarities. Um, in both cases,
you're taking advantage, uh, getting more performance by having large
numbers of processors that can attack some collection
of problems. Maybe a problem,
maybe a collection of problems. The- maybe
the biggest difference, between high performance computing and cloud computing and this is a difference that is, uh, definitely
a shade of gray, is that in high
performance computing, well, first, as I mentioned, the, uh, focus on performance, is quite important. Many high performance computing
problems require the, uh, coordinated work
of all of those processors on this same problem
at the same time. Uh, high performance
supercomputers tend to have, uh, very high performance networks that have low latency
and high bandwidth and these networks are
significantly more powerful than the ones you find
in the cloud system, there're also significantly
more expensive. [laughs] But they're needed for
the kind of tight coordination. I often use a-a symphony
orchestra sort of analogy. The kind of programs that we run
in high performance computing are often like symphonies, in they have to be
well-coordinated. Y'know, maybe not
by a single director, but they have to work
very closely together. In fact, uh, anybody who's a
m-musician knows that, uh, even the stage
for a symphony orchestra has to be defined well so that the musicians
can hear each other well, and keep things coordinated. Um, clouds can do that
under some circumstances, but they're much more optimized towards independent work that's, um, less
frequently coordinated; it's not uncoordinated,
but less frequently. And so you don't have to, uh,
have the same tight control of what's going on. And so, these communities, uh, HPC, high performance
computing community and the cloud
computing committee, um, are sort of, they sound
very similar to each other from what you're describing. Can they learn from each other
in terms of techniques? Uh, uh, I think they can. Uh, and definitely
in both directions. So, it's interesting there was a recent paper
from people at Google, where they had discovered stuff about, uh, performance
irregularities in codes that we have known
in high performance computing for decades. Uh, and we also have solutions
for the those problems. [laughs] Uh, at the same time, uh, um, the access model
that clouds provide is something
that I find an increasing number of computational scientists
clamoring for, the ability to get resources
on demand that scale to the size
of their problem, uh and that's requires
a different way of thinking about how you
provide the access. Um, I think also the, uh, a lot
of high performance computing has been designed
around applications that take advantage of the fact that each of those
compute elements runs at the same speed
as the other ones. Uh, this is no longer true, although, uh, a lot
of applications still think that it is, and it's going to become
less true over time. And this is exactly
the sort of situation that cloud systems are already
operating in, and so, they, um, they've looked at that from some different viewpoints. And finally, another issue that
has been coming up as we're looking at taking
extreme scale computing and high performance computing, uh, beyond where
we're at now to systems that are a hundred or a thousand times faster than current systems is that it's gonna become
increasingly difficult to require that the system
be completely reliable. And, another thing is that, uh, has been developed
in cloud systems is, uh, exploiting cheaper,
less reliable components, which made sense there, but in the scientific computing you don't need to go cheaper. But as we looked
at the extreme scale systems, it's gonna be
increasingly expensive to be, the sort of ultra-light
reliable that you need. And so again,
there's an area where what's going on
in cloud computing will offer some insights,
maybe not to solutions, because the problems
have different characteristics, but some insights
on how to attack them. So can you say
a little bit about, uh, what kinds of research problems
you are working on now? Sure, so, they're really
in-in two groups, so, one of them is
a computational science problem. So, I'm the lead PI for, uh, the Center on Plasma
Coupled Combustion, here, which is funded
by the Department of Energy. What it's looking at is trying
to understand, uh, what is, uh, really a new way
to control combustion by using plasmas and you might use this
to, uh, hold onto the flame in a hypersonic jet engine. Where one of the big problems is that the fact
that it's hypersonic means that it's very hard to keep
the flame from being blown out. Plasma gives you a way
to hold onto the flame. Uh, also allows you to guide
where the combustion happens, so you might be able
to make a far cleaner, more efficient burning
internal combustion engine. But the problem is, that, uh, no-one really knows
what's-how that works. You know, you can do it
in a lab, uh, set up a little experiment and we can do that here, it's really great, and it's part
of our, uh, project as we have people
who do these experiments. We can set them up
and they can do them and they can measure stuff, but if you want to design, uh,
an engine that uses this, um, you need to have some
insight into what's going on. You need to be able to do
predictions about, uh, how effective it's going to be, you need something to help you optimize the design, and for that,
we-we do this by computing, and the kind of computing that's required
for this is enormous, because you hafta understand
what's happening on link scales that
you can see in your hand, and you need to understand
what's happening at link scales which are the atoms bouncing off
the electrodes that are creating the plasma, and everything in between. And that's a problem that's too
big for any one, uh, processor, or even ten or a
hundred processors. And so, in fact, the Department
of Energy is interested in this, less because of the science,
although it's interesting, but more because
they're interested in understanding the techniques both computer science techniques the applied math techniques to handle problems
of this complexity, which are really at-at the, uh,
at the edge of what we can do. And then, the other part
of my research is focused on say, the computer science part of that, which is, how do I express
those programs? Uh, how do I write the programs
so that it's efficient, and it has to be efficient,
on an individual node, and it has to be efficient running across a hundred thousand
or a million nodes. And, um, I think you'll be
asking me a little more about that later,
so I'll-I'll wait for that. But that's the two parts
of my research at this time. Okay, um, let's move on
to a different topic, uh, MPI, which is pretty close
to your heart, uh. You are of course,
one of the inventors of this very popular
programming paradigm, MPI. Can you say a little
about what MPI is? Sure, so, MPI's, um,
very boringly stands for Message Passing Interface. Uh, it's a, uh,
standard, if, well, maybe sometimes called
an ad hoc standard because it wasn't an official
organization behind it. Uh, but it's a ad hoc standard that codifies communicating sequential processes. Uh, at least it started
like that. Over time it's added
more and more, uh, techniques for doing the kind
of parallel computing that we do
in high performance computing. So one of the features of MPI
is it's designed for reliable systems, designed for systems,
uh, at very large scale, and I'll say a little bit about
what that means in a minute, uh, and it's designed
for, uh, systems that need to get
the utmost in performance, um, out
of their applications. Um, it's not a high level,
easy to use necessarily model. But it's been a very powerful
and very flexible one. Uh, and astoundingly, it's now
over 20 years old, which, uh, even I have trouble
believing at times. Uh, never expected it
to succeed so well. Um, to give everyone a sense of,
um, the scale which it's used, there are MPI programs now that typic-that run
on over a million processors. [laughs] Uh, so it scales, y'know,
well past what, uh, current cloud systems look like. Uh, the cost
of moving data from, uh, user process to user process
in this message passing model is typically on the order
of a microsecond or less on, uh, a HPC system, and the bandwidths
for the data that's being moved, uh, exceeds y'know, on this-on the-the slowest systems it's several hundred
megabytes per second, and, uh, exceeds gigabytes per
second, uh, on the best systems. Uh, and the bisection band,
with the ability of, um, say, half the-half
of those million processes taught the other
half a million processes, uh, is often, on today's systems
well over a terabyte per second, uh, and all of that is
achievable, uh, with MPI, and MPI programs
that were written 20 years ago, some of them are still running
today and doing good science, which, um, I think speaks to the flexibility and
generality of the design. And is MPI, would you say MPI
is applicable in, uh, data centers,
and clouds as well? Can the programming model
be used just as easily there? Yes, it is, and I mean, I run
MPI programs on my laptop. The-one assumption
that MPI makes, that is maybe awkward
for some cloud systems, is it does assume that there's
reliable communication layer, um, and it doesn't have
built in facilities to deal with, uh,
a lack of reliability, um, so that's an issue. It also, uh, tends to assume a
static group of processes, uh, although there are
features in it to add and subtract processes, but I would say
that they're weaker than what you might want
if you were doing it a lot. But, uh, for example,
the reduction operation that you might have talked
to people about, uh, MPI provides a number
of different versions of that, depending on how
you are doing your reduction. And those reduction, uh,
im-those reduction operations and the algorithms behind them
had been tuned over the decades, to be very, very fast, um, there's some very clever
ways to do that. The same is true
for the sort of reverse of that to do a broadcast, um, we can, um, move data from one process
to all other processes, uh, pretty much at that
terabyte per second rate. But, and it sounds like from
what you are saying, that MPI could be combined with
things like membership services, which already exist, had to-to build a system that would be oriented
more towards clouds? Absolutely. Absolutely. And there are people who were
running MPI on clouds now, so it's not, uh, something
that's terribly strange. The, uh, the biggest thing
is not so much MPI, but the kind of applications that are written with MPI that, as I mentioned before,
tend to assume, uh, uniform performance
of their computing elements. What were the motivating factors behind coming up with the paradigm in the first place? So the, uh, the situation when
um, MPI was developed was that there were
a number of vendors, uh, large and small, so, um, start-up companies, um,
IBM, uh, Intel, uh, and they all had their own APIs, their own
programming interfaces. Uh, mostly built around
this communicating, sequential processes model, message processing model, um, for writing these programs. And, uh, Ken Kennedy is well
known in parallel computing, particularly in, uh, compilers, was working on a par-, uh, compiler for a parallel language and he wanted
to just have one API for, for, as a compiler target. And he got a bunch
of us together, so us, meaning people
who were developing one of these
different interfaces. And we all explained why they
all had to be different, and Ken, uh, said,
this is great, looks like we're all
in agreement that we can find
a common standard. Um, this is sort of
a mark of a great man, who, uh, uh, and he was right.
[laughs] Um, so over the next, uh, year,
or so, uh, a proposal was made, uh, many of us reacted
to the proposal by saying we have to do
better than this. Um, and I'm, should say,
it was not a bad proposal, but it wasn't good enough. And a lot of people
got together, uh, the vendors
sent their best people, um, the research group
sent their best people, some application groups, uh, who had the same
sort of desire that Ken did, they wanted to s- you know,
they wanted to put their time into writing
a better application, not importing
from system to system. And over about a year
and a half, we came up
with a s- uh, standard, and as part of that, I had committed my group to developing and implementation, so as we were
developing the standard we had something that
ran, that we could, explore and experiment with and make sure we were making
the right choices. And, uh, that came up with what
became the MPI1 standard, um, we took advantage of, uh, people who had been working
on the standard for high performance FORTRAN, which was another
ad hoc standard. Uh, we even used the same hotel
in north Dallas which really encouraged you
to s- um, stay there and work. [laughs] Um, and, we developed
a careful standard. We got it published. It was published by, uh,
International Journal of High Performance
Computing Applications. Um, we made it freely available so, uh, you can
download the pdf, and you can do that now,
with MPI3, you can go
to the MPI-forum.org website and get the standard, so, we don't charge
any-anything for it. And the- um, there was also
an implementation available, and, uh, with that,
people could start using it. We also wrote, uh some books,
there's Using MPI, Using MPI2. Um, Using MPI is
in its second edition, and its third edition was sent to the
publisher last month. Um, another, um, thing that's
hard to, uh, hard to believe sometimes that it's
been around that long. Uh, and that produced a standard that applications people could start programming to and that meant that they had,
they could no longer they no longer had to worry
about, um, spending time every time a new parallel
machine came out, moving their code to it. And, because we had in,
had a very open process, the meetings were open, because we involved
application developers, as well as the vendors
and as well as people who were doing research into these parallel
programming systems, we made sure that the design was fast, efficient,
and complete enough so that over the years
the application, uh, developers have not really
needed anything else. They made one
and a few other things, and there is an MPI2
and an MPI3, both of which have added
features, but by and large, uh, applications
have been able to write whatever they needed to in MPI. And that's different than
some other efforts where, for example, uh,
what was provided was what the people
doing the development provided, but it wasn't,
it didn't have the breadth, didn't have the completeness that was needed
by the applications. Sounds like, uh, standardization was one of the
motivating factors for the development of MPI. I-i-it was, and I-I wanna say
that it wasn't the first effort to standardize this kind
of parallel programming. Um, eh, one-one challenge
for people is standardization sounds great,
sounds like, uh, you would, it's amazing
the number of people who wanted
to standardize something because they look
at the success of MPI and they want
to duplicate that success. Uh, but what they forget was, that there were several efforts to standardize message passing before MPI that failed. Um, and it's important to have
a mature enough system, a mature enough community
of understanding the issues, before you start
to standardize, um, but yeah. Once you have that knowledge, then it's time
to standardize and move on. Well, um, that's the last
question I have for you. Thank you for, uh, taking
time to talk with us. It's my pleasure. Thanks, Bill.

## Quizzes and assignments

### Part 1 Quiz 2

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
