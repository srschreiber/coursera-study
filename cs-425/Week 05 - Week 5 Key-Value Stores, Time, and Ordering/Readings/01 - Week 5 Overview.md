# Week 5 Overview

- Coursera: https://www.coursera.org/learn/cs-425/supplement/qbAGW/week-5-overview
- Lesson: Week 5 Overview

# Week 5: Key-Value Stores, Time, and Ordering

## Overview

This week we first explore the design of key-value/NoSQL storage systems. This topic is important because it shows how industry-popular systems leverage some of the concepts we’ve learned so far in the course. For instance, you will see concepts from some topics, like P2P systems and Membership, reused in our discussion of key-value/NoSQL storage systems. Also in Week 5 we begin to dive into the core distributed algorithms and theoretical concepts that underlie distributed systems. Week 5 features an introduction to time, synchronization, and logical timestamps (like Lamport timestamps).

## Time

This week should take **approximately ****10 - 15 hours (this estimate excludes time spent on the programming assignment, which varies based on your background) **of dedicated time to complete, with its videos and assignments.

## Lessons

The lessons for this module are listed below (with assignments in bold italics):

|

**Lesson Title** |

**Time Estimate ** |
|

**Lesson 1: Key-Value Stores NoSQL** |

 |
|

Lecture 1.1. Why Key-Value/NoSQL? |

16 minutes |
|

Lecture 1.2. Cassandra |

28 minutes |
|

Lecture 1.3. The Mystery of X The Cap Theorem |

20 minutes |
|

Lecture 1.4. The Consistency Spectrum |

10 minutes |
|

Lecture 1.5. HBase |

11 minutes |
|

**Lesson 2: Time and Ordering** |

 |
|

Lecture 2.1. Introduction and Basics |

11 minutes |
|

Lecture 2.2. Cristian's Algorithm |

6 minutes |
|

Lecture 2.3. NTP |

5 minutes |
|

Lecture 2.4. Lamport Timestamps |

15 minutes |
|

Lecture 2.5. Vector Clocks |

12 minutes |
|

**Interview** |

 |
|

Interview with Marcos Aguilera |

15 minutes |
|

**_Part 1 Quiz 4_** |

1 - 2 hours |
|

**_Part 1 Programming Assignment_** |

30 - 45 hours |
|

_**Homework 2** _is released. |

10 - 15 hours |

## Goals and Objectives

After you actively engage in the learning experiences in this module, you should be able to:

-

Know why key-value/NoSQL are gaining popularity
-

Know the design of Apache Cassandra
-

Know the design of Apache HBase
-

Use various time synchronization algorithms
-

Apply Lamport and vector timestamps to order events in a distributed system

## Key Phrases/Concepts

Keep your eyes open for the following key terms or phrases as you complete the readings and interact with the lectures. These topics will help you better understand the content in this module.

-

Key-value and NoSQL stores
-

Cassandra system
-

CAP theorem
-

Consistency-availability tradeoff and spectrum
-

Eventual consistency
-

HBase system
-

ACID vs. BASE
-

Time synchronization algorithms in asynchronous systems: Cristian's, NTP, and Berkeley algorithms
-

Lamport causality and timestamps
-

Vector timestamps

## Guiding Questions

Develop your answers to the following guiding questions while completing the assignments throughout the week.

-

Why are key-value/NoSQL systems popular today?
-

How does Cassandra make writes fast?
-

How does Cassandra handle failures?
-

What is the CAP theorem?
-

What is eventual consistency?
-

What is a quorum?
-

What are the different consistency levels in Cassandra?
-

How do snitches work in Cassandra?
-

Why is time synchronization hard in asynchronous systems?
-

How can you reduce the error while synchronizing time across two machines over a network?
-

How does HBase ensure consistency?
-

What is Lamport causality?
-

Can you assign Lamport timestamps to a run?
-

Can you assign vector timestamps to a run?

## Readings and Resources

There are no readings required for this week, but you can look at the following documentation:

-

**[Cassandra](http://www.datastax.com/documentation/cassandra/2.0/cassandra/gettingStartedCassandraIntro.html)**
-

**[HBase](http://hbase.apache.org/)**
-

[**Cassandra 2.0 Paper**](http://www.datastax.com/documentation/articles/cassandra/cassandrathenandnow.html)
-

[**Cassandra NoSQL Presentation**](http://www.slideshare.net/Eweaver/cassandra-presentation-at-nosql)
-

[**Cassandra 1.0 documentation at datastax.com**](http://www.datastax.com/docs/1.0/index)
-

[**Cassandra Apache wiki**](http://wiki.apache.org/cassandra/ArchitectureOverview)
-

[**MongoDB**](http://www.mongodb.org/)

## Tips for Success

To do well this week, I recommend that you do the following:

-

Review the video lectures a number of times to gain a solid understanding of the key questions and concepts introduced this week.
-

When possible, provide tips and suggestions to your peers in this class. As a learning community, we can help each other learn and grow. One way of doing this is by helping to address the questions that your peers pose. By engaging with each other, we'll all learn better.
-

It's always a good idea to refer to the video lectures and readings we've completed during this week and reference them in your responses. When appropriate, critique the information presented.
-

Take notes while you read the materials and watch the lectures for this week. By taking notes, you are interacting with the material and will find that it is easier to remember and to understand. With your notes, you'll also find that it's easier to complete your assignments. So, go ahead, do yourself a favor, and take some notes!

##
