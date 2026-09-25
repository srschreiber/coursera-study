# Week 05 - Week 5 Key-Value Stores, Time, and Ordering

Contents: 4 readings, 13 lectures, 2 quizzes/assignments.

## Readings

### Week 5 Overview

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

### Optional Lamport Timestamps (Ukulele Version)

- Coursera: https://www.coursera.org/learn/cs-425/supplement/ZyNjA/optional-lamport-timestamps-ukulele-version
- Lesson: Interview

Here is a link to the optional ukulele version of [timestamps](https://www.youtube.com/watch?v=dG2wmdkkeY0).

### Part 1 Quiz 4 Instructions

- Coursera: https://www.coursera.org/learn/cs-425/supplement/sVvAf/part-1-quiz-4-instructions
- Lesson: Quiz

**Topics: **Key-Value Stores, Time and Ordering

## Instructions

-

 The quiz must be done individually.
-

 You can use any of the course resources, the course staff, or the Pizza forum to complete this assignment.
-

 However, when using the Piazza forum, you cannot post solutions on it! You can only use it to discuss ideas and concepts.
-

 For multiple choice, please note whether the question says there are MULTIPLE correct answers. For questions with MULTIPLE answers, you must specify ALL the correct answers and no wrong answers.

## Evaluation

Each quiz question is worth 1 point in Coursera. But the point value will be scaled down to 0.25 pts per question to calculate the grade of the quiz in this course.

## Important Dates

For deadline, refer to Course Deadlines, Late Policy and Academic Calendar page.

### Homework 2 & Solutions

- Coursera: https://www.coursera.org/learn/cs-425/supplement/zuZoT/homework-2-solutions
- Lesson: Homework

link to HW 2 solutions will be posted here:

[https://courses.grainger.illinois.edu/cs425/fa2026/assignments.html](https://courses.grainger.illinois.edu/cs425/fa2026/assignments.html)

## Lectures

### 01 - Week 5 Introduction

#### Transcript

[MUSIC] This week, we first start off
by discussing Key-value and NoSQL Storage Systems which are very
important component of today's cloud computing systems. This new generation of
cloud storage systems, NoSQL Systems is quickly replacing
the traditional relation of databases. We'll see how these new systems
are different from traditional databases, we'll see how these new
systems are designed. We'll see the insides of these
systems in an under the hood look and we'll also see apache Cassandra and
hBase in detail. These are two of the systems
that are very popular, in fact probably the most popular most
sequence storage systems in use today. We've also seen many of the building
blocks that you have seen so far, including gossip and
membership come together and be used in a real system as we
study systems like Cassandra. That's the first focus of this week. Later on in this week, we will start
a topic called Time and Ordering. Why we study this topic is
the distributed systems, as I've mentioned before very early in
the course need to deal with time or rather the lack of synchronization
among servers and clients. Remember that one of the characteristics
of a distributed system when we defined it was asynchrony which means that servers
and clients are each running their own clock and these clocks are not
synchronized with each other. They show different times and
they're running at different rates. So we'll first see techniques to
synchronize the clocks of these servers and clients with each
of the time synchronization. Then we'll see techniques to assign time
stamps to events that does not need time synchronization. And these logical time
stamps are a very important core concept in distributed systems
that are used in today's cloud systems, that have been used for
many decades in this distributed systems. And it will continue to be used in future
generations of distributed systems. So this topic of Time and
Ordering also marks the beginning of our deep dive into theoretical concepts that
underlie cloud and distributed systems. And these are very important concepts. [MUSIC]

### 02 - 1.1. Why Key-ValueNOSQL

Slides: `C3_Key-valueStores_A_CSRAfinal.pdf`

#### Slide text

```
•   (Business) Key  Value
•   (twitter.com) Tweet id  information about tweet
•   (amazon.com) Item number  information about
    it
•   (kayak.com) Flight number  information about
    flight, e.g., availability
•   (yourbank.com) Account number  information
    about it

•   It’s a dictionary datastructure.
      • Insert, lookup, and delete by key
      • E.g., hash table, binary tree
•   But distributed
•   Sound familiar? Remember distributed hash
    tables (DHT) in P2P systems?
•   It’s not surprising that key-value stores reuse
    many techniques from DHTs.

•   Yes, sort of
•   Relational Database Management Systems
    (RDBMSs) have been around for ages
•   MySQL is the most popular among them
•   Data stored in tables
•   Schema-based, i.e., structured tables
•   Each row (data item) in a table has a primary key
    that is unique within that table
•   Queried using SQL (Structured Query Language)
•   Supports joins

      users table
user_id     name          zipcode   blog_url               blog_id

101         Alice         12345     alice.net              1         Example SQL queries
                                                                     1. SELECT zipcode
422         Charlie       45783     charlie.com            3            FROM users
                                                                        WHERE name = “Bob”
555         Bob           99910     bob.blogspot.com       2
                                                                     2.   SELECT url
                                                                          FROM blog
Primary keys                                       Foreign keys           WHERE id = 3

                                                                     3.   SELECT users.zipcode, blog.num_posts
                                                                          FROM users JOIN blog
      blog table                                                          ON users.blog_url = blog.url
id          url                     last_updated           num_posts

1           alice.net               5/2/14                 332

2           bob.blogspot.com        4/2/13                 10003

3           charlie.com             6/15/14                7

•   Data: Large and unstructured
•   Lots of random reads and writes
•   Sometimes write-heavy
•   Foreign keys rarely needed
•   Joins infrequent

•   Speed
•   Avoid Single Point of Failure (SPOF)
•   Low TCO (Total cost of operation)
•   Fewer system administrators
•   Incremental scalability
•   Scale out, not up
     • What?

•   Scale up = grow your cluster capacity by replacing with
    more powerful machines
     • Traditional approach
     • Not cost-effective, as you’re buying above the sweet
         spot on the price curve
     • And you need to replace machines often
•   Scale out = incrementally grow your cluster capacity by
    adding more COTS machines (Components Off the Shelf)
     • Cheaper
     • Over a long duration, phase in a few newer (faster)
         machines as you phase out a few older machines
     • Used by most companies who run datacenters and
         clouds today

•   NoSQL = “Not Only SQL”
•   Necessary API operations: get(key) and put(key, value)
     • And some extended operations, e.g., “CQL” in
        Cassandra key-value store

•   Tables
     • “Column families” in Cassandra, “Table” in HBase,
         “Collection” in MongoDB
     • Like RDBMS tables, but …
     • May be unstructured: May not have schemas
           • Some columns may be missing from some rows
     • Don’t always support joins or have foreign keys
     • Can have index tables, just like RDBMSs

                                                     Value
                        Key
•   Unstructured              users table
                        user_id         name      zipcode      blog_url
•   No schema           101             Alice     12345        alice.net
    imposed
                        422             Charlie                charlie.com

                        555                       99910     bob.blogspot.com
•   Columns
    missing from                                              Value
    some rows      Key

                          blog table
•   No foreign     id             url                       last_updated       num_posts
    keys, joins
                   1              alice.net                 5/2/14             332
    may not be
    supported      2              bob.blogspot.com                             10003

                   3              charlie.com               6/15/14

NoSQL systems often use column-oriented storage
• RDBMSs store an entire row together (on disk or at a
   server)
• NoSQL systems typically store a column together (or a
   group of columns).
    • Entries within a column are indexed and easy to
        locate, given a key (and vice-versa)
• Why useful?
    • Range searches within a column are fast since you
        don’t need to fetch the entire database
    • E.g., get me all the blog_ids from the blog table that
        were updated within the past month
           • Search in the the last_updated column, fetch
             corresponding blog_id column
           • Don’t need to fetch the other columns

Design of a real key-value store, Cassandra.
```

#### Transcript

[MUSIC] Hi there. In this next series of lectures we'll
be looking at at the new generation of storage systems called key value
stores and NOSQL storage systems. We'll see the overall concept and
then we'll see in detail. The architecture of two different
systems that fall in this pace. So what is the key-value store? What kind of an abstraction
does it really provide? essentially, key-value stores
map a key to a given value. For instance if you're
a company like Twitter.com. Where you receive millions of
tweets from millions of users. You are making a key-value store where, the key comma value pairs
have the key as the tweet ID. So every id in twitter has a unique ID,
the tweet ID. And the value associated with that tweet
ID is information about that tweet, such as the 140 characters
of the tweet itself. Who tweeted it what time was it tweeted
and any links that it might contain. A different retailer, online retailer like
Amazon, might maintain key value pairs where the key is the item number and
the value is information about the item. For instance, who's selling it how
many copies of the item are left. What are the recommendations for
the item, and so on and so forth. An online booking agent like
Kayak might maintain a key value store where the flight number is mapped
to information about that flight. For instance,
how many seats are left in that flight. And of course a lot of banks and financial
institutions map your account number. The information about the account,
such as the balance, or the user ID and so on and so forth. So essentially, key value pairs are used
by a variety of businesses to map essential an important keys to values. However if you know your computer science,
you might be saying, well, that's just a dictionary data structure,
right? So, it's a data structure where you can
insert, look up, and delete by key. For instance, this is provided by
the hash table or by the binary tree. However, here because of the sheer
amounts of data that are involved, imagine the billions of tweets
that are maintained by Twitter, all of which need to be maintained. You can't maintain all of that on
a single server where you have a single process running the strict,
dictionary data structure. Instead, you need to maintain this data
on a distributed cluster of servers. So essentially, you need to
build a distributor hash table. And this should start to
look familiar to you. We have already discussed distributed hash
tables when we discussed peer to peer systems, and it's not a surprise
that as a result the new generation of key values towards the no
sequence storage systems actually reuse a lot of the design decisions from DHT
that we studied in peer to peer system. This will become evident as we go along. Also you might be wondering well
isn't that just a database. A database maintains large amounts of data
and the data can be queried it can be looked up and
it can be especially queried as well. And in fact relational
database management systems or RDBMSs, have been around for
ages, for many decades. And one of the more popular
ones among them is MySQL. In these database systems,
data is stored in tables. These are structured tables so every
table has a structured schema meaning it specifies which columns
are present in that table. And each show,
that is each data item in the table, has a primary key which is
unique in that table and that key can be used to look up
that particular item in the table. The structured query language or SQL or
SQL, is used to query such relational database tables, and relational database
tables often support joins as well. So let's see an example of
a relational database table. Here is an example of relational database
with just one table to start with. It's called the users table. The users table has a primary key,
called the user ID,. The primary key has to be
unique across all the rows. It also has multiple columns, in this case
name, the zip code, the blog_url, and the blog_ID that is
maintained by that user. For instance the second row over
here has a unique user ID 422, and then the name of user is Charlie,
the zip code is 45753 and the blog URL is charlie.com then
the blog ID is 3 in this case. There might be a second table
present here called the blog table. The blog table again has a primary key
which is the ID of the blog itself. Then it also has columns URL,
when it was last updated, and the number of posts to that blog. Now, in relational databases,
there are also foreign keys. A foreign key in a table like users refers
to a primary key in a different table, like the blog. For instance, the second row
again here has a blog ID of 3. This is a foreign key that
refers to the primary key of 3 over here in the blog table. And essentially the foreign
keys are used to look up the entries quickly in the other tables. So what kinds of queries can you do on
collections of tables such as this? Well, you can do simple select
queries where for instance, you select from the zip code. sorry, you select from the users table. The zip code of all
the users whose name is Bob. So in this case, the answer will
just be one item, would be 99910. But if there were multiple users
named Bob in the users table, it would return all of
their zip codes as one. Has a list essentially or a table. You can also select from the second
table all the URLs where the ID equals 3 this would just return one entry
because after all ID is the primary key. You can also do joins on the tables,
for instance you can join the user's table with the blog table,
over here so you say from users join blog. And essentially this calculates
a cross product of all the entries in the users table with the entries in
the blog table, and it retains only those where the users dot blog URL the blog URL
column over here in the first table entry. Is the same as the URL entry,
this URL entry, in the second table. So if those two match,
then it returns a zip code and the number of posts for that particular
combination in the cross product. So this is what is called a join in SQL. And there, again,
many different kinds of joins. We just covered one particular
kind of join over here, but there are many variants of joins. So that's a relational database. And it's been around for very long. And it supports fairly
expressive SQL queries. So why not just use this for
our new workloads? Well, unfortunately, the workloads that
exist today in the world of Twitter and Facebook and Google. Are sort of a mismatch with
the relation databases. So the data here is large, and
it's often unstructured, which means that it's often hard to come up with schemas,
into which the data can be fit. If you select a schema for a table,
you might soon come across key value pairs that don't necessarily fit that schema
which may have extra columns in there. Also, the workload involved here,
involves a lot of reads and writes coming from multiple clients,
millions of clients in some cases. And this is not necessarily a good
match with relation databases. A lot of these workloads are write-heavy, meaning that there are a lot
more writes compared to reads. And relational databases are typically
optimized for read-heavy workloads. A foreign key as we saw in the previous
slide are not not needed that often in todays workloads. And in fact joins are not needed
that often in todays workloads. Which means that we could
potentially come up with a sort of watered down simpler relation database
not even relation just a database. Which is much faster as a result. And that's essentially what happens
in this, what has happened in this new generation of key value stores
and those equal storage systems. So what are the needs
of today's workloads? Well first of all you needs speed,
essentially you won't want users to go away from your system just
because the system is slow, and it returns queries very quickly. for instance Netflix runs
a key value store, and if Netflix was slow,
you just wouldn't use it. You would use a competing,
a competing product. You'd also want to use you also want to
avoid a single point of failure, which means that you don't want the failure of
one or a few servers in your system, to lead to loss of data or to unavailability
of data for reads and writes. You want to minimize the TC or
the total cost of operation also known as total cost
of ownership of your infrastructure. This is again for the provider
side of companies like Twitter or Netflix which might be running key
value stores rather than the customers. So the companies like Netflix and Twitter they really want to minimize how
much money they're spending in running the infrastructure,
in running the key value store. And part of this is using
fewer system administrators to administer the service itself. And then you also want
incremental scalability. You want to grow your system based
on the load as smoothly as possible, and you want to scale out, not scale up. Let's look a little bit at
what this really means. Scale up is the ability to
grow your cluster capacity by replacing your existing machines
with more powerful machines. Machines that have more CPU, more memory,
more disk, faster memory busses and faster busses in general. This has traditionally
been the approach for for scaling relation databases,
for instance. However, this is not really cost-effective
as typically you are buying fairly powerful machines that are above
the price curve's sweet spot. And of course as the technology
grows very quickly you need to replace your
machines fairly often. Scale out, on the other hand, which is preferred by the new
generation of systems, helps you to incrementally grow your cluster by
adding more off the shelf machines, or what is known as COTS machines or
Components Off the Shelf machines. Essentially, you buy workstations or
servers that are available on the sweet spot in the price curve right now and
you simply add them to your cluster. This obviously is cheaper. And over long duration, you can choose to phase out the very old
machines in your cluster, while replacing them with the current sweet spot machines
that are available off the shelf. So essentially you have a collection
of machines that are not the most powerful that you can buy today but
of course are not too wimpy, either. But somewhere in the middle of the,
of the price curve. But you can add machines very easily and also removed machines
very easily if you want. And this is the approach for scale out
approach that is used by most companies in today's Cloud computing environment. Just because it's cost effective and
it's also easier to manage a larger cluster of off the shelf machines
than it is to manage a few very powerful, very specialized machines. So what does NoSQL really stand for? NoSQL does not stand for no SQL. It sta, actually stands for Not Only SQL. The name is a little bit a bit
of of a misnomer for this area. Essentially, NoSQL and key-values stores
support are two necessary API operations. They are get, by a key, and
put, by key or a value. This either creates a key, value pair of
updates the value for an existing key. There are also other
operations that are supported. For instance in the Cassandra
key-value store. The Cassandra Query Language
also in a CQL. This is different from Sequel or SQL. Which traditionally has no support. The CQL language supports a small set
off extended operations that are more powerful than just get or put. But are not as powerful
as the SQL language. So what are the concepts in these
key values store and NoSQL, systems? So first of all these new systems maintain
tables just like relation database tables, but the tables have different names. For instance in Cassandra the tables
are called column families. Essentially they are a group of columns
that share something in common. In age base the tables are called tables. In MongoDB,
the tables are called collections. These are just like relation database
tables, but they have a few differences. The tables may be
unstructured to start with. In other words, they may not have schemas. Some columns may be
missing from some rows. Some columns may be missing altogether. They don't always support joins or have foreign keys across tables,
like relation database tables. But like relation database tables,
they can have index tables, as well. So here is what a key value in NoSQL
system would look like for our data model. For this new data model. So once again, here I have
a users table and a blog table. You do have tables and
the users table has a key. So each row has a key and
the key in this case is just a user id. Again, that has to be unique and the value is essentially the rest
of the columns in that table. Similarly the blog table has
a key which is a blog id and the value is the rest of
the columns in the table. Unlike relationary based tables,
these tables are unstructured. This means that there's no schema imposed,
some items may be missing. For instance, the row for 422 named
Charlie does not have a zip code in it, and that's fine for
a key-value in NoSQL stores. Also, some entire columns may be missing
over here, and that's fine, too. You can add columns for particular rows, they don't need to be present in all the
other rows and that's optional as well. Again, there are no foreign keys and the
joins may not be supported in the systems just because the workloads don't
necessarily need foreign keys or joins. These new generation systems also
use column-oriented storage. So relation databases store an entire row together at a disk on a disk or
or at a server. This means that the entire key on all
the columns associated with that key are stored together. A no sequence storage systems
instead store a column together, which means that in the previous
slide the blog ID column might be or URL column might be stored as,
as one, in one place. And the user name column might be
stored as as one in a separate place. Well, why do you use
column-oriented storage? well, first of all,
entries within the column are indexed and easy to locate given the key,
and also vice versa. So you can find out which is the URL column that corresponds to
the user Charlie, for instance. But again, why do you do this? Well, you do this because
then searches that use one or more columns are easier to do and
more efficient, and they can be done by fetching only a part of the table
rather than fetching the entire table. So for instance,
if you want to get all the blog ids from the blog table that were
updated within the past month,. In the relation database approach where
you store the entire row essentially you have to refresh the entire
table all the rows and then look at the corresponding
column in each row. In the, in the NoSQL in the column
one data storage example you simply look at the last updated column. You fetch only that column. And then for the entries in the column
that match, which are within the past month, you fetch the corresponding
entries in the block ID column. Okay, so you don't need to fetch any of
the other columns at all that are present in the other table. Only these two columns are sufficient, and that means that you're incurring
less of an I/O overhead. And your query's going to be much,
much faster. So next in the next lecture, we'll be looking at the design of a real
key-value store Apache Cassandra, which is one of the most popular key value storers
that is being used in industry today. [MUSIC]

### 03 - 1.2. Cassandra

Slides: `C3_Key-valueStores_B_CSRAfinal.pdf`

#### Slide text

```
•   A distributed key-value store
•   Intended to run in a datacenter (and also across DCs)
•   Originally designed at Facebook
•   Open-sourced later, today an Apache project
•   Some of the companies that use Cassandra in their
    production clusters
     • IBM, Adobe, HP, eBay, Ericsson, Symantec
     • Twitter, Spotify
     • PBS Kids
     • Netflix: uses Cassandra to keep track of your
         current position in the video you’re watching

•   How do you decide which server(s) a key-value
    resides on?

                                                                   One ring per DC
Say m=7                                   0
                     N112                               N16
(Remember this?)
                                                             Primary replica for
                   N96                                       key K13

  Read/write K13                                             N32

                         N80                           N45
   Client                Coordinator
                                                           Backup replicas for
                                                           key K13
  Cassandra uses a ring-based DHT but without finger tables or routing
              Keyserver mapping is the “Partitioner”

•   Replication Strategy: two options:
    1. SimpleStrategy
    2. NetworkTopologyStrategy
1. SimpleStrategy: uses the Partitioner, of which there are two kinds
    1. RandomPartitioner: Chord-like hash partitioning
    2. ByteOrderedPartitioner: Assigns ranges of keys to servers.
              • Easier for range queries (e.g., get me all twitter users starting
                 with [a-b])
2. NetworkTopologyStrategy: for multi-DC deployments
      •   Two replicas per DC
      •   Three replicas per DC
      •   Per DC
              • First replica placed according to Partitioner
              • Then go clockwise around ring until you hit a different rack

•   Maps: IPs to racks and DCs. Configured in cassandra.yaml
    config file
•   Some options:
     • SimpleSnitch: Unaware of Topology (Rack-unaware)
     • RackInferring: Assumes topology of network by
         octet of server’s IP address
           • 101.201.301.401 = x.<DC octet>.<rack
                octet>.<node octet>
     • PropertyFileSnitch: uses a config file
     • EC2Snitch: uses EC2
           • EC2 Region = DC
           • Availability zone = rack
•   Other snitch options available

•   Need to be lock-free and fast (no reads or disk seeks)
•   Client sends write to one coordinator node in
    Cassandra cluster
     • Coordinator may be per-key, per-client, or per-
         query
     • Per-key Coordinator ensures writes for the key
         are serialized
•   Coordinator uses Partitioner to send query to all
    replica nodes responsible for key
•   When X replicas respond, coordinator returns an
    acknowledgement to the client
     • X? We’ll see later.

•   Always writable: Hinted Handoff mechanism
     • If any replica is down, the coordinator writes to
        all other replicas, and keeps the write locally
        until down replica comes back up.
     • When all replicas are down, the Coordinator
        (front end) buffers writes (for up to a few hours).
•   One ring per datacenter
     • Per-DC coordinator elected to coordinate with
        other DCs
     • Election done via Zookeeper, which runs a
        Paxos (consensus) variant
          • Paxos: elsewhere in this course

On receiving a write
1. Log it in disk commit log (for failure recovery)
2. Make changes to appropriate memtables
      • Memtable = In-memory representation of multiple key-
           value pairs
      • Cache that can be searched by key
      • Write-back cache as opposed to write-through

Later, when memtable is full or old, flush to disk
       • Data file: An SSTable (Sorted String Table) – list of
          key-value pairs, sorted by key
       • Index file: An SSTable of (key, position in data sstable)
          pairs
       • And a Bloom filter (for efficient search) – next slide

  •     Compact way of representing a set of items
  •     Checking for existence in set is cheap
  •     Some probability of false positives: an item not in set may
        check true as being in set
  •     Never false negatives
                                            Large Bit Map
                                                            0
                                                            1     On insert, set all hashed
                                                                  bits.
                                                            2
                                                            3     On check-if-present,
            Hash1
                                                                  return true if all hashed
Key-K                                                             bits set.
            Hash2                                                 • False positives
              .                                             6
              .                                             9     False positive rate low
             Hashk                                                • k=4 hash functions
                                                            111   • 100 items
                                                                  • 3200 bits
                                                                  • FP rate = 0.02%
                                                            127

Data updates accumulate over time and SStables and
logs need to be compacted
     • The process of compaction merges
        SSTables, i.e., by merging updates for a key
     • Run periodically and locally at each server

Delete: don’t delete item right away
    • Add a tombstone to the log
    • Eventually, when compaction encounters
        tombstone it will delete item

Read: Similar to writes, except
      • Coordinator can contact X replicas (e.g., in same rack)
            • Coordinator sends read to replicas that have
                responded quickest in past
            • When X replicas respond, coordinator returns the
                latest-timestamped value from among those X
            • (X? We’ll see later.)
      • Coordinator also fetches value from other replicas
            • Checks consistency in the background, initiating a
                read repair if any two values are different
            • This mechanism seeks to eventually bring all replicas
                up to date
      • A row may be split across multiple SSTables => reads need
         to touch multiple SSTables => reads slower than writes
         (but still fast)

•   Any server in cluster could be the coordinator
•   So every server needs to maintain a list of all the
    other servers that are currently in the server
•   List needs to be updated automatically as servers
    join, leave, and fail

Cassandra uses gossip-based cluster membership                    1    10118    64
                                                                  2    10110    64

                1   10120     66                                  3    10090    58

                2   10103     62                                  4    10111    65

                3   10098     63                            2
                4   10111     65                1
    Address        Time (local)                                    1   10120       70

       Heartbeat Counter                                           2   10110       64
                                                                   3   10098       70
    Protocol:
    •Nodes periodically gossip their
                                                        4          4   10111       65

    membership list                                 3
    •On receipt, the local membership list is
                                                        Current time : 70 at node 2
    updated, as shown                                   (asynchronous clocks)
    •If any heartbeat older than Tfail, node
    is marked as failed                                         (Remember this?)

•   Suspicion mechanisms to adaptively set the timeout based
    on underlying network and failure behavior
•   Accrual detector: Failure detector outputs a value (PHI)
    representing suspicion
•   Apps set an appropriate threshold
•   PHI calculation for a member
      • Inter-arrival times for gossip messages
      • PHI(t) =
            – log(CDF or Probability(t_now – t_last))/log 10
      • PHI basically determines the detection timeout, but
         takes into account historical inter-arrival time
         variations for gossiped heartbeats
•   In practice, PHI = 5 => 10-15 sec detection time

•   MySQL is one of the most popular (and has been for
    a while)
•   On > 50 GB data
•   MySQL
     • Writes 300 ms avg
     • Reads 350 ms avg
•   Cassandra
     • Writes 0.12 ms avg
     • Reads 15 ms avg
•   Orders of magnitude faster
•   What’s the catch? What did we lose?
```

#### Transcript

So in this lecture, we'll be looking at the design details of Apache Cassandra. So Apache Cassandra is a distributed key-value store intended to run in a data center and also across multiple data centers. Originally it designed as Facebook as an infrastructure for their messaging platform. However later, they decided to open source it. And today it's one of the most active Apache projects. A lot of companies use Apache Cassandra in their production clusters for a variety of different applications. These include blue chip companies such as IBM, Adobe, Hewlett-Packard, eBay, Ericsson, Symantec. Also newer companies such as Twitter and Spotify use Cassandra. Nonprofits such as PBS Kids use it. And if you've ever used Netflix, you've actually indirectly used Cassandra. Essentially, Netflix uses Cassandra to keep track of positions in the video. So, wherever you are in a particular video is kept track of in Cassandra. So that, if you pause the video, or if you stop it and then later resume, the Cassandra key-value store is used to fetch your latest scene position. So let's go inside the design of Cassandra itself. So the first question that has to be addressed about the design is given a key-value pair, how do you map the key to a server? How do you know which server stores that particular key-value pair? Well, it turns out that because key-value stores are similar to distributed hash tables, Cassandra uses the ring that we saw in distributed hash table. So you might remember this one from when we discussed peer-to-peer systems. Essentially, Cassandra places servers in a virtual ring. Again, the ring here consists of two power endpoints. And here, it's seven, so it's 120 endpoints. And the server is placed to the point in the ring. And essentially, then, you map the keys and the points in the ring. And the key get stored at servers that are successors to its point on the ring. So for instance, key with an ID of 13, which maps for 13, would get stored at servers 16, and also 32, and also 45. One of these might be the primary replica. One of these, the others might be backup replicas. As far as Cassandra is concerned, it doesn't necessarily need to have primary backup replicas, or need to know the initial primary or backup replicas, it just knows them as replicas. The client sends its queries to one of the servers in the system. It need not be one of the replicas, the server is called the coordinator. And again, the coordinator need not be on a per data center basis. It could be on a per client basis, on a per query basis, it doesn't really matter. There's also one ring present per data center. So if you have Cassandra running in two different data centers, each of those data centers would be using a separate ring with its own servers mapped to that ring. What is not present in Cassandra which was present in a distributed hash table like Chord, when we discussed it, is the notion of finger tables, or routing tables. So there's no routing used in Cassandra here. Instead, when the client sends a query to the coordinator, the coordinator simply forwards a query to the appropriate replicas or just some of the replicas, and for that particular key. This means that every server, which could be the coordinator, needs to know about where the keys are stored on every other server in the system. We'll come back to this later on, we'll discuss later on how servers know about each other. But for now, let's focus on the key to server mapping. So the mapping from key to server is called the "Partitioner" and that is what is used by the coordinator here to find out which are the replica servers to forward a particular query for Key13 to. So, there are different kinds of replication strategies. There are two main classes that are supported by Cassandra. They are the SimpleStrategy and the NetworkTopologyStrategy. The SimpleStrategy uses the partitioner, and there are two kinds of partitioners. The RandomPartioner uses hash-based partitioning just like Chord. So essentially, this is the version of Cassandra that is most similar to Chord where essentially keys are hashed to a point in the ring. And then are stored at servers that are close to that point of the ring, or are assigned to that segment in the ring itself. So for instance, if you assign to each server, the segment in the ring that is between that servers point in the ring, and its predecessor, then this becomes more similar to the Chord hash-based partitioning. There's also ByteOrderedPartitioner, which assigns ranges of keys to servers. You may want to maintain a table in Cassandra that preserves the ordering of the keys in there. For instance, the keys might be timestamps, and you might want to maintain the ordering of the timestamps. And this does not hash the keys, instead it simply maps the key on to a point in the ring based on the value of the key itself. So that two keys that are in order in the real space are also in the same order in the ring space itself. This is useful for range query. For instance, if you want to get all the Twitter users starting with A or B, then you can do a range query very easily, if you're using a ByteOrderedPartitioner by simply searching for the servers that will be storing that particular range of keys. If you are using the hash-based partitioning instead, you'd essentially have to ask every single server in that particular ring to see if the server has any key-value, key-value pairs that match this particular range. The NetworkTopologyStrategy is a different strategy which is used for multi-data center deployments. It supports a variety of different configurations. It supports one configuration where you can have two replicas of each key per data center. So if you have three data centers, then you essentially have six replicas to each data center for each key. There's also different configurations, with just three replicas per data center. Now, how do you select replicas within each data center? So on a per data center basis, you first place the first replica according to the partitioner. Again, you can use a RandomPartitioner, or a ByteOrderedPartitioner here. And then for the next replica, you want to make sure that you are storing that second replica on a different rack. Why? Well, you don't want a rack failure within the data center to lose all copies of a given key. So you place the second copy of a key on a different rack. Essentially, you go around the ring clockwise, until you encountered the first server that is in a different rack from the primary, the first replica that you placed. And you place your key at that first server. So this ensures that there is rack fault tolerance, and it also ensures that there are two replicas in this particular case for that key for the data center. So, Cassandra uses a mechanism known as Snitches to map IP addresses to racks and data centers. You can configure this in the cassandra.yaml configuration file. Cassandra offers a variety of Snitch options and I'm going to discuss a few of those options here. And the first option is a SimpleSnitch, which is unaware of the topology. In other words, your application really cannot know much about which IP addresses matter to which racks and which data centers. In some cases, this works for instance, if you're running only one VM, then you don't really want to Snitch and SimpleSnitch is fine. The second Snitch is the RackInferringSnitch which tries to guess from the IP address what the rack and the data center might be. Essentially, the IP address breaks up into four octets. And the first octet is ignored. The second octet is used to map to the data center. The third is used to map the rack, and the fourth is used to map to the node. So for instance, if I have an IP address that goes 101.102.103.104 then essentially 102 is the data center octet. So any other node that, any other IP address that starts with 101.102 will belong to the same data center as this particular IP address given over here. The third octet is the rack octet. So any other IP address that starts with 101.102.103, will belong to the same data center and rack as this IP address given here. And finally, the last octet 104, identifies the node. So, any other IP address that has exactly the same four octets shown over here, will be the same identical address namely with reference to the same IP address and server or VM as this particular IP address shown over here. And this of course is a best effort guess because IP addresses may not map actually to rack from data centers as shown over here. But not knowing anything else, this is a pretty reasonable guess. You can also, if you want to be really accurate about which IP addresses matter, which racks and data centers, if you actually know this information, you can create this in a property file and this is called a PropertyFileSnitch. And you write this into a configuration file. Finally, if you're running your Cassandra on EC2, EC2 of course uses regions and within regions that are availability zones. So the EC2 Snitch in Cassandra allows you to guess the rack and data center as the availability zone and the EC2 region respectively. And you can use this information then to do the Cassandra mapping. For instance, replication and also within the data center and across racks as we discussed previously, and also across data centers. There are a variety of other Snitch options available as well in Cassandra. If you're interested in this, please look at the Cassandra web pages. So how are writes and reads supported? So, remember that when a client sends a write to a coordinator, the coordinator needs to forward the write to one or more replicas for that particular key that is present in the query and the write itself. Writes need to be lock-free because we're dealing with write heavy workloads here, and they need to be fast. So you want to incur few disk reads are seeks. Preferably, no disk access at all for the write in the critical write path. So the client sends the write to one coordinator node in the Cassandra cluster. The coordinator again, maybe per-key, per-client, or per-query. If you have a per-key coordinator, this ensures that all the writes to that particular key are serialized why that coordinator. But again, this is not a requirement for Cassandra. The coordinator when it receives this write, uses the partitioner to find out which of the replicas that map to that particular key. It then, sends the query to all the replica nodes responsible for that particular key. Then, some of the replicas respond when X replicas respond, the coordinator returns an acknowledgement to the client that the write is done. What is this value of X? We'll see that later. For now, let's just assume that X is some small number specified by the client that is smaller, less than, or equal to the number of replicas for that particular key. So, keys always need to be writable. So you want to make sure that even if you have failures, the writes succeed, and return an acknowledgment to the client. So for this Cassandra use is what is known as a Hinted Handoff mechanism. This works as follows, if any replica is down, the coordinator writes to all the other replicas, but it also keeps a copy of the write locally, and when that down replica comes back up, it is then sent a copy of that write. This ensures that replicas when they fail and then recover, they receive from the coordinator some of the latest writes. However, all the replicas might be down, it's possible. It may be unlikely but it's possible that you have three replicas for the key, and when a write comes along, all the three replicas happened to have failed. In this case, instead of rejecting the write, the coordinator stores the write locally at itself. It buffers the writes. And then, when one or more of the replicas comes back up, it then release the writes to the corresponding replicas. The coordinator of course has a time on how long it stores these writes. Otherwise, it may be storing writes forever. And this time on is typically a few hours which is good enough for replicas to recover and rejoin the system. Again, this mechanism is known as Hinted Handoff because the coordinator based on the hints that it receives from the failure information it might assume the ownership of that key for just a temporary duration of time. So, if you have multiple data centers running, Cassandra, you maintain one ring per data center, and you might also use a per data center coordinator. This coordinator is different from the coordinator used by client queries. The per data center coordinator coordinates with the other per data center coordinators to make sure that the data center to data center coordination is done in a correct manner. The election of the per data center coordinator is done by a Zookeeper, which is a system again an open source Apache system which runs a variant of Paxos and we'll see Paxos later and elsewhere in this course. So, what does a replica server do when the coordinator forwards it write? Well, the first thing it does is that it logs information about the write. Just a little bit of information in a comment log that is present on disk. This is used for failure recovery, so that if the replica server fails at any point of time here on, it can know by looking at the disk log after it recovers that there were some write that it completed only partially and then it can ask the coordinator for information about this write. After this, the replica server updates memtable. A memtable has an in-memory representation of multiple key value pairs. Essentially, memtable maintains some of the latest key value pairs that have been written at this particular replica server. It's a cache that can be searched by key so you quickly search the particular key that you're trying to write. If it's present on the memtable you update the corresponding value, if it's not present in the memtable then you simply append to the memtable another key value pair. This memtable is called Write-back cache meaning that you are storing it temporarily and tentatively in memory rather than writing it directly to disk. If you were writing it directly to disk then it would be called write-through cache, and write-through caches that are much slower than write-back caches. However, the memtable has a maximum size and when this maximum size is reached,or when the memtable is very old then it is flushed to disk. Essentially, you create an SSTable or a Sorted String Table since you take the memtable and you sort all the keys within them so that the keys are sorted and the values are present alongside the keys as well, and then you store it on disk as an SSTable. Now, if you want to search for a particular key in the data file itself, in this data file that is the key value pairs it might take a long time because it consists of both the keys and the values so you maintain an index file as well, which stores an SSTable of (key, position in data SSTable) pairs so that you can quickly look up the position of a particular key in the data SSTable by looking at the index file SSTable itself. However, in most of the cases you might be checking for existence of a key in SSTable and the key is just not there. In this case, doing a binary search through the index file to look for that key would just result in a very large overhead. If you have a large number of SSTables essentially, each SSTable containing M entries then you're going to incur an order log M overhead per SSTable in trying to look for a particular key. And so what you do is you add a Bloom filter, which is a quick way of looking for whether or not a particular key is present in an SSTable. So a Bloom filter is a well-known data structure which Cassandra uses. So what is a Bloom filter? And what does it look like? Well, here's a Bloom filter, an example, a Bloom filter is a compact way of representing a set of items so that the most common operation which is checking for existence in that set becomes very cheap and becomes very low overhead. The most common operation for Bloom filter is you say well, is this particular key present in this particular set or not? The other operation that the Bloom filter supports is inserting an item into the Bloom filter. The Bloom filter has some probability of false positives, an item not in the set may be returned as true as being in the set and for the Cassandra example, this just results in a little bit of extra overhead when you look through the index file and then subsequently do not find that item. But you never have false negatives, which means that if you've inserted an item in the set you would always return true when that item is checked for the membership. So, how does a Bloom filter work? Well, a Bloom filter is essentially a very large bitmap. Here's an example of a Bloom filter, which has 128 bits shown as numbers 0-127. The bits are all, each of them has a number as an ID. Initially, all the bits are zero so the entire Bloom filter is zero. When you have a key say K you use a small set of hash functions one through small K to hash that Key-K. Each of these hashes returns a number between 0-127 both ends inclusive. For instance, hash1 applied on the Key-K returns a value 1. If you're trying to insert the Key-K, you're going to set that bit to be one over here. Again, hash2 when applied to the Key-K, returns a value of 69, and so if you are inserting the Key-K, you would set that bit number 69 to be a 1. Similarly, Hashk returns a of value of 111 and you set that bit to be one. So whenever you want to insert a particular key you set all the corresponding small key Hash values to be one's. If you insert a second key you would go ahead and set those corresponding bits that, that particular key maps to as one. If any of those bits is already one you leave it as one. So you can see that over time as many keys are inserted into the system a small set of bits in this particular Bloom filter are are set to one. Now, what happens when you want to check if a particular key is present in the Bloom filter or not. Well, once again you do the same thing you take the key, you hash it using the K hash functions and then check if all of these hash2 bits are all one's. If any of them is a zero then you return false saying this particular key is not present in the Bloom filter. And this is the correct answer because if that key had been inserted in the Bloom filter all those bits would have been one. If all those hash2 bits of this Key-K are set then you return a true saying that, that key is present in the Bloom filter. Well, this is not guaranteed to be correct. However, it is correct with a high probability. However, it's possible that this key was never inserted into the Bloom filter and that half of these bits were set by one other key and then the other half of the bits were set by a different key. And so you might end up returning an answer of true for membership even though that key was never inserted into the system. This is what is known as a false positive. However, the false positive rates can be tuned on to be very low. For instance, if you use 4 hash functions 100 items inserted into a Bloom filter with 3,200 bits that's just 3.2 kilobits. The false positive rate is as low as 0.02%. So 0.02% or 0.0002 of the membership checks will return an answer of 2 when the real answer is false. And you can tune the false positive rate to be much lower for instance, increasing the number of bits that are present in the Bloom filter itself. Coming back to Cassandra, over time a particular server might have a lot of SStables it had written to disk and given key might be present in multiple SStables. So whenever in a system is written to disk, you don't check the other SStables that are present on disk. So given key might be present in multiple SStables, so you will look out for a particular key, for instance, a "Read" comes in for a key you want to look up. You may need to look up multiple SStables and this is prudentially wasteful. So, in order to avoid this waste you do compactions. So over time you take the multiple SStables that are present on disk and you merge them essentially, you merge the updates for key a given key. So if a key is present into SStables, you take the latest update for that key and you replace the older update with that latest update. The compaction process is run periodically by each server and it is run locally on the SStables at that server. "Delete". When you want to delete a particular key value pair, you don't delete the item right away instead you "Write" to the log or to the SStable what is known as a "Tombstone." A tombstone is essentially a marker that says, "When you encounter this, please delete this particular key." Eventually, when the compaction algorithm runs, it encounters this tombstone and when it does so, it will delete the particular key value pair from the table itself. Okay, now let's come back to "reads." How do reads work? Well, "Reads" are very similar to "Writes". Again, the client sends the "Read" operation to the coordinator, the coordinator can contact set of replicas. It doesn't necessarily contact all the replicas, it constructs only X replicas. X is the number again specified by the client. Typically, the coordinator might prefer a replicas that have responded the quickest in the past. These are replicas for instance, that might be in the same rack as the coordinator or that might be on nearby racks in the underlying data center topology itself. When these X replicas respond, if they don't respond then the coordinator might end up sending the "Read" query to other replicas of that particular key. In any case, when any of the X replicas respond, it doesn't need to be just the X closest replicas. Any of the X replicas when they respond, the coordinator can then return the latest timestamp value from among those X. Well, the different replicas for a given key might return different values because we didn't say anything about consistency, which means that some of the replicas may have received the latest "Write" to that key. Other replicas may still be working with a stale of the value for that particular key. This means that when you get back answers from these X replicas for a "Read", some of them maybe stale value, some of them maybe newer values. So, essentially, the coordinator looks at the time stamp of these values, and the highest time stamp or the latest time stamp value is returned to the client. Once again, what is the value of X here? We'll see again when we discuss the next lecture. The coordinator also features values from the other replicas for this particular key. Why does he do this once again? Some of the values may be staler than others and we want to make sure that these values are updated and repaired to the latest value, so if any of these values are older then the coordinator initiates a "Read Repair" on these older values. Essentially, the "Read Repair" informs these older values or rather the replica servers that "Hey, here is the new and the latest value, the latest time stamp value that is associated with this particular key. Please update your corresponding memtable and eventually SStable." If this goes on for long enough, this mechanism will eventually bring all the replicas for a given key up to date, meaning that all of them will reflect the latest value that has been written to that particular key. For "Reads" however, if compaction doesn't run often enough, then a row maybe split across multiple SStables, then "Reads" need to touch multiple SStables. This means that all the values or all the columns for a given row are not necessarily written in the same SStable because you may have updated only one of the columns for a given row and for a given key, and only that particular column along with a key would be present in that SStable. So, even aside apart from compaction, you might need to touch multiple SStables you're trying to read the entire row because the lowest split across multiple SStables. This results in "Reads" being slower than "Writes", but as we'll see soon, the overall system is still quite fast. Next, we come to "Membership". So, remember that we said that the coordinator needs to know about all the other servers present in the cluster and this is true of all the other servers as well. Every server needs to know what are all the other servers that are present in the cluster. So, every server maintains a list of all the other servers present in the cluster, and this list needs to be updated automatically as servers join, leave, and fail. And this should be familiar to you from a previous lecture in the course. So, essentially, what Cassandra needs to do is, it needs to maintain a membership list at each server. And Cassandra uses the gossip style membership list which you've seen previously in the course. I won't discuss this in detail again, for details of this please refer to the membership and the gossip style membership lectures earlier in the course. In addition to the gossip style membership, Cassandra uses suspicion mechanisms to make sure that when servers are being directed as "Fail", there is a low probability that this is a mistaken detection, so it tries to increase the accuracy of detections. For this, the use of suspicion mechanisms, this is different from the previous suspicion mechanisms that we have discussed in the membership lectures. It uses what is known as an accrual detector. The failure detector outputs a value known as PHI which represents the suspicion. The Apps set an appropriate threshold, for instance, if you set a threshold of five, this results in about 10 to 15 second detection time. The way the PHI calculation works is as follows. It takes into account the inter-arrival time for gossip messages. So the inter-arrival time for gossip messages from a particular server have been long in the past, then it waits slightly longer for the next heartbeat before marking the server as having failed. Essentially, the PHI looks at not just the inter-arrival times but it also looks at their cumulative distribution or the probability between when the last cluster was received and the time now and based on that it outputs a value. When this value crosses the specified application threshold, that server is marked as having failed. Because as usual, this is a failure adaptive way of setting the thresholds for detection on a per server basis. So some servers that are responding slower than others, will end up being given a slightly more laxity in the sense of other servers waiting for a slightly longer for heartbeats from that particular slow server and other servers that are faster, might have a shorter timeline. So essentially, the suspicion mechanisms are a way of setting a time was adaptively on a server by server basis in the gossip style membership protocol. So, how about speed? How fast is Cassandra? MySQL which is one of the more popular relation database engines out there. On 50 gigabytes of data, took on average 300 milliseconds for "Writes" and on average 350 milliseconds for "Writes". In comparison, Cassandra took only 0.12 milliseconds on average and 15 milliseconds for "Reads". This of course orders the magnitude faster and this should lead you to think, "Well, what did we really lose? What's the catch over here?" And that will discuss in the next lecture.

### 04 - 1.3. The Mystery of X-The Cap Theorem

Slides: `C3_Key-valueStores_C_CSRAfinal.pdf`

#### Slide text

```
•   Proposed by Eric Brewer (Berkeley)
•   Subsequently proved by Gilbert and Lynch (NUS and
    MIT)
•   In a distributed system you can satisfy at
    most 2 out of the 3 guarantees:
    1. Consistency: all nodes see same data at any time,
       or reads return latest written value by any client
    2. Availability: the system allows operations all the
       time, and operations return quickly
    3. Partition-tolerance: the system continues to work
       in spite of network partitions

•   Availability = Reads/writes complete reliably
    and quickly.
•   Measurements have shown that a 500 ms
    increase in latency for operations at Amazon.com
    or at Google.com can cause a 20% drop in
    revenue.
•   At Amazon, each added millisecond of latency
    implies a $6M yearly loss.
•   SLAs (Service Level Agreements) written by
    providers predominantly deal with latencies
    faced by clients.

•   Consistency = all nodes see same data at any
    time, or reads return latest written value by any
    client.
•   When you access your bank or investment
    account via multiple clients (laptop, workstation,
    phone, tablet), you want the updates done from
    one client to be visible to other clients.
•   When thousands of customers are looking to
    book a flight, all updates from any client (e.g.,
    book a flight) should be accessible by other
    clients.

•   Partitions can happen across datacenters when
    the Internet gets disconnected
     • Internet router outages
     • Under-sea cables cut
     • DNS not working
•   Partitions can also occur within a datacenter,
    e.g., a rack switch outage
•   Still desire system to continue functioning
    normally under this scenario

• Since partition-tolerance is essential in today’s cloud
  computing systems, CAP theorem implies that a
  system has to choose between consistency and
  availability

 • Cassandra
    • Eventual (weak) consistency, availability,
        partition-tolerance
• Traditional RDBMSs
    • Strong consistency over availability under a
        partition

•   Starting point for                        Consistency
    NoSQL Revolution
•   A distributed storage
    system can achieve at
    most two of C, A, and
    P.
                              HBase, HyperTable,                   RDBMSs
•   When partition-           BigTable, Spanner
    tolerance is important,
    you have to choose
    between consistency
    and availability

                         Partition-tolerance Availability
                                                Cassandra, RIAK,
                                               Dynamo, Voldemort

•   If all writes stop (to a key), then all its values
    (replicas) will converge eventually.

•   If writes continue, then system always tries to keep
    converging.
     •   Moving “wave” of updated values lagging behind the latest values
         sent by clients, but always trying to catch up.

•   May still return stale values to clients (e.g., if many
    back-to-back writes).

•   But works well when there a few periods of low
    writes – system converges quickly.

•   While RDBMS provide ACID
     • Atomicity
     • Consistency
     • Isolation
     • Durability
•   Key-value stores like Cassandra provide BASE
     • Basically Available Soft-state Eventual
       consistency
     • Prefers availability over consistency

•   Cassandra has consistency levels
•   Client is allowed to choose a consistency level for each
    operation (read/write)
     • ANY: any server (may not be replica)
            • Fastest: coordinator caches write and replies
               quickly to client
     • ALL: all replicas
            • Ensures strong consistency, but slowest
     • ONE: at least one replica
            • Faster than ALL, but cannot tolerate a failure
     • QUORUM: quorum across all replicas in all
         datacenters (DCs)
            • What?

In a nutshell:
•     Quorum = majority
        • > 50%                                         A second
•     Any two quorums               A quorum              quorum
      intersect
        • Client 1 does a
             write in red quorum
        • Then client 2 does
             read in blue
             quorum                                        A server
•     At least one server in blue
      quorum returns latest
      write
•     Quorums faster than ALL,
      but still ensure strong        Five replicas of a key-value pair
      consistency

•   Several key-value/NoSQL stores (e.g., Riak and
    Cassandra) use quorums.
•   Reads
     • Client specifies value of R (≤ N = total number
        of replicas of that key).
     • R = read consistency level.
     • Coordinator waits for R replicas to respond
        before sending result to client.
     • In background, coordinator checks for
        consistency of remaining (N-R) replicas, and
        initiates read repair if needed.

•   Writes come in two flavors
     • Client specifies W (≤ N)
     • W = write consistency level.
     • Client writes new value to W replicas and
        returns. Two flavors:
          • Coordinator blocks until quorum is
             reached.
          • Asynchronous: Just write and return.

•   R = read replica count, W = write replica count
•   Two necessary conditions:
    1. W+R > N
    2. W > N/2
•   Select values based on application
     • (W=1, R=1): very few writes and reads
     • (W=N, R=1): great for read-heavy workloads
     • (W=N/2+1, R=N/2+1): great for write-heavy
        workloads
     • (W=1, R=N): great for write-heavy workloads
        with mostly one client writing per key

•   Client is allowed to choose a consistency level for each operation
    (read/write)
     •    ANY: any server (may not be replica)
             •   Fastest: coordinator may cache write and reply quickly to client
     •    ALL: all replicas
             •   Slowest, but ensures strong consistency
     •    ONE: at least one replica
             •   Faster than ALL, and ensures durability without failures
     •    QUORUM: quorum across all replicas in all
          datacenters (DCs)
             •   Global consistency, but still fast
     •    LOCAL_QUORUM: quorum in coordinator’s DC
             •   Faster: only waits for quorum in first DC client contacts
     •    EACH_QUORUM: quorum in every DC
             •   Lets each DC do its own quorum: supports hierarchical replies

•   Cassandra offers eventual consistency
•   Are there other types of weak consistency
    models?
```

#### Transcript

So, uh, when we discussed
the design of Cassandra in the previous lecture, uh, we use
this magic value of X, which, uh, is,
uh, specified by the client alongside every
read or write query, and X specifies
the number of replicas that the coordinator waits for until, uh, it can return
either a read value or an acknowledgement
for the write for the client. How do you set this value of X? Well that brings us
to the discussion of, uh, the famous theorem known
as the CAP theorem. The CAP theorem was proposed
by Eric Brewer from Berkeley, and was subsequently
proved theoretically by Gilbert and Lynch,
um, from, uh, NUS and MIT. Uh, and basically it
says the following: uh, in a distributed system, uh,
there are three properties that are considered
to be very important. Uh, typically this
is for a storage system. Um, and unfortunately,
in a, uh, distributed system such as an asynchronous distributed system, you can only satisfy, at most, two out
of these three properties. You can't guarantee
all the three. The three properties are: consistency, availability,
and partition-tolerance. Consistency essentially says
that even though there are multiple clients that are
reading and writing the data, uh, all the clients,
uh, see the same data at, uh, at any given
point of time. Uh, and that the reads,
uh, by any client return, uh, the latest written value
by that particular client. Availability says
that the system allows, uh, read and write operations
on all the keys all the time, and these operations return
very, very quickly. Partition-tolerance says that, uh, when the system
is, uh, partitioned, when the network is
partitioned into say two parts that cannot talk
with each other, the system continues to work and, uh, guarantee both the
consistency and the availability that we outlined earlier. So the CAP theorem
essentially says that you cannot guarantee
all the three, you have to choose, at most,
two out of the three. So why are
these three important? Before we discuss
the actual CAP theorem, and so let's look at why consistency, availability,
and partition-tolerance are really important. Availability refers,
uh, to the fact that, uh, first of all, you can read and write keys all the time, and also that reads and writes complete reliably
and very, very quickly. Well, quick-the quickness
in, uh, reading and writing is very important because
it essentially translates to revenues
for today's businesses. Measurements, for instance,
have shown that a 500ms increase in latency for operations
at Amazon.com, um, uh, or at Google.com cause a 20% drop in,
uh, the numbers of users that, uh, come
into that particular site. And this results in essentially
a 20% drop in the revenue for that particular,
uh, company. At Amazon.com, um, each added
millisecond of latency resulted in six million, uh, uh,
dollars of, uh, loss per year. And this is an enormous amount. And again, this is really
why these companies care for availability. They care to make the latencies as small as possible
for all reads and writes. Uh, so service level agreements, uh, or SLAs, which are typically written by providers, uh, for any of their customers,
uh, for instance, Amazon webservices
might have SLAs that it provides to Netflix, which uses Amazon
webservices infrastructure, um, uh, SLAs, uh, predominantly
deal with latencies that the customers, uh, want
the provider to, uh, guarantee. So why is consistency important? Um, uh, consistency essentially
says that all nodes see the same data at any time and that reads
returned by a client refer to the latest writes
to that key. Well, when you access your
bank or investment account by a multiple, uh, client
such as your laptop, your workstation, your phone or your tablet, you want all the updates
to reflect, uh, uh, in all the devices. You don't want, uh, to update
something from your tablet and then immediately
go to your workstation and find that that update has not been reflected
on your system. Also when you have multiple
clients reading and writing, uh, the same set of, uh, keys, um, uh, for instance when you have thousands
of customers and client machines that are trying to book
the same flight, you want
the same consistent information, uh, reflected
to all the clients. You don't want some clients
to see only two seats available, other clients to see only
to-uh, one seat available. You don't want two different
clients booking the same seat, uh, on the same flight. And again, partition-tolerance,
the third one of, uh, the CAP, uh, is, uh, important
because partitions can happen across data centers when
the internet gets disconnected. This may happen
during internet router outages, it may happen
because the under-seas je-se-Atlantic internet
cables get cut, uh, or because the DNS or the
Domain Name System doesn't work, or because of censorship, because of, uh, uh,
certain governments. Partitions can also occur
within a datacenter. For instance, uh, uh, rack
switch might go out, which means that all the servers
in that rack are, uh, for now,
uh, disconnected from the rest of the work. And in spite of this partition,
these partitions occurring, you still desire the system
to continue functioning, uh, normally, and providing
consistency and availability under these partition scenarios. So the CAP theorem says that again you can
only, uh, get three, only at most
two out of these three: consistency, availability,
and partition-tolerance. Since partition-tolerance
is really, really important in today's, uh, uh, uh, world
and because partitions do occur, uh, let's say the P
is really, really required. Essentially this means that,
uh, the CAP theorem implies that you have to choose between either consistency
or availability in today's systems. So Cassandra, which is the system we have been discussing so far, uh, always
chooses availability. So it chooses availability A, and partition-tolerance P. Which means that it has
to punt on the consistency. It can only provide weaker forms
of consistency, and it provides a weak form known
as eventual consistency. Cassandra does not provide
strong notions of consistency. Traditional relation databases, uh, prefer strong consistency instead over availability or insert availability whenever
you have a partition. Okay, so this is a-a market
change, uh, a sea change, uh, in these new generations
of key-value stores. So, uh, the CAP trade-off
has been the starting point for the NoSQL revolution, uh, once again
it says that you can get, at most, two
out of three of C, A, and P. Uhm, and-so if you draw
a triangle where you have consistency, availability,
and partition-tolerance at the three edges
of the triangle, different systems that exist
can be put at different points on the spectrum. So relation databases prefer
consistency and availability in in the-in scenarios, uh,
where they are single server and they really don't care
about partitions. Okay, so when you don't have
multiple servers, you can provide both C and A. However, Cassandra, and also
other, uh, key value stores, such as RIAK, Dynamo
and Voldemort, uh, prefer availability
and partition-tolerance, and they provide weaker notions
of consistency. Other NoSQL systems such as HBase, HyperTable,
BigTable, and, uh, Spanner, where, um, uh, BigTable and
Spanner are both from Google, prefer consistency
as well as partition-tolerance, and they might have, uh,
weaker notions of availability when there are, uh, partitions
that can happen in the system. So what is eventual consistency
which is provided by Cassandra, what does it really mean? Eventual consistency essentially
says the following: given a key, suppose all
the writes to that key stop. Then all the replicas
of that key, uh, all the values that
are mating on the server side, will eventually converge
to, uh, the latest write that has been written
to that particular key, okay. Typically the latest write, it doesn't need
to be the latest write, it is some one value. Essentially is says that all
the values uh, need to converge um, uh, to being the same value. Um, again this is the
theoretical definition, um, uh, the, uh, reality though is that writes
will continue coming, they'll keep coming
to the system. Uh, if this is the case, then the system will always try
to keep converging, that's what eventual consistency
always tries to do. Essentially you have a, um, uh, uh, a front wave of the
latest writes that are going on in the system and then you have
a, um, a moving later wave of updated
values of the replicas and the moving wave is always
trying to catch up to that, uh, front wave. Yeah, and if the writes,
uh, become slow at some point of time, uh, then, uh, the moving wave
will catch up, uh, to, uh, the latest values. However, because the moving wave
is always lagging behind, is oftentimes lagging
behind the front wave, uh, some reads might
return stale values, uh, to the clients,
uh, for instance, if there are many
back-to-back writes and, uh, mechanisms we-
that we have discussed, like the read repair,
uh, don't have, uh, time enough to catch up, uh, uh, to the front wave itself of updates, then, uh, the, um, uh, then some
of the reads from clients may return,
uh, the staler values, older values that replicas. So, uh, relation databases, uh,
provide what is known as ACID, these are very strong,
uh, guarantees, uh, ACID stands for Atomicity, Consistency, Isolation and Durability. We'll discuss these
later on, uh, in the course. Uh, ah, in comparison, key
value stores like Cassandra are reputed to provide, uh, the
opposite of ACID, which is BASE. Uh, this is sort
of a tongue-in-cheek, uh, terminology, uh, but it-it
seems to make sense here. BASE stands
for Basically Available Soft-state Eventual Consistency. Uh, basically available you
know, because Cassandra, uh, wants to always support
reads and writes, no matter what happens
in the system, soft state refers
to the fact that it maintains a lot
of in-memory information, especially like the mem tables that we have already discussed. Eventual consistency, like we
have discussed, ensures that, uh, when, uh, writes stop
or become slow, then all the replicas
of a given key will converge
to the same value. Again, uh, Cassandra prefers
availability over consistency when it comes
to partition-tolerance. Now, back to Cassandra. Let's look at the value of X. So how do you specify
the value of X for a given read or a write? Uh, the value of X is what is known as a consistency
level in Cassandra. The client is allowed
to choose the consistency level for each operation,
a read or a write, for any key,
uh, that it sends out. So for each operation
that the client sends out, it can specify a given consistency level for that particular operation. If the consistency level is ANY, this is an allowed consistency level by Cassandra, it means that
any server can store that particular, uh, write, um, and then return immediately to, uh, the, uh, uh, client. This is really useful
because it's the fastest, even if all the replicas
are down, the coordinator simply caches, uh, the write
and returns immediately, um, to, uh, the, um, uh,
to the, uh, client, okay. So this is the fastest. The slowest, on the other hand,
is the consistency level of ALL. This says that all the replicas if there are three replicas
for a given key, then all the replicas
need to acknowledge to the coordinator
before the coordinator can say that the write has been done and return and acknowledgement
to, uh, the client, okay? This ensures the strongest
consistency because essentially, uh, it ensures that
all the replicas acknowledge, and all the the replicas
have gotten the latest write, uh, before an, uh,
an acknowledgement is sent back
to the client. But of course, it's the slowest, because some of the replicas may respond slower than others, and essentially
you end up waiting for the slowest replica,
uh, among the group. Uh, so in between ANY and ALL, uh, is a spectrum
of consistency levels. Along the spectrum lies ONE, where you say
that the coordinator, uh, needs to receive back
a, uh, an acknowledgement from any ONE of the replicas, uh, this is again different
from ANY because ANY applies, a-a-allows even
the coordinator to store, uh, the, uh, the written value before returning
an Ack to the client, ONE does not allow that. ONE, uh, says that
at least one of the replicas must return an Ack,
uh, to the coordinator before it's returned back,
uh, to the client. This is of course,
faster than ALL, uh, but it cannot
tolerate a failure, so if all the replicas fail,
then, for instance, then ONE will result
in a write operation that fails. Um, QUORUM y-uh, says
that, uh, the coordinator needs to, uh, receive
a quorum of replies, uh, from replicas before it Acks
back, uh, to the client. What is a QUORUM? We'll see on the next slide. By the way, uh, in this slide
I have so far discussed the consistency levels, uh,
as far as writes are concerned, all the consistency levels
we have discussed can also be applied to reads, um, uh, the consistency level essentially specifies how many replicas the coordinator needs to hear from before it returns the latest time stamp value to the client. So let's look
at what a QUORUM is. So Quorum, essentially, uh,
in, uh, the simplest terms, a quorum refers, uh, to, uh, at least a majority, at least 50%. So suppose I have a quorum,
um, of, uh, say, suppose I have a group
of, uh, five replicas, for a given key value pair, so each of these,
uh, servers are storing, uh, uh, a copy
of the key value pair, a quorum is at least 50%,
essentially a quorum is at least three out
of the five, uh, replicas. So, I have one quorum here, the
blue quorum, and another quorum, the red quorum over here. Suppose, um, uh, a Client 1
does a write in the red quorum, meaning that it updates, the coordinator updates
these three, uh, replicas in the red quorum, uh, and then returns
an Ack to the client. A client two subse-Client 2 subsequently does a read, and the, uh, the read also does a, uh, also uses quorum and it does, uh, the read
in the replicas of the blue quorum using
these three replicas. Now because a quorum is at least
50%, any pair of quorums, any two quorums, such as the red
quorum and the blue quorum over here, will intersect
in at least one server. Okay, that's guaranteed to you. So this server over here, which is common to both the red
and the blue quorums will return the latest written value,
um, uh, to that particular key. Okay, so, uh, quorums are nice,
because they don't require you to wait for all the replicas
to return an Ack. They are not as slow
as the ALL consistency level, however, um, uh,
they are, uh, giving you a fairly strong notion
of consistency almost as strong as, the uh,
ALL, uh, consistency level, um, um, uh, in spite of not
incurring that much of overhead. So quorums are very, uh,
interesting technique and a very important technique that are fairly fast, uh, essentially you send out
the write to all the replicas, all the five replicas, and whenever the first three
of them acknowledge, you can send back an acknowledgement to the client. Again, so it's fairly fast, uh, it's, um, uh,
not as slow as ALL, but it gives you a fairly
strong consistency guarantee, uh, that is the same as ALL. So, many key value stores such as Riak and Cassandra
use quorums, essentially the reads specify a,
uh, read consistency level of R, again the value of R  N, the total number
of replicas for that key. Uh, the coordinator waits
for R replicas to respond before sending
the result to the client. And in the background,
the coordinator checks the other N-R replicas to see if they have older values, staler values, and if so, then it initiates
a read-repair to bring them up to date. For writes, um, writes come
in two flavors, um, uh, we'll see
those two flavors, uh, the client again speficies, uh, the write consistency level, W  N, the number
of replicas for that key. Um, the client writes the value,
the new value, written value to the W replicas, and returns. There are two flavors, uh, the first flavor has
a coordinator blocking until the quorum is reached, and only when the replicas, uh, acknowledge to the coordinator does it return an Ack
to the client. The asynchronous, uh, instead has, uh, the coordinator returning an Ack immediately to the client
and then thereafter very find that the, uh, um,
write consistency level is reached by insuring
that at least W replicas, uh, Ack to the coordinator. This, uh, allows the client
to proceed with other reads and write operations, rather than waiting for all
the W, uh, replicas to Ack, uh, and it, um,
uh, offloads the responsibility of insuring that W replicas
have been written to the coordinator itself. So, you have a combination,
more the read replica count and the write replica count
and the values you choose for these, uh, insure either
strong consistency or not. So if you really want to insure
strong consistency in your system, then you wanna make sure
that the value of W+R>N, the number of replicas
for each key and that the value of W>(N/2), essentially, the second
condition here says, the, says that W+W>N. The first equation here,
insures that if you have a write quorum
and a read quorum they intersect
in at least one server, um, uh, among
the replicas of that key, and this insures that reads
will return the latest write. The second condition here
insures that if you have two write quorums then they
intersect in at least one, um, uh, uh, replica server
and this replica server will, uh, keep the latest value
of the write. Essentially, this is also used
for returning conflicts, if you have
two conflicting writes, then at least one server
detects that conflict. The values you select
for W and, uh, and R, really depend on your workload. So, for instance, uh, if you
have very few writes and very few reads, you want to select W
to be small and R to be small, so that they're fast
and, essentially, you don't, uh, expects too many conflicts, uh, in this system, uhm, you expect
that the-that the, uh, by the time the reads come along
all the, uh, replicas would have gotten updated, um, uh, and, uh, you choose
a small values of W and R for this. If you have read-heavy workloads
you want the reads to be fast, so you choose R
to be a small number, like one, but if you want to make sure that both of these equations
are satisfied, then you choose W to be N. 'Kay, this insures
that W+R>N. If you have
write-heavy workloads you choose both W and R
to be (N/2)+1, this satisfies
both the above equations, that we discussed, uh,
and, uh, it also makes sure that the writes don't need
to wait for, uh, N replicas, instead they only wait
for a quorum of replicas. Um, also, you can choose, um,
uh, for write-heavy workloads with, uh, only one client
writing per key, you can choose W
to be one, because essentially you don't have,
uh, multiple clients trying to write to a key but multiple clients might be trying to read, uh, from a key. So, in order to make sure
that reads are consistent and return the latest,
updated value, you set your read quorum,
uh, to be N. So, we've discussed
those three consistency levels. There are also other consistency
levels that Cassandra provides, uh, using the notion of quorums. Uh, the quorum consistency level in Cassandra, uh, says that, you need to get a quorum across
all the replicas in all the datacenters. Uh, so this means that,
if you have three datacenters, uh, each with, uh, three
replicas for a given key, then you need to get, um, uh, at least five
of those replicas, across all the datacenters, to return an Ack
before an Ack can be returned, uh, to the client. A local quorum says that,
you need to get a quorum in the coordinator's datacenter, uh, this is one of
the fastest versions of quorum, so again, using our, uh, example
of three, uh, datacenters each with three replicas
for the given key, the client typically contacts
one, uh, uh, coordinator, in one of the datacenters and that datacenter contains
three replicas for the key, if any of the two
of those three replicas, uh, send Acks
to the, uh, coordinator, the coordinator
can then send back an Ack to the client without waiting
for the other datacenters. Finally, each quorum says
that you need t- uh, uh, reach a quorum in each
of those, uh, datacenters. So again, using our example
of, uh, three datagen, three datacenters each
with, uh, three replicas, in order to make sure
that two replicas, in each of those datacenters, each of the three datacenters, uh, sends back an Ack, um, uh, to, uh,
the, uh, clients coordinator, so that then an Ack can be returned, uh, to the client. So this, uh, allows each
datacenter to, essentially, do its own quorum and it
supports hierarchical replies, where the replicas
in each datacenter re- uh, send a message back
to that datacenters coordinator and then that sends, uh, message back to- an Ack back, uh, to the clients coordinator in the clients,
um, uh, contact datacenter, and then that coordinator
can then send back an Ack to the client itself. So, Cassandra offers
Eventual Consistency but there are other kinds
of consistency models that are weak consistency models
that are out there too and that have emerged
in the last few years. Well really, they've not emerged, they've been around for many years, from the, uh,
notions of paddle systems and the area of architecture,
computer architecture, but in the last few years
they have, uh, started to emerge
in the area of key value stores and no sequel storage systems. We'll discuss that
in, uh, the next lecture.

### 05 - 1.4. The Consistency Spectrum

Slides: `C3_Key-valueStores_D_CSRAfinal.pdf`

#### Slide text

```
Faster reads and writes

             More consistency              Strong
Eventual                             (e.g., Sequential)

  •    Cassandra offers eventual consistency
        • If writes to a key stop, all replicas of key
           will converge
        • Originally from Amazon’s Dynamo and
           LinkedIn’s Voldemort systems

                Faster reads and writes

                   More consistency                            Strong
Eventual                                                 (e.g., Sequential)

  •    Striving towards strong consistency
  •    While still trying to maintain high availability
       and partition-tolerance

                     Red-Blue
      Causal                        Probabilistic

               Per-key sequential                               Strong
Eventual                               CRDTs              (e.g., Sequential)

  •    Per-key sequential: Per key, all operations have a global
       order
  •    CRDTs (Commutative Replicated Data Types): Data
       structures for which commutated writes give same result
       [INRIA, France]
         • E.g., value == int, and only op allowed is +1
         • Effectively, servers don’t need to worry about
             consistency
                     Red-Blue
      Causal                        Probabilistic

               Per-key sequential                                        Strong
Eventual                               CRDTs                       (e.g., Sequential)

  •    Red-blue consistency: Rewrite client transactions to separate
       ops into red ops vs. blue ops [MPI-SWS Germany]
        • Blue ops can be executed (commutated) in any order
             across DCs
        • Red ops need to be executed in the same order at each
             DC

                     Red-Blue
      Causal                        Probabilistic

               Per-key sequential                                      Strong
Eventual                               CRDTs                     (e.g., Sequential)

  Causal Consistency: Reads must respect partial order based on information flow [Princeton,
  CMU]     W(K1, 33)
 Client A
                                         W(K2, 55)
 Client B                                                                                         Time
                     R(K1) returns 33
 Client C

              W(K1, 22)                 R(K1) may return
                                                                          R(K1) must return 33
                                            22 or 33
                                                             R(K2) returns 55
      Causality, not messages

                             Red-Blue
            Causal                              Probabilistic

                     Per-key sequential                                                   Strong
Eventual                                             CRDTs                          (e.g., Sequential)

•   Linearizability: Each operation by a client is visible (or
    available) instantaneously to all other clients
     •   Instantaneously in real time
•   Sequential Consistency [Lamport]:
     •   "... the result of any execution is the same as if the operations
         of all the processors were executed in some sequential order,
         and the operations of each individual processor appear in this
         sequence in the order specified by its program.
     •   After the fact, find a “reasonable” ordering of the operations
         (can re-order operations) that obeys sanity (consistency) at all
         clients, and across clients.
•   Transaction ACID properties, e.g., newer key-value/NoSQL
    stores (sometimes called “NewSQL”)
      • Hyperdex [Cornell]
     •   Spanner [Google]
     •   Transaction chains [Microsoft Research]
```

#### Transcript

So in the previous, uh, lectures we have seen, uh
eventual consistency which is what, uh, Apache
cas-Cassandra supports, uh, but that's not the only kind of, uh, weak consistency model
that can be supported. In fact, there is a spectrum
of consistency models ranging from, uh, weak eventual all the way
to strong consistency models such as sequential
consistency models. As you move from left
to right on the spectrum, you get stronger and stronger
consistency models and you get slightly slower, uh, reads and writes, especially when
you have, uh, partitions. So essentially,
if you really care, uh, or your application really cares about fast availability of reads and writes, uh,
for your data, you wanna move to the left side of the spectrum. But if you care more
for consistency of your data, uh, then you wanna move toward
the right side of the spectrum. So Cassandra offers, uh, the eventual
consistency, uh, uh, model which says that if writes
to a key stop, then all replicas of that key will, uh, converge eventually. Uh, typically they converge
the latest written value, uh, or the last writer wins policy
is used, which is LWW. Uh, this is taken from, uh, Amazon's Dynamo system
or Amazon's DynamoDB. Uh, and Cassandra was inspired
by the DynamoDB system. LinkedIn's Voldemort
key-value store also, uh, was, uh,
inspired by DynamoDB, and it shares,
uh, the same, uh, feature. But a lot of, uh, work has
been done in the last few years where, uh, um, systems have
developed that strive towards, uh, stronger and stronger
notions of consistency. Stronger than eventual, uh, while always trying
to, uh, maintain, high availability, uh,
and partition-tolerance, which is what is guaranteed
by systems like, uh, Cassandra. Uh, these include
a variety of models ranging from Per-key
sequential models, uh, to, um, uh, CRDTs, uh,
to, uh, Causal models to Probabilistic models
to Red-Blue consistency models, uh, and also
Strong models, of course. We'll discuss some
of these over, uh, this lecture. So Per-key sequential
essentially says that on a per-key basis, all operations
have a global order. So, uh, you could ensure this
by maintaining, uh, a per-key coordinator, and ensuring
that all the reads and writes are serialized
through the coordinator, uh, and, uh, therefore they have
a single global order. This, of course, may be, um, uh, restrictive because
if that coordinator fails and you need
free like another coordinator, uh, however, it, uh,
does guarantee some stronger notion
of consistency. CRDTs are a new, uh, replicated,
uh, data structure known as Commutative
Replicated Data Types. Uh, um, and these data
structures, um, uh, commuting-or commutating writes
give the same result. Essentially, commutating writes
means that if you reverse the order of two writes,
then the end result is the same. For instance,
if your data structure which is an integer, and the only operation
allowed on the data, uh, in there is a +1, essentially this is
what is known as a counter, uh, a counter is
a commutative data type. If you have two writes coming
in from two different clients, each of those writes is essentially a +1 operation. If client one's
operation goes first and then client two's operation is applied, you get the same result,
which is a +2, as if you applied client
two's operation first and then client one's operation, you'll again get a +2. So commutating those two writes
results in the same end result. Essentially if you have, uh,
if you have a CRDT the servers really
do not need to worry about, uh, ordering the writes with respect to each other; all the writes have,
uh, the, um, have, uh, have the same effect. Or rather, all the writes can be
commutated with each other and, uh, the end result of any permutation of these writes is the same
as any other permutation. The notion of CRDTs was discovered
by researchers in INRIA, and it has been extended
to not just counters, uh, which are the simplest,
uh, notion, uh, but also other complicated
data structures such as, uh, documents, um, which are shared and are being written and read
by multiple users at the same time. Um, so related to the CRDTs is the notion
of red-blue consistency. Uh, it's not always possible
to write operations, um, which, uh, or transactions, uh, on the clients' side which only have commutated, um, uh, uh,
the commutative property. There are some operations
that absolutely need, uh, and require to be ordered, uh, at all the data centers, uh, in the same order. So the red notion
of red-blue consistency from the Max Planck Institute
in Germany essentially, uh, uh, writes client operations, uh,
in, uh, in such a way that the operations are split into either red operations, ah, or blue operations. So each operation is
either red or blue. The blue operations
are commutative, so they can be executed
in any order, uh, with respect to each other
across data centers. But the red operations
absolutely need to be executed in the same order
across all data centers. And this way, you can, uh, by rewriting the original
client transactions, uh, into, uh, red
and blue operations, you can support a stronger
notion of consistency, um, uh, while still supporting some notions of availability. One of the newer notions
of consistency that has emerged, uh, from researchers
in Princeton and Carnegie-Mellon is the notion
of causal consistency. Uh, let's look
at an example here, um, so, uh, I have three clients here, clients A, B, and C. Client, uh, A, does a W(K1, 33). Subsequently, Client B
does a R(k1) which returns this value of 33. And this means that this, uh,
read, uh, is causally, uh, dependent on the, uh,
write from Client A. So there is a causal rink-link
in between, uh, this write to this read. Uh, this doesn't effect the messages that flow
between Client A and B, in fact, Client A and B
may not communicate with each other at all directly. However, because the read
returns the same value as the write, there is a causality that flows
from the write to the read. Of course there is causality
at that client that says so after the R(K1) by the client, uh, W(K2), uh, W(K2, 55) is done by the same client so this read happens
before this particular write, causally speaking. And then later on, if another
Client C does a R(K2) and returns 55, then there is of course
a causality from the write by Client B, uh,
to that read by Client C. Subsequently if, uh,
the Client C does a R(K1), K1, the first key, over here, this must return 33 because, uh, the W(K1)
is causally related to this. 'Cuz essentially there
is a causal path going from W(k1, 33) to R(K1)
at Client B to R-to W(K2) at Client B to R(K2) at Client C to R(K1)at Client C. This is the causal path, and this means that the write of, uh, (K1, 33) happened before
this key, uh, this, uh, R(K1) and so this key-
uh, uh, this read must return, uh, the, uh, value of 33 and not an older value
such as, uh, 22, which may have been written
by a client previously. Okay, so this is causality, and essentially causal
consistency says that reads obey causality and they return the, uh, latest causally written value, uh, by, uh, any, uh, client. However, there might be multiple
causally written values as you see elsewhere
in this course, uh, and so, uh, the causal consistency allows a read to return one
of potentially many different, um, uh, written, uh, values and so it's not as strong
as the strongest notion of consistency
but it's quite close. So what are these strong
consistency models that I keep talking about? Well, there are, uh,
tw-at least two, uh, major, uh, strong consistency models. There are linearizability
and sequential consistency. Linearizability is one
of the strongest notions of consistency, uh, which says that each
operation by a client is visible or is available instantaneously, and when I say instantaneously
I mean in real time to all the other clients. This is as if
there were only one copy of every key value pair, and they were being stored
on exactly one, uh, server. So this is one
of the strongest notions of- notions of consistency
and however it's very, um, uh, difficult to support in, uh,
distributed systems. Uh, sequential consistency's
also a strong notion of consistency, but it's not
as strong as linearizability. Sequential consistency was
originally, uh, stated by Lamport as follows, says: Essentially, this is
an after-the-fact way of, uh, reordering
the operations that, uh, that occurred
so that there is still sanity in this new ordering, uh, and the sanity also obeys
the order at each client. Okay, so, essentially
this reordering, uh, obeys, uh, uh,
things like causality, it obeys, um, uh, uh, clients being able to read
their own writes, and it also obeys, uh,
the, um, uh, ordering- the linear ordering
at each client itself. The sequential ordering
that you come up with may not be same
as the linearized, uh, ordering. It may be slightly different,
but it still makes sense. Okay, so, um, uh,
a transaction ACID properties, um, uh, um, are being supported, uh, by some of the newer
generations of NoSQL systems, these are sometimes
called as NewSQL systems. These include academic systems
such as Hyperdex from Cornell, uh, also, uh, Spanner,
uh, from Google supports transactions and, uh, stronger notions of consistency, and also other systems, uh, which support
transaction chains such as from Microsoft Research.

### 06 - 1.5. HBase

Slides: `C3_Key-valueStores_E_CSRAfinal.pdf`

#### Slide text

```
•   Google’s BigTable was first “blob-based” storage
    system
•   Yahoo! Open-sourced it  HBase
•   Major Apache project today
•   Facebook uses HBase internally
•   API functions
     • Get/Put(row)
     • Scan(row range, filter) – range queries
     • MultiPut
•   Unlike Cassandra, HBase prefers consistency (over
    availability)

                                                                      Small group of servers running
                                                                      Zab, a consensus protocol (Paxos-like)

   Client                                              HMaster
                             Zookeeper

HRegionServer                 HLog                                                  HRegionServer
 Hregion
  Store        MemStore                    Store       MemStore
   StoreFile         StoreFile             StoreFile             StoreFile    ...                     ...
                 …                   ...                 …
    HFile                 HFile              HFile                HFile

                                              HDFS

•   HBase Table
     • Split it into multiple regions: replicated across servers
           • ColumnFamily = subset of columns with similar query
              patterns
           • One Store per combination of ColumnFamily + region
                  • Memstore for each store: in-memory updates to
                     store; flushed to disk when full
                        • StoreFiles for each store for each region:
                            where the data lives
                              - HFile

•   HFile
     • SSTable from Google’s BigTable

Data           …               Data                … Metadata, file info, indices, and trailer

Magic    (Key, value) (Key, value)                  … (Key, value)

  Key      Value Row        Row       Col Family     Col Family    Col         Timestamp      Key Value
length    length length                length                      Qualifier                 type

                        SSN:000-01-2345 Demographic               Ethnicity
                                         Information

                                                        HBase Key

Client                                 HRegion                       Store       MemStore
                                                           2. (k1)
                                                                     StoreFile         StoreFile
                                         .                                         …
         (k1, k2, k3, k4)                                              HFile                HFile
                                         .
                             (k1, k2)    .
                                                                                  .
            HRegionServer                                                         .
                                       HRegion
                            (k3, k4)                     1. (k1)                  .
                                                                     Store       MemStore
            Log flush                                                StoreFile         StoreFile
                                                                                   …
                                                                       HFile                HFile

                                                 HLog

         Write to HLog before writing to MemStore
         Helps recover from failure by replaying Hlog.

•   After recovery from failure, or upon bootup
    (HRegionServer/HMaster)
     • Replay any stale logs (use timestamps to
        find out where the database is w.r.t. the logs)
     • Replay: add edits to the MemStore

•   Single “Master” cluster
•   Other “Slave” clusters replicate the same tables
•   Master cluster synchronously sends HLogs over
    to slave clusters
• Coordination among clusters is via Zookeeper
• Zookeeper can be used like a file system to store
    control information
1. /hbase/replication/state
2. /hbase/replication/peers/<peer cluster number>
3. /hbase/replication/rs/<hlog>

•   Traditional databases (RDBMSs) work with strong
    consistency and offer ACID
•   Modern workloads don’t need such strong guarantees
    but do need fast response times (availability)
•   Unfortunately, CAP theorem
•   Key-value/NoSQL systems offer BASE
     • Eventual consistency, and a variety of other
         consistency models striving towards strong
         consistency
•   We discussed design of
     • Cassandra
     • HBase
```

#### Transcript

So in this, uh, lecture we'll look at, uh,
the, um, architecture of, um, the No SQL system
called HBase. So, uh, Google's BigTable system was the first "blob-based" storage system that was introduced, and of course Google, uh, did not
open source the code, but they published
a paper on this. Uh, Yahoo! wrote an open-source implementation of this which came to be called
as HBase, um, uh, this is
a major Apache project today. A variety of companies use HBase including, uh, Facebook,
which uses HBase, uh, for one of it's internal,
uh, architectural stacks. Uh, HBase supports,
uh, basic API functions, uh, such as Get or Put
on a per-row basis. This is again
a Get or Put by key, just like key-value stores. You als-this also allows you
to scan by a row range, um, this allows you
to do range queries. For instance, you might fetch, uh, all the users whose names start-start with A and B. And also it allows you
to do MultiPuts where you put
multiple key value pairs into, uh, the, um, uh, system itself. Unlike Cassandra, which
preferred availability over consistency,
under partitions, HBase prefers consistency over availability, under partitions. So here is what the HBase
architecture looks like: you have a client over here which, uh, can send queries,
reads, and writes, uh, to the HBase system. Uh, the coordination between the
clients and the servers is done by a Zookeeper, which is a small group
of servers running a
consensus-like protocol uh, a
Paxos-like protocol which is, uh, which is elsewhere
in this course. Uh, the, uh, HBase system itself
has multiple HRegion Servers, uh, as you notice here. This is one HRegion Server
that's blown up, there might be
other HRegion Servers as well. The HRegion Server
might contain, uh, multiple, uh HRegions. Uh, one HRegion is
sown-shown over here. The HRegion itself might contain
multiple stores, one store is shown over here. The store, uh, might contain,
uh, multiple store files, and each store file
contains an HFile. The HFile is essentially a file that is stored
in the underlying HDFS, the same Hadoop
distributed file system that is used in Hadoop. The store in relation,
also contains a MemStore and a HRegion Server is
associated with an HLog, over here. There's also an HMaster, uh,
which, uh, uh, communicates with the Zookeeper and also
coordinates with, uh, the HDFS, uh, and, uh, I'll discuss
each of these, uh, individual, um, uh,
components in detail in the next slide. So the HBase Table,
when you have a table, you know a reg-a regular database table, the HBase Table
is split into regions. Um, uh, for instance,
essentially these regions are a collection of rows
in that HBase Table. Each of these regions
is replicated, uh, across, uh, servers
and split into regions because you don't wanna store the entire table, some tables might be large,
other tables might be small, you don't wanna store, uh, large
tables, um, uh, as one, you wanna split them
into regions so that they are
more manageable. Then you have a ColumnFamily. A ColumnFamily is essentially
a subset of columns within that, uh, table, and within that region, uh, with similar query patterns. Uh, essentially
it's within the tables, so all the regions
for a table contain, uh, the same set
of columns within, uh, their corresponding
Column Families. Uh, then for every combination
of, uh, region and ColumnFamily, so for every ColumnFamily within
a region, you maintain a store. Okay, and that's what you saw on the previous
architectural slide. Uh, each store
contains a MemStore, the Memstore is,
um, uh, uh, uh, uh, something that maintains
an in-memory, uh, version of the latest updates that
have been done to that store. This is like the MemTables we
discussed in Cassandra, when the MemTa- MemStore is, uh,
um, uh, full or when it is old it is flushed to disk. There are also StoreFiles which, um, uh, are maintained on a per store basis for each region. This is where
the actual data lives, and the store file
contains an HFile which stores
the actual data itself, and that is stored, uh,
in the underlying HDFS, okay? The Hfile is oriented
essentially like, uh, an SSTable from the Google's
BigTable system, and very similar to the SSTable that we saw from,
uh, in the Cassandra system. So here is what
an HFile might look like. The Hfile contains, uh, a lot of
data, uh, followed by more data, uh, and then there might be some
metadata, file information, uh, indices, and a trailer
information at the end. Let's blow up one of
these data pieces. So, um, uh, the data itself
contains a magic number to identify that uniquely, followed by a variety
of key value pairs. Let's blow up one
of these key value pairs. The key value pair contains, uh, information such as
the key length first, then the value lengths, and then the row length, so you know how many
bytes each of these contain. Then you have the row itself, uh, you have
the ColumnFamily length followed by
the actual ColumnFamily, uh, the column qualifier, um, uh, a timestamp when this
value was la-last written, uh, the key type,
and then the, uh value itself. The HBase, uh, treats this
entire, um, uh, uh, segment of, uh, entries shown
here as the HBase Key. So let's look at, uh, some
of these entries here. What is the row? The row, uh, eh, for, uh, a
particular application which maintains, for instance,
census information, might be the Social
Security number of that
particular individual. The ColumnFamily might be demogragric-demographic
information, so it might say
all the demographic information about that
particular individual. Uh, one of the columns
within the ColumnFamily might be the ethnicity
of that particular individual. Uh, uh, it might be
Asian-American or Caucasion or African-American, and
so on and so forth. So, whichever is, uh,
the ethnicity of that individual is maintained over here. Uh, so this is essentially a
hierarchic-hierarchical way of, uh, breaking down,
uh, a column, and specifying the
entire, uh, column itself. And you also have the timestamp
and the key type over here. So, how does, uh, HBase
maintain strong consistency? It does this by-by using a
write-ahead log, or a HLog. Again, the HLog is maintained on
a-on a per HRegion Server basis. So suppose a client sends in
operations for four different keys, a key one, key two,
uh, key three, key four. Uh, key one and key two might
be assigned to HRegion, uh, the first HRegion, and key three and
key four might be assigned to another HRegion. Sooo, the HRegion server
appropriately routes the, uh, operations
to the appropriate HRegion. Uh, when an HRegion receives an
operation such as for (k1), it first enters, um, uh, this,
uh, into, uh, uh, the HLog, and so it, uh, writes
an entry to the HLog before it writes to the actual, uh, MemStore itself. Uh, it does this so that, uh,
if there is a failure after writing into the log,
then you can, uh, replay this write by looking into your HLog. Okay, so this operation
is done first, and then the corresponding, um, uh, operation is sent to the store, which then writes
into the MemStore. Eventually, when the MemStore
is full, it's flushed into a store file, and that is stored
as an Hfile or HDFS. So when you do have a failure,
you just need to replay the log. Uh, after you recover from
your failure on bootup, um, uh, either the HRegionServer or the HMaster
does the following: it replays
any stale log entries, again, it uses the timestamps
to find out where the database
is with respect to the logs, and it replays any
of the log entries, um, uh, since the database timestamp itself. Uh, when you replay you add
edits to the MemStore, which eventually
will get flushed into, uh, the, um, uh,
HFiles themselves. Now when you can have Hrefs running across multiple data centers as well, uh, there is
a single master cluster of all the data centers. You have one
of the data centers marked as a "Master" data center. The other data centers are
simply "Slave" data centers, uh, and they replicate
the same tables. The Master cluster, uh,
synchronously sends the logs, the HLogs, over
to the Slave clusters, which then use the logs to simply update
the corresponding MemStores, which eventually get
flushed, uh, to disk. The coordination
among the Master and the Sl-and
the Slave clusters is done via Zookeeper again. And Zookeeper not just runs a
Paxos-like consensus protocol, it also can be used to store, uh, uh, information
just like a file system in a hierarchical fashion. So for instance, you
can use, uh, the address "/hbase/replication/state" to store the current state
of the database. You can use the address "/hbase/replication/peers/
<peer cluster number>" to store information about that particular master
or slave cluster. And then you can also store
the HLog, um, information in this, uh, third, um, uh, address, which is "/hbase/replication/rs/<hlog>"
itself. Essentially, Zookeeper
can be used as a naming system that maps this to the
actual location of the, eh, of that information itself. So, uh, to wrap up
our discussion of, uh, key value stores
and NoSQL storage systems, traditional database,
the relational database systems, uh, uh, work
with strong consistency and offer strong notions
of consistency such as ACID. But modern workloads don't
necessarily always need such strong guarantees, uh, what they do need is fast availability
or fast reads and writes, uh, or fast response times
to clients, because this is
directly correlated with, um, uh, revenue, uh,
to the companies that run cloud computing services today. Unfortunately, the CAP theorem
says that you cannot guarantee both availability
as well as strong consistency when you really care about
partition-tolerance: you have to choose
one or the other. Key-value stores
such as Cassandra offer BASE, which is basically available
soft-state eventual consistency, and essentially they punt on the
strong notions of consistency, just because the workloads don't
necessarily require them, but at the same time
they're able to grant, uh, very good, uh, response times, very fast response times. There has been
a lot of other work on stronger and stronger
notions of consistency that are closer and closer to the strong versions
of consistency, uh, while still offering
fast availability. We have discussed,
uh, the design of, uh, the Cassandra key-value store, and also the
HBase system which prefers, uh, consistency
over availability while Cassandra preferred availability over consistency.

### 07 - 1.6. Consistency Models by Aishwarya Ganesan

Slides: `consistency-spectrum-with-quiz.pdf`

#### Slide text

```
CS 425 / ECE 428
Distributed Systems
      Fall 2024
     Aishwarya Ganesan
   w/ Indranil Gupta (Indy)
  The Consistency Spectrum
                              All slides © IG/AG

Consistency Models

Contract between distributed system and application
Dictates what results can the system return for operations              clients
     Concurrent reads and writes by clients on replicas
     Depending on how operations are performed, guarantees offered by
     the distributed system differ
     Consistency model dictates what is permissible
System developers – design/optimize system to meet contract
                                                                         system
Application developers – need to understand what contract is
for application correctness

                                                                              2

Consistency Spectrum

                Faster reads and writes

                  More consistency               Strong
     Eventual                             (e.g., Linearizability,
                                               Sequential)

                                                                    3

Spectrum Ends: Eventual Consistency

Cassandra offers Eventual Consistency
     originally from Amazon’s Dynamo and LinkedIn’s Voldemort    req        resp
                                                                     W(x=1)
If writes to a key stop, all replicas of key will converge      C1
Reads might see any previous write                                            W(x=2)
                                                                C2
    weak guarantee
                                                                                   R(x)=0
More performant – allows concurrent writes                      C3
More availability – disconnected operation
                                                                                            R(x)=0
Need to resolve conflicts between multiple object versions      C4
     Cassandra – latest timestamp wins

                                                                                                4

Spectrum Ends: Strong Consistency

Linearizability [Herlihy and Wing]
                                                                                  W(x=1)
Strong consistency (the C in CAP)                                  C1
Intuitively, each operation by a client is visible instantaneously                           W(x=2)
to other clients
                                                                   C2
     instantaneously in real time                                                          R(x) 12
                                                                             C3
All operations are totally ordered in a way that respects
real-time order of operations                                                                         R(x) ?1 2
                                                                             C4
     if A completes before B begins, A ordered before B
     what if A and B are concurrent?
            order in a way such that total order is a valid sequential one
Appears to be a single machine (one-copy semantics)
Trades off performance and availability                                                                    5

Spectrum Ends: Strong Consistency Models II

Sequential Consistency (Lamport):
                                                                                           W(x=1)
    "... the result of any execution is the same as if the operations of all the   C1
    processors were executed in some sequential order, and the operations of
    each individual processor appear in this sequence in the order specified                               W(x=2)
    by its program."                                                               C2
All operations are totally ordered                                                                     R(x) 2
    total order respects local order of operations at clients                      C3
                                                                                                                       0/1/2
Sequential vs linearizability?                                                                                      R(x) ?
                                                                                   C4
    sequential is weaker than linearizability (can have stale reads)
    but strong compared to many models                                                  W(x=1)   R(y)1 0
                                                                                   C1
                                                                                        W(y=1)   R(x) 1? Must be 1 and
                                                                                   C2                      never 0
                                                                                                                         6

                             Question
Which of the following is a STRONGER consistency model?
(a) Eventual
(b) Sequential

                                Question
Which of the following is a STRONGER consistency model?
(a) Eventual
(b) Sequential

Answer: (b)
Explanation: Sequential is stronger – it provides a total ordering of
operations and respects client’s local order

 Consistency Spectrum

                             Faster reads and writes

          Eventual                                            Sequential       Linearizable
                                     More consistency

Linearizability is easy to program against, but can lead to low performance/availability
Eventual consistency is performant and leads to high availability, but hard to program against
There is a variety of options in-between
                                                                                                 7

Causal Consistency

No total order of operations
Available under partitions                                                                  Causality, not messages
                                                                        W(x=1)
Avoids many inconsistencies that happen with eventual              C1
Operations must respect partial order based on                                      R(x)1      W(y=1)
information flow or causality                                      C2
     Operations from same client are causally related                                R(x)                     R(y)1   R(x)
     If client C1 does a write and a read at client C2 sees it,    C3
     then these ops are causally related                                         may return 0 or 1                    must
     Transitive                                                                                                       return 1

           Eventual                                           Causal        Sequential               Linearizable        8

 Session-based Consistency Models [Terry et al. 1994]

Monotonic reads (MR) – intuitively, reads cannot go back in time
        if a client issues read R1 and then R2, R2 must at least observe the state as of R1
Monotonic writes (MW) – if a client issues write W1 and then W2, clients must see W1 before W2
Read my writes (RMW) – if a client issues W1 and then R1, R1 must see the effects of W1

All these models are available in the presence of partitions

                         MR

          Eventual      MW                    Causal           Sequential   Linearizable
                      RMW                                                                   9

                              Question
Which of the following is TRUE?
(a) Causal consistency implies monotonic reads
(b) Causal consistency implies read-my-writes
(c) Both (a) and (b) are true
(d) Both (a) and (b) are false

                                 Question
Which of the following is TRUE?
(a) Causal consistency implies monotonic reads
(b) Causal consistency implies read-my-writes
(c) Both (a) and (b) are true
(d) Both (a) and (b) are false

Answer: (c)
Explanation: Causal consistency respects client’s local order, which ensures
that reads do not go back in time and clients always see their own writes.

Newer Consistency Models

CRDTs (Commutative Replicated Data Types): Data structures for which
commutated writes give same result [INRIA, France]
    E.g., value == int, and only op allowed is +1
    Guaranteed to eventually converge
    Effectively, servers don’t need to worry about consistency and
    conflict resolution

Red-blue Consistency: Rewrite client transactions to separate ops into red
ops vs. blue ops [MPI-SWS Germany and others]
      Blue ops can be executed (commutated) in any order across DCs
      Red ops need to be executed in the same order at each DC
      Composite model: blue ops are eventually consistent and red ops are
      strongly consistent

                                                                             10

Newer Consistency Models (Contd.)

Bounded staleness
    Guarantees that data lags at most by K versions or T time units
    User or app can set K or T on reads

Probabilistically Bounded Staleness (PBS)
    expected bounds on staleness with respect to both versions and time
    SLA-style consistency predictions

                                                                          11

                               Question
Which of the following is a CRDT?
(a) A value of type integer with the only operations allowed being
    additions and subtractions
(b) A value of type string that supports appending additional
    characters to the end of the string

                              Question
Which of the following is a CRDT?
(a) A value of type integer with the only operations allowed being
    additions and subtractions
(b) A value of type string that supports appending additional
    characters to the end of the string

Answer: (a)
Explanation: Additions and subtractions to an integer commute with
each other. Appends to a string do not commute.

   The Consistency Spectrum

[1] Viotti and Vukolic 2016   12

Which Consistency Model should you use?

•   Use the lowest consistency model that is
    “correct” for your application
     • Gets you fastest availability

                                               13
```

#### Transcript

Hi everyone, this is Aishwarya. And today we are going to be talking
about different consistency models. So in the previous lectures we talked
about eventual consistency, but it turns out that there are many more
consistency models that are out there, and so we are going to be talking
about some of them today. Before we go into that, let's see, what exactly do we mean by
a consistency model, right? A consistency model is nothing but the
contract between the distributed system and the end application or the application
development developer, right? And it basically dictates what results
the system can return upon an operation. So in a distributed system, you would have multiple concurrent clients
that are interacting with the system, doing reads and
writes on the multiple copies, right? So on the right here, we have such
a distributed system where we have three copies of an object and these objects
actually have different values and concurrent clients
are interacting with the system. So depending upon like how these
operations are performed on these replicas, the guarantee that the system
offers would vastly differ, right? And consistency model exactly
dictates what those guarantees are. And specifically it dictates what
values can different operations return, like how these different
operations are ordered, how they are performed on these replicas,
what values they return. And these are all dictated by
the consistency model that the system provides. So it's basically the contract that
the system needs to adhere to. So the system developer can design or
implement the system in any way, they can optimize it in any way as long
as it doesn't violate the contract. And the application developer needs to
understand clearly what the contract is so that they can develop their
application in a correct manner. Okay, so it turns out that there are many
different consistency models out there. In fact, it's a spectrum. So on the left you have
the weakest consistency model, which is eventual consistency. And as you go towards
the right on the spectrum, the consistency guarantees that the system
offers become better and better. So at the right you have strong
consistency models like even, sorry, sequential consistency or
linearizability. So what's the catch? As you move towards the right
of the spectrum, although you get strong consistency guarantees,
the performance of the system gets worse. And more importantly,
the availability that you get, especially when there's a partition,
is much worse. So for example, the consistency models
on your right, like linear stability and sequential consistency, are not
available when there is a partition. Whereas eventual consistency,
because it's a weak guarantee, we'll exactly talk about
what the guarantee is. But because it's a very weak guarantee,
the system can provide very good performance and
availability in the presence of partition. Okay, so first,
let's talk about eventual consistency. So Cassandra offers eventual consistency,
right? Which is the system that we saw earlier. Cassandra is actually based on an earlier
system from Amazon called dynamo. So eventual consistency dictates
that if writes to a key stop, then at that point all the replicas
of the key should converge. Basically they should all be identical and
have the same values for that key, right? So what that means is when clients
are interacting with the system, and let's say they're trying to read
the value of a particular key, the read could return any
of the older values, right? It need not necessarily return the latest
write that was performed to the key. So let's look at that with an example,
right, so here you have client C1, which performs a write to key x,
and it's updating x to one, right? And basically we have like sort of
a timeline here where we have two bars. The bar on the left indicates when the
operation was initiated by the client, so indicated by rec. And then the bar on the right basically
indicates the point at which the client received the response and
the operation completed, right? So that's what we mean
by this representation. So you have the request from the left and
then the response on the right, and the operation spans throughout from
the request to the response, right? So this is something that we'll
be using throughout this lecture. Now let's say we have another client C2,
which tries to update x to 2. And then let's say you have client C3,
which well after client one received the response for
the first write, initiates a read. In eventual consistency,
you could actually see an older value. Let's say x was initially zero,
so this read could return zero. Now let's suppose that another client C4,
tries to read x, right? And it's doing this well after both
the updates from C1 and C2 have completed, the system could still return zero. So as you can see, this is like a very
big guarantee that the system offers. So why do systems want to offer this,
right? That's because eventual consistency
is very performant, and eventual consistency also offers
very good availability guarantees. So in particular, eventual consistency, the system can allow
mini concurrent writes. Basically, different replicas could be
updated by different clients concurrently. You don't have to do
a lot of coordination. And what that means is that even if there
is a partition and some replicas are not reachable, the system could be available
in both the partitions, right? So a system that offers eventual
consistency is basically in the spectrum of availability and
partition tolerance and cap. So it doesn't give you strong consistency. So one thing to note with eventual
consistency is that a system that is providing eventual consistency should have
a way for merging concurrent rights or resolving conflicts when you have
concurrent rights to the same object. So for example here, right, like c one, let's say it's updating one replica and
of x and updating it to one. C2 is updating a different replica and
updating to two. So how do you eventually ensure that
both these replicas converge and have the same values? So you need to be able to resolve
between concurrent versions or conflicting object versions. Different systems use
different ways to do that. Like for example, in Cassandra it uses
the latest timestamp wind policy. So basically each update is
associated with the timestamp. So in Cassandra it's the timestamp of
the coordinator when the operation was performed. And you can basically to resolve
conflicts between two versions, you just compare the timestamps
of these two versions and just pick which one is the latest
as the latest version. And that would be the version that would
eventually survive on all the replicas, right? Okay, now let's talk
about strong consistency. So strong consistency models
are the other end of the spectrum, and linearizability is one of the strongest
consistency models that are out there. In fact, this is what we refer to
when we mean strong consistency. This is the C in the cap theorem. So, in linearizability, intuitively,
each operation that's performed by a client is instantaneously in real
time, visible to all the other clients. More formally, in linear accessibility, all the operations that are performed by
different clients are ordered in such a way that the order respects
the real time ordering of operations. So the total order of all the operations
respects the real time ordering of operations. So for example, if operation A completes
and then another operation B begins, then A is ordered before B. So for example, here you have two
operations, one from client C1 and another from client C3. And the read happens in
real time after the write. What that means is the read should
be ordered after the write, and it should see the fx of the write. So the read should here return
the value of the write. It will return one. Now, what if there
are concurrent operations? For example here, let's say you have
another client C2 issuing a write x of 2. Then these two operations from c two and
c three are concurrent to each other. Then in linearizability you could
order them in any way as long as the total order is valid in
the sequential order, right? So you could either order in this example,
c3 s read before c2s or after. If let's say you were to order
the c3 read before c2 strike, then c3 read here would return one. If you were to order it after c2 straight,
then it would return two. But both are valid in linearizability. Let's extend this example. Let's say you had another client c4,
which again issues a read. And this read is happening in
real time after c1 right, and it's also happening in real
time after c3 is write. So this read from c three and
the read from c four can both return one. That's valid because both c3 read and
c four's read are concurrent to c2. So you can order them in any way. So you could order here in this example
when both of them are returning once they have ordered ct read and
c4 read before c2 straight. Let's suppose you have
ordered c three's read after c2 write, so
c3 is returning two on that read. Now, what should c4 return
on the read to x for it to be valid under linearizability? So let's see this example in more detail. Note that C force read as being in
real time happening after c3 suite. So it should be ordered after c3 suite, which means that you have to see two,
you cannot see one. So that's what we mean by the total
order in linearizability, such that it respects the real
time ordering of operations. Okay, this is a very strong guarantee. Makes it so
that the distributed system appears as if there is just single copy in the system. So it hides in some way the fact that
things are replicated from the end applications, but it rates of some
performance and availability. So you cannot have a system that
provides both strong consistency, that is, linearizability, and be
available in the presence of partitions, we have another strong consistency model,
which is sequential consistency. So sequential consistency was
introduced by lamput, and here's the definition that lamput gives. I'm not going to read that. So in sequential consistency two,
all the operations are totally ordered, but the total order just respects the
local order of operations at the clients. But it doesn't respect the linear real
time ordering like linear accessibility, right? So sequential consistency is
definitely weaker than linearizability. So you could have stale reads
in sequential consistency. Because in sequential consistency,
if a client performs a write and then there is a read much after that,
and that happens in a different client, then you don't need to see
the result of the write. If both of these are happening in the same
client, then you need to see the results of that write in the second read because
you need to respect the client order in sequential consistency, but
it's still strong compared to many models. So let's look at the same
example from the previous slide. So we had these four clients where
these clients are performing different operations. Remember in the previous slide I
told that when the client c four is performing the read, it can only return
to in sequential consistency you could see any of the previous reads,
because in the total order you could order c four much before c1s and
c2s and c3s read. That's a valid total order that respects
the local order at different clients, because all the clients
just have one operation. So you could order. Basically there is nothing tricky
here when it comes to local order, and that's a valid total order. You don't, you can just order c four
much before c one, c two and c three. And that's a valid total order that
is spec sequential consistency. But this wouldn't respect linearizability. Now let's look at a slightly
different example. So we have again two clients. Client one is performing
a write updating x1, and it's performing a read to y, and
client two is performing a write to y and updating it to one, and
it's also performing a read to x. Now what can these two reads return? These two reads can very well return one. So basically they can both
return the latest values. Can they both return
zero at the same time? For example, let's say the first client, the read at the first client to
y returns zero under sequential consistency, can read to
x at client c2 return 0. So in sequential consistency you cannot
return zero, you have to return one. Here. This is because you have already
ordered the read operation at C1 before the write operation at C2,
because the write of write where you update y equal to
one is not reflected by the read. The read is still returning
the older value zero. So you have already ordered C1 write and
c one's read before C2 write. So you have because you have to
respect the local order at clients. The read at c two should appear
after the write at c two, but the write at c two is ordered after
the write and read at c one, which means that the read Athenae c two should
see the effects of the write at c one. So we have looked at the different
consistency models at the ends of the spectrum. So you have linear accessibility,
which gives you very good guarantees, which makes it actually very
easy to program against. So it makes the job of the application
developer much easier when the system is providing linear accessibility, but
it comes at the cost of performance and availability. But if you have a system that
offers eventual consistency, although it's offering you good
performance and availability guarantees, it can be sometimes very hard to program
against because the application developer has to now deal with all the weird
behavior from eventual consistent systems because it could return any of the older
values when there are concurrent writes happening in the system. So people have come up with many other
consistency models that are stronger than eventual consistency, but still offer some good performance and
availability guarantees. So it makes the job of
the application developer easier, but while still not sacrificing
availability and performance. So we're going to take a look at some
of those models next in this slide. So now let's take a look
at causal consistency. So in causal consistency there
is no total order of operations, unlike even strong consistency models like
linearizability or sequential consistency. As a result, Causal consistency is
actually much more available under partitions. It's a weaker model than the strong
consistency model that we looked at, but it still avoids many inconsistencies
that happen with eventual consistency. This is because in causal consistencies, operations respect the partial order
of causality between operations. So what operations
are causally related exactly? So operations that are from
the same client are costly related. And if a client C1 performs a write,
and then let's say a different client, C2, performs a read, and this read sees
the effect of the write and then the read becomes causally related to that write,
and causality is also transitive. Let's look at it from an example. So let's say you have an operation
from C1 updating x equal to 1. Let's say you have another read at C2,
and then this read observes the effect of that write, then the read and the write
becomes costly related to each other. Now, let's say C2 performs another
write of updating y equal to 1. Now let's say there is a read at c three. This read can return either zero or one. There is no restriction on this read
that's dictated by causal consistency. So this read is free to
return either zero or one. Now let's suppose there is another
read at c three which is reading y and it returns one. Now again, you have a causality
between the right updating y equal to 1 and this read,
that is reading 1 at C3. Because of transitive nature of causality,
C1's right of x equal to 1 and C3's read of y equal to 1 become
causally related to each other in that this read should come after
that write to respect causality. Now, let's suppose that
there is a read to x at C3. What should c three return? The read at c three should return one. Here. This is because this read
is causally related to the write of x equal to 1
that happened at C1, right? Because of causality is transitive,
you inherited the causality, right? So this read at c three,
the last read at c three is costly, related to the write at c one,
so it should return one so it cannot return any old value like zero. So that's causal consistency. So in the spectrum,
causal consistency is much more stronger than eventual consistency because
it respects causality and orders costly related operations in
a manner that always respects causality. But it still doesn't provide you with a
total order like sequential consistency on linear stability, but it's much more
available compared to those two models. There are also, other models that
people have proposed in the past, and there is a bunch of models, in fact, and all of them together are called
session based consistency models. So we have many session
consistency models, the first of which is monotonic reads. Intuitively, monotonic reads dictate
that reads cannot go back in time. So, for example,
if a client issues a read R1, and then let's say it issues another read R2. And then let's say you observe
some state on r1, you can. On R2, you cannot observe
a state that's older than R1. So you have to at least observe
the state at least as latest as R1, which essentially means is that your
reads cannot go back in time, okay? Then you have something
called monotonic writes. That essentially means that if
a client issues a write W1, and then let's say it performs another
write W2, then all the other clients in the system should see the fx
of W1 before it sees the fx of W2, right? So that's monotonic rights, and you have another session consistency
model that is called read my writes. In read my writes,
if let's say a client issues a write W1, and then the same client issues R1,
then R1 should see the effects of W1. So basically, if there is a write
operation and a read operation, and both of them are happening
in the same client session, this read operation should return what the
write set or something later than that, right, it should see the effects of this,
right? So that's what read my rights dictates. So many practical systems provide
some of these guarantees, and these are referred to together as
session-based consistency models. And all of these models are still
available in the presence of partitions. So that's the good thing
about these models, but they are still much stronger
than eventual consistency, because in eventual consistencies,
your reads could go back in time. Your writes need not be ordered in
the way that it respects the order in which writes were performed
in a client session, or your writes need not
see your latest write. So, in a way that these three models are
stronger than eventual consistency, but it's difficult to compare
these models with each other. So in some sense, they are like,
this is only a partial order, this is not a total order, right? The order of different consistency
models is just a partial order. So these three session-based models
are stronger than eventual, but with respect to each other,
they are not comparable. Causal consistency is stronger than all
of these three session-based models. In the recent years, researchers and
practitioners have proposed newer consistency models and we're going to
take a look at a few of them now. So, the first is CRDT, or
Commutative Replicated Data Types. This is actually not
a consistency model as such, but CRDT is referred to a class of data
structures that have a certain property. In particular, all the write operations to CRDT data
structures commute with each other. So what does that mean? That means that if you have two write
operations to the same data structure, it doesn't matter the order in which
you execute these two operations, they will always produce the same result. For example, let's say you have a CRDT
data structure, which is a simple integer. And let's say the operation that's
allowed on it is just an increment by 1. Let's say you have two clients, C1 and C2. C1 performs an increment by 1, C2
performs an increment by 1 again, right? It doesn't matter how you order these
two operations from the clients. You could order client one's operation
first and then client two or you could order client two and
then client one. Then result is the same,
the value is incremented by two. So that's the power of
commutative data structures. So where this helps is that,
the system when the data structure it's implementing CRDT, it doesn't
need to worry about consistency. Specifically, it need not worry
about resolving conflicts, because no matter the perform order
in which you perform the operations, the end result is going to be the same. You just need to ensure that all
the replicas perform all the operations. You don't have to worry about
resolving conflicts and to figure out which is the final value
the replica should hold, and so on, right? So this makes the system
development much easier. So that's the power of CRDTs. Related to CRDTs is the notion
of red-blue consistency. So researchers realized that it's often. Often not the case that all operations
commute with each other, right? Only some of them might commute with
each other while the rest do not. So, they realized that you could
rewrite client transactions and separate them into two
classes of operations. One they called red operations, and
the other they called blue operations. Blue operations are nothing but
operations that commute with each other. And so, they can be executed simply in
any order across different data centers. Whereas red operations
are much more stringent, and they cannot be executed in any order. So, red operations,
necessarily should be executed in the same order across
all the data centers. So, this red/blue consistency
essentially is a composite model, right? You have some operations,
that is blue operations, which are eventually consistent,
and then you have some operations which are red operations that
are strongly consistent. So, you can basically put together
a system that has strong consistency for summer operations and
eventual consistency for some operations. So, you get to have the most performance
for those blue operations and the most consistency for
the red operations. Now we have also some
staleness related models. The first one is bounded staleness. In bounded staleness, it's guaranteed
that the system will not return data that's more than K versions or
more than T time units would. For example, clients would specify
the value for K and T and ask for data that's not more than K versions or
T time units older. Then you have probabilistically
bounded staleness or PPS, where in this consistency model there
is an expected bound on the staleness that the system can return both
with respect to versions or time. So, here you could imagine having
SLA-type consistency guarantees. In the system, in 99% of the cases would
not return a version that's more than K versions old or return a data that's
more than T time units older, right? So, these are some new consistency models. I've taken this figure from a recent
survey paper that surveys different consistency models and tries to produce a partial order
of all the consistency models. So, this is actually the whole
consistency spectrum. And we have looked at some of
the points in the spectrum, but there are also many more
models that we haven't discussed. Okay, so we have looked at these
many different consistency models. So, how should you choose the right type
of consistency model for your application? Basically, you choose the lowest
consistency model that is required for the correctness of the application, because that gives you
the fastest availability, right? You don't want to get any stronger
than that or any weaker than that. So, that brings us to
the end of this lecture. Thank you.

### 08 - 2.1. Introduction and Basics

Slides: `C3_TimeAndOrdering_A_CSRAfinal.pdf`

#### Slide text

```
•   You want to catch a bus at 6:05 pm, but your watch is off by
    15 minutes.
     – What if your watch is late by 15 minutes?
        • You’ll miss the bus!
     – What if your watch is fast by 15 minutes?
        • You’ll end up unfairly waiting for a longer time than you
          intended.
• Time synchronization is required for both
   – Correctness
   – Fairness

•   Cloud airline reservation system
•   Server A receives a client request to purchase last ticket on flight
    ABC 123.
•   Server A timestamps purchase using local clock 9h:15m:32.45s,
    and logs it. Replies ok to client.
•   That was the last seat. Server A sends message to Server B
    saying “flight full.”
•   B enters “Flight ABC 123 full” + its own local clock value
    (which reads 9h:10m:10.11s) into its log.
•   Server C queries A’s and B’s logs. Is confused that a client
    purchased a ticket at A after the flight became full at B.
•   This may lead to further incorrect actions by C

•   End hosts in Internet-based systems (like clouds)
     – Each have their own clocks
     – Unlike processors (CPUs) within one server or
        workstation which share a system clock
•   Processes in Internet-based systems follow an
    asynchronous system model
     – No bounds on
          • Message delays
          • Processing delays
     – Unlike multi-processor (or parallel) systems which
        follow a synchronous system model

•   An asynchronous distributed system consists of a number of
    processes.
•   Each process has a state (values of variables).
•   Each process takes actions to change its state, which may be
    an instruction or a communication action (send, receive).
•   An event is the occurrence of an action.
•   Each process has a local clock – events within a process can be
    assigned timestamps, and thus ordered linearly.
•   But – in a distributed system, we also need to know the time
    order of events across different processes.

•   Each process (running at some end host) has its own clock.
•   When comparing two clocks at two processes:
     •   Clock Skew = Relative Difference in clock values of two processes
           • Like distance between two vehicles on a road
     •   Clock Drift = Relative Difference in clock frequencies (rates) of two processes
           • Like difference in speeds of two vehicles on the road
•   A non-zero clock skew implies clocks are not synchronized.
•   A non-zero clock drift causes skew to increase (eventually).
     – If faster vehicle is ahead, it will drift away
     – If faster vehicle is behind, it will catch up and then drift away

•   Maximum Drift Rate (MDR) of a clock
•   Absolute MDR is defined relative to Coordinated Universal
    Time (UTC). UTC is the “correct” time at any point of time.
      • MDR of a process depends on the environment.
•   Max drift rate between two clocks with similar MDR is 2 *
    MDR
•   Given a maximum acceptable skew M between any pair of
    clocks, need to synchronize at least once every: M / (2 * MDR)
    time units
     – Since time = distance/speed

•   Consider a group of processes
•   External Synchronization
     –   Each process C(i)’s clock is within a bound D of a well-known clock S external to the group
     –   |C(i) – S| < D at all times
     –   External clock may be connected to UTC (Universal Coordinated Time) or an atomic clock
     –   E.g., Cristian’s algorithm, NTP
•   Internal Synchronization
     –   Every pair of processes in group have clocks within bound D
     –   |C(i) – C(j)| < D at all times and for all processes i, j
     –   E.g., Berkeley algorithm

•   External Synchronization with D => Internal
    Synchronization with 2*D

•   Internal synchronization does not imply external
    synchronization
     – In fact, the entire system may drift away from the
        external clock S!

• Algorithms for clock synchronization
```

#### Transcript

Hi there, ah, so
in this series of lectures, we'll look at, uh, time
in distributed systems. Uh, time is a very important
and challenging concept, and, uh, we have to, uh,
either solve it as an issue or get around it,
uh, in, uh, some way. So, uh, here's an example
of, uh, why, uh, time is an important issue and
why you need synchronization. Suppose you wanna catch
a bus, at 6:05pm. But your watch
is off by 15 minutes. If your watch is,
uh, 15 minutes late, essentially you're gonna
miss the bus, cause you're gonna arrive
15 minutes late at the bus stop. If your watch is 15 minutes
early, maybe you'll end up, uh, waiting quite a long, uh, time,
15 minutes extra, while you might have been doing, um, something else
that was more useful. So, uh, because your clock
is not synchronized, because your watch
is not synchronized, uh, either you have
a violation of correctness, when you miss the bus, or violation of fairness, when you end up waiting
too long for the bus. What about in the cloud? Why is synchronization
needed in the cloud? So let's consider an example of a cloud airline
reservation system. So, this might be one
of the, uh, online airline- airline reservation sites that
you go to to book a flight. Um, uh, Server A receives, uh,
a client request, uh, to purchase the last ticket on a flight, say ABC123. It, um, replies to the client, uh, and simultaneously, uh, timestamps the purchase, uh, wi-with its clock
as 9h:15m:32.45s. It then logs it on desk. It replies ok to the client. Uh, now, that was
the very last seat, so the flight
is not full-now full. So A sends a message to Server
B saying the flight is full. B enters, uh, the information
that this particular flight is full into its log along
with its own local clock value, which happens
to read 9h:10m:10.11s. Notice that this is different
from server A's time, because a-after all, the two
servers are not synchronized in terms of their clocks. Now Server C,
a third server, comes along and queries A's and B's logs and it finds that A
has, uh, purchased a, uh, ticket on behalf of a client at 9:15, while the flight
was actually full at 9:10. And this confuses C and this may
lead, uh, C to take actions that are in fact, incorrect. Uh, and, uh, for instance, C might assume that more, uh,
seats have opened up on the flight and
that's not gonna be, uh, good or correct for any
of the passengers. So if A and B had been
synchronized in their clocks, this issue would not
have, uh, happened if both the clocks
had read exactly the same at any point of time. This iss-issue
would not have arised. So why is, uh, synchronizing
the clocks of different, uh, uh, uh, processes
so challenging, uh, in, uh, internet-based
systems like clouds? Well, each of the, uh, processes, uh, run on their own clocks, typically this is
a system clock, uh, on, the motherboard
of the, uh, machine on which that particular processor, uh, is running, where this process
is, um, uh, scheduled. Uh, but, uh, unlike
the processors on a, uh, single machine, which share
the same system clock, in a distributed system which is known as an
asynchronous distributed system, which, uh, is an internet,
uh, based system the different processes running
on different machines don't necessarily share
the same system clock. Uh, essentially all they share
is a network through which
they can send messages. Also there are no bounds on how long messages
take to get delayed, and there are no bounds
on how long processes take to process
individual instructions. This is what is known as the asynchronous
distributed system model. This is unlike the synchronous
distributed system model, which is true in multi-processor
or supercomputer or parallel systems where
many processes share a single system clock. And this, uh, asynchrony
makes it challenging to, um, synchronize clocks because of the
unpredictable message delays and you'll see this, uh,
quite soon as we go along. So, uh, some definitions
before we proceed. An Asynchronous Distributed
System consists of a number of processes. Uh, processes is
the plural of process, and, uh, each process is, what you might normally imagine a-a process is, it consists
of its own code, uh, its own heap, its own program counter, its own stack, its, uh, registers
and so on and so forth. So all of these put together, uh, all count
as the processes state. This includes the value
of its variables and everything. Now each process may change
its state by taking actions. An action might be
an instruction, uh, it may increment a variable and that changes that variable so it also changes
that process's state. Or it might send a message
to someone else, to some other process, or it might just receive
a message from another process. These are the three kinds
of actions, or events that can happen,
uh, in this system. An instruction, a message send
to another process, or a message being received, from another process. Now each process
has a local clock, um, and events within a process can be assigned timestamps, based on this local clock, because a local clock
only increases linearly, it only moves forward, it never moves backwards,
or- and it never gets stuck. Okay, so events within a given
process at a given process, can be ordered linearly. However, what we really wanna do
in a distributed system is order events across processes we want to say that this event
at Process A, um, and this other event
at Process B, uh, happened
in this particular order where, uh, maybe the first event
at Process A occurred before. So that's
the challenge over here. So, uh, when you want
to synchronize, uh, clocks across different processes in a group, um, uh, there are two terms
that come into play, they are
clock skew and clock drift. Clock skew is
the relative difference in the clock values
of two processes, while clock drift is
a reler-relative difference in their speeds, or their clock frequencies
or their clock rates. Uh, think of this as, uh, two
vehicles moving on the road. Clock skew is
the distance between them at any point of time, and
the distance may not be fixed. If the two, uh, vehicles are,
uh, moving at the same speed, then the clock skew will stay
the same as always. Uh, but if they are moving
at different speeds, then the clock skew
might change. Clock drift is the difference in
the speeds of the two vehicles. And so, a non-zero clock skew, uh, implies that clocks
are not synchronized. So what we really wanna do
if we wanna synchronize clocks is we wanna get
a non-zero clock skew. Uh, sorry- uh, sorry, we wanna
get a clock, zero clock skew, we want to have no difference between the clock values
of the two processes. In non-zero clock drift,
a difference, um, uh, in the speeds
of the two process clocks causes, uh, the two clocks,
to, uh, eventually drift. Clauses-causes the clock skew
to eventually increase. Okay, the faster vehicle
is ahead on the road, uh, it will drift away and the
clock skew is gonna increase. If the faster vehicle
is behind the slower vehicle, then it will catch up and eventually
then it will drift away. Um, uh, well ahead in front, and the clock skew will
eventually increase. So what we really want
to-to do is we want to get the clock skew,
uh, down to zero. So how often
do you wanna synchronize the clocks
of different processes? Well, uh, this sort
of defen-depends on the maximum drift rate
of the clock. Um, the absolute maximum
drift rate or absolute MDR is defined relative
to the UTC time, which is the correct time
at any point of time. The UTC time is maintained
by correct atomic clocks, um, uh, at standards bodies. Uh, the MDR for process, of a given process depends
on the environment. Okay, so MDR is, uh, uh, is-is
devin-defined with respect, uh, to something and,
uh, when you say absolute MDR, it's defined with respect
to the, uh, UTC. Now the maximum drift rate
between two clocks with similar MDR,
with the same MDR, with the same absolute
MDR is 2*MDR. Why is this? Well in the worst case, one
of these clocks may be MDR ahead or faster than UTC. The other clock may be
MDR slower than UTC, and so the-the
relative difference between them is (2*MDR). So given a maximum acceptable
skew M between any pair of, uh, process clocks- um, clocks
are two different processes, you need to synchronize,
uh, the clocks, uh, once every M/(2*MDR)
time units, okay, where MDR is your maximum, uh,
drift rate that you know for the individual processes and M is your maximum
acceptable skew, which the application
can tolerate. Why is it M/(2*MDR)? This is the same reason
as time=distance/speed. Now there are two terms
that come into play when you wanna synchronize,
uh, process clocks. They are external and
internal synchronization. In external synchronization, each process, uh, uh, clock
is, uh, synchronized with respect to an external,
um, uh, time source, such as a UTC time source. So process i's, uh, clock may
be, uh, at most D, uh, seconds, um, uh, eh, in error compared
with the external times clock. So, |C(i)-S|, is, uh, always
less than the bound D at all points of time. Okay, so examples of algorithms
that try to achieve external synchronization
are the Cristian's algorithm and the NTP algorithm, which you will see later on
in this lecture series. On the other hand,
internal synchronization does not use an external source. Instead the processes in the
group themselves, um, uh, use, uh, each of theirs
clocks for synchronize. And this means that, uh, if you
wanna bound inside the group, then you wanna make sure that
for any pair of processes (i,j) the difference
between their clocks, the clocks skew between i and j, uh, the absolute value
of that is less than, uh, D. An example of an algorithm that, uh, achieves internal internal synchronization is the Berkeley algorithm. So, th-the external
and internal synchronization are related to each other. If you have
external synchronization in a given group,
with a bound of D, this automatically implies
internal synchronization with a bound of 2*D. Why is this? Well, in the worst case, uh,
a process may be D ahead of the external source, and another process may be D
behind the external source, so that the difference between
them and distance is 2*D. But the other way around
is not true, so, if you have internal synchronization, in a group, ah, then there does not imply
external synchronization with respect to any time source. Uh, in fact, the entire group
may drift away, as a whole, from a given external source, and this is one of the, um, uh,
uh, one of the disadvantages of using internal,
uh, synchronization. So next- in the next lecture,
we'll see, uh, some algorithms
that are used, and some techniques
that are used in real systems
for synchronizing clocks in, uh, cloud computing systems and in distributed systems.

### 09 - 2.2. Cristian's Algorithm

Slides: `C3_TimeAndOrdering_B_CSRAfinal.pdf`

#### Slide text

```
•   External time synchronization
•   All processes P synchronize with a time server S

                                 Set clock to t           Time
    P
    What’s the time?
                          Here’s the time t!
    S
                       Check local clock to find time t

• By the time response message is received at P,
  time has moved on
• P’s time set to t is inaccurate!
• Inaccuracy a function of message latencies
• Since latencies unbounded in an asynchronous
  system, the inaccuracy cannot be bounded

• P measures the round-trip-time RTT of message exchange

                               Set clock to t   Time
    P
     What’s the time?
                        Here’s the time t!
     S
                   Check local clock to find time t

•   P measures the round-trip-time RTT of message exchange
•   Suppose we know the minimum P  S latency min1
•   And the minimum S  P latency min2
     – min1 and min2 depend on operating system overhead to buffer messages, TCP time
        to queue messages, etc.

              RTT
                             Set clock to t
                                                    Time
P What’s the time?
                     Here’s the time t!
S                Check local clock to find time t

•       P measures the round-trip-time RTT of message exchange
•       Suppose we know the minimum P  S latency min1
•       And the minimum S  P latency min2
         – min1 and min2 depend on Operating system overhead to buffer messages, TCP
            time to queue messages, etc.
•       The actual time at P when it receives response is between [t+min2, t+RTT-min1]
                   RTT
                                 Set clock to t
                                                        Time
    P What’s the time?
                         Here’s the time t!
    S                Check local clock to find time t

•       The actual time at P when it receives response is between [t+min2, t+RTT-
        min1]
•       P sets its time to halfway through this interval
         – To: t + (RTT+min2-min1)/2
•       Error is at most (RTT-min2-min1)/2
         – Bounded!
                   RTT
                                 Set clock to t
                                                        Time
    P What’s the time?
                         Here’s the time t!
    S                Check local clock to find time t

•   Allowed to increase clock value but should never
    decrease clock value
     – May violate ordering of events within the same
        process

•   Allowed to increase or decrease speed of clock

•   If error is too high, take multiple readings and
    average them
```

#### Transcript

In this lecture
we'll be discussing, uh, one of the algorithms for external synchronization
of clocks in, uh, uh, processes
in a distributed system, and this algorithm is called
the Cristian's Algorithm. All the processes, uh,
in the group synchronize, uh, their clocks with respect
to an external time server. So process P
would send a message to the external time server
saying, "Hey, what is the time?" When the server receives this,
it checks its local clock, finds the time t,
puts it into the reply message, and then sends a message back. When the process P receives
this message, it uses the value, uh, t in the message
to set its local clock value. So, what goes, uh, wrong
with that particular protocol? Well, by the time the response
message is received at P from, uh, the external server S, the time in external server S
has moved on, because the response message
takes non-zero time, uh, to make its way through
the network to the process P. And so process P si-time, uh, uh, is again
going to be inaccurate. It's gonna be behind,
uh, what, uh, process, uh, uh, the external server S's
current time actually is. Uh, and so the inaccuracy
in this algorithm is a function
of the message latencies. Uh, since latencies
are unbounded in an asynchronous system, this is a problem because now
this means that the inaccuracy in this algorithm
can also not be bounded. So, uh, what, um, uh, P does
to measure the accuracy, is it measures the round-trip
time of the message exchange which is, uh, the time between
when P sent the original message and between when, uh, it receives the reply. Okay, we call this set the RTT
or the round-trip time. And using this it can calculate,
uh, the, um, uh, uh, error in, uh, the clock value
that it sets. Okay, so suppose, uh,
we know the minimum P to S, uh, message transmission latency
let's call this as min1, and the minimum S to P, um, uh, transmission latency, which is min2
on the reverse path. What do min1 and min2 depend on? Well, min1 and min2 depend on, uh, the operating system overhead to buffer messages, uh, the TCP time
to queue messages, and any-any, uh, overheads
on the network path from, um, uh, S to P and P to S. If you don't know
what min1 and min2 are, you can just set them
to be zero, that's fine. But essentially this allows
you to incorporate any known minimum overheads
on the, uh, transmission pads into the, uh, error and account for them in the error, and retain a better
error bound, essentially. So using these, uh, uh, values
of min1 and min2, now P can actually
set its time to be better, uh, so that it has
a lower error, uh, and essentially, uh,
the actual time at P when it receives a response is somewhere between t+min2
and t+RTT-min1. You'll notice that RTT is
clearly greater than min1+min2. Why is it only
as small as t+min2? Well, uh, this would be the case
where the response message from S to P took
the minimum time, the min2 time to, uh, transmit across so the time at P when it
receives its message is t+min2. All right, so that's
the lower case. The upper case, t+RTT-min1,
occurs when the P to S message, the original
"what's the time" message took exactly min1 seconds
to make it across, which means that RTT- uh, uh, min1 was the time that,
uh, was taken by the response to come across. So in reality, the real time when, uh, P receives
a response message is somewhere
in-inside this interval. So, essentially what happens
in Cristian's Algorithm is that, uh, uh, that P sets its, uh,
clock to be halfway in between these two values. So essentially it sets
its, um, uh, clock to be, uh, t+, uh,
(RTT-min2-min1)/2. Okay, so it's halfway,
that's halfway between, uh, the extremes
of this interval. Well this means that, uh, the
error in this new clock value that has been set is, uh, half
the size of this interval, which is (RTT-min2-min1)/2. And this is, uh, kind
of, uh, convenient here, uh, the better you know
min1 and min2, uh, the lower is gonna be the error
on the, uh, clock value that you set. So, this means that the, uh,
clock error can now be bounded, and as you notice, it's a
function of the round-trip time. The longer your
round-trip time is, uh, the more is going
to be your error. So shorter round-trip times
mean, um, smaller errors in the clock value that you set according to the
Cristian's Algorithm. So, a few gotchas here. When you set your clock value, um, you're only allowed
to increase your clock value but you should never
set it backwards, um, uh, this is because you
always wanna makes sure that the events
at a given processes are or-are ordered linearly
with respect to each other. Okay, so you wanna
make sure that, uh, if your algorithm is telling you to set your clock backwards, you just retain
your current clock value and continue moving forward. You are, however,
allowed to increase or decrease the speed
of the clock, uh, depending on what's been
happening in the algorithm. So, for instance, if the algorithm has
consistently been telling you, every time you run it, uh,
to set your clock forward, you might want to just
tweak your, uh, clock speed to be slightly higher so that,
uh, you know, eh, so that, uh, perhaps you're better in sync
with the external source. Once again, uh, there is, uh, Cristian's Algorithm
does not specify necessarily a way to increase or decrease
the speed of your clock, but you're allowed to do this. You can increase
or decrease its speed as long as you do not set
your clock itself backwards. Now you might take multiple
readings and the errors or the round-trip times
may be very high. Uh, you can take multiple
readings and then average out, uh, the, um, RTTs that you get,
uh, over those multiple readings and use that
to set your, uh, clock time.

### 10 - 2.3. NTP

Slides: `C3_TimeAndOrdering_C_CSRAfinal.pdf`

#### Slide text

```
NTP = Network Time Protocol

• NTP servers organized in a tree
• Each client = a leaf of tree
• Each node synchronizes with its tree parent
                         Primary servers

                                 Secondary servers

                                           Tertiary servers

           Client

   NTP Protocol
         Message 1 recv time tr1
                                   Message 2 send time ts2
                                                             Time
 Child
   Let’s start protocol
                                          Message 2          ts1, tr2
                     Message 1
Parent
                                      Message 2 recv time tr2
                  Message 1 send time ts1

What the Child Does

• Child calculates offset between its
  clock and parent’s clock
• Uses ts1, tr1, ts2, tr2
• Offset is calculated as
   o = (tr1 – tr2 + ts2 – ts1)/2

Why o = (tr1 - tr2 +
ts2 - ts1)/2?
•   Offset o = (tr1 – tr2 + ts2 – ts1)/2
•   Let’s calculate the error
•   Suppose real offset is oreal
     – Child is ahead of parent by oreal
     – Parent is ahead of child by -oreal
•   Suppose one-way latency of Message 1 is L1
    (L2 for Message 2)
•   No one knows L1 or L2!
•   Then
     tr1 = ts1 + L1 + oreal
     tr2 = ts2 + L2 – oreal

Why o = (tr1 - tr2 +
ts2 - ts1)/2?
•   Then
     tr1 = ts1 + L1 + oreal
     tr2 = ts2 + L2 – oreal
•   Subtracting second equation from the first
     oreal = (tr1 – tr2 + ts2 – ts1)/2 + (L2 – L1)/2
     => oreal = o + (L2 – L1)/2
     => |oreal – o| < |(L2 – L1)/2| < |(L2 + L1)/2|
     – Thus, the error is bounded by the round-trip-
     time

And yet…

• We still have a non-zero error!
• We just can’t seem to get rid of error
   – Can’t, as long as message latencies are non-zero
• Can we avoid synchronizing clocks altogether and still be able to
  order events?
```

#### Transcript

In this lecture, we'll be looking at one of the standards for synchronizing clocks
in the internet. The standard is called NTP. NTP stands
for Network Time Protocol. Uh, here the NTP servers,
which are managed, are organized
in a tree structure. Uh, I'm showing the tree
structure here with, uh, the root of the tree
or the primary server, uh, being shown here. That's the one, uh, that
has a UDC time added. There are secondary servers
that are, uh, the children of the primary, uh, server. And, uh, that
synchronize directly with the primary server. Then there are tertiary servers
which synchronize with their corresponding parent, uh, at the secondary
server level. Your client might be
one of the work statio- might be one of the leaves
in this, uh, tree, and I'm showing one
particular client over here. So essentially, each node
in the tree here synchronizes with its parent in the tree. How does it synchronize? Well here is how
the NTP protocol works and then we'll look
at how it sets the clock over the next few slides. So a child, uh, sends a message
to the parent saying, "Hey, let's start the protocol,
I wanna synchronize my clock." The message, uh, uh, uh,
sent by the parent in response is called message 1. Uh, the parent 1 respon-uh, records the time
at which it sends the message. This time is ts1 over here, and then the child
when it receives the message 1, it records
its receive time as tr1. Notice that these times are set
according to the local clocks at the corresponding processes. So ts1 is according
to the parent's local clock and tr1 is according
to the child's local clock, which of course
are not synchronized. Uh, the child then sends back
a response message, message 2. Records its sent time as ts2,
according to its own clock. And when the parent receives
a response, it, uh, marks, uh, the response received time as tr2 according
to its own clock. Finally, the parent sends
over the values of, uh, ts1 and tr2 to child, uh, and then the child
uses all these four values: ts1, tr1, ts2, and tr2
to set its clock. How does it set its clock? Let's, uh, look at it. So why is this particular offset
used by the child to set its clock? Why this particular
funky equation? So let's calculate
the actual error, uh, uh, due to this particular protocol. Suppose the real offset,
the real clock offset between the child
and the parent is, uh, oreal. We don't know what oreal
is, but let's say its oreal. This means that the child
is ahead of the parent by oreal and the parent is ahead
of the child by -oreal, or it's behind
the child by oreal. Now, the value of oreal
might actually be negative over here, right? So, uh, these two statements would still be true
in this case. Uh, suppose the one-way
latency of message 1 is L1, and similarly, the one-way
latency for message 2 is L2. We don't know the values
for L1 and L2, just because the clocks
are not synchronized, and this means that it's gonna
be, uh, hard, if not impossible, to measure the one-way
transmission latency. However, we can write down
the equations based on these variables. So the receive time
of message 1, tr1 equals the transmit si-uh,
the send time of the message 1 plus its, um, uh, uh, latency, uh, uh, message delay plus
the clock offset, oreal. Similarly, the receive time
of message 2 is, uh, equal to its send time plus
the message latency L2 minus, uh, the clock delay, because th-this message is going in the opposite direction as message 1. So, using
these two equations now, you can subtract the second equation from the first and this gives you, uh,
this equation for oreal. You can solve, uh,
for, uh, for oreal. Uh, and oreal turns out to be
this particular, uh, equation over when you massage the terms. And, uh, this first term
is in fact the same as, uh, the value of o
that you see up here at the title, uh,
part of this slide. And this means
that the second part in fact now becomes the error because now, uh, the
difference between oreal and o is bounded by, uh, (L2-L1)/2, and this is of course less than the |(L2+L1)/2|, and this is in fact
the round-trip time. So this means that the error, uh, in, uh, this particular algorithm, NTP algorithm, is bounded
by the round-trip time, um, uh, or at least half
of the round trip time in this particular case. Okay, so this is justification
for actually using this particular value o
to set, uh, the clock. However, we still
have a non-zero error. We just can't seem
to get rid of this error; it always seems to depend
on the round-trip time. Uh, whenever you have a non-zero
round-trip time it seems like, uh, the error is about half
of the round trip time. So the question arises, um, uh,
since it's getting so hard to synchronize clocks, why can't we just
not synchronize clocks and instead go directly
to the root of the problem, which is that we want
to assign time stamps to, uh, uh, uh, the, uh,
events that happen in a distributed system and do this without synchronizing clocks? We'll see how to do this
in the next lecture.

### 11 - 2.4. Lamport Timestamps

Slides: `C3_TimeAndOrdering_D_CSRAfinal.pdf`

#### Slide text

```
Ordering Events in a Distributed System
•   To order events across processes, trying to sync clocks is one approach.
•   What if we instead assigned timestamps to events that were not absolute time?
• As long as these timestamps obey causality, that
  would work.
   If an event A causally happens before another
   event B, then timestamp(A) < timestamp(B).
   Humans use causality all the time.
         E.g., I enter a house only after I unlock it.
         E.g., you receive a letter only after I send it.

Logical (or Lamport) Ordering
• Proposed by Leslie Lamport in the 1970s
• Used in almost all distributed systems since then
• Almost all cloud computing systems use some
  form of logical ordering of events

Logical (or Lamport) Ordering(2)
•   Define a logical relation Happens-Before among pairs of events
•   Happens-Before denoted as →
•   Three rules
     1. On the same process: a → b, if time(a) < time(b) (using the local clock)
     2. If p1 sends m to p2: send(m) → receive(m)
     3. (Transitivity) If a → b and b → c then a → c
•   Creates a partial order among events
     – Not all events related to each other via →

     Example
           A                    B               C             D     E
P1
                                                                         Time
                                E                   F     G
P2

                     H                              I                         J
P3
While P1 and P3 each have an event labeled E,           Instruction or step
these are different events as they occur at
different processes                                      Message

     Happens-Before
       A       B      C             D     E
P1
                                               Time
               E          F     G
P2

           H              I                         J
P3
  • AB                       Instruction or step
  • BF                        Message
  • AF

  Happens-Before (2)
       A        B   C             D     E
P1
                                             Time
                E       F     G
P2

            H           I                         J
P3•   HG
  •   FJ                   Instruction or step
  •   HJ                    Message
  •   CJ

In practice: Lamport timestamps
•   Goal: Assign logical (Lamport) timestamp to each event
•   Timestamps obey causality
•   Rules
     – Each process uses a local counter (clock) which is an integer
         • Initial value of counter is zero
     – A process increments its counter when a send or an
       instruction happens at it. The counter is assigned to the event
       as its timestamp.
     – A send (message) event carries its timestamp
     – For a receive (message) event the counter is updated by
                     max(local clock, message timestamp) + 1

     Example
P1
                                Time

P2

P3
               Instruction or step
                Message

 Lamport Timestamps
P1 0
                                             Time

P2 0

P3 0
                            Instruction or step
Initial counters (clocks)
                             Message

 Lamport Timestamps
P1 0
       ts = 1
                                                  Time

P2 0
               Message carries
P3 0                ts = 1
           ts = 1
         Message send            Instruction or step
                                  Message

 Lamport Timestamps
P1 0
       1   ts = max(local, msg) + 1
                = max(0, 1)+1                          Time
                     =2
P2 0
               Message carries
P3 0               ts = 1
           1
                                      Instruction or step
                                       Message

 Lamport Timestamps
P1 0           2
       1
                   Message carries                    Time
                       ts = 2
P2 0
                    2
                          max(2, 2)+1
                              =3
P3 0
           1
                                     Instruction or step
                                      Message

 Lamport Timestamps
                                        max(3, 4)+1
                                            =5
P1 0           2
       1               3
                                             Time

P2 0
                   2    3      4

P3 0
           1
                            Instruction or step
                             Message

 Lamport Timestamps
P1 0           2                       5      6
       1               3
                                                  Time

P2 0
                   2    3         4

P3 0
           1               2                         7
                               Instruction or step
                                Message

    Obeying Causality
          A              B       C                 D       E
P1 0                     2                             5       6
          1                          3
                                                                   Time
                         E           F         G
P2 0
                             2       3         4

                     H               I                                J
P3 0
                     1                   2                           7
•   A  B :: 1 < 2                           Instruction or step
•   B  F :: 2 < 3
•   A  F :: 1 < 3                            Message

    Obeying Causality (2)
            A            B       C                 D       E
P1 0                     2                             5       6
            1                        3
                                                                   Time
                         E           F         G
P2 0
                             2       3         4

                     H               I                                J
P3 0
                     1                   2                           7
•   H  G :: 1 < 4                           Instruction or step
•   F  J :: 3 < 7
•   H  J :: 1 < 7                            Message
•   C  J :: 3 < 7

 Not always implying Causality
          A                    B          C                 D       E
P1 0                           2                                5       6
          1                                   3
                                                                            Time
                               E              F         G
P2 0
                                      2       3         4

                    H                         I                                J
P3 0
                   1                              2                           7
 •   ? C  F ? :: 3 = 3                               Instruction or step
 •   ? H  C ? :: 1 < 3
 •   (C, F) and (H, C) are pairs of                    Message
     concurrent events

Concurrent Events
•   A pair of concurrent events doesn’t have a causal
    path from one event to another (either way, in the
    pair)
•   Lamport timestamps not guaranteed to be ordered or
    unequal for concurrent events
•   Ok, since concurrent events are not causality related!
•   Remember
     E1  E2 ⇒ timestamp(E1) < timestamp (E2), BUT
     timestamp(E1) < timestamp (E2) ⇒
                    {E1  E2} OR {E1 and E2 concurrent}

Next
• Can we have causal or logical timestamps from which we can tell if
  two events are concurrent or causally related?
```

#### Transcript

In this, uh, lecture today,
uh, we will, uh, look at Lamport Timestamps,
or logical timestamps, one of the most important building blocks in cloud computing systems and any kind of distributed systems. So, what we've seen so far, uh,
is that synchronizing clocks, uh, across, um, uh, processes
is a very hard problem and the reason we are doing
this is, essentially, because we want to order events, uh, across a distributed system, event that, events that occur
at different processes. So, uh, because, uh, proximate
relation is so challenging, why not, uh, just avoid doing clocks synchronization and instead, uh, directly assign timestamps to events. Uh, for this, uh,
the idea used here is, uh, the idea of causality. So, as long as the timestamps,
timestamps obey causality, uh, assigning, uh, the timestamps,
uh, to events might just work. Uh, this means, causality means, that if an event A causally happens before another event B, then the timestamp assigned
to A is less than the timestamp
assigned to B. What does causality mean? Causality means that one event
leads to another, that is there is
a path of events from the first event
to the second event. For instance, um, I can enter
a house only after I unlock it, so, the unlocking event, happens before the entering
of the house event. Similarly, you receive a letter,
only after I send it, so, the, uh, sending event
of the letter uh, happens before the, uh, receiving event,
of that particular letter. So, uh, logical or Lamport, um, uh, ordering and timestamps were proposed by Leslie Lamport in the 1970's, almost all distributed systems use it, uh, today, uh, and all cloud
computing systems, uh, or almost all of them, uh, use some form
of logical ordering, if not, Lamport timestamps, some variant of, uh,
Lamport timestamps is used. So, uh, the logical
or Lamport ordering defines a Happens-Before,
uh, ordering, uh, among pairs of events. Happens-Before is denoted as
a forward or horizontal arrow. There are three rules, uh,
that are used, uh, to determine whether or not two events are, uh, related by this
Happens-Before relationship. If the two events, a and b
are on the same process, uh, and, uh, the, uh,
time, uh, at event a, um, is less than
the time at event b, notice that this is the time using that processes
local clock, which only increases,
uh, eh, forward, which only moves forward, uh, if time a is less than time b
then a happens before b. 'Kay, this is fairly common
sense, y'know, this is like saying, uh, I, um...open the house, uh, I unlock the house and then, uh, uh, and then that event happens before me entering the house. Now, events might also happen
at different processes, so if, um, process p1 sends
a message m to process p2 then, uh, the, uh, sending
of the message is an event, similarly the receiving
of that message, is an event. The sending of that message m,
is an event that occurs at p1, while the receiving
of that message is an event that occurs
at a different process, p2. But we say, that the send of
that, uh, message m, that event, happened before the receive
of that event message m. Okay, this is like saying
I sent the letter and that happens before you receiving that letter. The third rule is transitivity
and essentially, it says, that if there are three events a, b, and c, such that, a happens before b
and also that b happens c, then it's also true
that a happens before c. And, this allows us to relate
very far away events, uh, to each other using
the Happens-Before relationship. The Happens-Before relationship, uh, creates only
a partial order among events, this means that, uh,
only some events, uh, only some pairs of events
are related to each other while a Happens-Before relationship, uh, not all events are. So, for instance, if processes, uh, never exchange messages
with each other, then all the events,
um, are, um, uh, essentially called
as concurrent events, they're not related
to each other, uh, at all, across different processes. Events within a process all
stid-are still related using the Happens-Before but across processes, you do not have the Happens-
Before relationship, at all. You'll see this, uh, notion
of concurrent events coming out as we discuss, uh, the examples. 'Kay, so these are the three
rules for, uh, using, uh, for, uh, deciding when
two events are, uh, logically related or causally related to each other. Let's see an example, here is
an example of three processes, P1, P2, P3, um, the time
goes from left to right. Uh, notice that the clocks
may not be synchronized here, at all. Uh, P1 executes
a local, uh, step, which we, uh, label
as an event A, then it sends a message to P2, the send event is labeled as B, the received event
is labeled as F, uh, P1 then executes
another instruction, C, uh, it receives a message
from P2 and the receive event
is labeled, as D, and then it sends
a message to P3, which, uh, is an event, uh, labeled, as E. 'Kay, and similarly P2
has a bunch of, uh, events, three events there, E, F, and G and P3 has three events,
H, I, and J. And a dot over here,
is an instruction or a step and an arrow here
shows a message. So, uh, here's what the
Happens-Before might look like, in this particular example,
uh, A clearly happens before B because these two are events
at the same process, P1 and the time at A
is less than the time at B, similarly B, uh,
happens before F, because B is the send of, uh, message and F is a received, of that same message. And now using our transitivity
rule, we can now say that, because A happens before B
and B happens before F, it's also true
that A happens before F. 'Kay, so essentially, what we
need is, we need a path, from one event to another, uh, in the causal space, uh, so that we can say
that the first event occurred before the second event. 'Kay, so let's see
some other examples of the Happens-Before relationship. Uh, the event H, which is at P3,
over here, uh, happens before, uh, the event G, which is at P2. Why is this? Well, there is a causal path that goes from H, to E, to F, to G, and therefore, H happens before G. Similarly, the event F at, uh,
P2 happens before, uh, the event J at P3. Why is this? Again, there is a causal path
that goes from F, to G, to D at P1,
to E, to J at P3. Similarly, H happens before J,
because again, there is a path that goes
H, E, F, G, D, E, and J. And finally, C happens before J
because, again, there's a path that goes from C, D, E, to J. So, you see several
examples here of, uh, the Happens-Before relationship, uh, being cleared out,
among pairs of events. So, how do you
assign timestamps? Which is what we really
wanted to do, right? So, how do you assign
these timestamps, so that, uh, thes-this causality
that we said, the logical ordering
is actually obeyed. Uh, so there are a few rules
that Lamport laid down, uh, to, um, assign timestamps, uh, each, uh, process uses
a local counter, which is an integer, we call this
as the process clock, 'kay. Uh, the clock is not the system clock, it's just an integer, the initial value of the counter
is zero, at each process. Remember that this is
a local, uh, counter so each process is the only one that can access and update its counter. Uh, now a process, uh, whenever
it executes an instruction or sends a message,
it increments it counter by one. 'Kay? And it assigns this new
timestamp to the, um, uh, uh, instruction event or
the sent event of that message. When it sends a message, the send, uh, message also carries the timestamp that was assigned the send event of that message. 'Kay, why is this, uh,
carried with the message? This is used
by the receiving process. When a process receives
a message, it looks at the timestamp
in the message, the send, uh, timestamp. It also looks at its local clock
value, it takes the max of those and then it adds one to it,
and it assigns this, uh, uh, value as the timestamp
of the receive event of that particular message. Why is this max operation done? Well, this is done because, you want to make sure that if two events are causally related, they get timestamps, uh, Lamport timestamps that obey that causality order. That the event that occurred
later on in the causal space gets a, um, higher,
uh, timestamp value. 'Kay, so let's see this, uh,
played out, uh, in action, uh, using our, uh, example. 'Kay, so this is the same
example as we had before, I removed the event names, uh, for-uh, so that
it's not cluttered. So initially, uh, all the processes start with, uh, uh, counters, uh, clocks which
are initialized to zero. Uh, then, uh, uh, process P1
executes a step, it assigns it a timestamp of 1, it increments its local clock, assigns it its timestamp of 1. Uh, P3, at the same time, um,
uh, sends a message, again it increments
its local clock to 1, it, uh, assigns this as
the send uh, uh, event timestamp and the message also carries this timestamp value of 1. Now, when P2 receives
this value, it looks at the, uh, message, uh, uh, timestamp,
which is 1 and its local clock, uh, which is 0, max
of those is 1, plus 1 is 2 and this is assigned as the timestamp of the received event, of this particular message. 'Kay, this insures
that the sent event, um, which happens before
the received event, uh, uh, uh, are getting timestamps, uh, which obey the causality and also, any event that occurred before, here, at P2, uh, would , uh, have
a lower timestamp than, uh, the received event
of this message. Now, carrying this forward, uh,
next what happens is that, uh, uh, P1 sends a message, uh, which it does by incrementing its, uh, local clock, uh, from 1 to 2, assigns this as
a timestamp to the send event, of that message and the message carries this timestamp. When P2 receives this,
uh, message it notices
that its local clock is 2, the message timestamp is 2, um, and the max of those 2
is 2 + 1 = 3 and that is assigned as the received timestamp, over here. Uh, similarly when, uh, P1
executes, uh, an instruction, it assigns it a timestamp of 3, uh, when P2 sends
a message to P1, uh, it increments its local clock from 3 to 4 and sends 4 as the, uh, timestamp
along with the message, when P1 receives it, it takes max of (3,4)
it adds 1 and that is 5 and that gives it,
the-the local clock, uh, value at its received event, that's also the timestamp
of the received event. Notice that, uh, P1
jumps from 3 to 5 from going from one event
to the next, and that's fine, as long as, the, uh, timestamp
of this event 3 is less than the timestamp of the next event, we're obeying causality. Carrying this forward, um, uh,
P3 gives a local instruction, which gets a timestamp of 2
because 1 is incremented by 1. When P1 sends a message to P3, it goes from a timestamp
of 5 to 6, it includes this in the message, when P3 receives this, it looks at the timestamp
in the message, 6, which is, uh, more than
the local clock value, 2, and so 6 + 1, 7 is assigned as
a timestamp to the receive, uh, event of, uh, this particular message from P1 to P3. So, that completes our example, but let's see, uh, a little bit, uh, how, uh, the timestamps
are assigned to the events that we said
were causally related. So, earlier we said
that A happens before B and you notice that here they get, uh, timestamps, uh, that obey that ordering,
so, 1 < 2. B, uh, happens before F, we said
earlier, and they get timestamps 2 and 3, which are, ordered
in that manner, 2 < 3. Similarly, A happens before F,
we said earlier, because the transitivity
and they are assigned times, times 1 and 3, respectively, and 1 < 3, which obeys causality. Uh, we saw a few other, uh,
causal relationships, H happens before G,
and they get timestamps, times 1 and 4, respectively,
and 1 < 4. Similarly, F and J get
timestamps of 3 and 7, which obey causality. H and J get timestamps of 1
and 7, which obey causality. And, C and J get timestamps of
3 and 7, which obey causality. However, there are some events, uh, which may not
be causally related. So, consider the two events
C and F, over here. There's really no causal path
that goes from C to F and also, no causal path
that goes from F to C, you can try to find a path, but, if you go forward
from C you'd only go to P3, over here, with J. If you go forward from F, again,
you'd only go forward to J. Uh, there is no causal path that
goes from C to F or from F to C. However, they get
the same timestamps, uh, these two events, which have no causal path,
from one to the other, are known as concurrent events. Consider these two events,
H and C, H over here at P3 and C at, uh, P1. They get timestamps 1 and 3, respectively. However, there is no causal path that goes from H to C
or from C to H, and so these 2, uh, events
are also concurrent events. However, they got Lamport
timestamps of 1 and 3, respectively, uh, at H and C, and this might seem to imply that these are causally related, but that's not necessarily true, uh, so this means that if two
events are causally related then there Lamport timestamps obey the causality, however, if you get Lamport timestamps for two events, uh, then that doesn't necessarily mean that the, uh, causality is in fact true
in between those two events. So, putting it in another way,
a pair of concurrent events doesn't have a causal path
from one event to the other, either way, uh, in the pair, and the Lamport timestamps are not guaranteed to be ordered, or unequal for such pairs
of concurrent events, um, they might be equal,
they might be different, it doesn't really matter. Uh, but this is fine, because these concurrent events are not causally related, so we're not violating causality by, uh, leaving this ordering
up to the air. So, essentially,
what I've been telling you, over the last few slides
is that, if two events, E1 and E2 are such that, E happens before E-
E1 happens before E2, using our logical ordering, then it's true
that the timestamp, the Lamport timestamp assigned to E1 is strictly less than the Lamport timestamp
assigned to E2. This is what I mean by saying
that, Lamport timestamps obey, uh, the causality. However, the reverse
is not true. If I give you two events, E1
and E2, so that the timestamp, according to Lamport timestamp, uh, of E1 is less than
the Lamport timestamp of E2, this means that either E1
might happen before E2 or E1 and E2
might be concurrent. 'Kay, the only, uhh, possibility that this is eliminating is that E2 happens before E1, that's definitely not true, but either of the other
two possibilities, uh, maybe, uh, the case, over here. 'Kay, so, the Lamport timestamps
are very causality but they don't always identify concurrent events, uh, so in the next lecture
we'll see a way of, uh, assigning timestamps to events so that, you can actually distinguish con- uh, concurrent events from ones
that are causality related.

### 12 - 2.5. Vector Clocks

Slides: `C3_TimeAndOrdering_E_CSRAfinal.pdf`

#### Slide text

```
•   Used in key-value stores like Riak
•   Each process uses a vector of integer clocks
•   Suppose there are N processes in the group 1…N
•   Each vector has N elements
•   Process i maintains vector Vi[1…N]
•   jth element of vector clock at process i, Vi[j], is i’s
    knowledge of latest events at process j

•   Incrementing vector clocks
     1. On an instruction or send event at process i, it increments only its ith
        element of its vector clock
     2. Each message carries the send-event’s vector timestamp Vmessage[1…N]
     3. On receiving a message at process i:
     Vi[i] = Vi[i] + 1
     Vi[j] = max(Vmessage[j], Vi[j]) for j ≠ i

     A       B   C              D    E
P1
                                           Time
             E       F      G
P2

         H           I                         J
P3
                         Instruction or step
                          Message

P1(0,0,0)
                            Time

P2
  (0,0,0)

P3
  (0,0,0)
Initial counters (clocks)

P1(0,0,0) (1,0,0)
                                Time

P2
  (0,0,0)

               Message(0,0,1)
P3
  (0,0,0)      (0,0,1)

P1(0,0,0) (1,0,0)
                                Time

P2
  (0,0,0)           (0,1,1)

               Message(0,0,1)
P3
  (0,0,0)      (0,0,1)

P1(0,0,0) (1,0,0)        (2,0,0)
                             Message(2,0,0)   Time

P2
  (0,0,0)           (0,1,1)         (2,2,1)

P3
  (0,0,0)      (0,0,1)

P1(0,0,0) (1,0,0)        (2,0,0)   (3,0,0)      (4,3,1)   (5,3,1)
                                                              Time

P2
  (0,0,0)           (0,1,1)        (2,2,1)     (2,3,1)

P3
  (0,0,0)      (0,0,1)               (0,0,2)              (5,3,3)

•   VT1 = VT2,
         iff (if and only if)
              VT1[i] = VT2[i], for all i = 1, … , N
•   VT1 ≤ VT2,
         iff VT1[i] ≤ VT2[i], for all i = 1, … , N
•   Two events are causally related iff
       VT1 < VT2, i.e.,
         iff VT1 ≤ VT2 &
                there exists j such that
                    1 ≤ j ≤ N & VT1[j] < VT2 [j]

• Two events VT1 and VT2 are concurrent
  iff
      NOT (VT1 ≤ VT2) AND NOT (VT2 ≤ VT1)

     We’ll denote this as VT2 ||| VT1

         A                      B         C              D     E
P1(0,0,0) (1,0,0)              (2,0,0)   (3,0,0)       (4,3,1)   (5,3,1)
                                                                     Time
                              E             F         G
P2
  (0,0,0)               (0,1,1)          (2,2,1)     (2,3,1)

                    H                       I                             J
P3
  (0,0,0)           (0,0,1)                (0,0,2)              (5,3,3)
  •   A  B :: (1,0,0) < (2,0,0)
  •   B  F :: (2,0,0) < (2,2,1)
  •   A  F :: (1,0,0) < (2,2,1)

         A                     B         C              D     E
P1(0,0,0) (1,0,0)             (2,0,0)   (3,0,0)       (4,3,1)   (5,3,1)
                                                                    Time
                              E            F         G
P2
  (0,0,0)               (0,1,1)         (2,2,1)     (2,3,1)

                    H                      I                             J
P3
  (0,0,0)           (0,0,1)               (0,0,2)              (5,3,3)
  •   H  G :: (0,0,1) < (2,3,1)
  •   F  J :: (2,2,1) < (5,3,3)
  •   H  J :: (0,0,1) < (5,3,3)
  •   C  J :: (3,0,0) < (5,3,3)

         A                      B             C               D     E
P1(0,0,0) (1,0,0)              (2,0,0)       (3,0,0)        (4,3,1)   (5,3,1)
                                                                          Time
                              E                  F         G
P2
  (0,0,0)               (0,1,1)               (2,2,1)     (2,3,1)

                    H                            I                             J
P3
  (0,0,0)           (0,0,1)                     (0,0,2)              (5,3,3)
  •   C & F :: (3,0,0) ||| (2,2,1)
  •   H & C :: (0,0,1) ||| (3,0,0)
  •   (C, F) and (H, C) are pairs of concurrent events

•   Lamport timestamps
     – Integer clocks assigned to events
     – Obey causality
     – Cannot distinguish concurrent events
•   Vector timestamps
     – Obey causality
     – By using more space, can also identify
       concurrent events

•   Clocks are unsynchronized in an asynchronous distributed system
•   But need to order events, across processes!
•   Time synchronization
     – Cristian’s algorithm
     – NTP
     – Berkeley algorithm
     – But error a function of round-trip-time

•   Can avoid time sync altogether by instead
    assigning logical timestamps to events
```

#### Transcript

In this lecture, we'll see vector clocks, which is another way of assigning timestamps to events in a distributed system. Vector timestamps are used in cloud computing systems such as Riak, which is a key-value store. In this approach, each process uses a vector of integer clocks. Think of this as an area of integer clocks. This is as opposed to integer clocks by themselves which were used in the Lamport timestamps approach. Suppose there are N processes in the group numbered one through N. Each vector at each process is going to have N elements. So, process i would maintain the vector V sub i, 1 through N. This vector has N elements. The jth element of the vector at process i, V sub i of j, is i's knowledge of the latest events that have happened at process j, because of whenever an event happens at process j and some message gets sent over to i, then Vi of j might get updated. However, j might also send messages to other processes, and this might get really transitively to i, and this would result in Vi of j also getting incremented. You would see as we discuss the rules. So, how do you increment vector clocks? We discussed the rules for incrementing Lamport clocks. Rules for incrementing vector clocks are simple, they are similar to the Lamport clock but they're slightly different. Whenever a process executes an instruction or sends a message to say this is process i, it only increments the ith element of its vector clock. So, only V sub i of i incremented whenever a process executes an instruction or sends a message. When a message is sent, it carries a send-event's vector timestamp. The entire vector here is assigned as a timestamp to that send-event, and this entire vector is carried along with that particular message. What does a process do when it receives a message? Well, when it receives a message with a vector timestamp in there, it uses it to update its own local vector clock. The ith element of the vector clock at the receiving process for i is simply incremented by one, because it stands for the number of events that have happened at process i. For each of the other elements in the vector, it simply takes the maximum of the corresponding element in the incoming message and in the local loop clock, and it takes the maximum of those two and it sets it to be the corresponding jth element in the local clock itself. Again, there are two simple rules. You simply increment your local ith element for every event, and whenever you receive a message you take the max for every other element in the vector. So, let's see this for our earlier example. Again, the same example as we saw previously. So, all the clock values here are initialized to be all zeros at all the processes. Again, these are local clocks, only getting updated by those processes. So, the process P1 executes an instruction. It simply assigns it an event (1, 0, 0) because it increments the first element of the vector, that's because process one is P1. Similarly, when P3 sends a message to P2, it increments the third element of the vector because it is P3, and assigns this resulting vector as the timestamp to the send-event of this message. The message also carries this timestamp (0,0,1), so that when P2 receives it, it can then use it to update its local clock. Remember again, that when it receives this message, P2 will simply update the second element of the vector by one and increments it by one. And for every other element, it takes the max from the corresponding elements in the local clock. So, zero here and zero here, sorry. Zero here and zero here result in zero for the first element and one from the received messaged, and zero in the local clock for the third element result in a max of one, being set for the third element of the local clock. So,(0,1,1) is assigned as the timestamp for the received event of this particular message being received at P2 from P3. Next, what happens in the system is that P1 sends a message to P2. In order to do this, it increments its first element from one to two, (2,0,0) is assigned as the timestamp of the send-event here, and that is carried with the message. When the message is received at P2, it increments its second element from one to two, that's shown in blue here. The other elements are all maxed. So, the green element, the first element is taken from the received message because that's higher than the corresponding first element in the local clock. And the third element is taken from the local clock, that's highlighted in red, the one, because that's higher than what is in the received message. Okay, so (2,1,1) is the resulting timestamp of the received event over here, and that is also updated to be P2's current clock. So, if you play the rules forward, you can see for yourself that these timestamps are true and these follow the rules that is laid out earlier. So, one of the reasons for preferring vector timestamp was that they obey causality. So, let's see the rules for obeying causality. Two vector timestamps, VT1 and VT2, assigned to events E1 and E2 respectively, are equal to each other if and only if the corresponding elements are all equal. So, the ith element of VT1 equals the ith element of VT2, for all i equaling one through N. Vector timestamp VT1 is less than or equal to vector timestamp VT2, if the ith element of VT1 is less than or equal to the corresponding ith element of VT2, for all i. Now, given this, we can say the two events E1 and E2, with vector timestamps VT1 and VT2, are causally related. That is, E1 happens before E2, if and only if VT1 is strictly less than VT2. Okay, this is different than less than or equal to. VT1 is strictly less than VT2, if and only if the following conditions are true: VT1 is less than or equal to VT2, so the corresponding elements of VT1 are less than or equal to the corresponding elements of VT2. But also, there exists some value of j such that, the jth element of VT1 is strictly less than the jth element of VT2. Okay, so, if these two conditions are true, then VT1 is said to be less than VT2, and is also true that the event to which VT1 is assigned as a timestamp happens before the event to which VT2 is assigned as a timestamp. Now, we can also say that two events are concurrent, VT1 and VT2, if and only if neither VT1 is less or equal to VT2, nor is VT2 less than or equal to VT1. Okay. This means that VT1 and VT2 are concurrent with each other. We denote it using three vertical bars between VT1 and VT2. So, let's see our example again and verify that these conditions are, in fact, true for some of the events in this particular run. So, A happens before B, and you notice that the timestamps assigned to them obey a causality. So, (1,0,0) is less than or equal to (2,0,0) because, for all the elements, the ith element of the left vector is less than or equal to the ith element of the right vector, and there is some index in this case one, where the first element of the left vector is strictly less than the first element of this second vector. Similarly, B happens before F is obeyed by the fact that (2,0,0) is less than (2,2,1), you have less than or equal to obeyed here, and several elements are smaller in the left vector compared to the right vector. Similarly, A happens before F again is obeyed because (1,0,0) is less than (2,2,1). Similarly, you can verify that for these other happens before relationships outlined here, the corresponding vectors obey the causalities. So, let's look at an example. F happens before J, F is assigned a timestamp of (2,2,1) and G is assigned a timestamp of (5,3,3). It's clear that all the elements of F are strictly less than all the elements of G. That's not required, you just need one of the elements to be smaller while all the other elements are less than or equal to, but in any case here, the left vector (2,2,1) is strictly less than the right vector (5,3,3). Similarly, for H and G, you see that (0,0,1) is less than (2,3,1), for H happens before J, you see that (0,0,1) is less than (5,3,3). Similarly, C happens before J is obeyed, because (3,0,0) which is assigned to C is less than J's timestamp which is (5,3,3). What about those concurrent events? Well, C and F are concurrent events, and you see that they get timestamps (3,0,0) and (2,2,1) respectively. These obey causality because they are not causally, we cannot say that one of the vector timestamps is less than the other. Why is this? Well, because each of the vectors has at least one element that is greater than the corresponding element in the other vector. C's vector has the first element, three, which is greater than the corresponding element in the other vector, two. And F's vector has the third element, one, which is greater than the corresponding third element in the C's vector which is zero. Neither of these two vectors is related to each other by less than or equal to, and so, we can say that C and F are, in fact, concurrent with respect to each other. Similarly, H and C are two other concurrent events, and H's third element, one, is greater than the third element in C, and C's first element, three, is greater than the first element in H, which is having a value of zero over here. Okay. So, in this way you can use the vector timestamps to verify that two events are either causally related if the vector timestamps are, in fact, one of them is strictly less than the other. And, on the other hand, if you cannot find a strictly less than relationship between two vector timestamps, then you know for sure that they are concurrent events. So, in Lamport timestamps, we assigned integer clocks to events in a way that the timestamps obey causality. But the problem there was that we could not distinguish concurrent events based on their Lamport timestamps. Vector timestamps come to the rescue, where you can clearly identify when a pair of events either are concurrent or are causally related to each other. Vector timestamps obviously take much more space at each process and also within the messages, but you have the added advantage, that you can identify concurrent events. So, that wraps up our discussion of time and ordering. Time is an essential problem to solve in anything in the distributed system, because the different processes have clocks that are not synchronized with respect to each other, and yet we would like to assign timestamps to events that happen at different processes in the distributed system. One way to do this is to use time synchronization to keep the clocks and processes close to each other, if not identical, and then use these clocks to assign timestamps to events. We discussed several algorithms for this including the Cristian's algorithm, the NTP algorithm. The Berkeley algorithm is essentially using synchronization only within the group, but in all of these cases, when you have a non-zero latencies in the underlying network, you're going to have an error in the clock that you set. So, the error is a function of the round-trip time. You can avoid time synchronization issues all together by instead assigning causal timestamps to events, either Lamport timestamps or vector timestamps to events.

### 13 - Interview with Marcos Aguilera

#### Transcript

I got my degree from Cornell University, that was back in 2000, and at that time, I was working on very theoretical problems in distributed computing. My adviser was Professor Sam Twigg. He was looking at problems like consensus and atomic broadcasting and so forth. And in 2000 after I got my degree, I joined the Compaq Systems Research Center, which used to be Digital Equipment Corporation, and the folks there were very, very applied. And so, I switched a little bit in my career and I started doing more applied system stuff, but still in distributed systems. And so, from that time until now, I've been doing a mix of theory and systems work, all in distributed systems. And so, in around 2002, HP acquired Compaq and so I was part of HP Labs from 2002 until 2008. In 2008, I decided to join Microsoft Research. So, I've been here for the past six years. And more recently, I've been working on still distributed systems but focusing more on distributed storage systems for large data centers. So, Microsoft is best known for its Windows operating system obviously, and has been known for many years. But Microsoft has done quite a bit of work in the Cloud computing space in the recent past. So, when someone says Cloud computing, what comes to your mind as a Microsoft employee? What do you think constitutes Cloud computing? Yeah for me, Cloud computing has to do with utility computing. The notion that there are large data centers that are under control of somebody else. And then, you can go and run your software there, and the Cloud is going to provide a lot of resources for you, and some Clouds will provide key value storage systems, some Clouds will provide databases, that is fine. But the main thing about that is that the Cloud itself is being managed by a third party. And you as a user of the Cloud, this is space paying for that as opposed to buying your own machine. I understand different people have different notions of what is Cloud computing, but for me really, Cloud computing has to do with utility computing. There's a third party controlling the Cloud, and then you can go and run your jobs there. And then, you pay by using it. You don't have to buy your own machines. So, distributed systems has the research in the area and the concepts in the area have existed for many, many decades. Can you say something about the relationship between Cloud computing and distributed systems or distributed algorithms? Yeah. Well, if you're going to be using the Cloud, that means automatically, you're going to be using the distributing system, right? Because the machine is not next to you. And in most applications that also running in the Cloud, are going to be applications that are distributed. There are a lot of people for example, that what they put in the Cloud there are web applications, and those things are being accessed remotely by clients and so forth. Of course, you can vary the amount of distribution that you're doing it. You could have just have simple server there where your system itself is one machine perhaps because you don't have to scale to such large sizes, and the clients are going to be out on the web. But still, it's a one type of distributed systems. But now, once you've put the computers away from you, now you have to already start working with the distributed system. And so, that's something which is inherent to the Cloud in my opinion. So, are distributed algorithms, distributed systems concepts, things like, Axles, or leader election, are these useful in Microsoft's Cloud systems both internally or externally? Yes. In many of the Clouds, these things are extremely useful, right? Because what's going on is that, the third-party vendor, which provides the Cloud needs to provide a good service and they want to make things for tolerance. And ideally, they have lots of machines running there, and they want one person to be looking over all of these machines. And when you talk about algorithms such as boxes, and now algorithms for consensus for replication and so forth, these are the mechanisms that are ensuring the faults tolerance to the Cloud so that you don't have to have as many people there to fix the machines when they break, right? And so, now many people have made this argument that, when you scale to a large number of machines, then you're going to have failures a lot of the time. And then, once you have you failures a lot of the time, you can have people trying to fix this failures all the time as well because otherwise, I think the cost starts to go up pretty quickly. And algorithms like boxes, I mentioned is used for replication. But there are many other distributed systems algorithms that are used in the Cloud like with system PowerShell for example, for the load balancing and so forth. And those things are extremely useful there. So, you have published quite a bit of research results in the last few years in the Cloud computing area, and of course, the students in the class are learning about key value stores NoSQL storage systems. Can you say a little bit of what you found in your research about Cloud computing in general, but also key value stores NoSQL storage systems? Yeah. One thing that we did, and that was in 2011, we started working before this in even, 2009, 2010. It was the problem of geo-distribution and geo-replication. And at the time, a lot of the distributed systems that were running inside a data center were limited to just one data center. And we thought, okay, but there's all these working wide area networks that the research community has already done. And on the other hand, when you run things in one data center, you are subject to problems like, disasters that will cause your application to go down. And also there will be a lot of ideas from a wide area networks that could be applied within a data center, and we start thinking of the, 'what do we need to do this', right? Well, we had study different, if you look at wide area P2P systems for example, there's a lot of concern about churn, and about people that are free riding in your system, and those things are perhaps less of a concern when you are inside a Cloud, and you are running the infrastructure because there are basically you there. I mean, there's all the third party people that are running the Cloud as well. But you control the infrastructure and usually don't have free riders because you're charging people to use the Cloud. And so, similar things which apply to previous research like free riding and so forth doesn't apply to the Cloud. But there's many other techniques that they did for example, techniques to high latency when you have to talk to free mode parties. And we started to think, "So, what are all these techniques that we can use, and what are the things that we are still missing, that we need to develop?" And so, one the things that we learned is basically, we develop our techniques for executing transactions efficiently when you have a geo-distributed system. So you have multiple data centers that, inside a data center, the connection is very fast across the data center, as it takes much longer to communicate. And so, you have this kind of hierarchical distributed system. And now you would like to efficiently execute transactions across the data centers, and well, some data maybe local, some of the data is remote, and you'd like to have some reasonable consistency conditions or isolation properties for your transactions that makes sense and that allow your transactions to execute efficiently. And so, we developed like an extent that allow you to do this by taking some ideas that are already existing, and when there were holes, we had to fill these holes. So obviously, there's a lot of work in the NoSQL space, which is making it more powerful and more expensive. Does this means relational databases, the old SQL databases they're going to go away in the next few years? I hope not there. So, what I can see from the NoSQL community is that there's a lot of work that tries to make NoSQL closer to SQL by any functionality that NoSQL did not have, but that they wanted to have. And so, take for example secondary indices, or take for example that they being able to do JOINs, and or, take the ability to do transactions for example. When we started off with NoSQL, this simple key value storage systems we had none of that. All you could do is just read and get, read and write or get input key value pairs. And then people realized, "Okay, I need something more than that." Actually, they started working on it. Okay, let's have analytics now or let's have the ability to do transactions. And so, if there's a real function that is there already provided by SQL. So, what you can see is that there's a lot of work from NoSQL that was only trying to add all these features that they're missing. Now, when you say relational databases, that intrinsically means that you have a schema, and this is one thing that the NoSQL folks that, to our advantage, we don't have schemas. But now, I think schemas, are a good thing in a way, but you don't be shackled by the schema in the sense that you want your data to be always fit the schema, and so there's some room for flexibility. That's how you can depart from just traditional relational SQL databases, but having a schema allows the storage system to understand what your data is. And if you want to implement some of the more powerful operations, like JOINs for example, you need to have the storage system know about what your data is. And so, a schema is really something which the application developer is given some information from the storage system about what the data looks like, and that is helping the storage system make those decisions. And if we removed that information, it becomes difficult to act in storage system layer. And so, I think having a schema is good. But again, I think there is a way to get the benefits of both having a schema and not having a schema, which is not to shackle the programmer with forcing in all that data to be fit exactly in the schema. And there are ways to do this. Like you can have blobs for example, where you can just put structured data in the schema, and the application is supposed to deal with the blob itself. And that is already supported to some extent by SQL. But I guess the bigger question is, how do you make the database, or the storage system do interesting work in those blobs when it doesn't have any information about this? And I think this is still an open question of how to do that. Of course, you can always try to index stuff as being free text for example, but you're still limited, right? Ideally, you'd like to have the storage system do a lot of interesting work with these unstructured data or schema that's data parts of the data itself. But at the same time, you don't want the application developers to be constrained about everything needs to fit exactly schema, right? And I think that's the challenge. So, it looks pretty exciting for the entirety of Cloud computing, but also key values to store our secret service systems. Let me ask you something which is a bit of a speculative question, of course, I miscontact your opinion, might only be your opinion and not Microsoft's opinion. What do you think Cloud Computing might be headed in the next say, 5-10 years? What might it look like five years from now? In my opinion, I think Cloud computing is the future of software right in. So, now, in my opinion more and more software which is not just something that you buy a shrink wrap from the software store, but rather, something that you rent and runs in the Cloud. You can see a little bit of that with, for example, software for the office, right, where you can do spreadsheets and you can do a word processing and you don't necessarily or even mail, for example, right. So, you don't buy or you could, I guess, download your own mail client and that's still useful. But there's a lot of things that you're not buying these stuffs anymore because you're just running these off from the Cloud, and the benefit of that is that you don't have to upgrade your software and then, if there's any problems with the stored systems, for example, you don't have to deal with fixing that, it's just the Cloud that will take care of it. And, I think, that's we're going to see more and more stuff running the Cloud in the future as opposed to running your own machines. And this is even true for the machines that you're carrying in your pocket for your phones, for example, there will be smart watches as well. And those things don't have much compute power or storage power, and so forth. And so, what's going to happen is that more and more of those applications will be running part in the Cloud and there will be some intelligent user interface to actually just display stuff nearby. And maybe a little bit of local computation as well. But, I really think that the Cloud will be the future of whatever software will be running in the future. Of course, there's always going to be need for some types of software locally. For example, in the study of car, you have all of these embedded systems for doing ideas or for doing drive by wire and that type of stuff needs to run inside the car and run. Okay, that's true that there will be cases where there's local competition as well, but I think, by and large most of the computation will be in the Cloud eventually. You ask about five years. I don't know if that's going to happen within the next five years, but, I think, we'll eventually get there. Last question, here, you've been at Microsoft Research for many years now. What do you like about working here, just work environment, the colleagues, and whatever the company provides you? Because there's a lot of things to like in Microsoft. And I really enjoy working here, but having good colleagues is always excellent. When you have this idea which you think is a nice idea. You talk to your colleagues and they'll say, "No, this sucks." And then you realize, okay, you're just saving your time not working on these ideas because there's all these XYZ things that you were not thinking about, but based on their experience or just based on having a fresh view of things they realize, there are some shortcomings, or they can say, "This is a good idea. I agree." And then they can take this feedback that you have from your colleagues and decide what to do with it. And so, now, having great colleagues is a good thing. And this is something we just don't find in many other places not something which is specific to Microsoft Research. Another great thing about Microsoft Research is the ability that you have to work on the problems that you'd like to work on, as opposed to having somebody tell you, "Today or this year, next year, you're going to be working on XYZ. The notion that you can go to conferences, and you can get inspired about new ideas, and you have your own idea and work on that. Or you can talk to colleagues and then, you understand that their ideas have value and are very interesting as well. But you have something to contribute there and the side to engage and start working with them. Now, the freedom to be able to do this is a very nice thing. Third thing that I like about Microsoft Research is that, there's a lot of resources available for research and so, you can see Microsoft is sponsoring a lot of conferences when it comes to trouble, for example, I can go to conferences and I don't have to worry about who's going to pay the bill for these things. And in terms of interns, for example, we are getting interns to come here for the summer. And it is no notion of shortage of these things in the sense that there is only a few number of slots available and the researchers have to compete against them. There's just resources are available, right. And I think, that's really important for research like if you don't have resource, especially, if it's experimental research, right? If you don't have the resources, it becomes very difficult for you to make progress and definitely, the Microsoft Research Resources is not missing at least not at this point. Nobody knows what's going to happen in the future, of course, but that's the idea in the current situation. Thank you. Thank you for taking the time to speak with us. It was my pleasure.

## Quizzes and assignments

### Homework 2

- Coursera: https://www.coursera.org/learn/cs-425/assignment-submission/Zku8C/homework-2
- Item type: staffGraded
- Grading status: NOT_STARTED

## Questions

_No submitted attempt found, so Coursera returned no questions or feedback._

### Part 1 Quiz 4

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
