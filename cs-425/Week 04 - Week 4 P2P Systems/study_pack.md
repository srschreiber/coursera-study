# Week 04 - Week 4 P2P Systems

Contents: 2 readings, 10 lectures, 1 quizzes/assignments.

## Readings

### Week 4 Overview

- Coursera: https://www.coursera.org/learn/cs-425/supplement/EUdOj/week-4-overview
- Lesson: Week 4 Overview

# Week 4: P2P Systems

## Overview

This week we will focus on Peer-to-Peer Systems. This area is important because it is a precursor to today's cloud computing. The topic is thus a good segue for us to discuss Key-value Stores next week (Week 5).

## Time

This week should take **approximately ****10 - 15 hours (this estimate excludes time spent on the programming assignment, which varies based on your background)** of dedicated time to complete, with its videos and assignments.

## Lessons

The lessons for this module are listed below (with assignments in bold italics):

|

**Lesson Title** |

**Time Estimate** |
|

**Lesson: P2P Systems** |

 |
|

Lecture 1: P2P Systems Introduction |

6 minutes |
|

Lecture 2: Napster |

7 minutes |
|

Lecture 3: Gnutella |

20 minutes |
|

Lecture 4: FastTrack and BitTorrent |

8 minutes |
|

Lecture 5: Chord |

22 minutes |
|

Lecture 6: Failures in Chord |

15 minutes |
|

Lecture 7: Pastry |

7 minutes |
|

Lecture 8: Kelips |

11 minutes |
|

**Interview** |

 |
|

Blue Waters Supercomputer |

10 minutes |
|

**_Part 1 Quiz 3_** |

1 - 2 hours |
|

**_Part 1 Programming Assignment_** |

30 - 45 hours |

## Goals and Objectives

After you actively engage in the learning experiences in this module, you should be able to:

-

Know how Napster, Gnutella, FastTrack, and BitTorrent work.
-

Know and analyze how distributed hash tables work (Chord, Pastry, and Kelips).

## Key Phrases/Concepts

Keep your eyes open for the following key terms or phrases as you interact with the lectures. These topics will help you better understand the content in this module.

-

Peer-to-peer systems
-

Industrial P2P systems: Napster, Gnutella, FastTrack, BitTorrent
-

Distributed hash tables: Chord, Pastry, Kelips

## Guiding Questions

Develop your answers to the following guiding questions while completing the readings and working on assignments throughout the week.

-

What is the difference between how Napster clients and Gnutella clients search for files?
-

What is the difference between Gnutella and FastTrack?
-

What is BitTorrent’s tit for tat mechanism?
-

What is consistent hashing?
-

Why are DHTs efficient in searching?
-

How does Chord route queries?
-

How does Pastry route queries?
-

How does Kelips route queries?
-

What is churn in P2P systems?
-

How does Chord maintain correct neighbors in spite of failures and churn?

## Readings and Resources

There are no readings required for this week, but you can look at the following documentation:

-

**[Gnutella v 0.4 paper (PDF)](https://courses.engr.illinois.edu/cs425/fa2014/gnutella_protocol_0.4.pdf)**
-

**[Chord paper (PDF)](http://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf)**

## Tips for Success

To do well this week, I recommend that you do the following:

-

Review the video lectures a number of times to gain a solid understanding of the key questions and concepts introduced this week.
-

When possible, provide tips and suggestions to your peers in this class. As a learning community, we can help each other learn and grow. One way of doing this is by helping to address the questions that your peers pose. By engaging with each other, we’ll all learn better.
-

It’s always a good idea to refer to the video lectures and readings we've completed during this week and reference them in your responses. When appropriate, critique the information presented.
-

Take notes while you read the materials and watch the lectures for this week. By taking notes, you are interacting with the material and will find that it is easier to remember and to understand. With your notes, you’ll also find that it’s easier to complete your assignments. So, go ahead, do yourself a favor, and take some notes!

### Part 1 Quiz 3 Instructions

- Coursera: https://www.coursera.org/learn/cs-425/supplement/wVR7n/part-1-quiz-3-instructions
- Lesson: Quiz

**Topics: **P2P Systems

## Instructions

-

The quiz must be done individually.
-

You can use any of the course resources, the course staff, or the Piazza forum to complete this assignment.
-

 However, when using the Piazza forum, you cannot post solutions on it! You can only use it to discuss ideas and concepts.
-

 For multiple choice, please note whether the question says there are MULTIPLE correct answers. For questions with MULTIPLE answers, you must specify ALL the correct answers and no wrong answer.

## Evaluation

Each quiz question is worth 1 point in Coursera. But the point value will be scaled down to 0.25 pts per question to calculate the grade of the quiz in this course.

## Important Dates

For deadline, refer to Course Deadlines, Late Policy and Academic Calendar page

## Lectures

### 01 - Week 4 Introduction

#### Transcript

[MUSIC] In this third week of the cloud computing
concepts course we jump into peer-to-peer systems which have been very popular
over the past decade in a half. We'll see both unstructured peer-to-peer
systems such as Gnutella and Napster, and structured p2pr systems just Chord and
Pastry. We'll see,
not only how the systems are used, in fact we'll hardly see how they are
used, but we'll jump under the hood and see how these systems work on the inside. We'll see the messages that are exchanged
among the different servers and clients in these systems. And we'll see the actual protocols
that work inside these systems. So this is a really under
the hood look into these systems. And these systems are very important,
especially the structure peer-to-peer systems because some of the concepts, some
of the techniques used here are reused and are being reused in two days generation
of key value and NoSQL storage systems. Which we will study in
next week in this course. [MUSIC]

### 02 - 1. P2P Systems Introduction

Slides: `C3_p2p_A_CSRAfinal.pdf`

#### Slide text

```
Why Study Peer-to-Peer Systems?

•   First distributed systems that seriously focused
    on scalability with respect to number of nodes

•   P2P techniques abound in cloud computing
    systems

     • Key-value stores (e.g., Cassandra, Riak,
       Voldemort) use Chord p2p hashing

Why Study Peer to Peer Systems?

A Brief History

•   [6/99] Shawn Fanning (freshman Northeastern University) releases Napster online music
    service
•   [12/99] RIAA sues Napster, asking $100K per download
•   [3/00] 25% University of Wisconsin traffic Napster, many universities ban it
•   [00] 60M users
•   [2/01] US Federal Appeals Court: users violating copyright laws, Napster is abetting this
•   [9/01] Napster decides to run paid service, pay % to songwriters and music companies
•   [Today] Napster protocol is open, people free to develop OpenNap clients and servers
    http://opennap.sourceforge.net
     •    Gnutella: http://www.limewire.com (deprecated)
     •    Peer-to-peer working groups: http://p2p.internet2.edu

What We Will Study

• Widely-deployed P2P Systems
   1.   Napster
   2.   Gnutella
   3.   Fasttrack (Kazaa, Kazaalite, Grokster)
   4.   BitTorrent
•   P2P Systems with Provable Properties
   1.   Chord
   2.   Pastry
   3.   Kelips
```

#### Transcript

Welcome. So, uh, in this series of
lectures we are going to study, uh, peer-to-peer systems, or
what are known as P2P systems. Peer-to-peer systems
started emerging in the, uh, late 1990s, early 2000s. Uh, they started with a variety of very popular peer-to-peer systems such as, Napster and Gnutella, and soon there was a lot
of academic research, uh, that was leading to, uh, peer-to-peer systems being developed, uh, as well. So we'll study
both these classes of peer-to-peer, uh, systems. Why do we want to study
peer-to-peer systems? Well first, uh, these are, uh,
distributed systems that, uh, were really the first very
large-scale distributed systems. Uh, peer-to-peer systems like
Napster and Gnutella had, uh, millions, tens of millions, in
some cases hundreds of millions of clients communicating with
each other at the same time, in the same system. And so when we want to study
scalable distributed systems, uh, this is a great, uh,
area for a case study. Uh, also, the ideas and techniques from the, uh, era of peer-to-peer systems have been leveraged and are used quite a bit
in cloud computing systems. Uh, later on, uh, we'll study
key-value stores, such as Cassandra, Riak, uh,
Voldemort from LinkedIn, and also DynamoDB
from, uh, Amazon. All of these, for instance,
use techniques, such as, consistent hashing, which we'll study in the Chord, uh, peer-to-peer system, uh, in this lecture series. So here is what, um, the, um,
user interface might look like for a peer-to-peer system. This is a snapshot of the
Napster user interface beta 7. Essentially,
what you do is, that you, uh, you, uh, type in key words, in this case the key word
is actually the file name, but you might be able to type
in other key words too, such as the artist's name,
the song name, the album name, and you hit enter, or you hit "Find It" in this case, uh, and then once you do that, uh, the system goes off and it, uh, retrieves
a series of locations, of potential locations,
for this file, and then you, uh, essentially, uh, click on the f- on the location that seems
to yield the fastest, uh, connection, this-uh,
the fastest download speed, and voila,
the file starts downloading. So our interest as distributed
systems designers, as cloud computing designers, is to see what goes on underneath the hood from the time
that you hit "Find It" until the results come back, and then after you click,
um, "Download" on one of the entries, what happens underneath? What are the messages exchanged
underneath among the clients and the servers in the system? That's what we want to do here;
that's what we want to study in this particular
lecture series. So a little bit of history
before we get started into the, um, uh, internals of Napster. Napster was founded in 1999
by Shawn Fanning, who was then a freshman
at Northeastern University, and, uh, Napster
was just a nickname that they used to call him. His roommate-roommates used
to call him Napster because he used to, um, uh, apparently, uh,
he loved to take naps, uh, and, uh, so he named
his system Napster and, um, uh, overnight Napster became very very popular, and users started using Napster to download MP3s and MPEGs, which unfortunately, uh, were covered by copyright. Copyright essentially means that the recording label that
is producing a song by an artist owns the copyright, and you cannot, uh, exchange, uh, that song for free without paying the recording label, and therefore
the artist as well. The same goes
for movies as well and the movie
production companies. So the Recording Industry
Association of America, uh, a group of recording labels, sued Napster and asked for
an exorbitant amount of money per download. Uh, subsequently, Napster,
uh, was, uh, uh, ruled by the US Federal Appeals Court as violating, uh, uh, copyright laws,
or rather, not as violating copyright laws, but helping users, uh,
violate copyright laws. So Napster, as you will see
from the design, was not directly infringing copyright laws, but was indirectly helping users to infringe copyright laws. At the same time Napster
continued to grow popular, there was a study in 2000
that showed that, uh, uh, all the traffic out of University of Wisconsin Madison, uh, 25% of that traffic was,
uh, Napster traffic. Many universities
subsequently banned it because it was hogging
the bandwidth, uh, in their, uh, networks. Napster reopened, uh, later
on, uh, as a paid service. Today it still runs
as a paid service. Essentially, you pay some amount
of money to download a song, and some of that payment
goes to the song-writers and the music labels as well. Napster is, uh,
is an open protocol, and people are free to develop Napster clients and servers, um, uh, today, and you can find more at the, uh, SourceForge page
for Napster. Another study, uh,
system we'll study, Gnutella, uh, also, um, uh,
used to be an open protocol, and recently
it's been replicated, um, and so we'll study that
as well in the next lecture. So what we'll study is, uh, a variety of widely pe-deployed peer-to-peer systems, uh, Napster, Gnutella, uh, Fasttrack, uh, uh, BitTorrent. Um, fasttrack is
the underlying system for Kazaa, Kazaalite and Grokster. Uh, and also we'll study
peer-to-peer systems that came out of academia, uh, systems like Chord,
uh, Pastry and, uh, Kelips. Once again, these are only
the tip of the iceberg. There are many other systems
that came out of academia. We are not going to be able
to cover all of those hundreds of
peer-to-peer systems, uh, but just representative ones, uh, from particular categories.

### 03 - 2. Napster

Slides: `C3_p2p_B_CSRAfinal.pdf`

#### Slide text

```
Napster Structure

                                       Filename Info about

           Store a directory, i.e.,   PennyLane.mp3 Beatles, @
                                                    128.84.92.23:1006
                                                       …..
       filenames with peer pointers
   napster.com
   Servers            S       S
Client machines           S
   (“Peers”)
           P                                  P

                  P                   P Store their own
                      P           P
                                              files

Napster Operations

Client
• Connect to a Napster server
     • Upload list of music files that you want to
       share
     • Server maintains list of <filename,
       ip_address, portnum> tuples. Server stores
       no files.

Napster Operations

Client (contd.)
• Search
     •   Send server keywords to search with
     •   (Server searches its list with the keywords)
     •   Server returns a list of hosts – <ip_address, portnum>
         tuples – to client
     •   Client pings each host in the list to find transfer rates
     •   Client fetches file from best host
•   All communication uses TCP (Transmission
    Control Protocol)
     •   Reliable and ordered networking protocol

    Napster Search

              2. All servers search their lists (ternary tree algorithm)

                                                Store peer pointers
   napster.com                                      for all files

   Servers
                          S       S
Client machines                             1. Query
   (“Peers”)                  S

          P                   3. Response             P     4. Ping candidates

                  P                            P
                                                           Store their own
                      P      P                                  files
              5. Download from best host

Joining a P2P system

•   Can be used for any p2p system
     •   Send an http request to well-known url for that
         P2P service - http://www.myp2pservice.com
     •   Message routed (after lookup in DNS=Domain
         Name System) to introducer, a well known
         server that keeps track of some recently joined
         nodes in p2p system
     •   Introducer initializes new peers’ neighbor table

Problems

•   Centralized server a source of congestion
•   Centralized server single point of failure
•   No security: plaintext messages and passwds
•   Napster.com declared to be responsible for
    users’ copyright violation
     • “Indirect infringement”
     • Next system: Gnutella
```

#### Transcript

So today we'll, uh, look
at the internal details of, uh, uh, of Napster. So Napster, essentially, has, uh, all, each of the users
run a Napster client, and so these clients
are called peers. We just call them as peers
because, essentially, uh, they are treated equally as far as the system is concerned. So these are denoted as the
green circles on this figure, with a "P" in them. Uh, now, when you upload a file, so you may upload a file
that is the song "Penny Lane" by Beatles, you upload it
to your Napster client. It doesn't go anywhere;
it stays on the machine, on the workstation or laptop, where your Napster client
is running. The files are stored
by the peers. Uh, they are not transferred
by default. There are also
a bunch of servers, in this case denoted
as red circles with "S", which are run by Napster.com, and these servers store directory information with file pointers
and peer pointers. Uh, essentially, uh, here, uh, in this figure, uh, we are showing, uh, the, uh, file, uh, PennyLane.mp3 as being stored at a particular IP address and a port number, and there's some more key f-key word information about that file such as the artist's name. This is the information
that is stored at, uh, the Napster.com servers. The Napster.com servers do not
store the files themselves; they only store
directory information. So when a client starts up, it first connects
to a Napster server. This was shown on the previous slide as the lines in between, let's go back
to the previous slide, uh, the line going in between
a peer and its server, essentially, is the connection between, uh, those two. Notice that the servers
also talk with each other; we'll come to that in a moment. Uh, when, uh, the client
connects to the Napster server it uploads a list
of music files that, um, that client wants to share, and the server maintains,
uh, tuples, which are <filename, ip_address, portnum> tuples. There might also be
other information, such as, key word
associated with it, and the server
does not store any files. So when a client
wants to search, suppose you want to search
for a particular song, essentially, you
would type in your, uh, key words
and you hit "Find It." When you hit "Find It," a message goes out to the server that your client is talking to, uh, with these key words
in them. The server, or the group
of servers rather, talk with each other and search their
directory information lists with these key words. They find all the matching <ip_address, portnum> pairs that have information
about this keyword and return it
to the querying client. The client when it receives this directly pings each
of the hosts in this list, to find the bandwidth or the transfer rates
from these hosts. Then, uh, the results
are visible to you, then when you double-click
on one of the results, the client starts
fetching the file directly from the peer
or from the host. In none of this communication is
the server actually involved in transferring the file. It is used in searching
where the file might be, but it is not used
in transferring the file. Now all along,
whenever I have said "messages," uh, I meant messages sent
using TCP sockets or transmission
control protocol, which is a reliable, uh, transport level,
uh, protocol. So here's a pictorial
depiction of, uh, how the query processing works. When you type in your keywords, a query message
goes out from your peer to the server it's talking to, containing those key words. The servers maintain
the direct information using a ternary tree. Essentially, a ternary tree is a sorted dictionary
data structure, uh, where, um, every internal node in the tree has three children. A binary tree has every node
with two children; ternary tree has every node
with three children. And so this is useful for
searching for, uh, information, uh, using, uh, the, uh, key of, uh, the objects being searched. Then when the objects
are, uh, ready, a response is returned
with all the, uh, <ip_address, portnum> pairs
to the, uh, querying peer, and then the querying peer pings the individual
candidates directly, finds out
the effective bandwidths, and then when you select
the best host, the download starts directly from the best host. Now, one question
that arises oftentimes is how do peers join
a peer-to-peer system? How do they know
which server to contact? Servers, after all,
have IP addresses. Essentially, uh,
the set of servers might be changing all the time, uh, and so, uh,
what you want to do is you want to have a well-known, um, uh, URL, uh, such
as my myp2pservice.com. This might be Napster.com
for Napster, for instance. And so when a client starts up,
it sends a message, uh, or rather it sends
a DNS, uh, query, or a domain name system query, to this URL,
which returns an IP address, in this case
of a Napster server, and then the peer starts talking to that particular
Napster server. Uh, in other
peer-to-peer systems, the domain name system
might return, um, uh, say a well-known server maintaining some recent, um, IP addresses
of recently joined peers, or it may return the IP address of one of the peers that is already in the system. In any case,
the DNS is a great way, uh, to, uh, get introduced
into the system, um, or communicate
with an introducer node or introducer peer,
that will, uh, then, um, uh, uh, tell you some
of the recently joined peers or some of the existing peers
in the system, and so you can
bootstrap your own, uh, uh, neighbor list
using that. And again, this technique
is useful not just for Napster for a newly joining peer
to know about, uh, one or more of the servers, but is also used later on
by our Gnutella system for a newly joining peer to know about some of the existing peers in the system. Now, some of the problems with
Napster included the fact that, uh, the servers are a
centralized point of congestion. If the servers are
overloaded with queries, uh, even though they
did not transfer files, the queries might
overwhelm them. Uh, then the entire system
might become slow because, essentially,
search has become slow. The server is also
a centralized point of failure. If someone took out one
or more of the servers, uh, then the system
would be compromised. Also, the original
versions of Napster did not have any security, messages and passwords
were all plaintext. However, none of these
was a reason that Napster actually was brought down. Uh, the main reason
it was brought down was the fact that the court declared that Napster, even though it was not directly infringing copyrights because it was not
transferring any files, it was instead helping users, uh, "indirectly
infringe" copyright. So "indirect infringement" is
a legal term, and Napster was, um, uh, found
to be guilty, of that. So, some of this, uh,
gave rise to a new system, Gnutella, which overlapped with Napster, in terms of timeline, um, uh, and, which
we'll study next, which addressed some
of these issues with Napster.

### 04 - 3. Gnutella

Slides: `C3_p2p_C_CSRAfinal.pdf`

#### Slide text

```
Gnutella

•   Eliminate the servers
•   Client machines search and retrieve amongst
    themselves
•   Clients act as servers too, called servents
•   [3/00] release by AOL, immediately withdrawn,
    but 88K users by 3/03
•   Original design underwent several modifications

 Gnutella

                                   Store their own
                                         files

 Servents (“Peers”)
      P                              P
                    P
                                        Also store
                                      “peer pointers”
                                       P
           P                 P
                                         P
Connected in an overlay graph
      (== each link is an implicit Internet path)

How do I search for my Beatles file?

•   Gnutella routes different messages within the overlay
    graph
•   Gnutella protocol has 5 main message types
     •   Query (search)
     •   QueryHit (response to query)
     •   Ping (to probe network for other peers)
     •   Pong (reply to ping, contains address of another peer)
     •   Push (used to initiate file transfer)
•   We’ll go into the message structure and protocol now
     •   All fields except IP address are in little-endian format
     •   Ox12345678 stored as 0x78 in lowest address byte, then 0x56 in next
         higher address, and so on.

    How do I search for my Beatles file?

Descriptor Header                                               Payload

Descriptor ID Payload descriptor TTL Hops Payload length
0                15         16                 17          18                      22

                                                                   Number of bytes of
                 Type of payload
ID of this                                                         message following
                 0x00 Ping
search                                                             this header
                 0x01 Pong
transaction
                 0x40 Push         Decremented at
                 0x80 Query        each hop,
                 0x81 Queryhit     Message dropped
                                   when ttl=0               Incremented at each hop
Gnutella Message Header Format     ttl_initial usually 7
                                   to 10

 How do I search for my Beatles file?

      Query (0x80)
          Minimum Speed Search criteria (keywords)
      0                  1   …..

Payload Format in Gnutella Query Message

Gnutella Search

  Query’s flooded out, ttl-restricted, forwarded only once
                                                             P
   P
                               P

                                                                 P
                TTL=2
            P                                  P
                                                                 P
                Who has PennyLane.mp3?

     Gnutella Search

QueryHit (0x81) : successful result to a query
Num. hits port ip_address speed (fileindex,filename,fsize) servent_id
0          1   3            7    11                               n           n+16
                                      Results
               Info about
               responder                        Unique identifier of responder;
                                                a function of its IP address

    Payload Format in Gnutella QueryHit Message

Gnutella Search

   Successful results QueryHit’s routed on reverse path
                                                          P
  P
                             P

                                                              P

          P                                 P
                                                              P
              Who has PennyLane.mp3?

Avoiding excessive traffic

•   To avoid duplicate transmissions, each peer
    maintains a list of recently received messages
•   Query forwarded to all neighbors except peer from
    which received
•   Each Query (identified by DescriptorID) forwarded
    only once
•   QueryHit routed back only to peer from which Query
    received with same DescriptorID
•   Duplicates with same DescriptorID and Payload
    descriptor (msg type) are dropped
•   QueryHit with DescriptorID for which Query not
    seen is dropped

After receiving QueryHit messages

•   Requestor chooses “best” QueryHit responder
     •   Initiates HTTP request directly to responder’s ip+port
           GET /get/<File Index>/<File Name>/HTTP/1.0\r\n
           Connection: Keep-Alive\r\n
           Range: bytes=0-\r\n
           User-Agent: Gnutella\r\n
           \r\n

•   Responder then replies with file packets after this
    message:
           HTTP 200 OK\r\n
           Server: Gnutella\r\n
           Content-type:application/binary\r\n
           Content-length: 1024 \r\n
           \r\n

After receiving QueryHit messages (2)

•   HTTP is the file transfer protocol. Why?
     • Because it’s standard, well-debugged, and
       widely used.
•   Why the “range” field in the GET request?
     • To support partial file transfers.
•   What if responder is behind firewall that disallows
    incoming connections?

Dealing with Firewalls

Requestor sends Push to responder asking for file transfer
                                                   P
    P
                          P
                                                Has PennyLane.mp3
                                                But behind firewall

                                                       P

           P                         P
                                                       P

Dealing with Firewalls

  Push (0x40)

  servent_id fileindex ip_address port

       same as in
   received QueryHit      Address at which
                        requestor can accept
                       incoming connections

Dealing with Firewalls

•   Responder establishes a TCP connection at
    ip_address, port specified. Sends
           GIV <File Index>:<Servent Identifier>/<File Name>\n\n

•   Requestor then sends GET to responder (as
    before) and file is transferred as explained
    earlier

•   What if requestor is behind firewall too?
     •   Gnutella gives up
     •   Can you think of an alternative solution?

Ping-Pong

    Ping (0x00)
             no payload
    Pong (0x01)
    Port ip_address Num. files shared Num. KB shared

•    Peers initiate Ping’s periodically
•    Ping’s flooded out like Query’s, Pong’s routed along reverse path
     like QueryHit’s
•    Pong replies used to update set of neighboring peers
      •    To keep neighbor lists fresh in spite of peers joining,
           leaving and failing

Gnutella Summary

•   No servers
•   Peers/servents maintain “neighbors,” this forms an
    overlay graph
•   Peers store their own files
•   Queries flooded out, ttl restricted
•   QueryHit (replies) reverse path routed
•   Supports file transfer through firewalls
•   Periodic ping-pong to continuously refresh neighbor lists
     •   List size specified by user at peer: heterogeneity means some
         peers may have more neighbors
     •   Gnutella found to follow power law distribution:
                                               −k
                           P(#links = L) ~ L         (k is a constant)

Problems

•   Ping/Pong constituted 50% traffic
     •   Solution: Multiplex, cache and reduce frequency of
         pings/pongs
•   Repeated searches with same keywords
     •   Solution: Cache Query, QueryHit messages
•   Modem-connected hosts do not have enough
    bandwidth for passing Gnutella traffic
     •   Solution: use a central server to act as proxy for such
         peers
     •   Another solution:
           FastTrack System (soon)

Problems (contd.)

•   Large number of freeloaders
     •   70% of users in 2000 were freeloaders
     •   Only download files, never upload own files
•   Flooding causes excessive traffic
     •   Is there some way of maintaining meta-
         information about peers that leads to more
         intelligent routing?
            Structured peer-to-peer systems
           e.g., Chord System (coming up soon)
```

#### Transcript

In this lecture we are going
to study, uh, Gnutella, which is the, um, uh, arguably the first fully distributed, uh, peer-to-peer system. So one of the problems
with Napster was the fact that the servers were maintaining
directory information and that they were,
uh, responsible for "indirect infringement," and so Gnutella's
solution to this was to eliminate
the servers altogether and instead use
the clients themselves to search and retrieve
using messages. So in effect the clients
act as servers too, or they take on some
of the responsibilities of the, uh, the servers, and so Gnutella clients are often called as "servents," which is a collage word that consists of "server"
plus "client." Uh, AOL actually released
Gnutella in 2000, uh, but realizing that there were
copyright issues with it, uh, withdrew it, but Gnutella
continued growing, and it had, uh, 88,000 users
around, uh, March 2003. Gnutella itself underwent, uh,
several revisions. Uh, we are gonna discuss the very first version
of, uh, Gnutella, uh, that was, uh, published,
uh, as tech report. So Gnutella, there
are no, uh, servers. Instead peers, uh, communicate
directly with each other. Um, peers, like in Napster,
store their own files; files do not go anywhere
by default. Ah, but peers also
store peer pointers. In other words, every peer
has one or more neighbors which are also other peers
in the system. So consider this peer over
here, it has five neighbors, uh, this, this, this,
this, and this peer. Essentially, a neighbor means
this peer knows about their IP address
and port number pairs and can send them, uh, messages using, uh, for instance, TCP. So essentially, uh, this, uh,
creates a graph among the peers; this is called an overlay graph. This is called an overlay graph because it's a graph that is overlaid on top of the internet. Uh, each of the links
in this graph, each of the edges in this graph, is essentially an internet path
in the underlying internet, but as far as the
overlay is concerned, it is, um, uh, the actual path
in the underlying internet is irrelevant. As long as the peers
can talk with each other, that's all that matters. So, um, how do I search for a
particular file, say the Beatles
"Penny Lane" file, which we searched for
in, uh, Napster earlier? Well, Gnutella routes
different messages within the overlay graph, and for this it uses five
different kinds of messages. For the search messages
which contain the key words, it uses the Query message. The QueryHit is a response to
the search, and we'll see these, uh, over the next few slides. In order to keep, uh, the list
of neighbors, uh, up to date, it uses Ping and Pong messages, and it uses a fifth kind
of message called Push, uh, for a file transfer. We'll go into the structure
of the messages now, and the protocol itself. Now, all of the fields
in the messages that I'm going to discuss are I, except IP addresses,
are in little-endian format. Um, you might have heard
of little-endian versus big-endian format. These are two different ways
of, uh, storing, say, integers in your memory. In the little-endian format,
essentially if you have a hex, which is 12345678, 78 is stored
in the lowest address byte, then 56 is stored
in the next higher address, and so on and so forth. Uh, in the big-endian format,
this would be reversed. Essentially, 12 would be stored
in the lowest address byte. So here is the header for all
the five kinds of messages in Gnutella; Query, Queryhit,
Push, Ping, and Pong. The first 16 bytes are, uh,
the ID of this transaction. This is typically
generated uniquely for every single search
from every peer. In other words, whenever your
client generates a, uh, search, it has to generate
a descriptor ID that is unique
throughout the entire system. For instance, you could, uh,
generate this by using the IP address
and port number of the client, and also an incrementing
sequence number at that client itself. This descriptor ID is useful
because the intermediate nodes can then use this
to distinguish messages that only belong
to this particular, uh, search, and not confuse it
with other searches. The next two bytes,
uh, essentially, uh, carry the type of payload, the kind of message
that this is, and this is one of five types for the five
different messages. Next you have TTL,
or "time to live." That's one byte, and then Hops, which is the number of hops that this, uh, message
has transmitted to. Whenever a message
is forwarded by a peer to its neighboring peers,
TTL is decremented by one. When the TTL hits zero, you do not
forward the message anymore. The TTL is set
to be a finite number, so that essentially a message doesn't keep circulating around the overlay
graph forever. You don't want the overlay graph
to have very old messages still going around
inside of them. The initial TTL is usually set to be somewhere
between seven and ten. The hops is also incremented every time
a message is forwarded. You might wonder, at this
point, and I'm sure you should, you're wondering, why you
need a hops when you have a TTL. Well, the reason
is the initial TTL may not be the same
at all the initial peers. Uh, some peers might choose
the initial TTL to be seven others might choose it
to be ten. In any case, most
of the protocol, uh, deviants we discussed don't really
use the Hops field; they mostly rely
on the TTL field. Finally, the message
might have a payload, which differs depending
on the kind of message it is, depending on the one
of the five kinds of messages. And so how many bytes are there
in the payload is present in the Payload
length field, so you know how far to look
for the end of the message. That being said, let's go
into the individual messages. The Query message contains, uh,
first of all the minimum speed that is requested
by the Querying peers, so if you're connected
to a, um, 100 MBps line, you might say
"Well, I need peers that are "at least 100 MBps
or at least 10 MBps," and then the search criteria,
these might be the keywords, say "Beatles Penny Lane"
that you're searching for. This is present in the Payload
portion of the previous, uh, message that I showed. But how are queries sent out? Well, let's imagine this, uh,
peer on the bottom left is the one that is trying
to search for PennyLane.mp3. It creates a Query message
which has a TTL of, say, two in this case, and it sends out,
uh, the Query message to its immediate
neighboring peers, this, uh, top left peer and also
this middle peer over here. When, um, uh, each of these
peers receives its message, it first of all searches
among its local files whether they have, um, uh,
any of their keywords matching the incoming
Query message, and also it floods out
the Query message to its immediate
neighboring peers. So this peer over here
that I'm showing, uh, floods out the Query message
to all the peers it has received except, uh-so all of its neighboring peers, uh, except the one
from which it just received, uh, the Query message, so in
this case that's four peers. This peer would have
done likewise, except that it received
the Query message, um, uh, from this other peer, so it doesn't send it, uh,
the same Query message. How does it know this? Well, the descriptor IDs
of these Query messages are the same,
and they are retained, um, as the messages transit through the overlay graph. Now, in this, um, arrow or also
in any of these arrows, the TTL of these messages is 1. So when this peer receives
a Query message, or the two Query messages, it decrements the TTL,
finds that the TTL is 0. It does not forward
the Query message anymore. So for instance, this peer over
here never receives the copy of the Query message because,
uh, all of its neighbors have already had a TTL of 0 when they received
that Query message. So the Query messages
are also TTL restricted. Finally, they
are forwarded only once, so once this peer
has forwarded a Query message, if it receives a duplicate, uh,
for instance, um, you know, this peer might receive
a duplicate from this peer, it doesn't forward
the Query message a second time. A-again, how does it know this? It knows this by,
uh, keeping track of the recent Query messages that it has forwarded, uh, and using
the descriptor ID field to find out whether or not an incoming
Query message is a duplicate. So in this way essentially
you're trying to, uh, flood out the Query messages, but not
to the entire network, only to some, uh, portion
of the overlay graph, um, uh, hopefully
a large enough portion that you'll get back
enough search results. Now, how do search
results come back? So when a peer finds that
it has some matching files which match the incoming Query's
keywords, what does it do? Well, it creates
a QueryHit message. The QueryHit message contains
the following payload. It contains
the number of hits, the number of files that match, it contains the port,
uh, and the IP address, as well as the speed
of the responding peer, this is the peer that is responding to the querying peer, and then it contains, uh, for each of the files
that match, information about that file
such as the filename, the file index,
and the file size. It might also contain
a servent ID, which essentially
is a unique identi-identifier of the responder. This might be derived
from its IP address. For most parts this
is not really used, um, uh, in the Query
and QueryHit. It might be used by the Push
message, but not really here. Now how does the QueryHit
make its way back to the querying peer? Well, QueryHits
are reverse routed. Remember we said that every peer
keeps track of, um, the recent Query messages
it has received. It also keeps track of which
of its neighboring peers it received
this Query message from. So when this peer either
generates a QueryHit message or receives a QueryHit message, it just, uh, simply, uh,
sends a QueryHit message back to the peer
from which it received the corresponding Query
message from. So this peer, uh, over here in
the, uh, top right corner, when it generates
a QueryHit message, it sends back the QueryHit
message to that peer which sent it
the corresponding Query message. This QueryHit message
that is sent back contains the same descriptor ID as the original Query message, so that, uh, the peer
that is receiving, uh, this QueryHit message knows, uh, which Query message is the corresponding matching
Query message for this QueryHit. And so, uh, in this way
the QueryHit messages make their way back
in the reverse path to the querying peer, uh, and the querying peer
now receives back all of these responses, and now it knows who are, which are all
the matching files, and it can display these
responses to the user. Now to avoid
duplicate transmissions, each peer maintains a list
of recently-received messages, uh, as we mentioned. The Query is forwarded
to all neighbors except the peer from which
you have received it, or peers from which
you may have received it. Each Query is
forwarded only once. The QueryHits
are reverse routed, uh, back to, uh, the peer from which the Query received
the same descriptor ID. And duplicates with the same
descriptor ID and payload typically, uh, Queries,
um, are, uh, dropped. Also, the overlay graph may
have changed, as we'll see soon, because some of the neighbors
may have shifted and changed, uh, in between the time that
the Query went through and, uh, until when the
QueryHit comes back. So, uh, this, in addition
to the fact that you're only maintaining some of the recently-received query messages may mean that you might receive
a QueryHit message, uh, for which you don't have
any information about a Query message with the
same matching descriptor ID. In this case, you do not flood
the QueryHit message; instead, you just drop it. Uh, this may result in some of
the, uh, responses being, uh, not shown
at the querying peer, but hopefully this is only a small portion of the total responses. So what happens when the
querying peer receives back, um, uh, the response? Essentially these are shown to,
uh, the client, and the client then, um, uh, selects one of them, depending on the, uh, bandwidth, uh, and then,
uh, the download starts. Well, how does
the download start? Well, initially the requester
or the querying peer, uh, sends an HTTP request to the responder's
IP address and port number. This is a GET http
request, as shown. It also contains, um, uh,
a connection type, which is a Keep-Alive, uh,
in this case an HTTP 1.0. It also specifies a range field. Uh, the range field
is essentially used, uh, to start partial file transfers. So for instance, if you started
to transfer a 1 MB file, and after you'd
transferred 512 KB the connection, uh, was killed for some reason, then you can trans ano-transfer- start another GET transfer by specifying the
range field that's 512 KB so that, uh, the file transfer
starts from the 512 KB, uh, onward, uh, rather than- and transfers only
the second half of the file rather than transferring
the entire file. When the responder receives
this GET message, it responds back
with an HTTP OK message, uh, with the content length,
the number of, uh, bytes, and then this
is followed immediately by packets that contain
the actual file data itself. So HTTP is a file
transfer protocol. Why the Gnutella developers
decided that-it's standard, it's well-debugged
and it's widely used, and they didn't want to reinvent a new file transfer protocol. The range field, as we
discussed, is used, uh, to support partial
file transfers so that you don't need to, uh,
restart the entire file, um, uh, transfer, uh, whenever
a connection gets dropped. Now one of the issues that
arises in the real internet is that, uh, some of these
peers are behind firewalls. A firewall is essentially used, uh, to prevent some kinds of messages,
uh, uh, from coming in. It does not, uh, prevent, uh,
messages from going out, or at least most messages
from going out, but it does prevent some
kind of messages from coming in. So if you go back, uh,
essentially, um, this HTTP message will not make its way to the responder if the responder
is behind a firewall. How do you then do
the file transfer? Well that's where the Push
message comes into play. What Gnutella does
is something very clever, which is that it uses
the overlay links themselves, remember that these edges in the overlay are already set up; they're already set up
TCP connections among, uh, the peers
or between pairs of peers. And so you can route whatever
messages you want, uh, using these links, and so that's what, uh, the, uh,
Gnutella requesting peer does. First it does try to set up
an HTTP connection to the responding peer. When it fails,
it guesses that hey, maybe the responding peer,
the yellow peer, in this case, is behind a firewall, and it routes a Push message via
the, uh, links in the overlay, and again, the Push message
is reverse routed along the Query hit path, okay, so it's reverse routed
along the reverse QueryHit path, and so when the peer receives
this, uh, Push message, it can then generate
an outgoing TCP connection. Here's what a Push
message looks like. Here's where the servent
ID field is used. This is, uh, taken from
the QueryHit message. The file index is also taken
from the QueryHit message so that you're not using
the entire file name. And then the IP address and
port number respond-correspond to the address
of the requesting peer so that the responding peer can create an outgoing
HTTP connection. When the responding peer
receives this Push message, it creates an, uh, uh, ah, uh, TCP connection that goes out
to the requesting peer. It sends a GIV HTTP
message along this. When the recei-when the
requestor receives this, it then sends a GET HTTP message
just like we discussed before, and then the file transfer
is completed just like we discussed before. If the requestor
is also behind a firewall, um, uh, then Gnutella gives up, uh, but you should be
able to think of, uh, a clear alternative,
uh, solution. Finally we come to the
Ping and Pong messages. These are used by peers, uh, to update, uh,
their neighbor lists. The Ping message, uh, is, uh,
flooded out, TTL restricted, and it is done so periodically
by every peer. Essentially, a Ping message
is sent by a peer to know its
immediate neighborhood. The TTL is typically-typically
the TTL is very small. It's typi- uh, typically
much smaller than 7 or 10, and this is used by the peer to know its one
or two Hop neighbors or three Hop neighbors maybe, so that it can
update its membership list. When a peer receives
a-a Ping message, it responds back
in the reverse route to the Ping message
using a Pong message. The Pong message contains
the IP address and port number of the responding peer, the number
of files it has shared, and the number of kilobytes
it has shared. These last two fields are used
by the, uh, pinging peer to prefer neighbors
which have more data and more files to share. Why is Ping and Pong needed? Well, because peer-to-peer
systems have a very high, um, rate of churn. Uh, clients are continuously
joining and leaving the system, and we'll discuss this
in a little bit, but the rate of churn
is so high that, the, uh, set of neighbors
that you have right now may not be there a few
seconds, uh, from now, because some of them
may have left the system. So it's very important for you
to keep your set of neighbors always, uh, fresh
and always, uh, fresh with the-with neighbors
that are are currently there in the, uh, uh, in the system so that you're not disconnected from the system. So in summary, Gnutella
maintains no servers. Instead, peers form
an, uh, overlay graph and they maintain neighbors. Peers store their own files,
queries are flooded out, TTL restricted,
forwarded only once, QueryHits are reverse routed along the reverse path. Gnutella also supports
file transfers when the responding peer
is behind a firewall, and it uses periodic Ping-pong to continuously refresh
neighbor lists so that, uh, peers maintain,
uh, connectivity to the overlay graph in spite
of churn in the system. Now because the size
of the list may be different, because different clients
may specify different maximal
neighbor list size, uh, they have found, um, uh, that there is heterogeneity
in the system, that different, uh, peers have
different numbers of neighbors. In fact, they've found that this
regular distribution, uh, the number of links
that a, uh, peer has follows a power
law distribution. In other words, the probability
that the number of neighbors you have is L ~ L/-k where k is a constant. This is a power
law distribution. Some of the problems with
original, uh, um, Gnutella have been solved since. Uh, the Ping and Pong traffic
in the original version of this Gnutella consumed a very
large amount of traffic, 50% of the traffic. One of the, uh, uh, fixes to
this was to multiplex. In other words, uh, when you
have multiple, uh, Pongs that are being received
from multiple peers, you, uh, make one Pong message out of it and, uh, send it forward instead of sending multiple
Pong messages. Similarly with the Pings, uh,
you forward, um, only one Ping when you receive multiple Pings. You can also cache
these messages. If you receive a Ping
from another, uh, peer and you have some
of the latest received Pongs for a previous Ping, you can simply send back, uh,
those cached pongs instead of forwarding
the Ping again. You can also reduce the
frequency of Pings and Pongs, uh, to bring down,
uh, this particular overhead. The same caching can
be used for keywords. Some files may be popular. A recently released song by some
artist may be more popular and may have, uh, may appear
in more Query messages. In that case you can cache
the QueryHit messages, and if you receive a query message with identical keywords to a previously cached
QueryHit message, then you can send back the previously cached
QueryHit messages instead of forwarding
the Query message themselves. Also, some peers just do
not have enough bandwidth. They might be connected over
very slow modems; um, they may not have enough
bandwidth for Gnutella traffic. In this case you may want
to use a central server to act as a proxy
for such, uh, peers. A different solution that leverages some
of the more powerful nodes in the systems, some of the more powerful appliance in a system, is called FastTrack,
which we'll discuss soon. Some of the other problems
with Gnutella, uh, which are not just problems
in Gnutella but problems with any
peer-to-peer system, uh, are the-is
problem of freeloaders. Uh, here, a-a freeloader
is essentially a user who only ever downloads files, never uploads files
to the peer-to-peer system. Studies, uh, have found that as
many as 70% of the users in the year 2000 in Gnutella
were freeloaders, um, and this meant that, um, only
a small fraction of the nodes, in this case 30%, uh, were taking on
most of the responsibilities of serving files, uh,
to the system. Again, this is a problem
that is not necessarily only Gnutella-specific. It's a problem that is-that
appears in all peer-to-peer, uh, systems because
of, uh, human behavior. This is not a technical issue, but rather
a human behavior issue. And I hope you have been
wondering all along, uh, why do you need to flood
the Query messages. Query messages being flooded
out are still fairly wasteful. A very large portion of the
entire overlay graph receives every single Query
message that is sent out. Uh, this can be very wasteful; this can use a lot of bandwidth. Instead, is there a way
of intelligently routing the Query messages so that it
reaches only those peers which are, um, currently storing, um, uh, copies of
the files that match, uh, the, um, what the querying
peer is looking for? That's essentially what a lot of the academic
peer-to-peer systems do. These are structured
peer-to-peer systems, and one of these systems,
called Chord, one of the first structured peer-to-peer systems that came out of academia, is one of the systems
that we'll study next.

### 05 - 4. FastTrack and BitTorrent

Slides: `C3_p2p_D_CSRAfinal.pdf`

#### Slide text

```
FastTrack

•   Hybrid between Gnutella and Napster
•   Takes advantage of “healthier” participants in
    the system
•   Underlying technology in Kazaa, KazaaLite,
    Grokster
•   Proprietary protocol, but some details available
•   Like Gnutella, but with some peers designated as
    supernodes

  A FastTrack-like System

Peers
                                 P
        P
                 P

                                     S

            P                S
                                     P
                Supernodes

FastTrack (contd.)

•   A supernode stores a directory listing a subset of nearby
    (<filename,peer pointer>), similar to Napster servers
•   Supernode membership changes over time
•   Any peer can become (and stay) a supernode, provided it has
    earned enough reputation
     •   Kazaalite: participation level (=reputation) of a user between 0
         and 1000, initially 10, then affected by length of periods of
         connectivity and total number of uploads
     •   More sophisticated Reputation schemes invented, especially
         based on economics (See P2PEcon workshop)
•   A peer searches by contacting a nearby supernode

   BitTorrent

Website links to              Tracker, per file   (receives
.torrent                                          heartbeats, joins
                                                  and leaves
                                                  from peers)
 1. Get tracker
                    2. Get peers
                                                  Peer (seed,
                                                         has full file)
    Peer                  3. Get file blocks

   (new, leecher)             Peer        Peer
                        (leecher,
                        has some blocks) (seed)

BitTorrent (2)

•   File split into blocks (32 KB – 256 KB)
•   Download Local Rarest First block policy: prefer early download of
    blocks that are least replicated among neighbors
     •    Exception: New node allowed to pick one random neighbor: helps in
          bootstrapping
•   Tit for tat bandwidth usage: Provide blocks to neighbors that
    provided it the best download rates
     •    Incentive for nodes to provide good download rates
     •    Seeds do the same too
•   Choking: Limit number of neighbors to which concurrent uploads
    <= a number (5), i.e., the “best” neighbors
     •    Everyone else choked
     •    Periodically re-evaluate this set (e.g., every 10 s)
     •    Optimistic unchoke: periodically (e.g., ~30 s), unchoke a random neigbhor –
          helps keep unchoked set fresh
```

#### Transcript

In this lecture
we will quickly review, uh, FastTrack and BitTorrent, uh, two systems
that are also very popular and have been very popular,
uh, for many years now. So FastTrack is, um, uh,
in a sense derived from Gnutella and is a hybrid between
Gnutella and Napster. Uh, it's a better version
Gnutella by, um, the fact that it uses some of the "healthier" participants, some of the more powerful peers in the system, uh, to make the system faster. FastTrack is
a proprietary system. It's the underlying technology in Kazaa, KazaaLite
and Grokster. Uh, though it's proprietary,
some of the details are known, and that's what we're
gonna discuss, uh, here. So FastTrack, for the most
part, is just like Gnutella. It maintains an overlay graph, but some of the peers, uh, have some special, uh, duties, and these peers
are known as supernodes. So this is what a FastTrack
system might look like. Uh, it looks just like a-a
Gnutella overlay, except that two of the peers, marked as "S" over here,
are supernodes. Uh, these peers might, uh, undertake some
of the responsibilities very similar to, uh,
Napster, uh, peers in the sense that they might be storing directory information that are used
by its neighboring peers in the overlay
to search for files. So a supernode stores
a directory listing of a subset of a nearby, um, uh, filename, uh,
peer pointer lists, uh, similar to what
Napster servers were doing. Uh, the supernode membership
might change over time. Essentially, a peer, uh, cannot
select itself to be a supernode. Instead, peers are selected
to be supernodes based on their contributions
in the past. Uh, essentially, uh, this
contribution is decided from a reputation level. For instance, in KazaaLite,
the participation level, the reputation, of a user
is between 0 and 1,000. When a user joins the system,
their reputation is 10. If the user has, uh, prolonged
periods of connectivity and more uploads
from that, uh, client, their reputation goes up, or the participation level goes up. When the participation level
crosses a threshold, uh, the peer might become
a supernode. Uh, there are also a lot of, uh, uh, sophisticated
reputation schemes that have been invented
in, um, the academic literature. Uh, there is an entire, uh,
workshop called P2PEcon, which, um, you might want to look at if you're interested, that covers some of,
uh, these ideas. With this, uh, the, uh, peers,
um, can now search much faster. They can just search
in nearby supernode, going back
to the previous figure. This peer on the bottom left
corner can now simply send a query, its query to, ah, its
neighboring supernode instead of flooding the query throughout the
entire overlay graph. Uh, why is there an advantage
to being a supernode? What is the incentive
to be a supernode? Well, a lot of your queries and
searches now become just local searches
in your local uh, data structure or your local
directory information, and so they do not incur
any network traffic. They are really, really fast. BitTorrent is
one of these systems that has been very popular
and continues to be popular. Uh, it has a lot of similarities with the systems
that we have discussed so far, but it works
in slightly different ways, uh, by incentivizing peers
to participate in the system. Remember that we discussed
that peers oftentimes do not contribute anything
to the system. They do not contribute files, they do not contribute even bandwidth in many cases, and BitTorrent addresses this
by having incentives, um, uh, for
the peers to participate so that the peers
can benefit from, uh, being unselfish
and helping other peers. So how does, uh,
BitTorrent work? Well, BitTorrent has
a notion of trackers. Uh, typically there is
one tracker per file. Uh, there might also be
trackers for multiple files. When a peer wants
to join the system, you f-somehow find, uh,
the torrent or the tracker, uh, and this, uh, enables you
to talk to the tracker. The tracker, uh, maintains
a list of some of the peers that are currently
transferring that file. Uh, it does so
by receiving heartbeats from, uh, the current, uh, peers heartbeat messages,
uh, from these peers. The peers are of two kinds,
a seed, which has a full file and is still continuing to be,
um, uh, part of the system and help the other peers download the file, and the leechers, which has some blocks from the file, a file is split up into blocks, [silence] typically equal sized blocks, and, uh, this
peer has some of the files and is still looking to download the other, uh, blocks
of that particular file. The new peer, when it joins this
particular, uh, group of peers, uh, is also a leecher
because it has, obviously, none of the blocks
of that particular file. A file is typically
split into blocks. Uh, the block size is fixed, maybe somewhere between 32 kilobytes to 256 kilobytes. Uh, now when a peer
starts to download a file from some of its neighbors, remember, going back
to the previous slide, the peer, when it joins, uh, when it joins the group, it has some neighboring peers, and it has multiple blocks
that it can download and multiple peers
from which it can download, uh, each of these blocks. How does it select
which block to download and which peer to download from? Well, it uses the Local
Rarest First policy. Essentially, um,
it prefers that block which is the least replicated among its current neighbors. Uh, this is useful because- because with churn
in the system, some of these blocks
might disappear quicker than other blocks, uh, and earlier than other blocks that are replicated more
among its neighbors. And so, uh, this Local Rarest
First policy helps to download those blocks
that are the rarest. There are of course
exceptions to this. Uh, a new node, newly joining
peer, is allowed to pick one, uh, neighbor at random,
and this helps in bootstrapping so that you don't
always get stuck, uh, with just one
deterministic group. Now incentives are provided by a tit-for-tat bandwidth
usage scheme. Um, uh, this incentivizes a peer
to provide blocks to neighbors, uh, so that, um, you-you're
providing blocks to neighbors that provided you the best download
rates in the past, okay? So this, uh, enables or
incentivizes your neighbors to provide download, uh,
speed to you so that you are then
able to provide, uh, blocks to it in the future. And the seeds do the same too,
not just the leechers. Now, the number of, uh,
concurrent transfers that might go on for-from a peer to its neighboring peers might become very large, um, so you don't want this to
overload the, uh, peer itself, and so choking is used here. Choking limits
the number of neighbors to which concurrent uploads
are going on. Um, uh, typically this is
a n-small number like 5. Uh, these are
the best neighbors. Everyone else is
considered to be choked. These selected neighbors are
considered to be unchoked. Uh, you periodically reevaluate
this set, say every 10 seconds, and you do
an optimistic unchoke, so periodically you
unchoke a random neighbor. This helps keep the, uh, set of
neighbors that are unchoked, uh, to be very, very fresh. Okay, and again, this is used,
uh, because the set of blocks that are-that are peers
is changing, and also the set of peers
in your group is changing because of, uh, churn. Okay, so choking, in summary,
helps peers to, um, uh, limit how many other peers they're, uh, uploading to, uh, so that the upload bandwidth is, uh, not overwhelmed.

### 06 - 5. Chord

Slides: `C3_p2p_E_CSRAfinal_v3-revised2.pdf`

#### Slide text

```
DHT=Distributed Hash Table

•   A hash table allows you to insert, lookup, and delete
    objects with keys
•   A distributed hash table allows you to do the same in a
    distributed setting (objects=files)
•   Performance concerns:
     •   Load balancing
     •   Fault-tolerance
     •   Efficiency of lookups and inserts
     •   Locality
•   Napster, Gnutella, FastTrack are all DHTs (sort of)
•   So is Chord, a structured peer-to-peer system that we
    study next

Comparative Performance

          Memory        Lookup    #Messages
                        Latency   for a lookup
Napster   O(1)          O(1)      O(1)
          (O(N)@server)

Gnutella O(N)           O(N)      O(N)

 Comparative Performance

          Memory          Lookup    #Messages
                          Latency   for a lookup
Napster   O(1)            O(1)      O(1)
          (O(N)@server)

Gnutella O(N)             O(N)      O(N)

Chord     O(log(N))       O(log(N)) O(log(N))

Chord

•   Developers: I. Stoica, D. Karger, F. Kaashoek, H.
    Balakrishnan, R. Morris, Berkeley, and MIT
•   Intelligent choice of neighbors to reduce latency and message
    cost of routing (lookups/inserts)
•   Uses Consistent Hashing on node’s (peer’s) address
     •   SHA-1(ip_address,port) 160 bit string
     •   Truncated to m bits
     •   Called peer id (number between 0 and 2 m − 1 )
     •   Not unique but id conflicts very unlikely
                                        m
     •   Can then map peers to one of 2 logical points on a circle

Ring of peers

Say m=7               0
6 nodes     N112          N16

          N96
                                N32

                N80       N45

Peer pointers (1): successors

Say m=7               0
            N112               N16

          N96
                                    N32

                N80           N45

                          (similarly predecessors)

Peer pointers (2): finger tables

                            At or to the clockwise of.

                            Also, use (n+2i) mod 2m.

What about the files?

•   Filenames also mapped using same consistent hash function
     •    SHA-1(filename) 160 bit string (key)
     •    File is stored at first peer with id greater than or equal to its
          key (mod 2 m)

•   File cnn.com/index.html that maps to key K42 is stored at first peer
    with id at or to the clockwise of 42
     •    Note that we are considering a different file-sharing
          application here : cooperative web caching
     •    The same discussion applies to any other file sharing
          application, including that of mp3 files.
•   Consistent Hashing => with K keys and N peers, each peer stores
    O(K/N) keys. (i.e., < c.K/N, for some constant c)

  Mapping Files

Say m=7               0
            N112          N16

          N96
                                N32

                N80       N45
                                File with key K42
                                stored here

      Search

      Say m=7                  0
                      N112         N16

                   N96
Who has cnn.com/index.html?              N32
  (hashes to K42)

                         N80       N45
                                          File cnn.com/index.html with
                                          key K42 stored here

      Search
                At node n, send query for key k to largest successor/finger entry <= k
                               if none exist, send query to successor(n)
                                                  0
                        N112                                        N16
   Say m=7

                   N96
Who has cnn.com/index.html?                                               N32
  (hashes to K42)

                           N80                                     N45
                                                                    File cnn.com/index.html with
                                                                    key K42 stored here

      Search
               At node n, send query for key k to largest successor/finger entry <= k
                              if none exist, send query to successor(n)
                                                  0
                        N112                                        N16
   Say m=7
                                                                       All “arrows” are RPCs
                                                                       (remote procedure calls)
                   N96
Who has cnn.com/index.html?                                               N32
  (hashes to K42)

                           N80                                     N45
                                                                 File cnn.com/index.html with
                                                                 key K42 stored here

    Analysis
                                                                  Here
Search takes O(log(N)) time
    Proof                                                                Next hop
    • (Intuition): at each step, distance between query and
       peer-with-file reduces by a factor of at least 2     Key

    •   (Intuition): after log(N) forwardings, distance to key
        is at most
    •   Number of node identifiers in a range of 2 m / N
        is O(log(N)) with high probability (why? SHA-1! and
        “Balls and Bins”)
        So using successors in that range will be ok, using
        another O(log(N)) hops

Analysis (contd.)

• O(log(N)) search time holds for file
  insertions too (in general for routing to
  any key)
    • “Routing” can thus be used as a building
      block for
        • All operations: insert, lookup, delete
• O(log(N)) time true only if finger and
  successor entries correct
• When might these entries be wrong?
    • When you have failures
```

#### Transcript

[MUSIC] So in the next series of lectures
we'll be discussing a variety of peer-to-peer systems that came
out of academic research. Some of these systems have
been deployed in the wild. The first system we'll study in somewhat
of detail is Chord, which arguably was one of the first few peer-to-peer
systems to be designed from academia. And it's also interesting because
it has several concepts and techniques that are widely used
in today's key value storage and NoSQL storage systems, which are very
popular in cloud computing today. So a lot of you might be familiar with
the data structure called a hash table. A hash table is a data structure
typically maintained inside one running process on one machine,
which allows you to insert, look up, and delete objects with unique keys. So you can perform these operations in
essentially order 1 time or constant time. And a hash table essentially
stores these objects in buckets based on a hash of the key, and
this allows you to look up and perform other operations like insert and
delete fairly quickly on each key. A distributed hash table, also known as
a DHT, is a similar data structure except that it runs in a distributed system
rather than in a single process. Again, objects here are files and
files have unique keys. Maybe the file name is the key. However, instead of storing
the objects into buckets, you store the objects at nodes or
hosts or machines in a cluster. And again, the cluster might be
distributed out throughout the world. Similar to the regular hash table, you have some concerns in
the distributed hash table. One is load balancing. You want each node or each host to have about the same number
of objects stored on it as everyone else. You don't want some hosts overloaded
with objects while others have far fewer objects. However, unlike the hash table,
where you can't lose a bucket but still have another, in a distributed
hash table you could lose a node but still have another around. So fault tolerance becomes a concern here,
which means essentially that you want to make sure that even though some
of the nodes might fail or might just leave the system due to churn,
you don't want to lose any objects. Just like a regular hash table, you want
to have efficient lookups and inserts and maybe perhaps even delete operations. And finally, you want to have locality,
which essentially means that you want the messages that are transmitted among
the clusters to be transmitted preferably among nodes that are close by in
the underlying network topology or in terms of the Internet
distance underneath. So Napster, Gnutella, and FastTrack
systems that we've just discussed so far are all kind of
distributed hash tables. But they're not really because they don't
really try to optimize the insert, lookup, and delete times,
as we'll see on the next slide. Chord is one of the first peer to peer
systems which tries to directly address this problem and tries to bring the
insert, delete, and lookup time down low enough that we can claim that it is, in
fact, a DHT or a distributed hash table. So here is how Napster and
Gnutella compare along three metrics, in terms of memory, both at the client and
at the server if applicable, and the lookup latency and
the number of messages for a lookup. So let's look at Napster here. Napster, at the client, essentially does
not store too much information other than the files that have been uploaded by
the user, so we'll discount that. But the only other information stored
is the address of the server or servers that it is talking to. However, at the server,
if there are N clients in the system and each one is uploading some constant
number of files, the server store directory information, which turns
out to be order and information. Essentially this means that it is linear
in the number of clients in the system. The lookup latency is essentially
just one round-trip time. Ignoring the time for
the servers to look up their internal ternary tree is just order 1. The number of messages for a lookup is also order 1,
because it's just one round-trip time. However, the server load is fairly high. It's order N. For Gnutella, however,
where you don't have servers and you only have this overlay graph,
the memory might be as high as order N. If the client does not have a limit
on the number of neighbors, then you could have peers that have
order N immediate one-hop neighbors in the underlying Gnutella overlay. The lookup latency would be as high as
order N in the case of a degenerate Gnutella topology that
essentially looks like a line. So you have one Gnutella
topology where all the nodes are joined in one straight line,
and you have a file that is
located only at one end of the entire topology, so
the file f is located here. And the query for it starts from here. So there's only one copy of the file. And because this is order N or N minus 1 links, essentially you have
a lookup latency that is order N. And so the number of messages for
the lookup is also 2 times N minus 1, which essentially means
that it's order N as well. So order N is a fairly large number,
especially when you're considering millions of nodes in the system, and
you really want to do better than this. And that's where Chord comes into play. It essentially makes all of these,
the memory, the lookup latency, and the number of messages for
a lookup order log N on expectation. Why is log N nice? Well, log N is nice because for practical
purposes, it's almost as good as constant. If we are taking, say, log base 2,
log base 2 of 1,000 is 10, log base 2 of 1 million is 20,
log base 2 of 1 billion is only 30. And when you consider the number of
IPv4 addresses, that's just 2 power 32, the log base 2 of that is just 32. So even though it's not really constant,
for practical purposes it's
considered to be a constant. Any case,
we won't push that under the carpet, we'll still refer to that as log N. So how does Chord achieve this? Let's look at that in
a little bit of detail. Little bit of history of Chord, so Chord was developed by researchers
from both Berkeley and MIT. Essentially Chord uses a technique
where each of the nodes in the peer-to-peer overlay selects its
neighbors in an intelligent fashion. Earlier Gnutella nodes essentially
selected their neighbors based on metrics like number of files shared,
number of kilobytes shared. And essentially,
they use the ping and pong messages. Here there are certain rules
that the nodes use to decide who their neighbors are. So we'll discuss the rules
over the next few slides. So Chord uses what is known
as consistent hashing. Consistent hashing has
different interpretations. I'll give one interpretation here and
the more popular interpretation later on. So consistent hashing basically means
that you take a peer's IP address and port number, which uniquely does
identify it, and you apply a well-known hash function such as the SHA-1 function,
which stands for secure hash algorithm. This is a well-known
cryptographic function. The output of this function
is a 160 bit string. No matter how large its input is,
its output is always 160 bits. And the nice thing about the hash function
is that if you run this hash function on the same input, no matter where you're
running it, no matter which host you're running it on, you're going to
get the same 160 bit output. So you take this 160 bit output and
you truncate it to m bits, where m is a system parameter. And this gives you a peer id,
which is essentially an m bit string, which is an integer between 0 to 2
power m minus 1, both inclusive. Now you can hash multiple
peers' IP addresses, address comma port number
of pairs using this. If m is large enough,
then the conflicts become very unlikely. You're not guaranteed to
not have conflicts, but they're very unlikely as
long as m is large enough. Essentially you want 2 power m to be much
greater than the total number of nodes or holes in your system. Essentially what this means is that
you can draw a circle which consists of 2 power m logical points running
from 0 to 2 power m minus 1. And if you have a set of nodes,
you hash each of these nodes, and you put them on the corresponding
hashed peer ID on this point. So, when you hash it, and
then you truncate it in bits, you get a number that is a peer ID. So, this node over here
has a peer ID of 16 or here when you hash the type port
number and so, we'll call it as N16. Similarly there is another
node with a peer ID of 32, another node with a peer ID of 45,
and so on and so forth. There are six nodes in
this particular cluster. In this system here we are using m equals
7 which means that these numbers run from 0 to 127 over here which
is the last point before the 0. Now, this is a ring and it loops around. So, at the point to the clockwise of
127 is 0 and then, you have 1 and so on and so forth. Now what are the neighbors
that the peers maintain? The first type of neighbors that the peers
maintain, as shown on this figure, are successors. Every node knows its immediate
clock-wise successor in the ring. So 16 knows about the IP address and
port number of 32, so it can send messages directly to it. 32 knows about the IP
address in port number of 45, can send messages directly to it,
and so on and so forth. Once again, 112 knows about the IP
address and port number of 16, so it can send messages directly to it,
and that completes the ring. Peer pointers are just
the successors in each node. Similarly you can have predecessors, where
each node knows its counter-clockwise, or anti-clockwise neighbor, in the ring. For most practical purposes,
caller only uses predecessors. That's the first kind of peer pointer. The second kind of peer pointer
which is somewhat complex is called the finger tables. But this is really useful to
route your queries very quickly. Now, in a system where you are using m,
the node has m finger table. So let say we have m equals 7 and we have
finger tables running from 0 through six. So that's run from 0 to m minus 1. Here is a rule for the finger table. The i finger table and
the peer that has peer ID n, is the first peer that
has ID immediately at or to the clockwise of n + 2 power i but
then, taking modular 2 power m. So, let's do the exercise for node N80. The value of N for 80 is just 80, right? So that's well known. So, let's say i equals 0. The 0 finger table at node N80 which is
this one over here, how did we get 96? So, 80 + 2 power 0,
n + 2 power i, that's 81, and so that's a point somewhere
here on the ring, right? The node immediately to
the clockwise of that, is 96, N96. And that's why we say that N96 is,
in fact, the zero-th finger table entry, at N80. So, N80 knows about N96 IP address and
port number, because it's zero-th finger table entry. Similarly, when you said i equals 1,
you get 80 + 2 power 1, that's 82. Again, already made it and
the clockwise of it is 96. And keep on going that way
until you reach i equals 4. When you have 80 + 2 power 4,
or 96 and again, that is 96, because 96 is at n + 2 power i. Now when you have i equals 5,
that's 80 + 2 power 5, that's 80 + 32 or a 112. And that gives you 112 as the fifth
finger table entry at node N80. Now instead of having 112, if you had for
instance a 113 and 113 over here then N113 would have been the fifth finger
table entry at this, at node N80 right? So, you are searching at n + 2 power i or
immediately to the clockwise of it. Now, coming to i equals 6 similarly n
plus 2 power 6 is 80 plus 2 power 6, that's 80 plus 64 that's 144. Let me right this down here. So that's 144 but
you need to now take modular 2 for m because 144 doesn't appear on the ring. Right, so you need to take 144 mod 128. And that essentially is 16. Right and so, you have this point
on the ring over here which is this point here and so, N16 becomes
the sixth finger table entry at node 80. So, one of the things you'll notice
here is that as you go along the ring, as you increase the value of i, the distance from one finger table
entry to the next doubles okay? And there's a reason for this, we want
to be using these for our searches, so that the searches are fast,
so that they are log in. And you'll see that in just a little bit. So that's how we place nodes on the ring. How do we place files, how would
we decide where files get placed? So unlike Napster Gnutella where clients
told their own files, and don't upload them by default, here instead find the
store in specific notes based on the same rules if your using for
placing the servers on the ring. In other words you take the filing, which we assume to be unique
across the entire system. You apply the same hash function to it,
the SHA-1 simple hash algorithm one. And get 160 bit string. Then, you truncate it again,
just like you did for peer ids, and then you map this file
onto a point in the right. Okay, so,
going back to the previous figure, the file might map to,
say, point 34, right. That's somewhere over here. Then the file is stored at the first peer
that is immediately to the clockwise, or right, of that point. So again, you need to take more mod 2
power m, so you wrap around the ring. So, for instance, if I have a file
name that's cn.com/index.html, this maps to a key, say 42. Once you hash and truncate it, that's
going to be stored at the first peer that is immediately to the right of 42,
which in our previous example would be 45. So here, notice that I'm
assuming unique files names and I'm using the URL as a unique file name. This is kind of intentional here. Typically, peer-to-peer systems that
have been developed in the wild are used to exchange MP3 and MPEG files,
but this is not a limiting factor. You can use peer-to-peer systems to
develop other applications such as cooperative web caching,
where client browsers across a large population of clients share their
web results with each other. So they have faster browsing because
you're able to fetch pages that have been fetched already by another
client that's near to you. In that case the URL's become
the name of the particular object and the objects here
are the webpages themselves. This essentially what I'm trying to
say here is peer review systems can be used for storing any kind of object,
no matter what kind of objects they are. As long as the objects have a unique
name in this particular case. So the most popular notion of consistent
hashing essentially says that with K keys and in the system and N peers in the
system, each peer will store about order, will store order keys over N keys. Okay, when I say order, O(K/N),
it just means that the number of keys at a peer is less than c times K over N for
some constant c with a high probability. And essentially this means that you have
good load balance across the different tiers in your system or
the different nodes in your system. Remember that this is what load balancing
was one of our goals when we started out. So, we still haven't talked about
how the rest of the system works. So once again, pictorially here is where the file
with key K42 would be stored at N45. I mean, if here the clockwise of maps. How the search work, okay, so
that's the next thing we need to discuss. So suppose N80 wants to search for
cnn.com/index.html, the first thing it does is that hashes
it and trunks it to embeds, gets 42. Now it knows that it needs to route
to the point 42 on the ring, or rather to the point that is
immediately to the north, that is immediately to
the clockwise of 42. How does it do this? Here is a search algorithm, and
this is applied recursively. So at node N, right now N is just 80,
when you have a query that is destined for key k, in this case k is 42. You forward the key to
the largest successor or finger table entry, essentially your
largest neighbor are, when I say largest it actually means it's the most to
the right wrapping around the ring. That is still to the left of K. Okay, if non exist then you
send the quality of successor. The second line ensures that even if
the finger table entries are wrong, then [INAUDIBLE] present,
then as long as the successors are correct you end up routing the query
to the correct server eventually. It might take a long time. It might take n hops in the worst case,
but you end up routing it to the right way. So let's ignore that same part for now but essentially at N80 remember that the finer
table entries an 96, 112, and 16. So the one among them that is
the farthest to the right, the farthest away clockwise from N80
that is still to the left of 42 is 16. That's why N80 will
forward the query to N16. When N16 received this, it does likewise. It calculates among it's neighbors
which are its successors and finger table entries, which is, the most
to right, but still to the left of 42. And you'll notice that 16 will
have 32 as a finger table entry because essentially,
16 plus 2 power of 4 is 32. But 16 plus 2 power 5 is 16 plus 32
that's 48 which means that the fifth, the next finger table entry
after 32 at 16 is N80, which means that 16 does not
even know about N45's existence. And so 16 has only two choices,
32 or 80 to forward the 32 and since 32 is to the left or counterclockwise
of 42, it forwards it to 32. 32 tries to do similarly but it doesn't have a neighbor that is to the
left of 42 so it simply forwards it to its successor and that's where
the second line comes into play. And that makes its way to 45. Whenever a node receives a query in
relation to this algorithm, it also checks its local files to see if any of those
files match, and in this case, 45 matches. And it can respond back directly
to anything with the response. Now in this case,
I've drawn three arrows here. Each of these are the hops
that the query takes. These hops are essentially RPCs or
remote procedure calls. This is a well known abstraction
in discriminate systems. So I claim that this algorithm
takes O(log(N)) time. Why is that?
Well, essentially what happens is that if
you consider the points on the ring, whenever query takes a step, whenever it
takes a hop from one pier to another. The distance between where
the query is and the ring and the point where the key is,
this dotted line, that distance goes on by
a factor of at least two. because as you do I'm
saying this is where so this is where the query currently is and
this is where the key is on the ring. Then if you consider the second
half of this particular segment that's where the query's
going to jump to next. Again why is this, this is again you
can prove this by contradiction. If this was not true, if the query jump to
the first half of the segment over here. Then we can show because of the doubling
of the finger table entries that there's going to be at least one
finger table entry in the second half. Which this node must know about and
you reach a contradiction. Essentially because the finger table
entries double this node over here. It's going to have at least one neighbor
in the second segment which is to the left of Key K. It's going to have at least one finger
table entry in the second segment which is to the left of Key K and
it's going to forward that to that one. So essentially, after log and forwardings
the distance to the key increases by a factor of two power log N and
that's just N. because we're taking log base 2 over here,
and so the distance between where the queries and where the keys in terms of points on
the ring, is 2 power N divided by N. So essentially, this means that now
even if you use the successors in this small section of the ring which
has two power m divided by n points. You want to have the query
reach the eventual key. But this using balls and bins you can show
that in the small segment of the ring. There is only order log N appears
with high probability, and so even if you use successors in
this small section of the ring. Once you have done these log N
forwardings, you can only hit another order log N peers with hyper mobility,
so that's log N plus log N, which is still order log N hops for the
entire equation to reach where the key is. Now the algorithm that
I described to you so far is essentially it's not just for
searching. So, so far we've assumed that it's for
searching but you can essentially use that
algorithm to route to any key. And the routing message is independent
of what operation you're doing on it. So you might have the routing message say,
hey, I want to insert this key. Or I want to delete this key. Or I want to update or look up this key. It doesn't matter. So routing essentially is the building
block that we have discussed so far. And it can be used for any of these
distributed hash table options, or DHT options. Now somebody said that, and were shown that time to do a routing
message to any key is order log in. But this is true only the finger tables
and the successor entries are correct. When could they be wrong,
well they could be wrong when you have a peers leave the system whether
they fail or whether they out. And the corresponding successors and finger table entries
have not been updated. [MUSIC]

### 07 - 6. Failures in Chord

Slides: `C3_p2p_F_CSRAfinal.pdf`

#### Slide text

```
Search under peer failures
                                              Lookup fails
      Say m=7                  0         (N16 does not know N45)

                      N112                    N16

                   N96                    X
Who has cnn.com/index.html?
  (hashes to K42)                         X
                                                    X
                                                    N32

                         N80                  N45

                                   File cnn.com/index.html with
                                   key K42 stored here

      Search under peer failures

                               One solution: maintain r multiple successor entries
      Say m=7                            0 In case of failure, use successor entries
                      N112                               N16

                   N96
Who has cnn.com/index.html?
  (hashes to K42)
                                                              X
                                                              N32

                         N80                            N45
                                                 File cnn.com/index.html with
                                                 key K42 stored here

Search under peer failures

•   Choosing r=2log(N) suffices to maintain lookup
    correctness w.h.p. (i.e., ring connected)
     • Say 50% of nodes fail
     • Pr(at given node, at least one successor alive)=
                                        1 2 log N      1
                                    1− ( )        = 1− 2
                                        2             N
     • Pr(above is true at all alive nodes)=

                                                   1
                                        1 N /2 −
                                   (1 − 2 ) = e 2 N ≈ 1
                                       N

      Search under peer failures (2)

      Say m=7                  0                      Lookup fails
                      N112                   N16      (N45 is dead)

                   N96
Who has cnn.com/index.html?                      N32
  (hashes to K42)                        X

                         N80               X
                                           N45
                                   File cnn.com/index.html with
                                   key K42 stored here

      Search under peer failures (2)

                              One solution: replicate file/key at r successors and predecessors
      Say m=7                                     0
                      N112                                           N16

                   N96
Who has cnn.com/index.html?                                               N32
  (hashes to K42)
                                                                           K42 replicated

                         N80                                       X
                                                                   N45
                                                          File cnn.com/index.html with
                                           K42 replicated key K42 stored here

Need to deal with dynamic changes

    Peers fail
•    New peers join
•    Peers leave
       •    P2P systems have a high rate of churn (node join, leave and failure)
               •   25% per hour in Overnet (eDonkey)
               •   100% per hour in Gnutella
               •   Lower in managed clusters
               •   Common feature in all distributed systems, including wide-area (e.g.,
                   PlanetLab), clusters (e.g., Emulab), clouds (e.g., AWS), etc.

So, all the time, need to:
 update successors and fingers, and copy keys

 New peers joining
          Introducer directs N40 to N45 (and N32)
          N32 updates successor to N40
          N40 initializes successor to N45, and inits fingers from it
          N40 periodically talks to neighbors to update finger table
Say m=7                             0
             N112                                    N16      Stabilization
                                                              Protocol
                                                              (followed by
                                                              all nodes)
          N96
                                                          N32

                                                               N40
                N80                                 N45

 New peers joining (2)

       N40 may need to copy some files/keys from N45
            (files with fileid between 32 and 40)
Say m=7                       0
            N112                      N16

         N96
                                            N32

                                              N40
               N80                    N45
                                                  K34,K38

New peers joining (3)

•   A new peer affects O(log(N)) other finger
    entries in the system, on average [Why?]
•   Number of messages per peer join=
    O(log(N)*log(N))

•   Similar set of operations for dealing with
    peers leaving
     •   For dealing with failures, also need failure
         detectors (we’ll see these later in the course!)

Stabilization Protocol

•   Concurrent peer joins, leaves, failures might cause
    loopiness of pointers and failure of lookups
     •   Chord peers periodically run a stabilization algorithm
         that checks and updates pointers and keys
     •   Ensures non-loopiness of fingers, eventual success of
         lookups and O(log(N)) lookups w.h.p.
     •   Each stabilization round at a peer involves a constant
         number of messages
     •   Strong stability takes O ( N 2 ) stabilization rounds
     •   For more see [TechReport on Chord webpage]

Churn

•   When nodes are constantly joining, leaving, failing
     •   Significant effect to consider: traces from the Overnet system
         show hourly peer turnover rates (churn) could be 25–100% of
         total number of nodes in system
     •   Leads to excessive (unnecessary) key copying (remember that
         keys are replicated)
     •   Stabilization algorithm may need to consume more bandwidth
         to keep up
     •   Main issue is that files are replicated, while it might be
         sufficient to replicate only meta information about files
     •   Alternatives
           •   Introduce a level of indirection (any p2p system)
           •   Replicate metadata more, e.g., Kelips (later in this lecture series)

Virtual Nodes

•   Hash can get non-uniform  Bad load balancing
     • Treat each node as multiple virtual nodes
        behaving independently
     • Each joins the system
     • Reduces variance of load imbalance

Wrap-up Notes

•   Virtual Ring and Consistent Hashing used in Cassandra,
    Riak, Voldemort, DynamoDB, and other key-value stores

•   Current status of Chord project:
     •   File systems (CFS, Ivy) built on top of Chord
     •   DNS lookup service built on top of Chord
     •   Internet Indirection Infrastructure (I3) project at UC Berkeley
     •   Spawned research on many interesting issues about
         p2p systems

     http://www.pdos.lcs.mit.edu/chord/
```

#### Transcript

Following from our, uh,
previous, uh, lecture on, uh, Chord, uh, today we'll discuss, uh,
the effects of failures, um, on Chord and how Chord tackles,
uh, failures and churn. So when you have, uh,
peers that fail, the lookups might go wrong. So for instance,
in our previous example, where N80 was trying
to route to 42, if one of the intermediate
nodes, 32 in this case, uh, had failed and
the corresponding successors and finger table entries
had not been updated, then 16 does not even know
about the existence of 45, and it cannot forward it to 45. In fact, it can't forward it
to anyone because, uh, the next hop would in fact be the origin
query node in this case. So in this case the-the query
would in fact, uh, be lost and would never
receive a response. So one of the solutions to this is, uh, for nodes to maintain not just one successor entry but multiple successor entries, so, uh, the nodes maintain
up to r successor entries where r is
a fixed number systemwide but is a configurable number. How large does r need to be for, uh, queries
to be routed correctly in spite of a large number
of failures? Well, it turns out
that r=2log(N) or O(log(N)) suffices to maintain
lookup correctness with high probability;
that's what w.h.p. means. Uh, in other words, a ring stays
connected, uh, in spite of this. Why is this? Well, essentially remember that
the mechanism we are using here is that a node
goes through its successors, and if it finds
at least one successor alive, then it forwards
a query to that successor, and if this happens
at every node in the system that is alive, then we consider
that the query gets forwarded. Suppose as me is 50%
of the nodes fail in the system simultaneously. Yes, this is not
a common occurrence, but let's say this happens. Then, at a given node, the probability that at least
one of its successors is alive is 1 minus the probability that
all its successors are dead. Since 50% of the nodes fail, this probability
is (1/2)^2log(N). That's the probability
that all its successors, all its r=2log(N)
successors are dead. And so 1 minus that is the probability that at least
one of its successors is alive, and if you calculate this, because you're taking
log base 2, this is 1-(1/(N^2)). You want this to be true at all
the nodes that are alive that have not failed, and so the probability
of that happening is just this, uh, quantity raised
to the number of alive nodes, which is N^2, and there's a well-known limit
theorem that shows that this is e^-(1/2N), which is actually equal wa-to 1-(1/2N)
when, uh, N is large enough. And again, this is a well-known
limit theorem over here. And so you'll notice that this
number goes to 1 very quickly as N goes to infinity. So this is saying that
as the number of nodes or peers in your system scales up
as your system becomes larger, the probability
of lookup correctness will in fact increase and
go closer and closer to 1, which is a very good thing. This shows that the system
is fairly scalable. The other thing that could go
wrong is that the node or the peer storing the file
might itself fail. If 45 fails, then there is no copy
of the file cnn.com/index.html, and so no matter
where you route the query or what intelligent
routing you use, you'll never get
a copy of the file 'cause it doesn't exist. So the way to combat this
is to replicate the file. So you store multiple copies
of the file, uh, one at N45, but also some at its successors
and predecessors. So in this case you store
it at one successor and one predecessor, so N80 has a copy of the file and N32 also has
a copy of the file. In this case because N80 has
a copy of the file, its query becomes moot,
so it can just do a local search and the query is answered, but if N96 were sending
the query instead, then the query might
be able to hit N32 and, uh, N32 could respond back directly. So this has the second
additional advantage, other than fault tolerance,
of also load balancing. If you have a key that
is very popular, for instance, you are storing a file
that is an mp3 of a recently-released song
that is, uh, in the top 5 on the, um, uh,
Billboard top 100 list, then this file is likely to
receive a lot of, uh, queries, and so if you spread this file
out over multiple replicas, uh, the load on each of these
replicas also goes down. So load balancing
is a very important concern over here as well. So, so far we have discussed,
uh, peer failures, but no, uh, but peers
can also join the system and also leave the system. In general
this is known as churn, which is a high rate of, uh, peers or nodes joining, leaving and failing
from the system. Churn could be as high as 25% in
some, uh, peer-to-peer systems such as eDonkey, and as high as
100% in systems like Gnutella. Essentially this means that if
you had a Gnutella network, uh, if 10 million nodes were,
uh, in-in the Gnutella system at the beginning of the hour,
by the end of the hour, uh, 10 million nodes would have, uh, joined, left and failed away
from the system. It may not be the same set
of 10 million that were there
at the beginning, but it's a total count
of 10 million. The churn is lower
in managed clusters and in, um, in-in, uh, clouds such as, um, experimental clouds like PlanetLab and Emulab, and also, uh, clouds
such as the AWS, uh, but it's still present;
it's not zero. So when churn does happen,
essentially you need to update successors and finger table entries. Why, because you want to get
O(log(N)), um, lookup cost for your, uh, queries
and for your other operations. Also, you may need
to copy some keys. Um, you'll see why in a moment. So when a new peer joins, um, here's how it initializes its, uh, uh, membership list or its finger tables
and successor entries. Remember that the new peer
joins the system by contacting a well-known introducer using a DNS, we discussed this
a few lectures ago, and the DNS, um, uh,
the server that it contacts gives it the, uh, IP address
of some peer in the system. And now, you can use this peer
to route to its own ID, so the peer that is joining,
say, has an ID of 40. It routes a message to N40 using the regular
Chord routing protocol, and this makes its way to N45, because 45 is the first,
um, uh, peer that is immediately
clockwise of N40. Assuming that 45 knows its
predecessor, at this point N40, when it receives back
the acknowledgement from N45, knows its successor as well
as its predecessor in the ring. At this point, uh, the N32 upda-updates
its successor to N40, the new node, N40 initializes
its successor to N45, and it copies the finger
tables over from N45, okay? So it just doesn't copy it over;
it uses the population of, uh, peers that N45 knows about and considers that as the
entire population of the system, and uses those, along
with its finger table rules, to initialize its finger table. However, these finger table
entries may not be correct, because N45's neighbors were only a small subset
of the entire system. So in order
to, uh, have N40 know about more and more peers
in the system, a stabilization protocol
runs in the background. Essentially, the stabilizing
protocol, uh, which runs periodically
at each node, the node asks
its immediate neighbors, finger table entries
as well as successors, for their finger table entries
and successors. This, uh, gives it a larger
population of, uh, peers to consider
as its potential neighbors, and this will, uh, over time lead to more and more correct finger table entries and successors for the node. This stabilization protocol
is run by a newly joined node periodically as well as by all the nodes
that are there in the system. Essentially, any node
that is there in a Chord ring will have to run
the stabilization protocol periodically forever. So essentially,
as the churn happens, the stabilization protocol is always trying to play catchup and update the finger table entries and successors to the correct values in spite of churn already
happening in the system. So if the rate
of the stabilization protocol is fast enough, then it can-it can keep up
with the rate of churn. The other thing that needs to
happen when N40 joins the system is some keys need
to be copied over. Remember that the invariant
for keys was that the key, or the files stored
at the first peer that is immediately
to the clockwise of the key. So keys like 34 and 38 which
were previously stored at N45, will now need to be stored
at N40, because 40 is now, uh, the first peer immediately
to the clockwise of 34 and 38. So some of these keys will need
to be copied over, and this might mean
file transfer between, uh, the successor
of the newly joining node and the newly joining node. Now, over time the stabilization
protocol affects not just the newly joining nodes, finger table entries and successors, but also the finger table
entries and successors of some of the existing nodes. Why is this? Well let's go back
to the previous slide. Say some node was over here
and it's N+2^i for its ith finger table
entry fell at 33. Earlier, that ith finger table
entry was, um, of that node, was 45, but now it needs
to be updated to 40. How does this happen? Well over time 112 as is run- as it runs
its stabilization protocol, gets to know about
N40 eventually, and then it says "Aha! N40 is a better
finger table entry- ith finger table entry
than N45," and it updates
its ith finger table entry. So you can show that, um,
a new peer affects O(log(N)) other finger table entries
in the system on average. This is because of the symmetry, um, because every node
points to O(log(N)), uh, finger table entries. Um, then you can show that, uh, a newly-non, an,
because a newly joined peer has O(log(N))
finger table entries or the log(N)
other finger table entries throughout the entire system
would get affected and, uh, point
to the new peer on average. So the number
of messages per peer join is about O(log(N)*log(N)). Uh, and we have so-
we have discussed so far the, uh, the, uh,
messages required, or the techniques required
for dealing with failures as well as with node joins. Dealing with the peers
leaving voluntarily is similar to dealing
with failures, um, uh, uh, and, um, and-and essentially, uh, i-it has a similar
set of operations as we have-
as we've discussed so far. In order to deal with failures, you also need
a failure detector, uh, which we have discussed, uh,
elsewhere in, uh, the course. So a little bit about
the stabilization protocol. Uh, essentially, when you
have concurrent peer joins, leaves and failures, you don't just have one node joining and leaving
in the entire system. Because th-the scale
of the system is very large, you might have nodes simultaneously joining and leaving the system. To tackle this, uh, Chord peers
run the stabilization algorithm, which updates
the pointers and keys. It ensures non-loopiness
of fingers, uh, so that queries are not
just looping around forever but they actually make progress, and it ensures eventual success of, uh, lookups and, uh, efficient logarithmic lookups with high probability. Each stabilization round
at a peer involves a constant number of messages. Uh, essentially, uh, it
either queries a small number of, uh, its successors and finger table entries, or it queries all of them and log(N) can be considered
to be a constant. Now a notion of strong stability which means actual correctness of all finger table entries and, uh, um, finger table and-and successors, it takes
O(N^2) stabilization rounds. So once churn has stopped
in the system, you'd need another
O(N^2) stabilization rounds. Now, even though
the stabilizations were run periodically at nodes, uh, one of the things
is that, uh, the stabilization at each node is independent of the stabilization
at the other nodes, so they are not synchronized
with each other, and yet it takes
O(N^2) stabilization rounds, um, across nodes. So essentially
it takes O(N^2) time for the system to stabilize, and some have argued
that this is fairly high. There are more details on this if you're interested in knowing about O(N^2), uh, on the, uh, Chord web page, uh, where there is a tech report
that outlines these. So churn, as we have discussed,
uh, can be very high, uh, 25% to 100% in the system, and this could leave to-
lead to excessive copying. Remember that whenever nodes
join, leave and fail from the system, you need to, uh, transfer
some files over so that the file storage
invariants are maintained. Uh, the stabilization algorithm might also consume
more bandwidth to keep up, partly because
of these file transfers. If you're transferring mp3s
and MPEGs around all the time due to churn, uh, this is a fairly high uh, bandwidth usage. However, you can fix this
by using a level of indirection. As they say, uh, solution
to a lot of problems in computer science is to use
another level of indirection. Essentially, in this particular
case it means that instead of storing, uh,
the file at a particular peer, that is, to the clockwise of it, you store a pointer to the file. The file stays, for instance,
at the peer that uploaded it, but a-a pointer to it is the one
that is, uh, stored at, uh, the peer immediately
to the clockwise of the file ID, and whenever, uh, this peer, uh, is affected by a failure
or a-or a peer leave, uh, only the meta information
or the pointer about the file is changed around. This leads to a reduction
in the bandwidth that is used for copying keys when you have
no churn in the system. The other option is, uh, to push
this all the way through, uh, into the system itself and to replicate the entire
metadata as you will see, uh, with the Kelips system which we'll discuss
in a couple of lectures. Uh, one of the tricks
that Chord uses, uh, to achieve more load balance, uh, is that, uh, uses
the notion of virtual nodes. Because the hash, uh, function is not guaranteed
to be uniform, uh, this may lead
to bad load balancing, where if you have a long segment between you and your predecessor on the ring, you being a peer, uh, there a very large number
of keys may be assigned to you. In order to prevent this, every node pretends
to be multiple virtual nodes and joins as multiple
virtual nodes in the ring, and when you have
a larger population, this leads to a more, uh, load balanced set of segments, um, and so a more evenly load balanced, uh, distribution of, uh, keys or files across the, uh, peers in the system. So virtual ring and consistent
hashing that we studied in Chord are widely used
in key-value stores today, uh, Cassandra, Riak, uh, LinkedIn's
Voldemort, and Amazons DynamoDB, and a variety
of other key-value stores. Even though those
key-value stores no- don't necessarily use
all the techniques of these, um, of the Chord
peer-to-peer system, a lot of the techniques are
used, uh, as we'll see later on. Uh, the Chord project has been
used to build file systems such as CFS,
and Ivy on top of it, uh DNS system on top of it, uh, and an Internet Indirection
Infrastructure on top of it at Berkeley, uh, and it has spawned many
interesting, uh, research ideas and issues about
peer-to-peer systems. For more information, you can refer to this
URL noted on this, uh, slide.

### 08 - 7. Pastry

Slides: `C3_p2p_G_CSRAfinal.pdf`

#### Slide text

```
Pastry

•   Designed by Antony Rowstron (Microsoft
    Research) and Peter Druschel (Rice University)
•   Assigns ids to nodes, just like Chord (using a
    virtual ring)
•   Leaf Set – Each node knows its successor(s) and
    predecessor(s)

Pastry Neighbors

•   Routing tables based prefix matching
     • Think of a hypercube
•   Routing is thus based on prefix matching and is
    thus log(N)
     • And hops are short (in the underlying
        network)

Pastry Routing

•   Consider a peer with id 01110100101. It maintains a
    neighbor peer with an id matching each of the
    following prefixes:
      • 0*
      • 01*
      • 011*
      • … 0111010010*
•   When it needs to route to a peer, say 01110111001, it
    starts by forwarding to a neighbor with the largest
    matching prefix, i.e., 011101*

Pastry Locality

•   For each prefix, say 011*, among all potential
    neighbors with a matching prefix, the neighbor
    with the shortest round-trip time is selected
•   Since shorter prefixes have many more
    candidates (spread out throughout the Internet),
    the neighbors for shorter prefixes are likely to be
    closer than the neighbors for longer prefixes
•   Thus, in the prefix routing, early hops are short
    and later hops are longer
•   Yet overall “stretch,” compared to direct Internet
    path, stays short

Summary of Chord and Pastry

•   Chord and Pastry protocols
     • More structured than Gnutella
     • Black box lookup algorithms
     • Churn handling can get complex
     • O(log(N)) memory and lookup cost
         • O(log(N)) lookup hops may be high
         • Can we reduce the number of hops?
```

#### Transcript

Today we'll discuss, uh, another, uh, peer-to-peer system
that came out of academia. Um, this system
is called Pastry. This system was, uh, designed
by Anthony Rowstron from Microsoft
Research Cambridge, and Peter Druschel from, uh,
Rice University, um. And just like Chord, uh, this, uh, system
assigns IDs to nodes using a consistently-consistent
hashing function, so again, you can imagine a virtual ring
where peers are hashed onto a point on the ring. But the way in which, uh,
neighbors are maintained is slightly different in Pastry. Uh, the first kind of neighbor
that, uh, Pastry nodes maintain is a leaf set. So each node knows
its successors and predecessors, multiple successors,
multiple predecessors. This is kind of similar to the Chord successors
and predecessors. Uh, however, uh,
the routing tables, uh, instead of using the N+2^i rule that we used for Chord instead use prefix matching. This is sort of like
hypercube routing. So routing is based
on prefix matching and turns out to be O(log(N)) because a hypercube with N points is O(log(N)) in diameter. In addition Pastry, unlike
Chord, also pays attention to the underlying
network, uh, topology and tries to make, uh, the neighbor, uh, edges to be short in the underlying
neighboring topology as well. We'll see how that works, uh. So in Pastry
let's consider a peer with ID, uh, shown, 01110100101. Uh, this peer maintains,
uh, a neighbor peer with an ID matching
each of the following prefixes. Okay, so the first
prefix is a star (*). Essentially when I say a *,
I mean that the first bit is a bit that differs from this
peer's corresponding bit. So essentially this would be
any of the peers that starts its ID with a 1 instead of a 0. Uh, then, um, the next, uh,
neighbor it maintains, uh, this peer maintains,
is one that starts with a 0, and then the next bit
is different from this peer, so the next bit
would essentially be a 0, okay, so a 0, 0 and
then followed by whatever, else. Similarly, the next one
is a 0, 1 and a 0, because that differs
from this bit, uh, here, and, uh, so on and so forth. 'Cause, essentially,
if there is a, uh, peer with an ID that contains m bits, the peer might have
up to m, uh, neighbors, one for each
of the prefix matches. Now, given this, when you
need to route, ah, a message to a peer, say, suppose,
this peer with the ID that we considered earlier needs to route it
to a peer that is 01110111001, the first, uh, mismatching bit
that is different is, uh, this, uh, seventh bit over here
which is 1, okay? So the 0111101
is the matching prefix, and the next bit 1
is a, uh, differing bit. So this, uh, peer
that has the message, uh, destined for this
given IP address, uh, starts by forwarding it
to that neighbor of itself which has
the largest matching prefix. So in this case, it would be the neighbor
that starts with 011101, and then a 1, and
then followed by whatever. Uh, it might also have neighbors that have a larger
matching prefix, and if it does, then it forwards a message
to that neighbor. You can show that, uh,
this, uh, results in a O(log(N)) routing time
for messages in Pastry. Once again,
I hope you, uh, notice that this prefix routing
is fairly different, uh, and is, uh, unlike the routing
that was used in the Chord DHT that you saw earlier. Now, prefix matching is nice because it allows you
to be, uh, aware of the underlying
network distances. So for each prefix, uh, that a node wants
to maintain a neighbor for, say 011*, there
are many potential neighbors, all of which have, uh, a prefix
011 that start, uh, at their ID. Uh, among all these
potential neighbors, uh, you select that neighbor which has the shortest
round-trip time in the underlying network. So this allows the hop from you
to one of your neighbors, in this case 011*, uh,
to be, uh, the closest among all the potential neighbors for 011*. Now, since shorter prefixes, uh, mean, um, that there are, uh, many more, uh, candidates, shorter prefixes mean that there
are many more possibilities for the, uh, for the suffix, uh, it's likely that the closest one of these is much closer to you than, uh, it is
for a longer prefix. So in essentially, uh,
you're saying that, uh, going back to the previous slide the candidates
in these shorter prefixes are likely to be very close
to you in the round-trip time in the underlying network, as long as you select
the closest candidate among all. So when you use prefix routing, essentially this means
that the first few hops, the early hops
in the, uh, in the query are in fact very short hops, and the later hops
are much longer hops in the- uh, in the
underlying network. However, you can show, uh, as the original authors
and designers have shown, that the overall stretch compared to the
direct internet path between the querying node and
the eventual destination node is in fact very small and, uh,
is just a constant factor, which means that Pastry,
in spite of being able, i-in spite of routing via
many, ah, intermediate peers, is able to get you, uh, an
end-to-end, uh, round-trip time which is comparable, uh, to the underlying
internet round-trip time between the querying node and
the eventual destination node. So summarizing Chord and Pastry; Chord and Pastry are both more structured than Gnutella. They are essentially distributed
hash tables in the sense that they, uh, enable you to do
Insert, Lookup, Delete, Update, and essentially any operation
on the key in O(log(N)) time. Uh, the lookup algorithms are
essentially routing algorithms, so they are black
box algorithms. Uh, the churn handling
can get complex. Uh, Pastry also uses similiz-
similar stabilization protocol, um, or I shouldn't say similar, it uses a stabilization protocol uh, which has
the same goals as Chord. The memory is O(log(N)), because you maintain
O(log(N)) neighbors to look-up cost
results of O(log(N)). Um, uh, yet the O(log(N))
lookup costs may be high. We did say that log(N)
was a small number, but it's not 1, it's not 2. It's still maybe 10, 20, 30, uh, and, uh, if you're considering log(N) log base 2 and you're still saying order, which means that there is
a constant factor on top of it. So the next question that
arises, can we really design a system that has just
an O(1) lookup cost, just a constant number
of hops for the lookup? That's the next
system we'll discuss.

### 09 - 8. Kelips

Slides: `C3_p2p_H_CSRAfinal.pdf`

#### Slide text

```
Kelips – A 1 hop Lookup DHT

• k “affinity groups”                           15
    •   k~√N                                                76

• Each node hashed to
  a group (hash mod k)                                     18
                                                160
• Node’s neighbors                  129
    •   (Almost) all other nodes                           167
        in its own affinity group
    •   One contact node per
                                       30
        foreign affinity group

                                                      …
                                    Affinity              # k-1
                                                #1
                                    Group # 0

    Kelips Files and Metadata
                                           •   PennyLane.mp3 hashes to k-1
•   File can be stored at any              •   Everyone in this group stores
                                           <PennyLane.mp3, who-has-file>
    (few) node(s)
•   Decouple file                                             15
    replication/location                                                         76
    (outside Kelips) from
    file querying (in Kelips)                                                   18
•   Each filename hashed to                                  160
    a group                              129
     •   All nodes in the group                                                 167
         replicate pointer
         information, i.e., <filename,
         file location>
     •   Affinity group does not            30
         store files
                                                                           …
                                  Affinity Group # 0        #1                 # k-1

    Kelips Lookup
•   Lookup                                     •   PennyLane.mp3 hashes to k-1
                                               •   Everyone in this group stores
     •   Find file affinity group              <PennyLane.mp3, who-has-file>
     •   Go to your contact for
         the file affinity group                              15
     •   Failing that try another                                                     76
         of your neighbors to find
         a contact
•   Lookup = 1 hop (or a few)
                                                                                     18
     • Memory cost O(√ N)                                    160
    • 1.93 MB for 100K                   129
      nodes, 10M files
                                                                                     167
    • Fits in RAM of most
      workstations/laptops
      today (COTS                           30
      machines)
                                                                            …
                                     Affinity Group # 0      #1                    # k-1

    Kelips Soft State
                                           •   PennyLane.mp3 hashes to k-1
•   Membership lists                       •   Everyone in this group stores
                                           <PennyLane.mp3, who-has-file>
     •   Gossip-based
         membership                                        15
     •   Within each affinity                                                    76
         group
     •   And also across affinity
         groups                                                                 18
     •   O(log(N))                                        160
         dissemination time            129
•   File metadata                                                               167
     •   Needs to be
         periodically refreshed           30
         from source node
     •   Times out
                                                                         …
                                    Affinity Group # 0
                                                          #1                   # k-1

Chord vs. Pastry vs. Kelips

•   Range of tradeoffs available
     • Memory vs. lookup cost vs. background
       bandwidth (to keep neighbors fresh)

What We Have Studied

• Widely-deployed P2P systems
   1.   Napster
   2.   Gnutella
   3.   Fasttrack (Kazaa, Kazaalite, Grokster)
   4.   BitTorrent
•   P2P systems with provable properties
   1.   Chord
   2.   Pastry
   3.   Kelips
```

#### Transcript

In this lecture,
we'll discuss Kelips, which, uh, brings
constant lookup cost, uh, to, uh,
a distributed hash table. So in Kelips,
unlike in Chord and Pastry, which we have seen before,
we don't use a virtual ring. Instead we use affinity groups. There are k affinity groups. These are, of course,
virtual groups, and k is about square root of n, where n is the number
of peers in the system. Each node or each peer
is hashed to a group. Essentially, you take hash using, say, SHA-1, uh, and then you take modulo k, k being an integer. And so, say, a peer with, um, uh, peer ID 160 would get hashed to group #1 because that's what
hash mod k gave it, um, and, uh, uh, peer, uh, number 18 gets hashed
to group #1, and so on and so forth. Every peer belongs
to exactly one group, which is obtained,
uh, in a consistent way by hashing
and then taking modulo k. Now what are the neighbors
that each peer maintains? Well, the peer knows about all the other peers
in its own affinity group, so 160 would know
about all the other peers in its own affinity group,
such as 15. In addition, uh, 160
would know about, uh, th-uh, one contact member
in each of the other, k-1 affinity groups. So, since there are n
affinity groups... sorry, square root of n affinity groups and n peers, each affinity group contains, on average, square root of n peers, so that's the square root
of n local affinity group, uh, neighbors. And also, since k =
sqa-square root of n, um, each peer has
square root(n-1) contacts, in each of the other
affinity groups. That's a total
of 2*square root of n on average, uh, neighbors that each peer needs to maintain. You might think "Well, that's
much larger than log n," but we'll come
to that in a moment. Let's just put that
off for a while. Let's just go with it. Where is a file get stored? Unlike in Chord and Pastry, the files do not get stored at the nodes
in the affinity groups. Instead, they get stored
at whichever peer uploaded them just like Napster or Gnutella. Instead, what gets stored
in an affinity group is meta-information, so you decouple
the file replication location from the file querying. Uh, so, uh, the, um, uh, each file name is hashed to a group, so you take the file name
and hash it to a group. affinity group, say the file is PennyLane.mp3, it hashes to group k-1. All the peers in affinity
group k-1, uh, store, uh, PennyLane.mp3
along with information or a pointer
to whoever has the file. This would, for in-
for instance, be an IP address and port number pair. Again, you are replicating
this information completely within
the affinity group, so this might be
a very high overhead, but again, you're not
replicating the file itself; you're only replicating
meta-information about the file, which is very, very small, typically just a few bytes
or few tens of bytes. The affinity group- or none of the peers
in the system store the files themselves. So, how do you lookup
for a particular file? Suppose you want to look up
for PennyLane.mp3. Well the first thing
you do is you hash it and find its affinity group,
by taking modulo k. With that you get k-1. Say node 160 is the one that's, uh, trying to, uh,
find this particular file. Then it goes to its
contact for group k-1, in this case 167
is the group contact and it immediately fetches
the tuple for PennyLane.mp3 and it knows where
to locate the file. So this is essentially, in the best case it's just
a 1 round-trip-time, uh, lookup cost,
uh, for the file itself. However the contact may be down. Because of churn, 167
may not be there in the system, in which case 160 would ask one of its own
affinity group neighbors, if its contact in group k-1
was in fact alive. So, the lookup cost might go up
to 2 round-trip times, but not a whole lot more. And in fact, going back
to the previous one, the 160 to 167, uh, choice,
the choice of the contact, uh, need not be a random one. Among all the, uh, affinity
group members in, uh, k-1, 160 could select that
affinity group member that is the closest to it, in the underlying round-trip-time in the underlying internet, and that means that this hop could, in fact, be a very quick hop in the system. Essentially, what
the system Kelips is doing is that it is replicating
meta-information enough across the entire, uh, uh, uh, um, network so that
at a querying peer- any querying peer, you can obtain information
about any file from one of your neighboring, very nearby peers, uh, nearby
in the internet round-trip, uh, time, distance space. So the lookup cost is, uh, in the best case
it's one hop, and even when you have failures
it's just a few hops. Essentially, it's
O(1) lookup cost. Now the memory cost,
we return to the memory cost, returning- the memory cost
is O(square root(. You maintain square root( uh, neighbors inside
your affinity group and square root(contacts. You may also need to maintain, uh O(square root(information uh, meta-information for files that are inserted, um, uh, and, uh, and mapped
to your affinity group. However, square root( is fairly small. Uh, if you do
the calculation numbers, uh, just for
the membership information, uh, for 100,000 nodes in your system, square root(, uh, neighbors, uh,
both in affinity group and across affinity
group contacts, turns out to be just under
2 megabytes for 100K nodes, and also including 10 million files stored in the system. This is much smaller than, the amount of memory
that's available on most Component Off The Shelf, or COTS machines today, uh, the workstations
and laptops that are running, uh, these peer-to-peer systems. Even if I increase, uh, this by a, uh, order of magnitude, a couple of orders of magnitude, it still would fit
within a few gigabytes of RAM, uh, in, um, most
of these machines. Essentially, this means that, all of this information
about neighbors, uh, as well as the
meta-information about files can be maintained
completely in memory and, uh, therefore the lookups can be, um, uh, fairly fast. How do you update these
neighbors that you have? Well, um, you- uh, you would
see, uh, gossip-based, uh, protocols, uh, elsewhere
in this particular, uh, course, and gossip-based membership is the technique that is used, uh, here to update
these membership lists. It's used both within
the affinity group and also across
the affinity groups. Therefore, when a member fails it's uh, the time to disseminate
information about it to the affi-to the entire system
is O(log(N)). However, even if information
is out of date, uh, Kelips, uh, this system works just fine because it has other ways
to find information. Chord and Pastry have, uh,
a shortcoming, which is that because they use roots
to route a message, if any one
of those intermediate, uh, uh, uh, nodes has failed, you still need to find, you still need
to continue using that. You can't really backtrack. Uh, uh, you still need to find maybe, another successor if your next hop successor
has failed. In Kelips you have many,
many different choices. If your direct contact, for the destination affinity group is not alive, you ask one of your own
affinity group members. If that doesn't have,
uh, an alive, uh, contact, you ask another
affinity group member. Maybe you ask one of your
contacts in the oth-another, in another affinity group for its contact
in the k-1's affinity group. You have a variety of different
things that you can do, and the querying node has
a lot of flexibility on it because the, uh,
the depth of the search, uh, uh, space here is short
because it's just a few hops. The querying node
gets back a response or a fail response
fairly quickly, and it can decide what
to do and how to, um, uh, uh, try another path to get to the destination affinity group. Also, because all you're
trying to do is hit one, uhh, target, in the target affinity group k-1, not just a specific one,
like 167, you're trying to hit any one. If you hit 76 you're fine, 76 would have information
about the file because that meta-information
is replicated across the entire affinity group. If you hit 18,
that will be fine too, so any, uh, member of the k-1 affinity group would be okay, uh, to locate information
about this file PennyLane.mp3. Um, in addition,
the information about these, uh, files may get very large, so you don't want
to keep them around forever. The way Kelips de-deals
with this is that it times out and deletes the information about files. So, if you have a file
that is stored in the system, you need to periodically
send out heartbeats to keep that information,
uh, a fresh. So this heartbeating is very
similar to the gossip style, uh, heartbeating that is used for the membership, uh, and, uh, if you don't heartbeat a file, if you don't refresh
the file periodically, then meta-information about it, uh, will slowly disappear from the system
and will go away, uh, from the system,
uh, forever. The advantage
of this is, of course, uh, that, uh, you never need
to delete files to simply, you simply stop sending heartbeats for that file, and meta-information
from that file will disappear, uh, quickly, uh, over time across all the nodes
in the system. So there is a range of tradeoffs between Chord, Pastry,
and Kelips. The range, uh, uh,
involves memory, lookup cost,
and background bandwidth. So Kelips uses, uh, slightly
more memory than Chord or Pastry and slightly more
background bandwidth, to keep neighbors a fresh, but it has a much shorter
lookup cost, which is O(1). So while Chord or Pastry have
O(log(N)) for all, uh, for both memory and lookup, Kelips has, um,
O(square root(N)) for memory and O(1) for lookup cost. Uh, and so you have a tradeoff, and this gives you a good, uh, range of choices to choose from. So wrapping up our discussion
on P2P systems, we have studied both
widely-deployed P2P systems, uh, such as Napster
and Gnutella, which were two of the first popular peer-to-peer systems; uh, Fasttrack,
which is an underlying, uh, which is a proprietary, uh, peer-to-peer system underlying many, popular peer-to-peer systems such as Kazaa, Kazaalite and Grokster, some of which
have been shut down, uh, due to court cases since; and also we
have seen BitTorrent. We have also studied, peer-to-peer systems that
were developed in academia, and the advantage of this, of these systems is that they have provable properties. You can analyze their
lookup cost, their memory, their overhead,
their stabilization time, uh, and they, uh, they are trying to solve the problem of, uh, distributed hash tables, uh, which is a well defined, uh, problem that tries to make inserts, lookups and deletes, uh, very efficient. There we have discussed
three systems. Chord, which was developed by researchers from
MIT and Berkeley. Pastry, that was developed by researchers from Microsoft Research and Rice University. And, Kelips, that was developed by researchers from
Cornell University.

### 10 - Blue Waters Supercomputer

#### Transcript

[SOUND] [MUSIC] Well we're in the National Petascale
Computing Facility on the campus of the University of
Illinois. This is a facility that houses one of the
worlds most powerful computers. Not just for computation, but also for
data analysis. So it's unique in the sense of it's the
most intense data analysis system. As well as being one of the most highly parallel computers in the world
doing projects. For science and engineering and other types of scholarly work for the nation's
scientists. This is the twentieth super computer that
I've been involved with making work. I worked at Berkeley laboratory. I was the general manager of a, a system called NERSC, the National Energy Research
Scientific Computing Facility. And we had a number of supercomputers in,
in in NERSK. Before that, I worked at NASA/AMES.
Again making very large systems work. So when I heard of the Blue Waters project
I thought it was the best possible thing going on in
high-performance computing. And it was changing the way people were
thinking about these computers. It was converting from this idea, well we'll just worry about the peak
performance of the system and assume that I can make
use of all that, that power. Turns out that that's not the case, that
if you have to focus on what real work comes
out of the system rather than some theoretical
number And that was the entire philosophy of the Blue
Waters Project. To get real science work done at a scale
never before seen. Faster than anybody else could do it. And I thought that was great. Because that's really what motivates
people for, for helping do this.
What science impact is there. So I came and talked to some colleagues here, and eventually we worked out the
fact that I came from California, the Bay area, to
Illinois about five years ago, to make Blue Waters
work. And I've enjoyed it very much since then,
Illinois a great place. Well, we have about 60 projects that use
this system. And those projects are, come on to the system after stringent peer review by
different agency's. The largest amount of time is controlled
by the National Science Foundation. And they have about 35 research teams from
around the nation working on a variety of, a large variety of different areas.
So there are people that are doing astrophysics, how do how did the
universe form? How did galaxies form? What happens when galaxies collide? Another example is a recently announced
result, one of the first really ground breaking results
from the system. Because we've only been running it in
service now for about six months, and that result is how the AIDS virus infects a cell. And this is the first time such a high
resolution complex simulation has been done, and that was in the cover
of Nature at in May. Another example is climate studies, severe
weather in terms of what happens, what's going to happen
with our climate. But, at resolutions that have never been done before.
Resolutions where actually clouds form. [COUGH] At first principles rather then estimating how they form kilometer
resolutions. For the severe weather calculations they
are down to ten meters so that they can actually predict things like tornadoes
or gusts of wind in, in hurricanes. The system was used to run the biggest simulation ever of a
hurricane, Hurricane Sandy. And how that was different then other
different from other hurricanes, how the tracking was different, and why it
went the way it went. We are also doing a lot of chemistry
applications, material science, and some other things like how
does disease spread. Other biomedical applications as well. Well, it's the largest system that Cray
has ever built. It's about 50% larger than the next largest systems, which happens to be at
Oak Ridge National Lab in terms of size,
number of cabinets, the scale of all the
components. It is a system that has tremendous
processing power. We term that power in terms of sustained
performance, the time it takes to solve problems. And our mission here is to shrink the time
it takes to solve problems by a variety of science and engineering teams into
something that used to take years or decades in two months, or
even, sometimes, weeks. So these are problems that cannot be done
elsewhere. They're bigger than has ever been done before. They're more complex than has been done
before. So that's our job, that's why this system
is here at the university, serving the nation as a
national resource. It also has more memory than any other
system I know of in the world 1.7 petabytes of memory that all can be
accessed simultaneously [COUGH] by any of this,
the, the nodes. It has, the most intense data system not only
because of the size of the data system but also because
of the bandwidth. The amount of data that can move back and
forth from the parts of the, the system, the compute nodes, to
online disk, and then the online storage. So it has almost a half of an exabyte of
storage capacity in the system as well. And surrounding all that is one of the most highly
connected systems in the world with 100s of gigabits of networking bandwidths
coming from or leaving this facility, going to places in Chicago, and then being
connected throughout the entire world. So what we have here is the arrogation of
many, many components together that are designed all
to operate for single programs. So but they're really made of the same
components that are in your, your cell phones, or your
laptop computers. As a matter of fact it's almost a fractal
type relationship. Because while in your laptop computer you
have a processor that may have two or four cores in it.
We have processors, 288 racks of processors, that we use as a
computational unit. They have about 800,000 cores. That all operate simultaneously on the
same applications. We have the interconnects that go between
all those processors, so they all can communicate
with each other. They all can coordinate the work. And they're put together then with
linkages to our hard disk storage system, our rotating disk storage system.
That's about 36 petabytes of storage, as opposed to one or two terabytes that you
might have in your local machines. And then we have more storage that's near
by. It would be the equivelant of you plugging
in a USB drive as a secondary drive. We call that Near Line Storage, and that's about 500 petabytes, almost half an
exabyte of capacity. All connected together with a network, the
same as you do on your cell phone, or your other appliances, and to do that, you also need things like power supplies, like
cooling. So if you think of the chip in your, your
local computer it has a heat sync on it, you
have a fan. Well, we have a tremendous amount of
infrastructure to cool the heat coming off of this machine because it
produces it loses a lot of energy to do all these calculations as
fast as it does. We also have a tremendous infrastructure
for the power that comes into the building and then is distributed, very
efficiently, to all the devices here. So in one way it is just a much, much
bigger, combination of the equipment that you would have, but you have to be able to program it so it all operates
simultaneously on a single application. Which means that there's been a lot of
communication that goes on between the cores, between the processors,
in order to do these simulations. So what we have is very, very tightly coupled communication across hundreds of
thousands of cores. And that's how the programs are written on this system with some specialized
communication protocols. And this all happens very, very quickly. So that we can make progress and be very
efficient.

## Quizzes and assignments

### Part 1 Quiz 3

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
