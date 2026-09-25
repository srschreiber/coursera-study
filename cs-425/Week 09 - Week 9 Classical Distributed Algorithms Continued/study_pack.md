# Week 09 - Week 9 Classical Distributed Algorithms Continued

Contents: 4 readings, 11 lectures, 1 quizzes/assignments.

## Readings

### Course Part 2 Overview

- Coursera: https://www.coursera.org/learn/cs-425/supplement/IPRzK/course-part-2-overview
- Lesson: Course Part 2 Overview

# Course Part 2 Syllabus

## Course Description

Cloud computing systems today, whether open source or used inside companies, are built using a common set of core techniques, algorithms, and design philosophies – all centered around distributed systems. Learn about such fundamental distributed computing “concepts” for cloud computing. Understand how these techniques work inside today’s most widely-used cloud computing systems. Get your hands dirty using these concepts with provided homework exercises. In the optional programming track, implement some of these concepts in template assignments provided in C++ programming language.

## Course Goals and Objectives

Cloud Computing Concept Part 1 is a prerequisite for this course, Cloud Computing Concepts Part 2. At the end of this two-part Cloud Computing Concepts course, you will be able to:

-

Identify classical distributed computing problems that arise in today’s cloud computing problems.
-

Know and apply classical solutions to common distributed computing problems that arise in today’s cloud computing systems.
-

Know and apply the fundamental limitations of what is possible and what is not in cloud computing systems.
-

Know and apply knowledge of popular distributed systems used in industry today.
-

Analyze a given distributed algorithm in terms of computation and communication complexity, scalability, and fault tolerance.
-

Design algorithms and systems solutions to the core distributed computing problems arising in today’s cloud computing systems.
-

(Optional Programming Assignments) Build and debug a fully-working cloud computing system inside an emulated framework.

## Textbook and Readings

No textbook is required. You will learn the content through video lectures, homework, exams, and programming assignments. Links to some extra reading materials will be provided in the corresponding weeks.

## Course Outline

Part 2 consists of 5 weekly modules with focus on the fundamental distributed computing "concepts" for cloud computing.

### Week 9: Course Orientation and Classical Distributed Algorithms Continued

**Key Concepts:**

-

Course Overview
-

Part 2 Introduction
-

Leader Election
-

Mutual Exclusion

### Week 10: Concurrency and Replication Control

**Key Concepts:**

-

Concurrency Control
-

Replication Control

### Week 11: Emerging Paradigms

**Key Concepts:**

-

Scheduling Stream
-

Processing
-

Distributed Graph Processing
-

 Brighten Godfrey Interview

### Week 12: Classical Systems

**Key Concepts:**

-

Scheduling
-

Stream Processing
-

Distributed Graph Processing

### Week 13: Thanksgiving break

### Week 14: Real-Life Behaviors

**Key Concepts:**

-

Security
-

Structure of Networks
-

Datacenter Outage Studies
-

Paul Kwiat Interview

##

### Week 9 Overview

- Coursera: https://www.coursera.org/learn/cs-425/supplement/hdm1t/week-9-overview
- Lesson: Week 9 Overview

# Week 9: Distributed Algorithms, Continued

## Overview

 Cloud Computing Concepts (C3) Part 2 picks up where we left off in Cloud Computing Concepts (C3) Part 1—with distributed algorithms fundamentals. This week (Week 9) we explore two more important topics, Leader Election and Mutual Exclusion, and how they are used in industry.

## Time

This week should take **approximately ****10 - 15 hours (this estimate excludes time spent on the programming assignment, which varies based on your background)** of dedicated time to complete, with its videos and homework.

## Lessons

The lessons for this module are listed below (with assignments in bold italics):

|

**Lesson Title** |

**Estimated Time Required** |
|

**Lesson 1: ****Leader Election** |

 |
|

Lesson 1.1. The Election Problem |

9 minutes |
|

Lesson 1.2. Ring Leader Election |

15 minutes |
|

Lesson 1.3. Election in Chubby and ZooKeeper |

10 minutes |
|

Lesson 1.4. Bully Algorithm |

10 minutes |
|

**Lesson 2: ****Mutual Exclusion** |

 |
|

Lesson 2.1. Introduction and Basics |

13 minutes |
|

Lesson 2.2. Distributed Mutual Exclusion |

11 minutes |
|

Lesson 2.3. Ricart-Agrawala's Algorithm |

12 minutes |
|

Lesson 2.4. Maekawa's Algorithm and Wrap-Up |

17 minutes |
|

_**Part 2 Quiz 1**_ |

1 - 2 hours |
|

_**Part 2 Programming Assignment**_ |

60 - 90 hours |

## Goals and Objectives

After you actively engage in the learning experiences in this module, you should be able to:

-

Design Leader Election algorithms including Ring algorithm and Bully algorithm.
-

Design Mutual Exclusion algorithms including Ricart-Agrawala’s algorithm and Maekawa’s algorithm.
-

Know the design of Leader Election used in industry systems: Google’s Chubby system and Apache Zookeeper.
-

Know how industry systems like Google’s Chubby support mutual exclusion.

## Key Phrases/Concepts

Keep your eyes open for the following key terms or phrases as you complete the readings and interact with the lectures. These topics will help you better understand the content in this module.

-

Google Chubby Leader Election
-

Apache Zookeeper Leader Election
-

Ring Mutual Exclusion
-

Ricart-Agrawala’s Mutual Exclusion
-

Maekawa Mutual Exclusion

## Guiding Questions

Develop your answers to the following guiding questions while completing the readings and working on assignments throughout the week.

-

What are the safety and liveness conditions for Leader Election?
-

Why is Leader Election hard?
-

How long does the Ring Election algorithm take to complete?
-

 How long does the Bully Election algorithm take to complete?
-

How does Google Chubby use quorums for election?
-

What are the safety and liveness conditions for Mutual Exclusion?
-

How do semaphores work?
-

 How long does the Ring Mutual Exclusion algorithm take to complete?
-

How long does the Ricart-Agrawala’s algorithm take to complete?
-

Why is Maekawa’s algorithm “optimal”?
-

How does Google Chubby use quorums for mutual exclusion?

## Readings & Resources

-

(Optional, fun video) [Amazon Web Services (AWS) Training Videos](http://aws.amazon.com/training/intro_series/)
-

(Optional, fun video) [Amazon Web Services (AWS) Training Videos (China host)](http://aws.amazon.bokecc.com/)

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

### Part 2 Quiz 1 Instructions

- Coursera: https://www.coursera.org/learn/cs-425/supplement/N3H1K/part-2-quiz-1-instructions
- Lesson: Quiz

**Topics:** Leader Election, Mutual Exclusion

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

### Looking ahead to the Part 2 Programming Assignment

- Coursera: https://www.coursera.org/learn/cs-425/supplement/LzZ0M/looking-ahead-to-the-part-2-programming-assignment
- Lesson: Looking Ahead: Part 2 Programming Assignment

Coming up soon in this course, around Week 13 (CS 425 version; location may vary for the Cloud Computing Concepts MOOC), you will find the programming assignment for the second half of the course. It's called MP2: Fault-Tolerant Key-Value Store.

(Programming assignments in the University of Illinois CS department are traditionally labeled "MP". Depending on who you ask, it stands for "machine problem," "machine programming," or "machine-processed.")

You should look ahead to that item and try to get started on it as soon as possible, because it may take some time for you to design and debug your solution. Please take note of the assignment deadline while you preview the instructions. **Please don't wait until Week 13 to begin the assignment.**

## Lectures

### 01 - Introduction to Cloud Computing Concepts, Part 2

Slides: `C3_Course2Intro_CSRAfinal.pdf`

#### Slide text

```
Goal of C3 - Part 2

• Course about the internals of cloud computing
• Distributed systems and algorithms that underlie today’s
  cloud computing technologies
• We’ll discuss
    – Concepts
    – Techniques
    – Industry systems, including open-source (from the inside)
• Builds on “Cloud Computing Concepts (C3) – Part 1”
    – C3 – Part 1 is a prerequisite for C3 – Part 2
    – We’ll be reusing and relying on many concepts you learnt in Part 1
      throughout Part 2

Syllabus for C3 – Part 2

• Classical algorithms: Leader Election, Mutual Exclusion,
  Scheduling
• Scalability: Concurrency control, Replication Control
• Trending Areas: Stream processing, Graph processing,
  Structure of Networks, Sensor Networks
• Miscellaneous: Distributed File systems, Distributed
  shared memory, Security, Datacenter outage studies
• Fun: Interviews with leading managers and researchers,
  from both industry and academia

What We’ll be Relying on from C3 – Part 1

•   Introduction: Clouds, Mapreduce, Key-value stores
•   Classical Precursors: Peer-to-peer systems, Grids
•   Widely-used algorithms: Gossip, Membership, Paxos
•   Classical algorithms: Time and Ordering, Snapshots,
    Multicast

Exercises

• 5 Homeworks
• 1 Programming Assignment (C++)
   – Implement a fault-tolerant key-value store inside an emulator
   – Builds on Programming Assignment from C3 – Part 1
• 1 Exam

Onward!

• Cloud computing is an exciting area to be studying, very
  dynamic and continuously changing
• Come, let’s complete our journey through the landscape.
```

#### Transcript

[MUSIC] Welcome back to all the students
interested in learning more about Cloud Computing Concepts. This is Cloud Computing Concepts part two. In this course, just like the first
part of the Cloud Computing Concepts, remains about internals of cloud computing
which means distributed systems. And display the algorithms that underlie
today's cloud computing technologies. What underlies the hood is what
we are going to focusing on in the second part as well. We'll discuss concepts, and techniques and applications of these two industry
systems, as well as open-source systems. The second part of C3 Cloud Computing
Concepts course builds on the part one. C3 part one is a prerequisite for,
part two. We will be reusing and relying on many of
the concepts we have learned in part one, throughout part two for the homework, for the material that we discuss, as well as
for the optional programming assignment. So what are we going to cover in C3,
part two? We'll continue our discussion
where we left off in part one, and focus on more classical algorithms
including leader election, mutual exclusion, and scheduling, all of which are used in pretty much all
of the cloud computing systems today. We look at it a discussion of scalability. How do you support millions of
clients with concurrency control, and hundreds of servers, and
replicas with replication control? We'll look at new trending areas
such as real time stream processing, distributed graph processing, and
also, wisdom in structure of networks, as well as new areas like sensor networks. And finally, we'll discuss areas related
to cloud computing such as distributed file systems,
distributed shared memory, security. And we'll see case studies of what happens
when things go wrong in data centers. And we'll continue interviews with our
friends in Industria as well as Academia. What we'll be relying on from C3 part one
includes classical precursors, information about the widely used algorithms and
classical algorithms that underlie cloud computing systems, things that you've
already learned in part one, as well as knowledge about map reduce and key value
stores that you have seen in part one. Just like part one, here in part two,
as well, we're going to have homeworks. Here, we'll have weekly homeworks. In addition, you'll be doing a programming
assignment, and it's in C++. In addition, you'll be doing a programming
assignment, and it's in C++. In this programming assignment, you're
going to be implementing a fault-tolerant key-value store inside an emulator
that emulates a distributed system. This builds on the programming assignment
from the Cloud Computing Concepts, part one. So I highly encourage students who
have not taken part one yet to go and, take a look and even try out
the programming assignment from part one. And of course, at the end of the course,
there's going to be one final exam. >> Cloud computing continues to be
an exciting area, one that is dynamic and continuously changing. And I hope you will continue this
journey with me as we complete our tour through the cloud computing concepts,
landscape.

### 02 - Orientation Towards Cloud Computing Concepts Some Basic Computer Science Fundamentals

Slides: `C3_Orientation_CSRAfinal_v2.pdf`

#### Slide text

```
What this Lecture is about

• Covers basic concepts in Computer Science that will be
  assumed in the Cloud Computing Concepts (C3) course
• For those of you already familiar, it’s a refresher
• Use this as reference if you don’t understand (during the
  course) how the basics are being used

What’s in this Lecture

I.     Basic datastructures
II.    Processes
III.   Computer Architecture
IV.    O() notation
V.     Basic probability
VI.    Miscellaneous

 I. Basic Datastructures: Queue

 • Queue: First-in First-out datastructure

Remove from head  3 5 8 0 7      Insert at tail

 • Next item dequeued (removed) is 3.
     – Then 5
     – Then 8
     – And so on

  Basic Datastructures: Stack

  • Stack: First-in Last-out datastructure
Remove (Pop) from top          Insert (Push) at top

                           3
                           5
                           8
                           0
                           7
  •   Insert (Push) 9: goes to top
  •   Remove (Pop): gets 9
  •   Pop: gets 3
  •   Next pop: gets 5 (and so on)

II. Process = a Program in Action

P1    main()

                int f1()
     int f2()

                     void main() {
                          …          Code
                     }
                     int f1() {
                          …
                          x=1;
                          …
                     }
                     int f2() {
                          …
                     }

    Inside a Process

                                                              Heap and Registers
     P1            main()                                     holds variables’ values

                               int f1()
                                                             x=1
                  int f2()

                                      void main() {
        Stack                              …          Code
                                      }
Passes                                int f1() {
                       Program             …
args and return                            x=1;
                       Counter (PC)
values                                     …
                                      }
among functions                       int f2() {
                                           …
                                      }

III. Computer Architecture (Simplified)
              Registers

    CPU

          Cache

      Memory

           Disk

  Computer Architecture (2)

• A program you write (C++/Java etc.) gets compiled to
  low-level machine instructions
    – Stored in file system on disk
• CPU loads instructions in batches into memory (and cache,
  and registers)
• As it executes each instruction, CPU loads data for
  instruction into memory (and cache, and registers)
    – And does any necessary stores into memory
• Memory can also be flushed to disk
• This is a highly simplified picture!
    – (but works for now)

IV. Big O() Notation

• One of the most basic ways of analyzing algorithms
• Describes upper bound on behavior of algorithm as some
  variable is scaled (increased) to infinity
• Analyzes run-time (or another performance metric)
• Worst-case performance

Big O() Notation: Informal Definition

• “An algorithm A is O(foo)”
         Means
• “Algorithm A takes < c * foo time to complete, for some
  constant c, beyond some input size N”
• Usually, foo is a function of input size N
    –e.g., an algorithm is O(N)
    –e.g., an algorithm is O(N2)
• We don’t state the constants in Big O() notation

Big O() Notation: Example 1

• “Searching for an element in an unsorted list is O(N),
  where N = size of list”
• Have to iterate through list
• Worst-case performance is when that element is not there
  in the list, or is the last one in the list
• Thus involves N operations
• Number of operations < c* N, where c=2.

Big O() Notation: Example 2

• “Insertion sorting of an unsorted list is O(N2), where N =
  size of list”
• Insertion sort Algorithm:
     – Create new empty list
     – For each element in unsorted list
          •   Insert element into sorted list at appropriate position

•   First element takes 1 operation to insert
•   Second element takes (in worst case) 2 operations to insert
•   i-th element takes i operations to insert
•   Total time = 1+2+3+…+N=N(N+1)/2 < 1*N2

V. Basic Probability

• Set=collection of thingies
    – S=“Set of all humans who live in the world”
• Subset=collection of thingies that is part of a larger set
    – S2=“Set of all humans who live in Europe”
    – S2 is a subset of S

Basic Probability

• Any event has a probability of happening
• If you wake up at a random hour of the day, what is the
  probability of the event that the time is between 10am and
  11am?
• There are 24 hours in a day
    – Set of hours contains 24 elements: 12am, 1am, 2am, … 10am, 11am,
      …11pm
• You pick one hour at random
• Probability you pick 10am = 1/24

    Multiplying Probabilities

• E1 is an event
• E2 is an event
• E1 and E2 are independent of each other
• Then: Prob(E1 AND E2) = Prob(E1) * Prob(E2)
• You have three shirts: blue, green, red
• You wake up at a random hour and blindly pick a shirt
• Prob(You woke up between 10am and 11am AND that
  you’re wearing a green shirt) = (1/24) * (1/3) = 1/72
• But beware: can’t multiply probabilities if events are
  dependent (i.e., influence each other)!

  Adding Probabilities

• E1 is an event
• E2 is an event
• Then:
Prob(E1 OR E2) = Prob(E1) + Prob(E2) – Prob(E1 AND E2)

• If you don’t know Prob(E1 AND E2), then you can write
Prob(E1 OR E2) ≤ Prob(E1) + Prob(E2)

  VI. DNS

• DNS = Domain Name System
• Collection of servers, throughout the world
• Input to DNS: a domain name, e.g., coursera.org
    – Domain name is a name, a human-readable string that uniquely
      identifies the object
    – Can be derived from the URL (e.g., https://class.coursera.org/foo)

  DNS (2)

• Output from DNS: IP address of a web server (that hosts
  that content)
    – IP address is an ID, a unique string pointing to the object. May not
      be human readable.
• IP address may refer to either
    – Web server actually hosting that content, or
    – An indirect server, e.g., a CDN (content distribution network)
      server, e.g., from Akamai

VII. Graphs

                       Boston
              6                 2     Chicago
Amsterdam
                   3

       9                         14

                         Delhi
            Edmonton

   Graphs (2)
         Edge Weight                  “A is adjacent to B” = There is an A-B edge
                              B
       Edge
                      6                 2             C
Node or Vertex
        A
                          3

              9                           14

                                  D
                  E

What We Covered

I.     Basic datastructures
II.    Processes
III.   Computer Architecture
IV.    O() notation
V.     Basic probability
VI.    Miscellaneous
```

#### Transcript

Welcome to this cloud
computing concepts course. In this lecture, we'll be covering several
concepts ,that are assumed, as a part of the topics that we'll be discussing in
the cloud computing concepts course. So we'll be covering several of the basics
that are considered to be basics in computer science. Typically some of these concepts
are concepts that computer science students learn in their first couple
of years in a computer science degree, undergraduate degree program. So for those of you who are already
familiar with this material this could be a refresher, or you could just,
skip it if you already know the stuff. In any case you can always use this
orientation lecture as a reference to keep coming back to if you
encounter a term in regular lectures that doesn't make sense to you,
or that you'd like to be reminded about. So we'll discuss a few topics,
we'll discuss some basic data structures, what procese are. We'll discuss a little bit about
computer architecture, and then a little bit of math with big
O notation, basic probability, and a few other miscellaneous topics. So, let's get started here. So basically, the instructions will
discuss two different data structures. The first one is a queue. A queue is essentially
a First-in First-out data structure. Elements of the queue
could be any data types. In this example here,
I have elements that are integers, so in this example right now, the queue
has five elements, 3, 5, 8, 0, 7. This is an ordered list of elements. When you remove and
element from the queue, you remove it from the head of the queue. In this case the head is the element, 3. When you insert a new element, you insert
it at the tail of the queue which means that if I insert a new element, say 1, it's going to get inserted
right after 7 in this queue. So, removal always comes from the head, while insertion always
happens at the tail. So, for instance, given this particular
queue, consisting of five elements. If you, if you dequeue or
remove an item then that item will be 3. At that point of time,
the queue will only consist of 5, 8, 0, and 7, with the head pointing to 5. The next item that you dequeue or
remove, will be 5. After that the queue will cut to 8,
0, and 7. And then the next item dequeued
will be 8 and so on and so forth. Dequeues or removals as well as
insertions can occur concurrently. You can remove an element while
at the same time also insert an element at the table. So, that's a queue, which is a first-in,
first-out datastructure. A different data structure is the stack, which is a First-in Last-out
datastructure. Imagine a stack of dishes
that you place on your table. The dish that you put on the top,
that you add the last, will be the first one that you can remove. All right, and that's essentially a stack. So remove, or also known as a pop,
happens from the top. An inserter push also happens at the top. Okay, so in this case if you
push a new element into this particular stack say 9,
then 9 will go above 3. After that, if you pop or
remove an element, that's going to be the last element
that you added, which is 9 in this case. The next pop after that will get
3 because 9 was just removed and 3 is now the top of the stack. After you're able to move three the next
pop or removal will get you 5, and so on and so forth. After that you'll get 8 and then 0 and 7. Okay, so, once again, the removal always
returns you the last item that was added and insertion or a push adds an item
right to the top of the stack. So these two data structures, queue and stack are used very widely
in computer science. And in fact, we'll be using the notion
of the stack right away when we discuss processes soon in this particular
orientation lecture itself. What is a process? A process is essentially
a program in action. For instance, you might write a program
in a language like C, C++, Java. Are you know Python or Ruby on Rails. Whatever it is,
it doesn't matter what the language is. And when you execute that program,
say from the command line or from a gui, that executing
program is called a process. For instance here I have C like program. Which has a function main. Which in turn call a method f1. Which in turn call a method f2. This is shown pictorially here. A main calling f1, calling f2. When you instant shared this program and execute it, it becomes a process,
which in this case is labeled as P1. So this code part showing here
is only the program itself, the process itself consists
of multiple other components. The code typically doesn't change but
the other components might change. What are these other components? Let's look at them one by one. First of all there is a program counter, which is an index into the code which says
where the program is right now, what is the exact line number within the code
where the program is executing right now. Next you have a stack, which is used by the functions to
pass arguments and return values. For instance when main, main function calls F1 any arguments
that it needs to pass to F1 are call, are passed by the stack by pushing
an element on top of the stack. F1 can then pawn that element off and obtain the arguments
that are passed to it. Similarly when F1 calls F2 it then pushes
on top of the stack, the arguments that it has for f2 and f2 can retrieve these
arguments by popping the top of the stack. When f2 is done, it can return
the return values to f1 also by pushing the return values on top of the stack. So that when f1 resumes, it can pop the top of the stack to
obtain the return values from f2. Similarly, f1 returns its return values
to me by pushing on top of the stack. Now, the functions themselves
might declare variables. Some variables will be local variables. And local variables are also to begin
maintaining on top of the stack. I'm not showing them here. And this is the reason why when
a functional method is completed in its execution, any local variables
that are declared inside are then gone, because that part of this
tack has been popped. In addition function, but
also create new memory by, for instance, calling malup or new. In this case I'm showing
such a variable x. And such variables are stored
in a separate data structure, associated with the process
known as the heap. Also associated with a, a heap are also
registers, which typically refer to the recently accessed variables
in the in the process itself. So, for instance,
this variable x is is present in the heap. Such or new variables need to be
explicitly freed in most cases. However some programming languages
have automatic garbage collection. Now the reason we are discussing
a process here is really the main reason is that when
we talk of distributed systems, we are going to talk of multiple
processes communicating with each other. And we'll mostly focus on a process
to process communication, although later on we'll also talk
about how procedure calls or function calls can cross
process boundaries. In addition, the other reason we are
discussing a process here is that when you take a snapshot of a process, when I
say a process takes its own snapshot, this essentially includes everything
that I'm showing here on the slide and maybe a few more elements. It includes the code, the program counter,
the current status of the stack. The current status of the heap and the
registers and then a few other elements. Essentially, this information is enough
to resume this process from here onwards. Okay speaking of computer architecture, let's discuss a simplified
version of computer architecture. Computer architectures today can be
very complicated but typically when we, when we think of how a process
executes on a computer architecture. Again, think of a simplified view. So there's a CPU which executes the actual
instructions which are present in your code. There are also a bunch of registers
that are co-located with the CPU. These are small pieces of memory that
can be accessed very quickly by the CPU. Typically there's only
a small number of registers. Typically not more than
a few tens of registers. There's also a cache which is a slightly
larger memory than the collection of registers. And the larger a mem, piece of memory
is the slower it is to access it, so accessing a cache is
slower than registers. Than accessing registers, but
accessing the cache is still pretty fast. Then beyond the cache there is the main
memory or the random access memory or the RAM which is even larger than the
cache and the ca, and the memory itself, therefore, is slower than the cache,
but still it's pretty fast. And then finally, there's a hard disk,
or if you would like, a solid stave, state drive,
a flash drive or whatever. Which is a lot more memory than the main
memory but of course it's much slower. So as you go up from disk to memory to
cache, registers the speed increases. The total amount of storage
space that you have decreases. So when you write a program such as C++ or
Java or C and you compile it, it get compiled to low-level
machine instructions. The machine instructions might be specific
to the architecture the machine on which you are running or it might be a virtual
machine like a JVM kind of code. Any case these low-level instructions are
the executable version of your program. And this is stored in file system in
the file system, on, on you desk. When your program starts executing,
when it becomes a process. The CPU loads instructions in batches or
in a simplified, more simplified way,
it loads instructions, one by one. It loads them into memory, and
then into cache and, into registers. Typically the cache in the registers
contain the last few access instructions so they are, they fall under what is known
as the least recently used principle. Now as it executes each instruction
the CPU, which is executing the process, loads the data which is necessary for
the instruction into the memory, and then if necessary into the cache and
the registers. And if there are any necessary changes
that happen to a variable like x, then these are stored into memory
first into cache and then into memory. Once in a while,
you may need to store something on disk so that you have a permanent storage so
in case the process goes offline. Then you still have some data. Say for instance, the program might open
a file and write something into the file. So in this case you may want to write
those updates to the file onto the disk. Now of course this is a very
highly simplified picture. Computer architectures can be far
more complex than this today, but for our practical purposes in this course and
as far as explaining how processes work. This will suffice. So, next,
we move on to a few mathematical topics. The first mathematical
topic is a big O notation. A big O Notation is one of the most
basic ways of analyzing algorithms. When I give you an algorithm, and I say,
analyze the algorithm, mathematically. Essentially I expect you to come up with,
at the least a Big O notation and analysis of that algorithm. The, the Big O notation describes and
upper bound and the behavior of an algorithm
as some variable is scaled or increased in value to
all the way to infinity. Typically, this variable
is the size of the input. Maybe the number of input elements. You'll see some,
you'll see a few examples of this. So essentially, this Big O
analysis tells us how does the a, algorithm itself scale as the size
of the input is increased. This analyzes the run-time or typically
another performance metric as well. Most of the time, we analyze run-time. Sometimes, as you'll see in the course, we'll analyze things
like number of messages. Even bandwidth that is exchanged in a,
in the total network itself. The important thing about
big O notation is that it captures worst case performance. Okay?
So this is not expected performance or best case performance. Big O is worst case performance. Given this algorithm, what is
the worst that it can do in terms of this performance metric
that you're measuring? So essentially when I say an algorithm A
is order of foo, this means that algorithm A takes less than c times foo time to
complete, as you mean time is the metric we are measuring, for some constant c, a
fixed constant c, beyond sum input size N. Okay, typically this foo that is
the present of this definition is some function of input size N. For instance,
I could say that an algorithm is order N which means that the algorithm A takes
less than C times N, time to complete for some constant C be on some input size N. So the algorithm might be order
N squared which means that. It is quadratic in time. And it takes time less than c times
n squared for some constant c. Once again, when we say O(N2) or O(N), notice that we do not include
the constant c in the definition itself. This is because
the constant is irrelevant. As long as there is a fixed constant,
some fixed constant. That is good enough for us as far
as Big O() notation is, concerned. Okay, so we do not state
the constants in Big O() notation. So let's see a couple of examples. So first I give you an unsorted list, of,
say, integers, and I ask you to search for a specific element in the list. This essentially means that you
have to iterate through the list, one element at a time, and search for the element by trying to match it with
each element already present in the list. What is the worst case performance? That's what we need, for
bigger notation, right? So the worst case performance happens
either when the element is not there, at all in the list, so you return a false. Or the element the very
last one in the list, the very last one that you match against. Therefore the worst case performance
involves N operations, and the number of operations
involved is less than C times N. Where c equals 2, because the number of operations is N,
where N is the size of the list. Okay, so, the time as well
as the number of operations, assuming each operation takes one
unit of time, both the time taken for this, for this algorithm,
which I trace through the list. As number of operations are both order N. That's why we say order N over here. Let's take a different example
to see how big O notation works. This leads with insertion
sorting of an unsorted list. So suppose I give you a list of elements
say integers, and this is unsorted and I ask you to solve them say,
in increasing order of the elements. The insertion sort
algorithm works as follows. First you create a new list that is empty. Then you iterate through the elements
in the unsorted original list. You remove one element at a time, and you insert that element in the new
list at the appropriate position. Essentially, you sort through
the new list linearly, searching for the right position where
this element should be. So if you do this, the first element of
course takes one operation to insert. That's one insert operation. The second element, in the worst case,
takes two operations to insert. One operation for the comparison with
the one element that's already present in the new sorted list, and
one more operation to insert. Imagine the case, the worst case where
the second element is inserted right at the very end of the list. Similarly the third element will
take three operations to insert. Where the first two elements compared
with the two already existing elements. And the third operation inserts it
at the very end of the of the list. If you go on like this and the i-th
element takes i operations to insert. And you can calculate
the total time required. To insert all the elements as
1 plus 2 plus 3, so on til N. And this is a well-known sum which
comes to N times N plus 1 divided by 2. Which is, less than 1 times N squared. So with the value c equals 1, this, insertion sorting example is an algorithm
that takes order N squared in time and also order N squared in
number of operation. Next, we look at a little
bit of basic probability. Before probability,
we need to discuss a few definitions. The first definition is a set. A set is essentially
a collection of things. So, for instance, a set, S, might be a set of all humans who live
in this world at this current point. A subset is another set, which is a collection of things
that is a part of the larger set. So I might design, describe a set S
two which says a set of all humans who live currently in Europe today. S two is a subset of S because,
every element that is present in S two is also present in S but
the reverse is not necessarily true. Okay, so now probability. Any, any event has a probability
of happening, 'kay? So let me give you an example. If you wake up at
a random hour of the day. So you just wake at some
random hour of the day. Say you have jet lag or something. And I ask you what is a property that
the event at the time is between 10 a.m.,. .
and 11 a.m. Let's try to calculate this. Well, there are 24 hours in a day. So, you have a set that consists
of 24 elements, one for each hour. 12 a.m., .
1 a.m.,. .
2 a.m. All the way to 10 a.m., .
11 a.m.,. .
11 p.m. Okay, so when I say, and
I limit like 1 a.m., .
I mean the hour between 1 a.m.,. .
and 1:59 a.m. Similarly, 10 a.m. Means between 10 a.m. And 10:59 a.m. Out of the set upgrade for
elements, you pick one at random. And the probability that
you're going to pick 10 a.m. Is essentially 1 divided by 24, because
you're picking one element at random. And there are 24 elements in the set. And the probability that you pick
that one special element 10 a.m. Is one over 24 because you,
you want to pick, you want to be lucky. Of that, to pick that ten. So the probability that if you wake
up at a random hour of the day and the time is between 10 a.m. And 11 a.m. Then that probability is 1 over 24. Now there will be multiple events and you
might need to calculate the probability of conjunctions or
disjunctions of these events. I'll describe what these are soon. So say E1 is one event and
E2 is another event. And E1 and
E2 are independent of each other. This means that E1 does not influence E2,
E2 does not influence E1. Then the probability that E1 and E2 both happen is essentially
the multiplication of these probabilities. So you take the probability of E1. Multiply it by the probability of E2, and that gives you the probability
that both E1 and E2 are true. Let's discuss an example of this. Suppose you have three shirts. They're colored blue, green and red. And also you wake up at a random hour and
blindly pick a shirt. You put your hand into your closet and
you blindly pick out a shirt. What is the probability that
you woke up between 10 a.m. And 11 a.m. And that you picked a green shirt to wear? Well the probability that
you woke up between 10 and 11 is essentially 1 over 24. Like we calculated on the previous slide. The probability that you picked the green
shirt is essentially one out of three because there are three colors of shirts. You have three shirts. And you want to pick the green one. You want to be lucky to build the green
one so that's one over three. So the probability that both these
elements are true that you woke up between 10 and 11 and
that you wore the green shirt, is the multiplication of
the probabilities of those events. So it's 1 over 24 times 1 over 3. And that gives you 1 over 72. One of the things that you have to be
careful about here is that if E1 and E2 are not independent, meaning that
they influence each other in some way. Then you can not multiply
the probabilities with each other. Okay, so for instance if the shirt that you have in your closet
changed from one hour to another, because. Say someone in your house
changes them around, then you can't necessarily multiply
these probabilities as they are here. A different thing that we need to do with
two event probabilities is to OR them. So if I give you two events,
E1 and E2, and I ask you the probability that
of either E1 or E2 happening. Then you can see that the probability of
E1 or E2 is the probability of E1 plus the probability of E2 minus
the probability of E1 and E2. Okay, so this is the intersection
of probability here. If you do not now the probability of E1 or
E2. This last term over here. Then you can write the inequality
probability of E1 or E2 is less than or equal to the constituent probabilities. Okay. Sometimes we use these
inequalities to upper bound the, properties of the of these
junctions as we see here. DNS refers to Domain Name System. It's essentially a named
resolution system. It is run as a collection of
servers throughout the world, and it helps you to translate URLs,
actually domain names into IP addresses. So the input to the DNS is a domain
name so just Coursera.org and this is human readable string that
uniquely identifies the object. So we humans can easily remember
a name like Coursera.org. Actually we do need to remember URLs like
class.coursera.org/foo and when you enter this into your browser, your browser
extracts the domain name from this URL and then sends this off as
a query to the DNS system. The DNS system then returns to you
the IP address of a web server that potentially hosts that content. And an IP address is essentially a target,
or an address, or an ID, and it is a unique string
that points to the object. The difference between an ID and a name. The output and the input to a name
resolution system like DNS is essentially that IDs
are harder to remember. It's harder for
us human beings to remember IP addresses. It's much easier for us to remember names. Also, IP addresses change,
but names don't. Now, IP addresses might refer,
might refer to a actual web server, a unique web server that actually hosts
content, so that now your client. A browser can send a,
DCPN ACDP request to that server. Or it might refer to an indirect server or
even a group of servers, such as in a content distribution network,
as it is from Akamai. The fun thing about name resolution
systems is that they can be changed, so the ID or
the address obtained from one name, named resolution system can be given as
a name to another named resolution system, and that can return a different address,
and so on and so forth. And you can keep doing this until you,
reach your final object itself. Graphs. So when we say graphs in computer science,
we don't necessarily mean plots, which have x and y axes. A graph is essentially a network. So here I am showing you a graph
of some cities, Amsterdam, Boston, Chicago, Delhi, and Edmonton. And the travel times between
those cities by air. Rounded out to the nearest hour. Okay, so travelling from Amsterdam
to Boston takes about six hours. Travelling from Chicago to
Delhi takes about 14 hours. Say these are the flights available
on some particular airline. Right? So you see what cities here, as well
as connections between pairs of cities. And also some values
along those connections. Which are the number of hours that it
takes to transit between those cities. These all have names in the terms
in the world of graphs. So each city would be a node or a vertex. Each connection between a pair of
nodes would be called an edge and the value along an edge is
called the edge weight. Also when I say that A is adjacent to B, this means that A has an edge
that connects it to B directly. Typically an edge only goes
between two nodes or two vertices. An edge does not cross three nodes. So here for instance I have one,
two, three, four, five, vertices and
how many edges do I have? I have an AE edge, an AB edge,
a BE edge, a BC edge and a CD edge, so I also have five, different edges
each with its own, edge weight. So, in this lecture,
we have covered the basic datastructures, such as a cube and a stack. We have seen that processes
are programs in action, and that they consist of
multiple different pieces. Processes, of course,
are done under computer architecture, and it's important for you to know at least. A simplified version of
the computer architecture, so that you know what's operating
where when you run a process. We've seen some mathematical topics such
as big O notation which analyses the worst case performance of any given algorithm,
and in some basic probability. And finally,
we have seen a few miscellaneous topics. I hope you can come back,
keep coming back to this as a reference, whenever you need it
throughout the course. [MUSIC]

### 03 - Week 9 Introduction

#### Transcript

[MUSIC] >> Congrats you've completed C3 Part 1 and
you're onto C3 Part 2. If you recall,we ended C3 Part 1 with a
discussion of some of the core theoretical concepts that underline distributed
systems and that are used in Clouds today. This week in the first week of the C3 Part
2 course, we complete the remaining theoretical concepts that
are core in distributed systems. This include Leader Election and
Mutual Exclusion. And we'll also see not
just the algorithms, but also some examples of the use of these
algorithms in real Cloud systems today. Also, I wanted to remind you that at this
time if you'd like to do the programming assignment for this C3 Part 2 course,
please make sure that you complete the programming
assignment for C3 Part 1 course first. This is very critical because the C3 Part
1's programming assignment is a component or a building block for
C3 Part 2's programming assignment. Recall that C3 Part 1 is meant
as a prerequisite for C3 part 2. So, if you have not taken C3 Part 1 so
far, I would highly encourage you to go through the concepts in that course and
also to do the programming assignment if you intend to do
the programming assignment for C3 Part 2. [MUSIC]

### 04 - 1.1. The Election Problem

Slides: `C3_Election_A_CSRAfinal.pdf`

#### Slide text

```
Why Election?

• Example 1: Your Bank account details are
  replicated at a few servers, but one of
  these servers is responsible for receiving
  all reads and writes, i.e., it is the leader
  among the replicas
    •   What if there are two leaders per customer?
    •   What if servers disagree about who the leader is?
    •   What if the leader crashes?
        Each of the above scenarios leads to Inconsistency

More motivating examples

 • Example 2: (A few lectures ago) In the
    sequencer-based algorithm for total
    ordering of multicasts, the “sequencer” =
    leader

 • Example 3: Group of NTP servers: who is
    the root server?

 • Other systems that need leader election:
    Apache Zookeeper, Google’s Chubby
 • Leader is useful for coordination among
    distributed servers

Leader Election Problem

• In a group of processes, elect a Leader to
   undertake special tasks
    • And let everyone know in the group about this Leader
• What happens when a leader fails (crashes)
    • Some process detects this (using a Failure Detector!)
    • Then what?
• Focus of this lecture: Election algorithm. Its goal:
    1. Elect one leader only among the non-faulty processes
    2. All non-faulty processes agree on who is the leader

System Model

 •   N processes.
 •   Each process has a unique id.
 •   Messages are eventually delivered.
 •   Failures may occur during the election
     protocol.

Calling for an Election

 • Any process can call for an election.
 • A process can call for at most one
     election at a time.
 •   Multiple processes are allowed to call
     an election simultaneously.
      •   All of them together must yield only a single
          leader
 • The result of an election should not
     depend on which process calls for it.

  Election Problem, Formally

• A run of the election algorithm must always
   guarantee at the end:
     Safety: For all non-faulty processes p: (p’s elected = (q: a
      particular non-faulty process with the best attribute value) or
      Null)
     Liveness: For all election runs: (election run terminates)
         & for all non-faulty processes p: p’s elected is not Null
• At the end of the election protocol, the non-
   faulty process with the best (highest) election
   attribute value is elected.
    • Common attribute : leader has highest id
    • Other attribute examples: leader has highest IP address, or fastest
       cpu, or most disk space, or most number of files, etc.

Next

•   A classical leader election algorithm.
```

#### Transcript

[MUSIC] Hi there. In this series of lectures, we are going to look at the classical
problem called leader election, which has been useful in many variants of systems,
including today's cloud computing systems. In this lecture today we'll see what
leader election problem actually is. So let's start with an example. Suppose your bank account details
are replicated at a few servers that are maintained by your bank. But one of the servers that the bank
maintains is responsible for receiving all the reads and writes from a client, such
as ATMs or the banking application on your iPad or the banking application on the,
on the website, or so on and so forth. So this single special server
that is on the bank side is called the leader server
among the replicas. Okay, so the leader is responsible
essentially for coordinating the replicas. Now, there are several scenarios
that can happen with a leader. There might be two leaders per customer. This might be problematic because now
the group of replica servers is not sure who the leader is. And therefore reads and writes might
be split across these multiple leaders. Servers might also disagree
about who the leader is. Some servers might know leader,
server a as a leader and other servers might consider
a different server as a leader. And that server might not
even think it's the leader. And this might, again,
lead to inconsistency in the system. If the leader crashes and this means
that the clients may not be able to send reads and writes to the system. And once again, you may need to
re-elect a new leader in the system. So each of these scenarios that
I've described as a question, leads to either inconsistency or
unavailability in the system. Some more examples of situations
which require a leader. We discussed the Different
types of multicast ordering. And one of the ways of implementing
total ordering from multicasts was to use a sequencer process. And this was a special elected
process from among the group of processes itself and there needed to be
exactly one sequence of process, okay. This sequence is essentially the leader. If you have multiple sequencers, then a total ordering may in
fact be violated in the group. When we discuss time synchronization,
we discuss the network time protocol, also known as NTP, and the NTP
organizes all the servers into a tree. And there is one server at
the root of the tree and you need to elect who the server is from
among all the potential NTP root servers. Other systems in industry that also
leverage leader election include open source systems such as Apache Zookeeper
and also Google's Chubby system, on top of which a lot of Google's systems,
internal systems, rely on. Essentially in a nutshell,
a leader in a process group is useful for coordination among the processes
in the group itself. Typically these processes
are servers in a cloud. [NOISE] So, in a nutshell, in a group of
processes, we want to elect a leader. One of the processes needs to be elected
a leader to undertake special tasks such as coordination. Also, it's not just efficient to elect
a leader and let the leader know about it. You need to let all the non-leaders in
the group also know who the leader is. These are the two requirements
of the leader election protocol. What happens when this leader crashes or
fails? Well, first of all some
process detects this failure. How does it detect it? Well, it detects this using
say a failure detector. Using any one of the failure detectors
we have seen elsewhere in this course. You could also use other mechanisms as
you will see some of our systems do. But what happens after
you detect this failure? Well, after this failure you
is detected then you need to run another election algorithm so
that a new leader is elected. And this leader is a non-faulty process,
meaning one that has not crashed. And also you need to let all
the other non-faulty processes in the group know who the new leader is. So that's the goal of
the election algorithm. That's the leader election
problem in disabled systems. So once again, when someone gives you
a problem just make sure that you know what the system model is, under which
you are trying to solve the problem. Essentially the system model tells
you what the assumptions are. In this case our system model
consists of N processes. Each process has a unique id. For instance,
its IP address and port number. Messages that are sent from one process
to another are delivered eventually. They may take awhile but
they are delivered eventually and they're delivered reliably. Failures may also occur
during the election protocol. So for instance,
while you're trying to elect a leader, the leader might itself fail. The next would be leader might in fa,
might in fact fail. Or one of the other processes
in the system might fail, and the leader election protocol needs
to be tolerant to such failures. So, a few more requirements from
the view point of the election itself. Any process should be able to call for
an election. Why is this? Well first of all, any process in the system may
detect the failure of the leader. For instance, why the failure
detector most failure directors allow any process in the system
to detect the failure. For instance, heartbeat based failure detectors are [INAUDIBLE]
failure detectors. When a process detects that the leader
has failed, it an initiate an election, which essentially means it calls for
an election. A process can call for
at most one election at a time. We don't want multiple elections
running simultaneously. If multiple processes call
an election simultaneously, we want all of those together
to yield exactly one leader. We don't them to yield
conflicting leaders. But at a time,
you want only one election running. Also, the results of an election
must not depend on who caused it. So the initiator's ID whichever
processes initiated the election, that must not influence the outcome
of the election itself. Instead, outcome of the election must be
based on cert, certain other criteria that are important to this system or
are important to the application. So a little bit more formally,
a run of the election algorithm must always guarantee two
properties at the end. The properties are safety and liveness. Safety, once again just to remind you, is the property that
nothing bad ever happens. And in this case of the election, safety
says that for all non-faulty processes p. P's elected variable which stands for
p's vision of who the current leader is. Should either be q, a particular non-faulty process
with the best attribute value. I'll talk about attributes
in a little bit, but essentially assume that each
process in the group has an attribute. Say the IP address is the attribute. Right?
We want to elect that process as the leader that has the best attribute
value, say the highest IP address. So, safety says that p's
elected variable must point to the that non-faulty process in the group
that has the best attribute value. Or a p selected variable points to Null. In other words, p never makes a mistake
and points its elected variable to a, a leader, a process that must not be
leader according to the best attribute. Liveness property again,
informally speaking, liveness says that something
good eventually happens. And in this particular case
the liveliness property says that for all runs of the election,
the election run terminates, meaning that something you know,
all the processes quiet to the end. And then for all non-faulty processes p at
the end, p's elected is set to not Null. Okay?
So, p's elected is not Null at the end if p is a non-faulty process. So the combined safety and
liveliness essentially says that, at the end of the leader election run,
which terminates, the that process where the best
attribute value is elected as a leader. And all the other non-faulty
processes in the system have their local elected variables pointing
to this newly elected leader. So what do I mean by electing
the process with the best or highest election attribute value? Well one of the most common
attributes used is the highest id. So among all the ids in the group, you elect that process as
the leader that has the highest id. You can also reverse this and elect the
process with the lowest id in the group. That's fine too. Other attribute examples
include IP address. They include fastest CPU. Or you could use the disk space. Or you could use in peer-to-peer
like settings, you could use processes that have the most number of
files or the least number of files. As long as this attribute is fixed in
the beginning and all the processes know about it, you're going to get a consistent
leader election specification and protocol as well. So in the next lecture, we're going to see
a classical leader election algorithm. And then we'll follow that up by seeing
a few more leader election algorithms. [MUSIC]

### 05 - 1.2. Ring Leader Election

Slides: `C3_Election_B_CSRAfinal.pdf`

#### Slide text

```
The Ring

• N processes are organized in a logical
   ring
    • Similar to ring in Chord p2p system
    • i-th process pi has a communication channel to
      p(i+1) mod N
    • All messages are sent clockwise around the
      ring.

The Ring

      N12       N3

     N6
                     N32

          N80   N5

The Ring Election Protocol

• Any process pi that discovers the old coordinator has failed
   initiates an “Election” message that contains pi ’s own
   id:attr. This is the initiator of the election.
• When a process pi receives an “Election” message, it
   compares the attr in the message with its own attr.
    • If the arrived attr is greater, pi forwards the message.
    • If the arrived attr is smaller and pi has not forwarded an election
         message earlier, it overwrites the message with its own id:attr, and
         forwards it.
     • If the arrived id:attr matches that of pi, then pi’s attr must be the
         greatest (why?), and it becomes the new coordinator. This process
         then sends an “Elected” message to its neighbor with its id,
         announcing the election result.

The Ring Election Protocol (2)

• When a process pi receives an “Elected” message, it
    •   sets its variable electedi  id of the message.
    •   forwards the message unless it is the new coordinator.

Ring Election: Example

                                                Initiates the election
                   N12                     N3
                                                      Election: 3

                N6
                                                N32

                     N80                   N5

Goal: Elect highest id process as leader

                                                Initiates the election
                   N12                     N3

                N6
                                                N32

                                                   Election: 32
                     N80                   N5

Goal: Elect highest id process as leader

                                                     Initiates the election
                   N12                          N3

                N6
                                                     N32

                     N80                       N5

Goal: Elect highest id process as leader Election: 32

                                                Initiates the election
                   N12                     N3

                 N6
                                                N32

  Election: 80

                      N80                  N5

Goal: Elect highest id process as leader

                                      Election: 80
                                                     Initiates the election
                   N12                          N3

                N6
                                                     N32

                     N80                       N5

Goal: Elect highest id process as leader

                                                Initiates the election
                   N12                     N3

                                                      Election: 80
                N6
                                                N32

                     N80                   N5

Goal: Elect highest id process as leader

                                                    Initiates the election
                   N12                         N3

                N6
                                                    N32

                     N80                       N5
                                Election: 80
Goal: Elect highest id process as leader

                                                Initiates the election
                   N12                     N3

                  N6
                                                N32
    Elected: 80

                       N80                 N5

Goal: Elect highest id process as leader

                                                Initiates the election
                   N12                     N3
    Elected: 80

                  N6
  elected = 80
                                                N32

                       N80                 N5

Goal: Elect highest id process as leader

      elected = 80                                 Initiates the election
                     N12                      N3 elected = 80

                 N6
  elected = 80
                                                   N32 elected = 80

                      N80                     N5
                                Elected: 80        elected = 80
Goal: Elect highest id process as leader

       elected = 80                             Initiates the election
                      N12                  N3 elected = 80

                 N6
  elected = 80
                                                N32 elected = 80

                                           N5
       elected = 80 N80                         elected = 80
Goal: Elect highest id process as leader

Analysis

•   Let’s assume no failures occur during the
    election protocol itself, and there are N
    processes

•   How many messages?

•   Worst case occurs when the initiator is the
    ring successor of the would-be leader

     Worst-case

                    N12                    N3
Initiates the election
                 N6
                                                N32

                         N80               N5

Goal: Elect highest id process as leader

Worst-case Analysis

•   (N-1) messages for Election message to get from
    Initiator (N6) to would-be coordinator (N80)
•   N messages for Election message to circulate
    around ring without message being changed
•   N messages for Elected message to circulate around
    the ring
•   Message complexity: (3N-1) messages
•   Completion time: (3N-1) message transmission
    times
•   Thus, if there are no failures, election terminates
    (liveness) and everyone knows about highest-
    attribute process as leader (safety)

Best Case?

•   Initiator is the would-be leader, i.e., N80 is the
    initiator
•   Message complexity: 2N messages
•   Completion time: 2N message transmission
    times

Multiple Initiators?

•   Each process remembers in cache the initiator
    of each Election/Elected message it receives
•   (All the time) Each process suppresses
    Election/Elected messages of any lower-id
    initiators
•   Updates cache if receives higher-id initiator’s
    Election/Elected message
•   Result is that only the highest-id initiator’s
    election run completes

Effect of Failures

                                Initiates the election
                  N12      N3
  Elected: 80

                N6
 elected = 80
                                N32

                                  Election: 80 will
                                   circulate around
                     N80   N5
          Crash                   the ring forever
                                  =>
                                  Liveness violated

    Fixing for failures

•    One option: have predecessor (or successor) of
     would-be leader N80 detect failure and start a new
     election run
      • May re-initiate election if
            • Receives an Election message but times out
              waiting for an Elected message
            • Or after receiving the Elected:80 message
      • But what if predecessor also fails?
      • And its predecessor also fails? (and so on)

Fixing for failures (2)

 •   Second option: use the failure detector
 •   Any process, after receiving Election:80
     message, can detect failure of N80 via its own
     local failure detector
      •   If so, start a new run of leader election
 •   But failure detectors may not be both complete
     and accurate
      •   Incompleteness in FD => N80’s failure might be
          missed => Violation of Safety
      •   Inaccuracy in FD => N80 mistakenly detected as
          failed
            • => new election runs initiated forever
            • => Violation of Liveness

    Why is Election so Hard?

•    Because it is related to the consensus problem!
•    If we could solve election, then we could solve
     consensus!
      • Elect a process, use its id’s last bit as the consensus
         decision
•    But since consensus is impossible in asynchronous
     systems, so is election!
•    Next lecture: Can’t we use Paxos?
```

#### Transcript

[MUSIC] In this lecture, we're going to see
the first classical algorithm for leader election. We'll see another classical
algorithm later in another lecture. This classical algorithm is called
the ring leader election, or ring-based leader election. In the ring, we have N processes
organized in a logical ring. This is somewhat similar
to the virtual ring, or the logical ring that
we saw in the peer to peer system discussion when we discussed
the Chord distributed hash table. Essentially here the i-th process pi has
a communication channel to the i plus 1-th process, that is,
its successor clockwise in the ring. You needs to take modulo N so
that the process N minus 1 is pointing and
has a successor of process p0. All the messages are sent clockwise
around the ring from earlier process to its successor in the ring. Here is an example of a ring. Here I don't have process IDs in
continually increasing orders, but essentially, the processes
are organized in a ring where every process has a successor in the ring. So, N3 for instance, has a successor which
is N32, so it can send messages to N32. N32 in turn is a process
that has a successor of N5, which in turn has a successor of N80,
and so on and so forth, and then N12 has a successor
of N3, which completes the ring. So what does the algorithm look like? So let's look at the, an informal
description, pseudocode of the algorithm, and then we'll see the example of Haydock. Any process pi that discovers
that the old coordinator or the old leader has failed
initiates an election message. And the election message contains,
the initiator pi's own ID, along with its own attribute. Okay?
The ID is needed so that the you need, you need to be able to identify who
last wrote into the election message. And the attribute is needed so that you can elect the best or the highest
attribute process as the leader. Pi is the initiator of the algorithm. It then passes along this election
message to its successor. What does the process do when
it receives an election message? Well, when a process pi receives
an election message, it looks at its own attribute value and it compares
it with whatever is in the message. If the arrived attribute is greater than
its own attribute, then pi knows that it is not eligible to be a leader, because
it doesn't have a higher attribute. pi merely forwards a message as is. It does not change the message. However, if the arrived attribute is
smaller than pi's own attribute value and if pi has not yet
forwarded an election message earlier, it overwrites the message with
its own ID and its own attribute, because this is the max attribute
that has been seen by the message so far, and then it forwards this
newly overwritten message. Now, why do we say that pi
needs to check whether it has not forwarded an election message so
far? Because this will come back to
the termination criterion later on. But essentially what this rule
is saying over here is that when pi receives an election message, it compares the attribute in
the election message with its own. And if its own attribute is higher, then it overwrites the message
with its own ID and attribute. However, if the received
election message has an ID and attribute that matches pi, then this means
that pi's attribute was written into the message the last time it passed pi and
that the message has made one circle, or one circuit around the ring,
and has not changed. Which means that none of the other
processes in the system, in the ring, have a higher attribute
than pi's own attribute. In this case, pi knows when it receives
this duplicate election message with its own ID and attribute that it must be
the new coordinator or the new leader. Therefore, this process pi now
sends out an elected message to its neighbor containing the ID saying
that it is now the new leader. So what does the process do when
it receives this elected message? When a process pi receives
an elected message, it points its own local elected variable
to the id of the message saying that it now knows who the leader is, and then
it forwards the message to its successor. However, if it is the new coordinator or the new leader, it doesn't forward the
message anymore, because essentially this means that the message has made
one circuit around the ring and everyone has set their elected
variables to the new leader. So that in a nutshell is how
the the leader election protocol works using the ring. Now let's see an example with
the previous ring that we have discussed. Once again, here the goal is to elect the
process with the highest id as the leader in the group, and this essentially
means that the attribute is the id. The attribute we're using
in the election is the id. So N3 is the initiator, it's the one
that detects the failure or it's the one that just calls for an election
because it's time to call for an election. It initiates election by
sending an election message. It includes its id in that. It doesn't need to include a second
attribute because the id is the same as the attribute. So it sends this message,
the election message, to N32. When N32 receives it, it knows that its own id is higher
than what's in the message. 32 is greater than 3 3. And so
it overwrites the message with its own id, and then passes on the modified
message to its successor. N5 receives this message, compares the id
in the message 32 with its own id, and the message's id is higher. So it forwards the message
unchanged to its successor. N80 receives this message, sees that its own id 80 is greater
than what's in the message 32. And so it overwrites the message
with its own id 80, and then passes it on to its successor. Similarly the election
message goes through N6 and N12 unchanged because their ids
are lower than what's in the message. And now it reaches N3. N3, again, just passes on the message. It compares what's in the message. It's the initiator, but it doesn't stop
the election message from going around. What instead happens is that eventually,
the election message gets to N80, which sees that this is
a duplicate election message and that the id in the message is its own id. And so the election message
must have made one circle, or one circuit around the ring. And it was unchanged, which means
that none of the other processes in the ring have a higher id than itself. At this point, N80 knows that it
is going to be the next leader. And it starts an elected message
that says that it itself is going to be elected as a new leader. When this elected message is passed on
to its successor, N6, N6 receives it. It marks its own elected
variable to be 80. Which says that N6 knows that N80
is in fact the new leader, and then it passes on the elected
message to its own successor N12. Similarly, this elected message
makes its way around the ring, everyone marks their local
elected variables to be 80, and then finally it gets back to N80,
the elected message. N80 sees that the elected message's
id is the same as itself. And so it can now drop the message and
not forward it anymore. And at this point of time,
the election protocol is done. N80 has been elected as the leader,
it knows that it is a leader, and all the other non-faulty processes
in the group know that it, N80 is in fact the leader. So that's the termination
of the election over here. So let's analyze this protocol. First of all,
let's assume that there are no failures that occur during
the leader election protocol itself. Later we'll see the effect of failures. And let's assume that there
are N processes in the ring. How many messages are exchanged
in the leader election protocol? Well, the worst case occurs when
the initiator is the ring successor of the would-be leader. >> So, essentially going back to
the previous slide, if the successor, if the if the this, the initiator
of the leader election protocol would have an N6 in this particular case,
that would be the worst case. Essentially the initiator would be
the successor of the would be leader. Why is that? Well, let's let's see what happens. So if the N6 is a process that initiates
the leader election protocol, there are N minus 1 messages needed for the election
message to get from the initiator to the would-be coordinator, because it loops
from N6 all the way back around to N80. Then N80 marks the election
message with its own ID. Now the election message needs to make one
more circuit around the ring, another N hops until it get backs, gets back to N80
and N80 knows that it is a new leader. So that's another N messages. And finally, the elected message sent by
N80 makes another circuit around the ring. That's another N messages. So that's a total of, N plu,
N minus 1 plus N plus N messages. That's 3N minus 1 messages for the total leader election to be
completed in the worst case. The completion time is also 3N minus 1
message transmission times over here. If there are no message,
if there are no failures and if all messages are delivered eventually,
this election terminates because it terminates within a finite, a bounded
number of message transmission times. So that guarantees liveness. Also, everyone knows about the leader at
the end of the leader election protocol and the leader knows that it is a leader,
and so this guarantees safety. What is the best case that can occur? Well, the best case that can occur
is that the would-be leader, N80, in this in our example,
is in fact the initiator. So if N80 is the initiator,
then it starts an election message. It makes one circuit around the ring and gets back to N80, which then makes the
elected message go around the ring again. And that's another N messages and
the protocol is done. So that's N plus N 2N messages. And the completion time is 2N
message transmission times. Now, what happens when you
have multiple initiators? Remember that we said that if
you have multiple initiators in a leader election run,
we want all of them to, just one leader, not every initiator is election,
is a separate leader. That would be a violation of safety. Now, multiple initiators can be
supported by modifying the protocol we have discussed so far. By having each process remember in its own
cache the initiator of each election and elected message it receives, you can have the election elected message
carry the id of the initiator itself. Whenever a process receives an elected,
an, an election or elected message that has a
lower id initiator than one it has seen so far, it doesn't forward
those messages anymore. So this essentially means that the if
there are multiple initiators in the group, only the highest id initiator
will have its election complete and therefore that will lead
to exactly one leader. All the other elections called by lower
id initiators will be suppressed and they will never complete. Okay, so
this supports multiple initiators and it still guarantees safety
using our ring-based approach. Next we need to discuss what happens with
failures that occur during the election protocol itself. So for instance, if N80 fails,
the new would-be leader fails, when it has already sent an elected
message, elected equals 80 message, unfortunately, this is a case where
the election protocol may not terminate. In fact, the termination condition
here is that N80 must receive back an elected message and say, hey,
this is an elected message with my own ID, and so
I'm not going to forward it anymore. Unfortunately, because N80 has crashed,
even if the ring were reorganized so that N5 had a new successor of N6, the
selected message saying the new leader is 80 would circulate around
the ring forever, essentially. So liveness would be violated over here. And this protocol would not terminate. So one option to fix failures
is to have the predecessor or maybe the successor of the would-be
leader N80 detect its failure and start a new election run if N80 does not,
stops responding. So this successor or predecessor might
reinitiate the election if it receives an election message but times out waiting
for the elected message from N80. Or it might receive the elected message
and then it might not hear again from N80 again or N80 may not respond to the
pings that are sent by its predecessor. However, and in fact, this is the approach
that is used by some systems like Apache ZooKeeper, as you will see later
on in another lecture in this series. However, the predecessor itself,
which is responsible for detecting N80's failure,
might in fact fail, right? In which case you have no one to
check the failure of the leader. You might say, well, okay, what about the predecessor's predecessor,
which might now take over for its job. What if that process also fails? A second option is to use
a failure detector itself. Any process after receiving
the Election:80 message can detect the failure of N80 via its
own local failure detector. If so, if you detect a failure, then you can start a new
run of the leader election. However, failure detectors may not
be complete as well as accurate, because we've already seen this is true
in an asynchronous distributed system. Incompleteness means that N80's
failure might not be detected at all. And this might be a violation of safety, because the leader has failed and
and no one has detected it, and so there is no leader that is not
faulty in the group right now. Inaccuracy in a failure detector
would mean that N80 might be mistakenly detected as failed and
a new election might be initiated and every time you may have the worst
case happening, which is that the would-be leader is detected as having
failed and a new election is initiated. And this means that you may never, ever
terminate the leader election protocol. So why is it that the election
is turning out to be so hard? Well, that's because it's related
to the consensus problem. In fact, if we could solve election,
then we could actually solve consensus. How are we to do this? Well, a simple way to do this is to
elect a process using whatever election protocol you have, that is, guaranteeing
safety and liveness, even under failures. And then you use, the leader election,
the leader's ID, you use its last bit, which is either a 0 or a 1,
as the consensus decision. Because everyone knows who the leader is. They know what the leader's
ID's last bit is. And so everyone agrees on the value
of the consensus variable. However, since we know that consensus is
impossible to solve in an asynchronous system, so is leader election. however, it is still possible to use
consensus solving approaches such as Paxos to solve leader election. And we'll see that in the next lecture. [MUSIC]

### 06 - 1.3. Election in Chubby and ZooKeeper

Slides: `C3_Election_C_CSRAfinal.pdf`

#### Slide text

```
Can use Consensus to solve Election

• One approach
   • Each process proposes a value
   • Everyone in group reaches consensus on
     some process Pi’s value
   • That lucky Pi is the new leader!

Election in Industry

•   Several systems in industry use Paxos-like
    approaches for election
     • Paxos is a consensus protocol (safe, but
        eventually live): elsewhere in this course
•   Google’s Chubby system
•   Apache Zookeeper

     Election in Google Chubby

   • A system for locking
   • Essential part of Google’s stack                       Server A
         • Many of Google’s internal systems
           rely on Chubby                                   Server B
         • BigTable, Megastore, etc.
   • Group of replicas                                      Server C
         • Need to have a master server elected
           at all times                                     Server D

Reference: http://research.google.com/archive/chubby.html   Server E

Election in Google Chubby (2)

•   Group of replicas
                                                    Server A
     •   Need to have a master (i.e., leader)
•   Election protocol
                                                    Server B
     •   Potential leader tries to get votes from
         other servers
     •   Each server votes for at most one          Server C
         leader
     •   Server with majority of votes becomes      Server D   Master
         new leader, informs everyone
                                                    Server E

    Election in Google Chubby (3)

•    Why safe?
      • Essentially, each potential leader tries to
                                                       Server A    Quorum
        reach a quorum (should sound familiar!)
      • Since any two quorums intersect, and each      Server B
        server votes at most once, cannot have two
        leaders elected simultaneously
                                                       Server C
•    Why live?
      • Only eventually live! Failures may keep        Server D   Master
        happening so that no leader is ever elected
      •   In practice: elections take a few seconds.   Server E
          Worst-case noticed by Google: 30 s

    Election in Google Chubby (4)

•   After election finishes, other servers promise
    not to run election again for “a while”            Server A    Quorum
     • “While” = time duration called “Master lease”
     • Set to a few seconds                            Server B

•   Master lease can be renewed by the master          Server C
    as long as it continues to win a majority each
    time                                               Server D   Master
•   Lease technique ensures automatic re-
                                                       Server E
    election on master failure

Election in Zookeeper

•   Centralized service for maintaining
    configuration information
•   Uses a variant of Paxos called Zab (Zookeeper
    Atomic Broadcast)
•   Needs to keep a leader elected at all times

•   http://zookeeper.apache.org/

  Election in Zookeeper (2)

• Each server creates a new sequence
                                                     N12       N3
  number for itself
    • Let’s say the sequence numbers are ids
    • Gets highest id so far (from ZK file         N6
      system), creates next-higher id, writes                       N32
      it into ZK file system
• Elect the highest-id server as leader
                                                         N80   N5
                                                Master

  Election in Zookeeper (3)

Failures:
                                               N12     N3
• One option: everyone monitors
   current master (directly or via a
   failure detector)                       N6
    • On failure, initiate election                         N32
    • Leads to a flood of elections
                                       Crash
    • Too many messages
                                                 N80   N5
                                        Master

    Election in Zookeeper (4)

•   Second option (implemented
                                              N80                    N3
    in Zookeeper)
     •   Each process monitors its next-
         higher id process
     •   if that successor was the leader   N32         (Monitors)
         and it has failed                                                N5
            • Become the new leader
     •   else
            • wait for a timeout, and
               check your successor               N12                N6
               again

Election in Zookeeper (5)
•   What about id conflicts? What if leader fails during
    election?
•   To address this, Zookeeper uses a two-phase commit (run
    after the sequence/id) protocol to commit the leader
     • Leader sends NEW_LEADER message to all
     • Each process responds with ACK to at most one leader, i.e.,
       one with highest process id
     • Leader waits for a majority of ACKs, and then sends COMMIT
       to all
     • On receiving COMMIT, process updates its leader variable
•   Ensures that safety is still maintained

Next

•   Another classical algorithm: Bully
    algorithm
```

#### Transcript

[MUSIC] In this lecture, we're going to look
at how election is done in a couple of popular systems in industry and
they are Google's Chubby system and the open source Apache Zookeeper system. Both of these systems use consensus or consensus-like approaches
to solve election. One approach to using
consensus to solve election is to have each process proposal value. Everyone in the group reaches
consensus on some process Pi's value. And then Pi is elected as a new leader. Whichever is the lucky process who's
value is chosen as the consensus value, in fact becomes the lucky
leader in the group. This is one approach this is not
necessarily the approach that these systems follow in industry. The systems in industry follow
Paxos like approaches for election. Paxos as you've seen elsewhere in the
course is a consensus solving protocol. It's guaranteed to be safe. Meaning that it it assures that never is a
case that different decisions are reached by different processes for
the consensus variable. But it's only eventually live, which means that it doesn't guarantee
that the protocol will ever terminate. Google's Chubby system uses
a Paxos-like approach and Apache Zookeeper also use,
uses a Paxos like approach. So let's look at Google Chubby first. Google Chubby is a system for locking. It is an essential part of Google's
internal stack of systems. Many of Google's storage systems,
such as BigTable and Megastore rely on Google Chubby for locking and for
writing small configuration files. Chubby maintains a small
group of replica servers. For instance, a cell, a Chubby cell
might contain five replica servers. Server A, B, C, D and E. And one of these servers is elected as
a master server at all points of time. So at any point of time, exactly one
of these servers must be the master or the leader and all the other servers in the group must
get to know about who the leader is. This is eventually our
leader election problem. All right.
So for instance in this case,
Server D is the master here. Now in order to make sure that
there is exactly one master and everyone knows who the master is,
an election protocol is required. Potential leader,
a server that wants to be a master or a leader,
tries to get votes from the other servers. Each server votes for at most, one leader. And when a potential leader gets
a majority of votes from the group, in this case, a majority would be three or more of the servers voting for you is
then that server becomes the new leader. When you have at least three votes from
the group, you can become the leader. So why is this road safe? Well, essentially every potential leader
is trying to reach a quorum in the system. And once again, this is an example of a
technique that you have seen elsewhere in the course that should,
should be familiar to you. Quorum is essentially a majority or
larger. Since any two quorums, no matter which
processes they contain are guaranteed to intersect in at least one process and each
process can vote for at most one leader. You cannot have the case that there
are multiple leaders elected by this election protocol. So this algorithm guarantees safety. Why is this algorithm live? Well, it's only eventually live because,
of course, you cannot solve consensus
in an asynchronous system. And so failures may keep happening,
so that no leader is ever elected. But if things were right
in the in the future, when messages are not delayed to much,
when not too many bad failures happen, then the protocol has a good chance
of converging and terminating. In fact, the folks at Google saw
elections typically take a few seconds, that's a typical time to run an election. And the worst case that was noticed
in the original paper written on Chubby by Google, I noticed that the worst
case election run took only 30 seconds. Chubby also uses a concept
known as leases. After an election finishes,
meaning a leader has been elected, the other servers, servers,
in the group, this group over here. Server A through E guaranteed that they
would not run another election for awhile. Okay.
So this while up time or this time duration is
called a master lease. This is the minimum amount of time that
the master is guaranteed to be the leader. Okay. This is particularly
said to be a few seconds. The master lease must be
renewed by the master, by simply getting a majority again. So as long as it's able to get a majority, it can continue to be the leader
without going through the overhead of running the entire leader
election protocol all over again. This technique of leases or
master leases also ensures that if the master fates renewal lease,
for instances, it has failed or has just began really slow,
then automatically the other servers start a new election run where a new master is
going to be elected with a new quorum. Next we're going to look at
election in Apache Zookeeper. Apache Zookeeper is an open source
system that is a centralized service for maintaining configuration information. Zookeeper uses a variant
of Paxos called Z-A-B or Zab, which stands for
Zookeeper Atomic Broadcast. Zookeeper needs to have
a leader elected at all times. The way lead election works in Zookeeper,
at least the way of electing leaders in Zookeeper is by having each server
create a new sequence number for itself. Let's call these sequence numbers as ids. Essentially, each server
does the following. It gets the highest-id so far. It fetches this from
the Zookeeper file system. Creates a next-higher id and it writes
this into the Zookeeper file system. At the end, whichever id remains, the process
that wrote it becomes the new leader. Okay.
So the highest-id service becomes the new leader. So this ensures that as long as
the files are written anatomically, so that files are written over completely and you don't have partial rights
from two different servers. You're insured that there's exactly one id
in that Zookeeper file at the end and so everyone knows who the leader
is by looking at that file and the leader also knows who
the leader is by at the file. Okay.
So for instance, N80 might be elected as the leader, because it has
the highest-id in the group. What about failures? Well, when you have failures,
such as the leader itself crashes. One option is for
everyone to monitor the correct master. For instance, by using a failure detector,
such as heart beating or ping-ponging. When there's a failure detected,
the processes initiate a new election run. However, when the master fails, multiple
other processes in the group might initiate elections simultaneously and
this may lead to a flood of messages. Even though you could use a way to
suppress the election messages so that most one of them completes, failure
does lead to an explosion of messages. So the option that is actually
implemented in Zookeeper involves each process monitoring its
next higher ID process. So N32, which is the second highest id
process in the system monitors N80. N32 itself is monitored by N12. N12 is monitored by N6 and
so on and so forth. And of course, N3 is monitored by N80,
so that you wrap around the ring. If a process has a successor that
is the current leader in the group, this would be N32, who's successor is N80. And if that process successor has failed, then N32 can immediately
become the new leader. So, it doesn't even need to
run a new election protocol. However, if your successor
is not the leader. For instance, N12 or N6,
then you need to wait for a time out and you need to check your successor again. So, if you timeout waiting for
your successor to respond, then you make sure that you then
point to your successor's successor. If you successor was the leader,
then you can become the new leader. Now conflicts may happen in the system,
because two different processes might write the same sequence number into
Zookeeper file and might turn out that both of them think that they're
the leader in the, in the group. The leader might, the leader might
also fail during the election run. To address both these issues, Zookeeper
uses a two phase commit protocol, which is run after the sequence id
protocol that we have discussed before. In this two-phase commit, the potential leader would seize its own
sequence number in the Zookeeper file. Sends a new leader message to
all the processes in the group. Each process that receives a new
leader message, waits for a while. It might receive new leader messages
from multiple prospective leaders. It responds back with at most, one ACK
message with at most, one board message. And sends it back to that potential
leader that has the highest process id. Now, what does the leader do? Well, the leader waits for a majority
of processes to send it back ACKs. If it reaches a majority,
then it knows that it is a leader. Because each process will
have ordered at most once and if it's got a majority,
if this leader has gotten a majority, then it's sure that no other potential
leader would have gotten a majority. This is the same idea as quorums or majorities that we have
seen as well in the course. Once a leader has its majority of ACKs,
it can then send a commit message to all saying that it is
the new confirmed leader. And everyone, everyone else on receiving
this commit message, update the leader or elected variable to be the new leader. Okay.
So this ensures that safety is still maintained, because once a leader has a
quorum, no one else can have a quorum and so it becomes the new leader. However, this may not guarantee liveness. It's possible that two potential leaders
that send out new leader messages simultaneously, maybe there are mo, more
than two leaders, suppose there are three leaders in the group that
are sending out new leader messages. Each of them gets about
a third of the works or a third of the ACKs from the group and
so now no one has a majority. No one has a 50% or
more of the ACKs in the group. And so liveness is not guaranteed here, you may need to read on the lead
election protocol again. However, safety is guaranteed,
because of the use of quorums. So that concludes our discussion of
election Google Chubby and an Zookeeper. And next we'll discuss in the next lecture
another classical algorithm called the Bully algorithm. [MUSIC]

### 07 - 1.4. Bully Algorithm

Slides: `C3_Election_D_CSRAfinal.pdf`

#### Slide text

```
Bully Algorithm

• All processes know other process’ ids
• When a process finds the coordinator has
  failed (via the failure detector):
   • if it knows its id is the highest, it elects itself as
      coordinator, then sends a Coordinator message to
      all processes with lower identifiers. Election is
      completed.
   • else it initiates an election by sending an Election
      message
       • (contd.)

Bully Algorithm (2)

     • else it initiates an election by sending an
        Election message
         • Sends it to only processes that have a higher id
            than itself.
          • if receives no answer within timeout, calls itself leader
            and sends Coordinator message to all lower id
            processes. Election completed.
          • if an answer received however, then there is some
            non-faulty higher process => so, wait for coordinator
            message. If none received after another timeout, start
            a new election run.
 • A process that receives an Election message
    replies with OK message, and starts its own
    leader election protocol (unless it has already
    done so)

Bully Algorithm: Example

             N80                N3

           N32
                                     N5

                 N12           N6
                       Detects failure
                          of N80

  N80                           N3

N32
                                     N5

            Election
      N12                      N6
                       Detects failure
                          of N80

           N80             N3
Election

     N32
                                 N5
           Election

                      OK
            N12            N6
                      Waiting…

  N80             N3

N32
                        N5

        OK

      N12        N6
Waiting…     Waiting…

                  N80                   N3

   Times out N32
waiting for N80’s                            N5
    response
                  Coordinator: N32

                    N12                 N6

                Election is completed

Failures during Election Run

              N80              N3

            N32
                                    N5

                  N12          N6
           Waiting…      Waiting…

  N80                   N3

N32
                             N5
                Election

      N12              N6
Waiting… OK   Times out, starts
              new election run

  N80                    N3

N32
                              N5
                  Election

      N12               N6
                Times out, starts
            another new election run

Failures and Timeouts

•   If failures stop, eventually will elect a leader
•   How do you set the timeouts?
•   Based on Worst-case time to complete election
     • 5 message transmission times if there are no
         failures during the run:
          1. Election from lowest id server in group
          2. Answer to lowest id server from 2nd
              highest id process
          3. Election from 2nd highest id server to
              highest id
          4. Timeout for answers @ 2nd highest id
              server
          5. Coordinator from 2nd highest id server

    Analysis

•   Worst-case completion time: 5 message transmission times
     • When the process with the lowest id in the system
        detects the failure.
          • (N-1) processes altogether begin elections, each
            sending messages to processes with higher ids.
          • i-th highest id process sends (i-1) election messages
     • Number of Election messages
          = N-1 + N-2 + … + 1 = (N-1)*N/2 = O(N2)
•   Best-case
     • Second-highest id detects leader failure
     • Sends (N-2) Coordinator messages
     • Completion time: 1 message transmission time

Impossibility?

•   Since timeouts built into protocol, in
    asynchronous system model:
     • Protocol may never terminate => Liveness
        not guaranteed
•   But satisfies liveness in synchronous system
    model where
     • Worst-case one-way latency can be
        calculated = worst-case process time +
        worst-case message latency

Summary

•   Leader election an important component of
    many cloud computing systems
•   Classical leader election protocols
     • Ring-based
     • Bully
•   But failure-prone
     • Paxos-like protocols used by Google
        Chubby, Apache Zookeeper
```

#### Transcript

[MUSIC] In this section, we're going to discuss another classical
algorithm called the bully algorithm. In the bully algorithm, all the processes
know the other processes ids and when a process finds
that the coordinator or the leader has failed it can find
this via the failure detector. If the process knows that it is
the process with the next highest id after the leader,
it elects itself as the new leader. And it sends a coordinator message
to all the processes that have lower identifiers than itself. At this point, the election is completed. This is why this is
called a bully algorithm. Essentially, if you know
that the bully has crashed. The highest-id process and
that you're the next highest id process, then you become the new bully and
you tell everyone else with a lower id that in fact you are the new leader and
the new bully in the system. However if you know that you are not
the next highest id process in the system, then you can't be the bully. You initiate election by
sending an election message. Whom you send an election message to? You send election messages to only
those processes that have a higher id than yourself. Essentially, you're trying to ask these
processes, hey, are you guys still alive? Are you guys willing to be the leader or
should I be become the new leader? If none of these processes responds
within a timeout then this initiator becomes a new leader
by becoming the bully and it sends a coordinator to
all lower id processes. At this point, the election is completed. However, if an answer is received within
our timeout called an OK message, then there is some non-faulty
process with a higher id and so this process needs to wait for
the coordinator message. Once again, if it does not receive
a coordinator message within a time out, it starts a new election run. What does the process do when
it receives an election message? Now, remember that an election message is
always received from a lower id process. When election message is received
from a lower id processes, essentially the lower id processes
saying hey, the leader has crashed. Here's a new election run being started. Should I be the new leader? And you need to tell the lower id process,
you need to bully the lower id process into not becoming the leader
by sending it an OK message. And OK message would suppress
the lower ID initiator and it would make it wait for you. When you see the election message,
if this is the first election message you're seeing you would need
to start your own leader election by sending election messages to
processes that have a higher id than you. And the protocol continues
until the highest id process is elected as the leader. So, let's see an example of this. Again, we have a system of six processes
N80 was the old leader, it crashed. And say, N6 is the lucky one in the group
who has detected the failure of N80. What it does is that it realizes
that it is not the next highest id process in the group. And so it needs to send an election
message to all the processes that have a higher id than itself. Which are essentially N80,
the failure process. Yes, it does send a message to
the failed process as well. It sends an election message to N32 and
also to N12. When N32 and N12 receive these messages
they know that they are in fact alive. And so they send back an OK message to N6, which then waits for
the final coordinator message. In turn, N12 and N32 also start
election messages of their own by sending election messages to
their higher id processes. So N12 send election messages to N32 and
to N80 and N32 sent an election message to N80. But N32 receives and towards election,
elected message, it sends back and OK and this suppressed N12 and makes it wait. N32 would time out waiting for N80s reply,
because N80 after all has failed and it would now know that
it is the new leader. It then sends a coordinator message to
all the lower id processes in the system, which is essentially is all the other
processes that are alive in the system. And at this point of time,
the election is completed. And there is a new leader and
everyone else knows about this leader. So you can also have failures that
happen during the election run, so N32 might fail after it has
sent the coord, after it has sent the election message, but
before it sends the coordinator message. And at this point of time, N12 and
N6 need to do something about it. Right? So essentially what happens is that N6 or
N12 will timeout waiting for N32's response and then it would create,
it would start a new election run, which would send a message to N12, which would
then start another election run by itself. And eventually,
N12 will get elected as the, as the new leader in this particular case. If N12 also were to fail then N6 would
also time out waiting for N12's reply. After N12's OK message and
then it would start the new election and then it would time out and then it would
finally become the leader in the group. So if failure stop in the system
eventually you do elect a leader. But if failures keep happening,
then you will never ever elect a leader. But how do you set these timeouts? How long do processes wait? Well, how long processes wait really
depends on the worst case time to complete election. The worst case time turns out to be
five transmission message times, if there are no failures during the run
and you can set your timer to be this. Why is it five message transmission times? Well consider the worst case, which happens if the election is started
from the lowest id server in the group. So the lowest id process in the groups,
a group initiates lead election. Once it sends the election messages out,
it receives OK messages, so the answer that the lowest id initiator
gets from the 2nd highest id process. That would be leader takes another
transmission time, so that's step two. Next, you have the election message from
the 2nd highest id server that goes out to the highest id process, which is,
in fact, the fair leader. That's a third message transmission time. Then the second highest
id process waits for the highest id process to respond and
there's a timeout for that as well. That's the fourth message
transmitting time. And then finally when the 2nd highest id
process realizes that it, in fact, has a, is a new leader, it then sends
a coordinator message to everyone. That's another message transmission time. Those who have looked at this for awhile, may realize that the steps two and
three can in fact be commingled. And the finally, where you can send OK messages to
the lower id processes, alongside. And finally, with the election messages
that you send to the higher id processes. And so you can,
in fact you can reduce this to be just four message transmission
times if you so wish. So the worst-case completion time is five
message transcription times, that deter, that determines the timeout. What about the number of messages that
are transmitted during this worst-case? Well the worst-case happens when
the process with the lowest id in the system detects a failure. It sends election messages to
all its higher id processes and all the N minus 1 processes start
an election protocol by themselves. So this means that the number of
election messages sent out by the high, highest id process is i minus 1. And so you have a total number of election
messages in the system that is equal to N, N minus 1 plus N minus 2 plus 1 and
so forth all the way plus 1. Okay.
There is a number of OK messages that is equal to each value of this minus 1, because the highest id fail
leader does not respond. But essentially the number of total
message is ordered off of this value. This turns out to be N minus 1 times N
divided by 2, which is order N squared. So the worst-case message
complexity is fairly bad. It's quadratic but at least you
have sharp turn around time for the protocol to complete. Well, that's the worst-case. What about the best-case? The best-case happens when the 2nd
highest id process in fact is one that detects the leader failure. It immediately knows that
it is the next high id, highest id of process in the group and
is the new leader. It simply sends out coordinator
messages to the remaining N minus 2 processes with
a lower id than itself. And so the completion time is just
one message transmission time. And the total number of messages
involved is N minus 2 messages. So what were the impossibility here? It seems like this protocol might
actually solve a consensus. however, since timeouts are built
into the protocol itself. This means the protocol
will never terminate, because liveness is not guaranteed. But it doesn't guarantee liveness in
synchronous system where the message delays maybe unpredictable and
processes maybe arbitrarily slow. However, in the synchronous system model
where processes have a maximum time to take an instruction step. And there's a maximum upper bound on how
long a message takes to be transmitted. You can actually calculate the worst one,
worst-case one-way latency as a worst-case processing time for the instructions plus
the worst-case one-way message latency. Using these you can set your time
outs to be the worst-case values and in fact you can, guarantee liveness in this way in the synchronize system
using bully election protocol. To wrap up our discussion
of leader election. Election is an important component of
many cloud computing systems today. We have discussed two classical leader
election protocols ring-based and bully. But they are failure-prone,
because after all, leader election is related to consensus. Which turns out to be impossible to
solve in an asynchronous system. Many systems in industries,
such as Google Chubby as well as Apache Zookeeper which is an open source
system use Paxos-like approaches or quorum like approaches in order to do
elections, which guarantee safety. They may not guarantee liveness, but they
guarantee eventual liveness if things go right in the system in terms of
message losses and failures. And then,
the then the election succeeds and everyone knows about the unique
leader that is elected in the group. [MUSIC]

### 08 - 2.1. Introduction and Basics

Slides: `C3_MutualExclusion_A_CSRAfinal.pdf`

#### Slide text

```
Why Mutual Exclusion?

•   Bank’s Servers in the Cloud: Two of your
    customers make simultaneous deposits of
    $10,000 into your bank account, each from a
    separate ATM.
     • Both ATMs read initial amount of $1000
        concurrently from the bank’s cloud server
     • Both ATMs add $10,000 to this amount
        (locally at the ATM)
     • Both write the final amount to the server
     • What’s wrong?

Why Mutual Exclusion?

•   Bank’s Servers in the Cloud: Two of your
    customers make simultaneous deposits of $10,000
    into your bank account, each from a separate ATM.
      • Both ATMs read initial amount of $1000
         concurrently from the bank’s cloud server
      • Both ATMs add $10,000 to this amount
         (locally at the ATM)
      • Both write the final amount to the server
      • You lost $10,000!
•   The ATMs need mutually exclusive access to your
    account entry at the server
      • or, mutually exclusive access to executing the
         code that modifies the account entry

More Uses of Mutual Exclusion

•   Distributed File systems
     • Locking of files and directories
•   Accessing objects in a safe and consistent way
     • Ensure at most one server has access to object
         at any point of time
•   Server coordination
     • Work partitioned across servers
     • Servers coordinate using locks
•   In industry
     • Chubby is Google’s locking service
     • Many cloud stacks use Apache Zookeeper for
         coordination among servers

Problem Statement for Mutual Exclusion

• Critical Section Problem: Piece of code (at all
    processes) for which we need to ensure there is
    at most one process executing it at any point of
    time.
•   Each process can call three functions
      • enter() to enter the critical section (CS)
      • AccessResource() to run the critical
        section code
      • exit() to exit the critical section

Our Bank Example

  ATM1:                     ATM2:
    enter(S);                 enter(S);
     // AccessResource()       // AccessResource()
    obtain bank amount;       obtain bank amount;
    add in deposit;           add in deposit;
    update bank amount;       update bank amount;
    // AccessResource() end   // AccessResource() end
    exit(S); // exit          exit(S); // exit

Approaches to Solve Mutual Exclusion

• Single OS:
   • If all processes are running in one OS on a
       machine (or VM), then
   •   Semaphores, mutexes, condition variables,
       monitors, etc.

Approaches to Solve Mutual Exclusion (2)

• Distributed system:
   • Processes communicating by passing
       messages
Need to guarantee 3 properties:
    • Safety (essential) – At most one process
        executes in CS (Critical Section) at any time
    •   Liveness (essential) – Every request for a CS
        is granted eventually
    •   Ordering (desirable) – Requests are granted in
        the order they were made

     Processes Sharing an OS: Semaphores

     •    Semaphore == an integer that can only be accessed via two special
          functions
     •    Semaphore S=1; // Max number of allowed accessors
          1.      wait(S) (or P(S) or down(S)):
          while(1) { // each execution of the while loop is atomic
enter()               if (S > 0) {
                         S--;
                         break;
                    }
           }

               Each while loop execution and S++ are each atomic operations –
                   supported via hardware instructions such as compare-and-
                   swap, test-and-set, etc.
exit()    2. signal(S) (or V(S) or up(s)):
                     S++; // atomic

Our Bank Example Using Semaphores

  Semaphore S=1; // shared Semaphore S=1; // shared
  ATM1:                     ATM2:
    wait(S);                  wait(S);
     // AccessResource()       // AccessResource()
    obtain bank amount;       obtain bank amount;
    add in deposit;           add in deposit;
    update bank amount;       update bank amount;
    // AccessResource() end   // AccessResource() end
    signal(S); // exit        signal(S); // exit

Next

• In a distributed system, cannot share
  variables like semaphores
• So how do we support mutual
  exclusion in a distributed system?
```

#### Transcript

Hi there. In this next series of lectures, we will be looking at another important distributed computing problem. This problem is called mutual exclusion. Just to motivate the problem here is an example scenario. Suppose you're a bank where you store all of your money, runs it's servers in the Cloud. Now, say, two of your customers are trying to make deposits into your company's account, and the deposits are both $10,000. The customers make these deposits simultaneously, each from a separate bank branch or from a separate ATM. Here is the set of operations executed by the two ATMs which we'll call as the clients. Each ATM reads initial amount, say, it's $1,000 that's the balance of your bank account from the bank's Cloud server. Then, each ATM adds $10,000, the amount to be deposited to this amount which makes it $11,000. And then, each of these ATMs writes back the final amount to the server. So, the server in the end is storing a value of $11,000. What really went wrong? Well, you should have been storing $21,000 in the end of it, not $11,000. So, essentially, you ended up losing one of the $10,000 because your clients, the ATMs, did not have mutually exclusive access to your account. If you had allowed only one client at a time to access the bank account object that represents your bank balance, then you would have guaranteed mutually exclusive access, and you would have had a balance of $21,000 at the end of this particular series of operations. So, this is an example where mutual exclusion is important where you need mutual exclusive access to a given object. In general, you need mutually exclusive access to a piece of code. In this case, the piece of code would have a piece of code that fetches your bank balance, adds the deposit amount, and then, sends the final bank balance back. If at most one client is allowed to execute in that piece of code at any point of time, then correctness would have been maintained in this particular scenario. There are other situations where mutual exclusion is important and critical. In distributed file systems, clients typically need to lock files, and/or directories. And in this sort of a scenario, you need mutual exclusion where at most one client is allowed to access a file at any given point of time. In general, accessing objects in any distributed system, distributed object store, is a scenario which requires mutual exclusion so that at most once server is granted access to the object. Coordination across servers is another example of a situation requiring mutual exclusion, so that you can partition the work across servers, and the servers can coordinate using locks. In industry, mutual exclusion is fairly widely used. Chubby is one of the core systems underlying several of Google's internal systems. We'll see Chubby in a little bit of detail later on in this lecture series. Also, many cloud computing stacks that are based on open source use Apache Zookeeper for coordination among servers. So, what is the problem? Sort of formally, the mutual exclusion problem is also called as a critical section problem. The critical section is a piece of code which is available at all processes, but for which we need to ensure that there is at most one process executing inside that piece of code at any point of time. So each process has that piece of coordinates in it's own code. But whenever one process is inside that piece of code, the critical section code, no other process should be inside it's own critical section piece of code. So essentially, this is the mutual exclusion problem. Now, the way we define an API for this problem is via essentially two main functions. They are the enter function and the exit function. The enter function is called by a process before it enters a critical section. When the process exits from the enter function, then it can enter the critical section, it can call a function like AccessResource, that runs a critical section code. Then, once the process is done with a critical section, it needs to signal in some way to the other processes that it is done, so that the next waiting process can enter the critical section. And so when a process is done with the critical section, it calls exit to exit the critical section. Here's our example from the banks scenario earlier. Here are the two ATMs. The ATM on the left is ATM1 and the ATM on the right is ATM2. And both ATMs are running identical codes. And that's the beauty of mutual exclusion, that the program is being run at the different clients could in fact, be identical to each other. So, let's see what one of the ATMs does. So, ATM2 does the following, ATM1 does the same thing. First, it enters the critical section. Then, it accesses the resource where it obtains a bank balance, it adds in the deposit, and updates the bank amount. Finally, it calls exit on the critical section. And at this point of time, it's done. So, if you ensure that at most one ATM is executing the critical section in between the enter and the exit, then you're guaranteed that firstly, the ATM1 goes and enters its deposit, and then ATM2 goes, or the reverse happens. Where ATM2 goes first and then ATM1 goes next. And in either case, you're going to end up with the correct bank balance of $21,000 rather than $11,000. So, there are several approaches to solving mutual exclusion. Some of the most basic approaches arise when all the processes are running inside one operating system on a machine or inside a virtual machine. In this case, there are several abstractions that are provided by operating systems or their libraries. These include semaphores, mutexes, condition variables, and monitors. So, when you're talking of a distributed system however, where processes are communicating by exchanging messages, you can no longer use these abstractions that we talked about on the previous slide. Because essentially those abstractions on the previous slide, they need some of the shared variables among the processes, which is not possible in a message passing distributed system. So, you need essentially three important properties for any mutual exclusion solution. They are safety, liveness, and ordering. Safety essentially, once again just to remind you, safety is a property that nothing bad ever happens. And in this case, the bad thing would be two or more processes in the critical section simultaneously. So, safety would say that at most one process isn't the critical section at any point of time. Liveness, once again informally speaking is the guarantee that something good happens eventually. In this mutual exclusion problem, liveness would be the guarantee that when a client wants to access a critical section, that access or that request is granted eventually. These two are essential property, safety and liveness. There is also a desirable third property called ordering, which says that when multiple clients request access to the same critical section, these requests are granted in the order that they were made. And of course, there are many different kinds of ordering that we can talk about and you'll see those different kinds of ordering as we discuss the different solutions that exist to mutual exclusion. So, before we jump to the distributed version of the mutual exclusion problem, let's look at how the basic solution works in the case where processes are sharing an OS. And so, they can actually share variables such as semaphores. So, what is a semaphore? A semaphore informally said is an integer that can only be accessed via two special functions. It's a shared variable, so multiple processes can be sharing this variable. So, the semaphore S in this particular slide is initialized to one, and this means that one is a maximum number of allowed processes that are allowed inside the critical section. The two operations possible on the semaphore are wait and signal. Wait is often called as P or as down. A signal is often called as V or up. The P and V come from Dutch words that were associated with the original semaphore invention. The word semaphore itself is of course an English word that's been in the dictionary for many centuries. Essentially, semaphores were used in the old days to communicate from one hill top to another by burning a fire or beating a drum. And here, in computer science essentially, we are abstracting that out into code and using the same concept, but for mutual exclusion in our operating system. So, let's look at what the wait function does. Essentially, the wait function is what a process would call before it enters the critical section. The wait function enters a while loop. In the while loop, there is another if statement, and the entire execution of the while loop. One execution of while loop is atomic, which means that when a process is executing this particular piece of code, no other process can preempt this process in the process. So for instance, if the process executes the if statement and the S-- statement, and then, it's preempted by the scheduler when another process runs, that's not allowed. Once a process enters one execution of the while statement, it should complete that execution of the while statement before it is preempted. So what does each execution of while statement do? Well, it only checks if the value of the integer S is greater than zero. If it is, then it decrements it by one. And then, it breaks from the while loop in which case, the process can then enter the critical section. So, essentially, if there is only one process accessing the critical section, then according to the while loop and immediately break out, and the value of S would be zero. If another process came along and wanted to enter the same critical section, it would call wait S and it would essentially get stuck in this while loop. It will get stuck until the first process exited the critical section. When it called signal, exiting process would call signal which would simply increment the value of S by one. Once again, this incrementing is again an atomic operation, and the system must ensure that this is executed completely, and it's not executed in a way where the processor fetches the value of S, and then, the process gets preempted before the incremented value of S can be written back to the memory. So, at that point of time, the value of S is again one and the next execution, the while loop, and the second waiting process will break out, and the second waiting process can now enter the critical section. So, these atomic operations of the statement in the while loop and also the S++ operation in the signal operation are provided typically via hardware instructions such as compare-and-swap, test-and-set, and there are several other variants and different architectures. Most hardware platforms and processors provide such instructions so that semaphores and other mutual exclusion variables can be implemented easily in the OS. So, essentially, the wait would be the enter function and the signal would be the exit function. So, in the example of the bank, if ATM1 and ATM2 were in the same operating system as each other, then the code would look as follows. They would share the semaphore variable S, should be initialized to one. Then, before entering the critical section, each ATM would call wait(S). And then, after being done with the critical section, each ATM would then call signal on S. So that was where processes share and can share variables in a single operating system, but in a distributed system where processes communicate by exchanging messages, these solutions will not work. So, in the next lecture, we'll see a solution to the distributed mutual exclusion problem.

### 09 - 2.2. Distributed Mutual Exclusion

Slides: `C3_MutualExclusion_B_CSRAfinal.pdf`

#### Slide text

```
System Model

•   Before solving any problem, specify its
    System Model:
     • Each pair of processes is connected by reliable
       channels (such as TCP).
     • Messages are eventually delivered to recipient,
       and in FIFO (First In First Out) order.
     • Processes do not fail.
         • Fault-tolerant variants exist in literature.

Central Solution

•   Elect a central master (or leader)
     • Use one of our election algorithms!
•   Master keeps
     • A queue of waiting requests from processes who wish
          to access the CS
     • A special token which allows its holder to access CS
•   Actions of any process in group:
     • enter()
             • Send a request to master
             • Wait for token from master
     • exit()
             • Send back token to master

Central Solution

•   Master Actions:
     • On receiving a request from process Pi
           if (master has token)
                 Send token to Pi
           else
                 Add Pi to queue
     • On receiving a token from process Pi
           if (queue is not empty)
                 Dequeue head of queue (say Pj), send that
                 process the token
           else
                 Retain token

Analysis of Central Algorithm

• Safety – at most one process in CS
   • Exactly one token
• Liveness – every request for CS granted eventually
   • With N processes in system, queue has at most
         N processes
     • If each process exits CS eventually and no
         failures, liveness guaranteed
•   FIFO Ordering is guaranteed, in order of requests
    received at master

Analyzing Performance

Efficient mutual exclusion algorithms use fewer messages,
and make processes wait for shorter durations to access
resources. Three metrics:
• Bandwidth: the total number of messages sent in each
    enter and exit operation.
• Client delay: the delay incurred by a process at each
    enter and exit operation (when no other process is in, or
    waiting)
            (We will prefer mostly the enter operation.)
• Synchronization delay: the time interval between one
    process exiting the critical section and the next process
    entering it (when there is only one process waiting)

Analysis of Central Algorithm

•   Bandwidth: the total number of messages sent in each enter
    and exit operation.
     • 2 messages for enter
     • 1 message for exit
•   Client delay: the delay incurred by a process at each enter
    and exit operation (when no other process is in, or waiting)
     •   2 message latencies (request + grant)
•   Synchronization delay: the time interval between one
    process exiting the critical section and the next process
    entering it (when there is only one process waiting)
     •   2 message latencies (release + grant)

But…

•   The master is the performance bottleneck
    and SPoF (single point of failure)

    Ring-based Mutual Exclusion

                           Currently holds token,
          N12            N3 can access CS

         N6
                              N32

              N80        N5

Token:

    Ring-based Mutual Exclusion

                              Cannot access CS anymore
          N12            N3
                                    Here’s the token!

         N6
                              N32

              N80        N5

Token:

    Ring-based Mutual Exclusion

          N12            N3

         N6                      Currently holds token,
                              N32 can access CS

              N80        N5

Token:

Ring-based Mutual Exclusion

•   N Processes organized in a virtual ring
•   Each process can send message to its successor
    in ring
•   Exactly 1 token
•   enter()
     • Wait until you get token
•   exit() // already have token
     • Pass on token to ring successor
•   If receive token, and not currently in enter(),
    just pass on token to ring successor

Analysis of Ring-based Mutual Exclusion

•   Safety
     • Exactly one token
•   Liveness
     • Token eventually loops around ring and
        reaches requesting process (no failures)
• Bandwidth
   • Per enter(), 1 message by requesting process
        but N messages throughout system
     • 1 message sent per exit()

Analysis of Ring-Based Mutual Exclusion (2)

• Client delay: 0 to N message transmissions after
    entering enter()
      • Best case: already have token
      • Worst case: just sent token to neighbor
•   Synchronization delay between one process’ exit()
    from the CS and the next process’ enter():
      • Between 1 and (N-1) message transmissions.
      • Best case: process in enter() is successor of
         process in exit()
      • Worst case: process in enter() is predecessor
         of process in exit()

Next

•   Client/Synchronization delay to access CS still
    O(N) in Ring-Based approach.
•   Can we lower this?
```

#### Transcript

[MUSIC] Hi, there.
So in this lecture we'll start looking at the solutions to the mutual exclusion
problem in the distributed setting. So once again, before solving any problem,
you need to make sure that you know what the system model is,
under which you're solving the problem. So here are the assumptions
in our system model here, each pair of processes that is connected,
is connected by reliable channels, which means that when you send messages on these
channels they are delivered eventually. We can use TCP for these channels. The channels that
are point-to-point channels, which means that they have one sender and
one receiver. Messages along the channel are delivered
eventually to the recipient, and delivered in first in, first out order,
which means that if one message is sent before the second message, then the first
message is received before the second message as well, and finally we'll
assume the processes do not fail. There are many variants of
the algorithms that we'll discuss, all the algorithms that we'll discuss
that are fault-tolerant variants and these are present in the literature, so
our first solution is a central solution. This uses a central master or
leader which is elected using one of our leader election algorithms that
you have seen elsewhere in the course. The master keeps a queue of waiting
requests from processes who wish to enter the critical section. The master also has a special
message called the token message. Access to the token message allows the
holder to access the critical section so the token message is
a very special message. It's like cash, if you have it then you
can use it whether you're a good person or whether you're a thief. So when a process wants to access
the critical section it calls the enter function where it sends
a request to the master, and then it just waits in a loop for
the token from the master. When the processes receives the token,
it enters a critical section and hangs onto the token. When it's done with the critical section
it calls the exit function wherein it simply sends the token back to the master. What data structures does the master
maintain, and what does it do? Well when the master receives
a request from a process Pi, if the master currently has a token,
it simply sends a token to Pi, which gives Pi access to
the critical section. If the master does not have the token, this means that some other process has the
token, and in this case the master ends up queuing the Pi request alongside other
requests that may also be waiting. When there are other process that have
access to the critical section releases the token, this token is
received back at the master and the master then looks at its queue. If the queue is not empty it
takes the head of the queue, some process Pj,
whose request was sent and queued there and this process Pj is
then sent a token which gives it access. 'Kay, and notice that this process
Pj's request will be removed from the queue after it's sent the code,
after it's sent the token. However, the queue is empty, this means
that there are no outstanding requests and the master can then hang on to
the token at this point of time. So, let's analyze this algorithm, so
why does this algorithm guarantee safety? It guarantees safety because
it is exactly one token and only access to the token gets you
access to the critical section. What is guaranteed liveness, liveness is guaranteed if every
request is granted eventually. This is guaranteed because there are at
most N processes in the system and so if your request is queued at the master
there's going to be at most, N minus 1 requests ahead of you and so when each
of the requests finishes, because there are no failures and eventually when
your turn comes at the head of the queue, you will get access to the token and
the critical section. The ordering guaranteed here is FIFO,
in the order received at the master so if your request came in slightly earlier
than your friend's request at the master, then you will get access to the critical
section just before your friend's request, so those are correctness properties. What about performance properties? There are two requirements from
mutual exclusion algorithms. One is that they involve few messages, which means that they are incurring lower
overhead on the network itself, and second is that they incur low delays at the
clients that access the critical section. This means that the overhead of
access in critical sections and releasing them is fairly low. There are three metrics
that capture these. The first is bandwidth, which is simply
the total number of messages sent in the enter and exit functions. The client delay and
synchronization delay are as follows. The client delay is a delay incurred by
a process when there is currently no other process in the critical section, 'kay, which means that right now
there's no one in the critical section, one process comes a long and says, hey,
I need access to the critical section. How long does it take that process
to get into the critical section? The synchronization delay is the delay
between one process releasing the, the critical section, that is,
calling the exit function and the next waiting process getting access
to the critical section, 'kay, so we assume that there's only one resea,
releasing process and of course, and there is only one waiting process for
the synchronization delay. So, let's analyze the central
algorithm for this. Bandwidth once again for
the enter operation only involves the requesting process
sending a request to the master, and it receives a token back so
that's two total messages, no matter when these messages happen,
but that's two total messages. For the exit the requesting process or
the process in the critical section simply sends the token back to the master,
so that's one message for the exit. For the client delay, the master is has a token because there's
no one in the critical section and the requesting process sends a request to
the master which sends it back the tokens so that's two message latencies or
one round trip time. Synchronization delay the process
in the critical section exits the critical section by sending
the token to the master. So that's one message transmission,
then the master sends the token forward, to the next process in the queue,
which is another message transmission. So that's two message latencies for the synchronization delay,
in the central algorithm. So the master of course here is
the performance bottleneck because it could get overloaded with a lot of
requests and also if the master fails then you have a single point of failure,
which means that until this new master is elected you cannot
serve any mutual exclusion requests. So, our next algorithm tries to address is
eliminating the master all together and instead using a ring. Here we organize all the processes in
the system into a virtual ring where each process can talk to its
successor in the ring. Typically, this is a clockwise successor,
so for instance N3's is N3 is a process,
its successor is N32. It can send messages to N32. N32 is another process in the ring which
can then send messages to it's successor N5 and so on and so forth and
the ring loops around. We have a special message called
a token message shown as a blue message here on this slide. The process that has the token
message at any point of time can enter the critical section. No other process can enter
the critical section, so N3 currently has access
to the critical section. It, if it chooses so, can access the
critical section at this point of time. When it's done, it can pass on
the token to its successor in the ring. At this point of time, no one can access
the critical section anywhere in the loop, because the token is in transit,
it's on the network. But when N32 receives the token,
it can then access the critical section. If it's not interested, it simply
passes on the token to its successor. So once again,
we have N processes in a virtual ring. Each process can send a message
to its successor in the ring. There is exactly one token in the ring. In order to enter a critical section you
simply wait until you get the token. There is nothing you can do to
actively seek out the token. When you're done with the critical when
you're in the critical section you hang on to the token. When you're done with
the critical section, you simply pass on the token
to your successor in the ring. If you get the token, and you're not
interested in the critical section, meaning that you're not
in the enter function, then you simply pass on the token
immediately to your successor in the ring. So, why does this
guarantee guarantee safety? Well, there is exactly one token and
for the same reasons as in the central mutual exclusion algorithm
safety is guaranteed here. Liveness is guaranteed because there is a
finite a number of process in the ring and the token eventually loops around and
reaches a requesting process. This of course assumes no failures, which means that the token is not lost and
that the ring stays intact. Bandwidth, per enter operation there's
only one token message received by the requesting process, however the other
N minus 1 processes might have to put an effort in transporting
the token around. So the total number of
messages per request might be as high as N throughout the system. There is, of course,
just one message per exit operation, where the process passes on the token
to its successor in the ring. What about performance? Let's look at client delay. Client delay means that there is currently
no one in the critical section and suddenly, one process comes up and
says, aha, I need access to the critical section. The best case is when this process
already has access to the token. In which case, the number of
message transmissions is zero. The worst case is when this, the process
that just requested access in the critical section has just passed on the token
to its neighbor or to its successor. In this case the token now needs to ma, make it's way around the other N minus
1 processes because in a system of N processes in a ring, you have N links, and
this means N message transmissions for the token to come around, and
that's the worst case, so the client delay could be anywhere
between 0 to N message transmissions. What about synchronization delay? Synchronization delay means that
one process releases the token and one of the processes somewhere in
the ring is waiting for the token. The best case is just one message
transmission where the waiting process is the successor of the releasing
process which means that the, the, the token makes only one hop before
it gives access to the critical section. The worst case is when the process that is
waiting is the predecessor of the process that is releasing the token. In this case the token needs to make its
way around the ring in a clockwise manner to reach the requesting process, and that's N minus 1 message transmissions
in a system of N processes in the ring. 'Kay, so the synchronization delay could
be anywhere between 1 to N minus 1 message transmissions, so
we solved somewhat the the bottleneck problem with the central mutual exclusion
algorithm, but the client delay and the synchronization delay have gone up to
the other N, in the ring-based approach. The question is, can we do,
can we do better than this? Can we lower this kind of
synchronization delay further? And the answer,
we'll see in the next lecture. [MUSIC]

### 10 - 2.3. Ricart-Agrawala's Algorithm

Slides: `C3_MutualExclusion_C_CSRAfinal.pdf`

#### Slide text

```
System Model

•   Before solving any problem, specify its
    System Model:
     • Each pair of processes is connected by reliable
       channels (such as TCP).
     • Messages are eventually delivered to recipient,
       and in FIFO (First In First Out) order.
     • Processes do not fail.

Ricart-Agrawala’s Algorithm

•   Classical algorithm from 1981
•   Invented by Glenn Ricart (NIH) and Ashok
    Agrawala (U. Maryland)

•   No token
•   Uses the notion of causality and multicast
•   Has lower waiting time to enter CS than Ring-
    Based approach

Key Idea: Ricart-Agrawala Algorithm

• enter() at process Pi
   • multicast a request to all processes
         • Request: <T, Pi>, where T = current
             Lamport timestamp at Pi
     • Wait until all other processes have responded
        positively to request
• Requests are granted in order of causality
• Pi in request <T, Pi> is used to break ties (since
    Lamport timestamps are not unique for concurrent
    events)

Messages in RA Algorithm

• enter() at process Pi
      •   set state to Wanted
      •    multicast “Request” <Ti, Pi> to all processes, where Ti =
          current Lamport timestamp at Pi
      •   wait until all processes send back “Reply”
      •   change state to Held and enter the CS
• On receipt of a Request <Tj, Pj> at Pi (i ≠ j):
      •   if (state = Held) or (state = Wanted & (Ti, i) < (Tj, j))
                            // lexicographic ordering in (Tj, Pj)
            add request to local queue (of waiting requests)
          else send “Reply” to Pj
• exit() at process Pi
   • change state to Released and “Reply” to all queued requests.

Example: Ricart-Agrawala Algorithm

      N12          N3

                         Request message
                        <T, Pi> = <102, 32>
 N6
                         N32

      N80
                   N5

Example: Ricart-Agrawala Algorithm

      N12          N3

                        Reply messages

 N6
                        N32
                           N32 state: Held.
                           Can now access CS

      N80
                   N5

Example: Ricart-Agrawala Algorithm

N12 state:                          N3
           N12
Wanted         Request message
                  <115, 12>

  N6
                                         N32
                                            N32 state: Held.
                                            Can now access CS
                  Request message
              N80    <110, 80>
                                    N5
 N80 state:
 Wanted

Example: Ricart-Agrawala Algorithm

N12 state:                       N3
           N12
Wanted         Request message
                  <115, 12>    Reply messages

  N6
                                         N32
                                            N32 state: Held.
                                            Can now access CS
                  Request message
              N80    <110, 80>
                                    N5
 N80 state:
 Wanted

Example: Ricart-Agrawala Algorithm

N12 state:                       N3
           N12
Wanted         Request message
                  <115, 12>    Reply messages

  N6
                                         N32
                                            N32 state: Held.
                                            Can now access CS
                  Request message           Queue requests:
              N80    <110, 80>              <115, 12>, <110, 80>
                                    N5
 N80 state:
 Wanted

Example: Ricart-Agrawala Algorithm

N12 state:                       N3
           N12
Wanted         Request message
                  <115, 12>    Reply messages

  N6
                                        N32
                                           N32 state: Held.
                                           Can now access CS
               Request message             Queue requests:
           N80    <110, 80>                <115, 12>, <110, 80>
                                   N5
 N80 state:
 Wanted
 Queue requests: <115, 12> (since > (110, 80))

Example: Ricart-Agrawala Algorithm

N12 state:                       N3
           N12
Wanted         Request message
                  <115, 12>
         Reply messages
  N6
                                      N32
                                         N32 state: Held.
                                         Can now access CS
              Request message            Queue requests:
          N80    <110, 80>               <115, 12>, <110, 80>
                                 N5
 N80 state:
 Wanted
 Queue requests: <115, 12>

    Example: Ricart-Agrawala Algorithm

N12 state:                              N3
                N12
Wanted                Request message
(waiting for             <115, 12>
N80’s          Reply messages
reply) N6
                                             N32
                                                N32 state: Released.
                                                Multicast Reply to
                    Request message             <115, 12>, <110, 80>
                N80    <110, 80>
                                        N5
      N80 state:
      Held. Can now access CS.
      Queue requests: <115, 12>

Analysis: Ricart-Agrawala’s Algorithm

•   Safety
     • Two processes Pi and Pj cannot both have
        access to CS
          • If they did, then both would have sent Reply to
            each other
          • Thus, (Ti, i) < (Tj, j) and (Tj, j) < (Ti, i), which
            are together not possible
          • What if (Ti, i) < (Tj, j) and Pi replied to Pj’s
            request before it created its own request?
                • Then it seems like both Pi and Pj would
                   approve each others’ requests
                • But then, causality and Lamport timestamps
                   at Pi implies that Ti > Tj , which is a
                   contradiction
                • So this situation cannot arise

Analysis: Ricart-Agrawala’s Algorithm (2)

•   Liveness
     • Worst-case: wait for all other (N-1)
        processes to send Reply
•   Ordering
     • Requests with lower Lamport timestamps
        are granted earlier

Performance: Ricart-Agrawala’s Algorithm

• Bandwidth: 2*(N-1) messages per enter()
   operation
    • N-1 unicasts for the multicast request + N-1 replies
    • N messages if the underlying network supports
        multicast
    •   N-1 unicast messages per exit operation
          • 1 multicast if the underlying network supports
             multicast
• Client delay: one round-trip time
• Synchronization delay: one message
   transmission time

Ok, but …

•   Compared to Ring-Based approach, in Ricart-
    Agrawala approach
     • Client/synchronization delay has now gone
       down to O(1)
     • But bandwidth has gone up to O(N)
•   Can we get both down?
```

#### Transcript

[MUSIC] In this lecture, we look at, a classical algorithm to the distributed
mutual exclusion, problem. This algorithm is called
the Ricart-Agrawala's Algorithm. Once again, before solving any problem
just remind yourself of the system model. Once again, we assume that, each pair of processes that is connected
by a channel has, the channel be reliable. So if you send messages on the channel,
they are eventually delivered and they're delivered in
first in first out order. We also assume that processes do not fail. So, Ricart-Agrawala's algorithm is a
classical mission exclusion algorithm for distributive systems. It was published in the 1980's. It was invented by Glenn Ricart from
the National Institute of Health and Ashok Agrawala from
the University of Maryland. Unlike the previous algorithms you
have seen from each of the inclusions, the centered and green based algorithms,
there's no token involved here. Instead, this,
algorithm uses notions of causality and it uses multicast inside the blue. It has a lower waiting time to
enter the critical section than the Ring-Based approach. So, here is, the key idea ,and then we'll see an
example of the Ricart-Argawala algorithm. When, a process Pi wants to
enter the critical section, it multicasts a request to
all the other processes. The request includes,
the process ID, Pi, of course. But it also includes,
the current Lamport timestamp. This is the, causal or
logical timestamp at process Pi. Once Pi has sent this, multicast request, it waits until all the other N-1
processes have responded positively. To other requests. When it receives N-1 replies,
it can then enter the critical section. Requests in this system are granted
in the order of causality. The Pi in the request T,
Pi is used to break ties. Because two different processes
might have concurrent requests which might in fact end up
having the same timestamp. You need to have a way to break ties. And the ID of the processes
is used to break ties. Okay.
So here are all the messages in the Ricart-Argawala algorithm and
all the actions in their gory detail. And then we'll see an example
over the next few slides. When a process Pi wants to
enter the critical section, it first sets its state to be Wanted. And then multicasts a request
to all processes, the request simply consists of the Lamport timestamp
at Pi currently, followed by Pi's ID. So that's Ti, Pi. It then waits until all the N-1 other
processes have sent back a reply message. Once it has received this N-1 replies,
it then changes its state to be Held, and it can now enter the critical section. What does a process do when
it receives a request? So, when a process Pi receives a request,
from a Pj, which is tagged as Tj, Pj. Tj being the timestamp of the request,
Lamport timestamp. And Pj being the requester's ID. The Pi,
process first checks if its state is Held. If its state is Held then essentially it
cannot, send back a reply immediately because this means that Pi currently
is in the critical section. In this case Pi would add, the request
to a local queue of waiting requests. On the other hand if Pi's state is
Wanted which means that Pi has, currently another request. That it for
the critical section that has not yet been granted, then Pi checks whether or
not, the timestamp of Pi's own request is less than
the timestamp of the incoming request. Okay, in order to do this,
it first compares the Lamport timestamps. Ti and Tj. If Ti's less than Tj, then this is less
than equal or equal to condition succeeds. If Ti equals Tj, in which case,
the requests were concurrent. Then, it breaks ties by considering
whether i is less than j. If this condition is true,
which means that Pi's own request, has precedence over Pj's request, in this
case also, Pi would queue Pj's request. However, if none of these conditions is
true then Pi send a reply back to Pj. Okay. Now when a process is done
with a critical section, across Pi it's simply change,
changes it's state of Released and it sends a reply to all
of it's queued requests. Now notice that when, the process is
in the critical section it may receive multiple, requests from multiple other
processes for the critical section. It would end up queueing
all of these requests. When it is done with this critical
section, it would send back a reply to all of them saying, hey,
I'm done with that critical section. I am ready to acknowledge all of you
as ready to enter the critical section. That's essentially the algorithm called,
so let's see an example. Here is, again, a system of six
processes N3, N32, N5, N80, N6 and N12. N32 first sends a request message which
has a time stamp of 102 along with N32's own idea of 32. This is multicast out to the other
N-1 proxies in the system. All of them send back reply messages, because none of them are waiting
to access the critical section. N32's state is now Held, meaning that it is currently
enter in the critical section. Now let's make it slightly more complex. Suppose, that two other processes, N12 and N80 also want to access
the critical section. Notice that N32 is currently
also in the critical section, its state currently needs to be Held. However for each of N12 and N80, the state now becomes Wanted because these
are trying to enter the critical section. N12's request has a timestamp of 115. N80, N80's request has
a Lamport timestamp of 110. So let's see what happens now. The next thing that happens is that these
requests are received at some processes in the system. Specifically N6, N3 and N5 receive
both of the requests from N12 and N80. And because N3, N6, and N5 are not waiting for any, are not
waiting to enter the critical section, they send back replies to whoever
they receive requests from. At this point of time, N12 and
N80 each having three reply messages back, but they are waiting for
two other reply messages. The next thing that happens in
the system is that N32 receives these request from N12 and
N80 one after another. Because N32 state is now Held,
it queues both of these requests, both the timestamp as well as the IDs. So. N12's request 115, 12 is queued. Followed by N80's request 110, 80. The order of requ-, of queuing
here doesn't really matter because the replies are sent to the entire queue. Notice here that N12 and N80's requests
to each other are still in transit. So one of them is going
to get the request first. And you might think,
well whoever gets the request first. Is, likely to win the race,
or maybe lose out the race. But in fact,
causality comes to our rescue here. So let's say N12 gets,
N12's request is received first with N80. N80 receives this request
its state is Wanted. So it checks whether or not the incoming
request has a lower timestamp than it. It sees that incoming request
has a timestamp of 115. Which is higher than N80's own request. And so N80 ends up queuing its
queuing the incoming request. And since the incoming request
is queued which means that N80 would not have sent a response,
a reply message back to N12. N12 is going to end up waiting for
N80's, reply message. Next N80's reply message is received at N,
12, which then, is in a Wanted state and it checks whether the incoming
request has a lowertime stamp than it. And in fact, this is true because
the incoming request has a timestamp of 110 while N12's waiting
request has a timestamp of 115. In this case N12 would respond
back with a response message or a reply message back to N80. At this point of time,
N80 has four requests responses back or replies back from the group. N12 has three responses back for
the group. And N32 is currently in
the critical section. N32 then will release
the critical section. Once it is done with the critical section,
it releases its token. Sends back reply messages to N12 and N80. At this point of time,
N80 has five reply messages back. And it can enter the critical section. N12 cannot enter the critical section yet because it does not have
a reply back from N80. It only has four replies. And this is fine because N80 is
queueing the request from N12. When N80 is done with
its critical section. It will then send a reply back to N12, which will then enter
the critical section after that. Why is the Ricart-Agrawala's
algorithm safe? Let's look at the proof a little bit,
informally at least. Two processes Pi and Pj cannot both have access to
the critical section simultaneously because if they did, then both would
have sent a reply message to each other. And this would have meant that,
in the case of, one of them. Ti,i is less than Tj,j. And this is why Pj would
have given permission to Pi. Would have responded with a reply to Pi. And also it must be true
that Tj,j is less than Ti,i. And in this case Pi would
have given a reply to Pj. But both of these are not
possible together, you know, you cannot have two less than three and
also three less than two. That's not possible. So that's the crux of the proof. Now, of course, there is an exception
which some of you might think about, which is that it's possible that,
Ti,i is less than Ti,j. And Pi has already replied to Pj's
request with a positive reply. And only after that does Pi
generate its own request. At this point in time, it seems like Pj will also respond to
Pi's request with a positive reply. And both Pi and Pj might have
access to the critical section. So essentially, Pi gives Pj permission. Then Pi generates a request. And because now Pi's request has a lower
timestamp than Pj's Pj would also give a permission to Pi. However, this cannot occur because
once Pi has received Pj's request, any request that it generates subsequently based on Lamport timestamps based on
causality will have a higher timestamp. Therefore it must be true
that Ti is greater than Tj. This follows directly from. The use of Lamport timestamps. This is very the use of Lamport timestamps
really plays with the correctness and the safety of
the Ricart-Agrawala algorithm. And so, Ti greater than Tj is
a contradiction to what we had assumed, which is Ti,i is less than Tj,j, and
so this situation cannot arise either. Next liveness [COUGH] liveness is
true because in the worst case you process ends up waiting for
all the other N-1 processes to send reply. And once they send a reply, which will
happen, you know, the other N-1 processes might all be in the critical section,
and this process might be the very last. And when that happens,
when this process is given permission,. Then it will be able to
enter the critical section. Finally ordering here is guaranteed
in the sense that request with lower Lamport timestamps
are granted earlier and again if there is a,
conflict in timestamps, then. Then the process ID is used to break ties. But in any case,
if one process generates a request for the lower line stam-,
timestamp than our other process. Then that first process will get it's request satisfied earlier
than the second process. And so, even though we have done better
in the client/synchronization delay compared to the Ring Based approach. The bandwidth has gone up. And the question now is,
can we do better in both of these cases. We'll see that in the next lecture. [MUSIC] [MUSIC]

### 11 - 2.4. Maekawa's Algorithm and Wrap-Up

Slides: `C3_MutualExclusion_D_CSRAfinal_2.pdf`

#### Slide text

```
Cloud Computing Concepts

          Indranil Gupta (Indy)
        Topic: Mutual Exclusion
  Lecture D: Maekawa’s Algorithm and
                Wrap-up

Key Idea

•   Ricart-Agrawala requires replies from all processes
    in group
•   Instead, get replies from only some processes in
    group
•   But ensure that only process one is given access to
    CS (Critical Section) at a time

Maekawa’s Voting Sets

• Each process Pi is associated with a voting set Vi (of
    processes)
•    Each process belongs to its own voting set
•    The intersection of any two voting sets must be non-empty
     • Same concept as Quorums!
• Each voting set is of size K
• Each process belongs to M other voting sets
• Maekawa showed that K=M=ÖN works best
•  One way of doing this is to put N processes in a ÖN by ÖN matrix
    and for each Pi, its voting set Vi = row containing Pi + column
    containing Pi. Size of voting set = 2*ÖN-1

Example: Voting Sets with N=4

                                       p1 p2
                                 V2    p3 p4
P1’s voting set = V1

                       p1   p2

                       p3   p4

                V3                V4

Maekawa: Key Differences From Ricart-Agrawala

•   Each process requests permission from only its voting
    set members
     • Not from all
•   Each process (in a voting set) gives permission to at
    most one process at a time
     • Not to all

Actions

•   state = Released, voted = false
•   enter() at process Pi:
      • state = Wanted
      • Multicast Request message to all processes in Vi
      • Wait for Reply (vote) messages from all processes
          in Vi (including vote from self)
      • state = Held
•   exit() at process Pi:
      • state = Released
      • Multicast Release to all processes in Vi

Actions (2)

• When Pi receives a Request from Pj:
if (state == Held OR voted = true)
             queue Request
else
             send Reply to Pj and set voted = true

• When Pi receives a Release from Pj:
if (queue empty)
           voted = false
else
           dequeue head of queue, say Pk
           Send Reply only to Pk
           voted = true

Safety

•   When a process Pi receives replies from all its
    voting set Vi members, no other process Pj
    could have received replies from all its voting
    set members Vj
     • Vi and Vj intersect in at least one process
        say Pk
     • But Pk sends only one Reply (vote) at a
        time, so it could not have voted for both Pi
        and Pj

Liveness

                                                                                       V2
                                                      P1’s voting set = V1

•   A process needs to wait for at most (N-1) other
    processes to finish CS                                                   p1   p2
•   But does not guarantee liveness
•   Since can have a deadlock                                                p3   p4
•   Example: all 4 processes need access
     • P1 is waiting for P3
     • P3 is waiting for P4
     • P4 is waiting for P2                                           V3                V4

     • P2 is waiting for P1
     • No progress in the system!
•   There are deadlock-free versions

Performance

•   Bandwidth
      • 2ÖN messages per enter()
      • ÖN messages per exit()
      • Better than Ricart and Agrawala’s (2*(N-
        1) and N-1 messages)
      • ÖN quite small. N ~ 1 million => ÖN = 1K
•   Client delay: One round trip time
•   Synchronization delay: 2 message transmission
    times

Why ÖN ?
•   Each voting set is of size K
•   Each process belongs to M other voting sets
•   Total number of voting set members (processes may be repeated) =
    K*N
•   But since each process is in M voting sets
     •    K*N/M = N => K = M (1)
•   Consider a process Pi
     •    Total number of voting sets = members present in Pi’s voting
          set and all their voting sets = (M-1)*K + 1
     •    All processes in group must be above
     •    To minimize the overhead at each process (K), need each of
          the above members to be unique, i.e.,
             • N = (M-1)*K + 1
             • N = (K-1)*K + 1 (due to (1))
             • K ~ ÖN

Failures?

•   There are fault-tolerant versions of the
    algorithms we’ve discussed
     • E.g., Maekawa

•   One other way to handle failures: Use Paxos-
    like approaches!

 Chubby

 •   Google’s system for locking
 •   Used underneath Google’s systems like
     BigTable, Megastore, etc.
 •   Not open-sourced but published
 •   Chubby provides Advisory locks only
      • Doesn’t guarantee mutual exclusion unless
         every client checks lock before accessing
         resource

Reference: http://research.google.com/archive/chubby.html

Chubby (2)

•   Can use not only for locking but also writing small
    configuration files                                     Server A
•   Relies on Paxos
•   Group of servers with one elected as Master
      • All servers replicate same information              Server B
•   Clients send read requests to Master, which serves
    it locally                                              Server C
•   Clients send write requests to Master, which sends
    it to all servers, gets majority (quorum) among
    servers, and then responds to client                    Server D   Master
•   On master failure, run election protocol
•   On replica failure, just replace it and have it catch   Server E
    up

Summary

•   Mutual exclusion important problem in cloud
    computing systems
•   Classical algorithms
     • Central
     • Ring-based
     • Ricart-Agrawala
     • Maekawa
•   Industry systems
     • Chubby: a coordination service
     • Similarly, Apache Zookeeper for coordination
```

#### Transcript

[MUSIC] In this lecture, we are going to
discuss another classical algorithm for distributed mutual exclusion, and we also wrap up our discussion
of the mutual exclusion topic. So the Ricart-Agrawala Algorithm
that you've seen already from mutual exclusion requires replies from
all of the processes in the group, which is one of the reasons
that it has a high bandwidth. It has a bandwidth that is order N. The key idea in the Maekawa's Algorithm,
new algorithm, is that you need to get replies from
only some processes in the group, not all the processes but only some. But you also need to ensure that only one
process is given access to the critical section at any point of time which
means that safety is guaranteed. So Maekawa's Algorithm works as follows, each process Pi is associated
with a voting set called Vi. A voting set consists of a few
other processes from the group. Each process must belong
to its own voting set Vi. Now, the voting set is not all
the other process in the group which is essentially the approach of
the Ricart-Agrawala Algorithm, but the voting set is only
a small subset of the group. However, you need to make sure that
given any two voting sets Vi and Vj of process Pi and Pj, respectively. The intersection of these two
voting sets is non-empty. Which means that there's at least
one process that belongs to both Vi as well as Vj. So given any pair of voting sets, Vi and
Vj, you need to make sure that at least one process is in common
between those two voting sets. This might sound familiar to you, in fact,
it is the same concept of the same idea as Quorums, which you have
seen elsewhere in the course. And however,here, the usage of this
is slightly different of course. Now each voting set is of size K. So all the voting sets
are of similar size. And each process contributes by
belonging to M other voting sets, including, of course, its own. Maekawa shows that the values of K
= M = square root of N, work best. We'll see a calculation
later on in this lecture, which calculates why square
root of N is a good value. One way of assigning voting sets so that
they are always intersecting in any pair of voting sets, and so that you get
order square root of N voting set sizes, is to put all the N processes in a square
root of N by square root of N matrix. And whatever process falls in the matrix, you consider that the processes column and
you also consider the processes row. And all the processes in the column and
in the row all together, the union of them is considered
to be the voting set of that process at the intersection of the row and
the column. So, this would result in voting set
size that is 2*square root of N-1, which is still order of square root of N. So let's see an example. So suppose I have four processes
in the system, of course, this is a perfect square. So we can put them in a matrix
as shown here, p1, p2, p3, p4. And if you select a processes
drawing column as its voting set, then you get voting sets as shown
on the left side of the slide. So consider p1 and the process p1, it's
row consist of the process p1 and p2 and its column consists of the process p1 and
p3. So it's voting set consists of
those three process, p1, p2 and p3, as shown by this circle over here. Similarly, V2 which is the voting set for
p2 consists of the processes p1, p2 and p4, and so on and so forth. You notice that any pair of
processes intersect in at least one, in many cases,
two of the process in the system. So [INAUDIBLE] V1 and V4,
they intersect in two process, p2 and p3, in other systems. So let's see how these
voting sets are used, then. So first of all, each process requests permission from only
its voting set members, not from all. And this is one way in which
the Maekawa's Algorithm differs from the Ricart-Agrawala Algorithm,
that we've seen previously in the course. Second, each process that
is in the voting set, gives permission to at most
one process at a time. And again, this is different from the Ricart-Agrawala
Algorithm where a process may have given permission to multiple, perhaps
all the other processes in the group. Okay, so these are two key differences. Anyway, let's look at how
the algorithm actually works. So first,
initially the state of a given process. Again, we described the algorithm by
describing what happens at a given process. The state of a given process is released
which means that currently does not holding the lock or
it's not in the particular section. Also it's state for voted is false,
meaning that it has not yet voted for any other process to get
access to the critical section. Now, when this process Pi wants to enter
the critical section it first sets its state to be wanted, meaning it wants
to enter the critical section. Then it multicast a request message to all
the processes in its own voting set Vi. Notice that this votings
in Vi also includes itself. So, when Pi sends and receives its own
request, then you have to process it. And I'll describe how this processing
is done in the next slide. Then the process, after sending out
this request message, it waits for a reply or a vote message from all
the processes in its own voting set. And that includes a vote from itself. When it has all these votes,
it can then set a state to be held and then proceed in to the critical section. What happens when a process is
done with the critical section? Well, the first thing it does is that
it sets its state to be released again. Meaning, that it's done
with the critical section. And then multicast release message to all
the processes in it's own voting set Vi. This is not all that there is for
the protocol. Now, when a process Pi receives
a request from Pj, first, it checks if it's own state is held, meaning,
it currently is in the critical section or if it has voted in the past meaning
it's voted variable is true. If either of these conditions is true then
it queues this new request because it means that someone answers
in the critical section. Otherwise, it sends a reply or
a vote back to Pj and it sets its voter variable to be true,
indicating that it has recently voted. Now, when a process Pi receives
a release message from process Pj, recall from the previous slide
that a release message is received when Pj has just exited
the critical section. And informs all its voting set members
that it has exited the critical section. Pi looks at its queue of waiting requests. Remember, that Pi may be in
not just Pj's voting set, but also in the voting set of other processes. And these other processes may
be waiting for a vote from Pi. But if Pi's queue is empty, it means that
Pi doesn't have any outstanding requests and so it sets its voted variable to be
false and it exits in the point of time. However, if there's
something in the queue, then a dequeue is a head of the queue,
say a process, Pk. Remember, that this means that
Pk's voting set contains Pi and that Pk has previously sent a request
to Pi which has been queued. And the queueing happened
here in the past or right at the top of the slide over here. That's where the queueing happened. And in this case, the entry for
Pk is dequeued and a reply message is sent to Pk, meaning that Pi now has voted
for Pk to enter the critical situation. And so
Pi sets its voted variable to be true. So why does this algorithm
guarantee safety? Well, when a process Pi receives replies
from all its voting set members Vi including itself, no other process
Pj could have received replies from all its voting set members Vj. Because Vj would've had intersection
with Vi in at least one process Pk. And Pk could have sent only one reply or
vote at a time. And it always send a vote to Pi, which
means that it could not have voted for Pj as well. And so this means that safety is
guaranteed by the Maekawa Algorithm. For liveness, a process needs to wait for at most N-1 other process to
finish the critical section. And you might think this
guarantees liveness. However, Maekawa's Algorithm has
a subtle behavior in its original form that can actually violate liveness
because it can result in a deadlock. Here is an example of a deadlock. Again, another example of four process P1,
P2, P3, P4. Suppose all the four processes request
access to the critical section. P1 gets some replies but
is waiting for P3's reply. P3, in turn, is waiting for P4's reply,
which is in its voting set. P4 is waiting for P2's reply and P2,
in turn, is waiting for P1's reply. Now, we've complete a cycle or
a circle among these processes, and this is called a deadlock. There is not going to be any
more progress in the system, because these processes are going to
be waiting for these replies forever. So the original Ricart-Agrawala Algorithm
as we've discussed is deadlock prone and these deadlocks can occur. There are of course variance of Maekawa's
Algorithms that have been published that address this issue and
that are free from deadlocks. Returning to original Maekawa's Algorithm,
let's analyze its performance. The bandwidth involved in entering
the critical section is square root of N messages that you send out
to your voting set members. And then square root of N replies so
you see back, so that's 2 times the square
root of N messages. For exit operation you're simply sending
a reply message to all your votings and members, that's just
square root of N messages. These numbers are better than Ricart and Agrawala's Algorithms which
had bandwidths of order N. You might think square root
of N is still a large number. It's not constant for sure,
but it can be fairly small. So if N is a million for instance, then the square root of N value is about
1,000, which is a fairly small number. What about the delays? Well, for the client delay, when no one
has access to the critical section, a process comes up and says hey,
I need access to the critical section. It sends out a request to all
of its voting set members, that's one message transmission because
all these messages are in parallel. And then the responses are received back
also in parallel that's another message latency in the backwards direction. So that's one round trip time. Synchronization delay means that one
process is currently in the critical section, and
one of the processes is waiting to get in. And at this point of time, the releasing
process will send a reply message back to the process Pk, which is the common
process between the two voting sets of the releasing and the waiting process. And then that Pk process which
isn't common will forward a vote to the waiting process which can
now enter the critical section. So that's two message transmission times. One from the releasing process to
the common intersection voting member, and from the voting member
to awaiting process. So why is the square root
of N the right size for the voting sets in Maekawa's Algorithm? Once again, each voting set is of size K, each
process belongs to M other voting sets. Now, the total number of voting
set members is K times N, because each of the N processes
has K members in its voting set. And so, K times N is the total
number of voting set members. Of course because
the voting sets overlap and intersect members or processes
maybe repeated in this K times N. But each process belongs to exactly M
voting sets, so K times N divided by M should be equal to N, because each process
appears exactly M times in this K times N. So K*N/M = N. And if you evaluate this by canceling N
out on both sides you get that K = M. Which means that the sides of
the voting set should equal the number of voting sets that each process is in. Okay, so let's have that equation and
hold it to the side. Now, consider a process Pi. Right, so the number of voting
sets that are there in the system is equal to a Pi's own voting sets so
that's the +1 over here. There are K members in Pi's voting set,
right, that K processes. And each of those processes
has their own voting sets. Right, so that's the total number of
voting sets that is there in the system. Because each of this is a K voting
set member of Pi's is involved in M total voting sets. But one of them is Pi's own voting set. So the remaining voting
sets are simply (M-1)*K. Okay, so that's the total number of
voting sets present in the system. However, the number of voting sets
should equal the number of processes in the system, so
we have N equaling this value. Now, we substitute in the value of M
equals K from the earlier equation, and you get N = (K-1) *K + 1. Solving this you will see that K equals
about a square root of N give or take a little bit. And this explains why K equals M equals
square root of N is the optimal value for minimizing the overhead of K. So in order to minimize K,
we set N = (M-1)*K + 1. And then we use the earlier equation,
K = M, to give us a K = square root of N. Now, the Maekawa's Algorithm of
course does not handle failures. Neither does the ring-based or
the centralized algorithm or the Ricart-Agrawala Algorithm. Of course, there are fault-tolerant
versions of all of these algorithms that exist out there in the literature. Other ways to handle failures include
Paxos-like approaches to handle failures. So Google system called Chubby,
which is used for unlocking is a fairly popular
way to handle failures. To handle failures while doing mutual
exclusion inside of Google's stack. So Chubby uses a system used underneath
Google's storage system such as BigTable and Megastore. Chubby is not been open-sourced but
the technical details and the design of Chubby has been
published in a paper by Google. And that's what we're going to
discuss in very brief detail in this slide and the next. Chubby provides only Advisory locks,
this means that clients must ensure that the access locks before they access the
critical resource, or the object itself. So if clients forget to access the log, then hey,
then mutual exclusion may be violated. So this is why this is
known as Advisory locks. So Chubby, of course,
uses a cluster of servers, and there are five servers by
default in the Chubby cell. One of the servers is marked as Master. Again, this is elected using one of
the Leader Election Protocol that we send you before. In this particular figure,
Server D is a Master. Chubby allows clients
to not only do locking, but also writes small configuration files. And Chubby relies on the Paxos
consensus algorithm. Chubby again, is a group of servers,
as one elected as the Master, the other servers in the group,
the non-master servers are just slaves. They replicate the same
information as the Master. When a client wants to read one of
these small configuration files on the lock file, it sends a read request
to the Master which can serve it locally. Okay, so
the Master serves all the request locally. When a client wants to write, however,
it sends a write request to the Master, which then forwards it to all
these servers in the group. It then gets a majority of them
to respond back to the Master. When a majority of them respond back,
you reach a quorum in the system. Then the Master can send back a response
to the client acknowledging that the write has been done. And so, this is where mutual
exclusion comes into play. If some other client has already got
an access to the critical section, it means that it has access, it has permissions from at least
a quorum of the servers via the Master. And the next request that goes to
the Master will not reach a quorum, and it will wait until that first
process exits its critical section. Now, you can have failures here. If you have failures at the Master,
and the Master fails, then you simply rerun the election
protocol to elect a new master. If the replica fails you simply replace
it, or it reboots by itself, and then have the new replica catch up with
the other servers on the group, or with the Master itself. So Chubby present say fought in way of not
just doing mutual exclusion in the system, but also to maintain
small configuration files which reflects the ways in which Chubby
is used inside of Google stacks. Now being upon discussion
mutual inclusion, it is a very important problem
in cloud computing systems. There are a variety of
classical algorithms. We've discussed four. The Central, the Ring-based,
the Ricart-Agrawala Algorithm and the Maekawa Algorithm. They are not all fault-tolerant but they are fairly efficient and they all
try to guarantee safety and liveness. And as we progress down
from Central to Maekawa, the algorithms have gotten better and
better in terms of performance. Industry uses a variety of systems for
coordination and for mutual exclusion, these include
Chubby at Google which is used for locking and also to maintain
small configuration files. And also Apache Zookeeper which is
an open-sourced system that is used for coordination, and I encourage you to
look up Apache Zookeeper on the web. [MUSIC]

## Quizzes and assignments

### Part 2 Quiz 1

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/TEDtN/part-2-quiz-1
- Item type: staffGraded
- Grading status: NOT_STARTED

## Questions

_No submitted attempt found, so Coursera returned no questions or feedback._
