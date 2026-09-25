# Week 02 - Week 2 Introduction to Clouds, MapReduce

## 01 - Introduction to Cloud Computing Concepts, Part 1

Slides: C3_intro.C3Part1_CSRAfinal.pdf

### Transcript

Hello everyone, I want to thank you
for, uh, joining me on this, uh, journey through
Cloud Computing Concepts. This is the first part of the Cloud Computing
Concepts course, which is a two part course. Uh, this course here is about the internals
of cloud computing. This means that
we'll go underneath the hood and look at the distributed systems concepts, and the distributed algorithms, and the distributed techniques, that underlie today's
cloud computing technologies. This course is not about
how to write cloud systems or cloud applications. There is a separate course, uh, that's coming up,
called Cloud Applications. Uh, and, uh, this course
is not about networking either, in the cloud. There's a separate course called Cloud Networking
that's coming up, uh, that's about networking inside the Cloud. Uh, both, uh, w-well all
of these courses, the Cloud Computing
Concepts course, this course, both parts, as well as,
the Cloud Applications course and the Cloud Networking course are part
of a Cloud Specialization, which is being offered,
uh, to students. What we'll discuss in this
cloud computing concepts course, uh, both part one
and part two is, uh, three things. Uh, concepts that underlie today's
cloud computing systems, especially,
distributed systems concepts. Uh, techniques, uh,
that are used, uh, fairly widely, in a variety of cloud computing
systems today. And we'll also, uh, while discussing concepts
and techniques, uh, look at, uh, some facets and some aspects
of industry systems including open source systems, uh, like Hadoop and NoSQL storage systems and many others. So the cloud competing
concepts course is really a mix
of distributed systems, uhh, er, with a mix
of distributed algorithms. And both of these combined
as applied, uh, to cloud computing systems
as they are today. So what we'll discuss
in this first part, the first five week, uh, part of the Cloud Computing Concepts course. Eh, first we'll have
an introduction to Clouds, what they are, why they are, the way they are. Uh, we'll look at Mapreduce
and Key-value stores, uh, two of the, uh, emerging, subareas of cloud computing. Then we look at some
of the precursors, previous generations
of cloud computing systems, like Peer-to-peer systems
and Grids, that, uh, are ancestors, parents of, uh,
today's cloud computing systems. Then we'll, uh,
go underneath the hood and start to look at
widely used algorithms, for Gossip, Membership,
Paxos for consensus, uh, and also
classical algorithms, including, Time and Ordering, Snapshots, and, uh, Multicast. Along the way, uh,
in some weeks, we'll have interviews
with leading managers and researchers from industry, as well as, academia, uh, and I hope these will be interesting to you, as well. The, um, uh, the course is structured so that you can learn as you move along, uh, so there are five homeworks, uh, spread throughout
the course, uh, uh, as well as,
a programming assignment. The programming assignment involves, uh,
writing code inside an emulator. In the first part of C3,
uh, course, uh, you will be writing, uh,
a membership protocol inside an emulator
that we will provide to you. We'll provide you the template, the C++ template
and you can write it. and the one final exam. Well, cloud computing is
an exciting area to be studying, to be working in. And, uh, it is also a very dynamic
and continuously changing area. And that's what, uh, that's part of what
makes it exciting, as well. I'm really looking forward
to working with you and interacting with you as this course
move al-moves along. Uh, come join me as we start
our tour of the cloud computing

## 02 - Week 2 Introduction

### Transcript

[MUSIC] Thank you for joining me on this
journey into Cloud Computing Concepts. In this first week of the course we
are going to see first an introduction to clouds. What are clouds, why they evolved,
and the history of previous generation of distributed systems that
lead to the emergence of clouds today. So in this we'll see many
precursors to cloud computing. Next we'll see why this course is
really about distributed systems. Even though we are starting cloud
computing, the concepts underneath the cloud computing systems are in
fact distributed systems concepts. We'll see why clouds are in
fact distributed systems, and we'll also try to define
the term distributed systems. And we'll start to see examples of
distributed systems that are used in clouds today. The first example we'll see is Mapreduce
and the open source Apache Hadoop. We'll see what the paradigm is,
how it works. We'll see many examples of Mapreduce
being used, and we'll delve a little bit into how the scheduling works
inside Mapreduce and Hadoop. [MUSIC]

## 03 - 1.1. Why Clouds

Slides: C3_IntroClouds_A_CSRAfinal.pdf

### Transcript

Welcome. In this, uh, lecture series,
uh, we'll be looking at, uh, an introduction
to cloud computing, and we'll focus a little bit on, uh, the aspects
that distinguish, uh, cloud computing
from previous generations of, uh, distributed,
uh, systems. So, uh, first of all there's a lot of hype
around cloud computing. Uh, several, uh,
forecasting agencies which, uh, forecast mark-market trends for different, uh, markets have said that
cloud computing is large and it's only going to grow,
uh, perhaps exponentially. Gartner,
which is one of the most, uh, popular forecasting firms, said in 2009 that
cloud computing revenue would exceed
$150 billion by 2013, and that it would represent a significant fraction
of IT spending, uh, by 2015. IDC in 2009 said that, uh, in, um, the, uh,
next 5 years, uh, spending on IT cloud services would triple and would reach several
tens of billions of dollars. Forrester said
that cloud computing would go to $240 billion
as an industry by 2020. And it's not just in industry. Several governments have also started relying
on cloud computing, including fedbizopps.gov,
which was set up, uh, set up many, uh, years ago
by the federal, uh, government. So obviously there is
a lot of hype, uh, but then the question is what exactly is cloud computing? Well, there are many
cloud providers, as I'm sure, uh, many of you, uh, might have heard of. One of the most, uh,
popular cloud providers is AWS, or Amazon Web Services. There are also other, uh,
providers here, Microsoft Azure, uh,
Google Compute Engine, and there are a whole bunch
of other companies, including Rightscale,
Salesforce, EMC, Gigaspaces, 10gen, Datastax, Oracle,
VMWare, Yahoo, Cloudera, and hundreds of more companies that are too many
to, uh, mention here. So let's just focus on the, um,
uh, AWS, uh, portion. Uh, AWS offers
a variety of services; three of their most popular services are called EC2, S3 and EBS. EC2 is an elastic compute cloud, which provides
the computing services, S3 is a simple storage service, which provides you
the ability to store data so that you can access it
from anywhere in the world, and EBS is
Elastic Block Storage, which is essentially
volume storage that the EC2 instances can access while they are running. So there're two categories
of clouds, uh, today. Uh, they are either
public cloud or a private cloud. A private cloud is one
that is accessible only to, uh, special privileged
employees or personnel. For instance, if you're working in a company X, and the company X
has a data center or a cluster or a cloud which is accessible only to the employees
of the company, that's a private cloud;
it is not openly accessible. On the other hand, uh, a-a public cloud is one
that can be accessed by anyone, anywhere in the world,
as long as they have a credit card
and are willing to pay. Uh, private clouds, for
instance, also include, uh, the first category
also includes, uh, you buying a data center
or a cloud and running it yourself; that's your own
private cloud, obviously. So among public clouds, the ones that
are openly accessible, uh, um, as I mentioned, uh, there are a couple
that are, uh, fairly popular, Amazon AWS services,
uh, Google Compute Engine, and, uh, the, uh, Microsoft Azure tend to be popular. Uh, the AWS and Azure
share a lot of, uh, traits, so I'll just focus on AWS here. Uh, the S3
Simple Storage Service allows you to store
arbitrary data sets, and you pay per gigabyte month that you store; there are no upfront costs. The Elastic Compute Cloud,
uh, once again allows you to upload and run
arbitrary OS images. Essentially they are-
these are virtual machines, or VMs, and you pay
per CPU hours that you use. So if you use, say, 5 VMs for 1 hour, uh, each,
all at the same time, you'd be paying, uh,
for 5 CPU hours. And similarly,
the other services that, uh, AWS or Microsoft Azure
might offer, uh, are also, uh,
priced accordingly. Uh, there are a variants
of this of course. Google AppEngine
or Compute Engine offers the ability
to develop applications within, uh, their AppEngine, uh, and then you upload the data that would be imported
into their format, and you run your application. So for instance, you could use these
to host your own web services, you could use these, um, to host your, uh, data
so that it is served out, or you could host these
to run your own computation, uh, that you might want to run. So, cloud computing is attractive to customers because, uh, it allows them to save
both time as well as money. Uh, Eli Lilly, which is one
of the largest, uh, um, customers of AWS, reputedly, uh, for instance, uh, er, uh,
has been, uh, benefiting from the ability to bring up
new servers fairly quickly. Earlier they reported that
it used to take, uh, seven and a half weeks for them
to deploy a new server. This would, uh, involve,
uh, them, uh, um, uh, uh, setting the specs
for the server, then actually purchasing it, and then going through
the purchasing process, uh, the server comes in
and they set it up, uh, and install the necessary s- operating system and software, and all of this takes, uh,
took several weeks. Now they can rig up a new server
in, uh, around 3 minutes, and a 64-node Linux cluster
in 5 minutes, uh, while it was taking
months, uh, earlier. This of course saves them time; it also saves them money, because, uh, they
can save the costs that they might have otherwise had to pay the sysadmins. GlaxoSmithKline reported that, uh, they saved about 30%
by moving to the cloud. Uh, Jim Swartz, uh, from CI-
the CIO Sybase said that, uh, they've been saving
$2 million since 2006, and this is
only going to increase. And as a result,
it's not surprising that hundreds of startups
across Silicon Valley, uh, are leveraging, uh, some of the cloud providers,
who I mentioned, and a variety of other
cloud providers as well, rather than buying
their own machines. But once again, this brings us back to the question of what exactly is a cloud
for us, uh, technical folks, who want to understand
the deep, detailed, uh, aspects of cloud computing. We'll discuss that in,
uh, the next lecture. [electronic music]

## 04 - 1.2. What is a Cloud

Slides: C3_IntroClouds_B_CSRAfinal.pdf

### Transcript

So, we left over last time with the question of, what exactly is a Cloud? When you ask different people in industry or in academia, what a Cloud is, they'll give you very different answers. Some would say, Oh, it's just a cluster, a bunch of servers strung together by a network. Others might say, No, it's a supercomputer. It has more power than a simple cluster that you might run in your lab. Others might say, No, it stores a lot of data, so it's different from a supercomputer because it stores data rather than computes things. Others might say, Well, it can do a lot more things than all of these together. And some of them will, some of the folks you asked will say, Well, it's none of the above. It's a completely different beast. And others will say, It's all of the above. So, there is no single definition for a Cloud itself. It is often taken to mean not just compute and storage resources, but also include the network, and so on, and so forth. For the purposes of this course, however, I'm going to come up with a very simple definition, it's a working definition. It's not perfect. It's not meant to be perfect. It's meant to be good enough for us to learn more about the technologies that exist out there. So working definition says, that a Cloud consists of a lot of storage resources, so you can store gigabytes, terabytes, petabytes, maybe even more of data with compute cycles located nearby. Notice that this definition is not the reverse which is it doesn't say, you have compute cycles with data moving around. Essentially, there is so much data. It is a data intensive world that we live in, that you can't really move around the data all that easily. So, you need to bring the compute closer to the data rather than bring the data closer to where the computer is. And you see this theme coming back several times as we move along in the lecture and in the course. So, what is a Cloud? There are two kinds of clouds, a single-site cloud or a geo-distributed or geographically distributed cloud. A single-site cloud, known as a Datacenter often, consists of the following components, of course, it have been source of servers or compute nodes, these are grouped into racks, a rack as a unit of several servers which typically share the same power and often share a top of the rack switch. This top of the rack switches are often connected via a network topology. For instance, a tree like topology, a hierarchical topology, one of the most popular being just a two level tree where you have the top of the racks at the one level, and then you have the cores which is connecting all the top of the racks to each other. In addition to these nodes which are used for computing the servers, there are also backend nodes also in the racks, but those are predominantly used for storage. These might be nodes that have SSDs, or larger, or more hard disks on them. And then, there are user facing servers where the client requests come in or users consume a job if it is a batch processing system. And finally, there is software that is running at all of these servers as well as the routers. The software includes operating systems that includes a user level applications. It includes the actual IP protocol, and the switches, and the routers, and it also includes other routing protocols. So that's a single datacenter. Typically, such a datacenter is housed in a single building or a single warehouse in the case of some of these large companies. But a large company might also have multiple geographically distributed datacenters, multiple, and they might be connected to each other. So, these are multiple sites, each site being the datacenter and this is often called a geographically distributed or a geo-distributed cloud. Each site typically has the same structure and services as the other or at least as far as a software is concerned, it has the same software stack. But this is not a hard and fast rule, different sites might have different software stacks. So, let me illustrate a sample Cloud topology, a hierarchical topology which I was talking about in the previous slide. You have the servers and the leaves of the topology essentially. The servers are grouped into racks. There is a top of the rack switch which connects all the servers that are in that rack. And then, there are multiple such racks obviously here I'm just showing two racks, but there might be multiple such racks. And there is a core switch as well. Obviously, all of these, core switches and all the rack switches are limited in terms of bandwidth and in the number of ports that they have. So, if you have way many more servers than the cores which it can support, then you would need to grow out your topology to be more than just two levels as you see here. But then, that still begs the question, what is a cluster? Because this, after all looks like a cluster, right? So, what is it that is new about cloud computing that was not previously there in the clusters that we already know of?

## 05 - 1.3. Introduction to Clouds History

Slides: C3_IntroClouds_C_CSRAfinal.pdf

### Transcript

So I wanted to take a detour
and give a little bit of history of how cloud computing
came about, to be. Cloud computing is not
the first distributed, uh, system in the wild, uh,
that has existed. Uh, there have been many,
uh, over the decades. In fact, the first few computers
that were built, including the very famous,
uh, ENIAC, and other computers such
as the ORDVAC and the ILLIAC, which were built in the 1940s. These were the first computers that were built
in the architecture, or similar architecture
as we know of today. They were in fact datacenters; they occupied entire, uh, large halls and entire large labs. So those were
in the 40s and the 50s. Then in the 1960s and 70s
there was an era of industry called timesharing
and data processing industry. This was an industry that took
large amounts of data large for that, uh,
those periods of time, those might have been
kilobytes or megabytes and process them
and then gave the outputs. Typically this, uh, input was given in the form
of punchcards, as well as the outputs
were spewed out in the form of, uh, punchcards. Then in the 1980s personal computers
became popular, and the data processing industry and timesharing
companies declined, but PCs also made it easier
to build clusters or networks of workstations,
and this lead to the evolution of other eras of computing
such as grid computing, and then
very large-scale systems such as peer-to-peer systems
in the 1990s and the 2000s. And only now have we been
coming back sort of full circle to the timesharing
and data processing industry by building
very large-scale clusters that process
very large amounts of, uh, data. And so clouds and data centers,
a lot of us argue, are in fact coming back
full circle to the 1960s and 70s,
except with a lot more scale and very different workloads than in the 1960s and 70s. So, uh, this is a very, uh,
crowded slide, obviously, and there's lot of detail
on this slide. Uh, I don't mean to go through
all the elements on the slide. One of the things
I want to point out is that the data
processing industry, uh, which is often called a precursor to this
cloud computing industry, was a fairly large industry, so if you look at
the numbers here, in 1960 the data processing
industry was $70 million. By 1970 it had become
$3.15 billion . Given the rates of inflation, uh, and how much
the dollar has inflated, this was a fairly large industry at that point of time. The players then
were very different from the players that we have today, in cloud computing. Uh, Honeywell, IBM
and a whole bunch of companies, including Xerox
were big players. That era also resulted
in several machines which are the precursor
for the architecture of many of our, uh, workstations and even servers, uh, today. This included
the, uh, DEC PDP-10, as well as the IBM 370, uh, which were very popular,
uh, at that time. The networks
and workstations which, uh, are built from PCs
or servers, uh, included the Berkeley Network
or Workstations project and also server farms, uh, at several companies, including at, uh, IBM. Uh, grids became fairly
popular in the 1980s. These were a way to connect
several sites together the sites being
not very large-scale, not as large-scale as
the datacenters, but being large enough,
and grids were born out of the Grid Physics
Network Project, also known as
the GriPhyN, uh, Project. The peer-to-peer systems
that were popular in the 1990s and continue to be popular today included, original systems
of Napster and Gnutella, which we'll be seeing later on in the course, uh, as well as BitTorrent,
which is, uh, um, still popular today. And all of these,
I argue, culminated in
today's cloud computing. All of the wisdom, as well as, all of the
technical infrastructure and the software protocols
that have been developed have culminated
and enabled us to develop, uh, the cloud stack
as we know it, today. So there are several trends, uh, that are well-known
in computer science. Uh, the, uh, most popular trend
is that, uh, um, uh, the CPU compute capacity doubles once about every 18 months. This is often known
as Moore's Law. It is also, um, uh, uh, true that storage doubles
once about every 12 months and bandwidth doubles
once about every 9 months. When I say "doubles"
I essentially, uh, mean that per dollar
you can buy twice the amount of capacity. So Moore's Law, which says that,
uh, the CPU compute capacity or at least,
the original version said that, CPU compute capacity doubled, uh, once every 18 months said that CPU,
uh, frequency doubled once every 18-
every 18 months, but that has hit a power wall, so nowadays,
what you will find is that the CPU speeds
don't increase anymore. Instead, CPUs grow horizontally. In other words, uh,
you find, uh, the number of CPUs that come out on motherboards that you can buy, of the market, is doubling once about
every 18, uh, months or so. But there are
significant differences as a result of this
exponential growth, um, in what was used
in the 1980s and 90s and what is typical today. Bandwidth, for instance, in 1985 consisted of mostly
56K links nationwide. Today, uh, our, uh, um, backbone links in the internet are much faster than this. Uh, this capacity, uh, today's, uh, PCs, workstations that you buy, or even laptops, uh, sometimes have
hundreds of gigabytes, in some cases terabytes,
and this is much more storage than a supercomputer
back in the 1990s. Not only the hardware
and the software, but also the user's
expectations have changed. Uh, biologists, for instance,
in 1990 were running, uh, small single-molecule simulations, but today they run, uh,
fairly large-scale, uh, genome sequencing experiments. Um, companies that
sequence your genome might run very large-scale jobs on a, uh, cloud. The, uh, Large Hadron Collider,
um, which is run by CERN, uh, and a variety of other, um, uh, uh, physics,
uh, and astronomy, uh, applications and setups, uh,
produce a lot of data per year. All this data
needs to be stored somewhere. It needs to be processed, a-and it is this storing
and processing that allows them to make
large discoveries such as, uh,
the discovery of the or the confirmation
of the Higgs boson, the confirmation
of the gravitational field, and a variety of other advances that have all occurred because of the ability
to store and process large amounts of data from, uh, these, uh, particle colliders. So one of the prophecies
that was, uh, made in the 1960s, uh, by Fernando Corbató
and other designers of this operating system
called Multics is that eventually, uh, the, um, computing would be available
as a utility, just like power is
available as a utility. Today we plug in our, uh, devices into the wall
and we get power, or you open the tap
and you get water. Uh, similarly
they envisioned that computing would be available
by just plugging and, uh, playing your client,
uh, into maybe an ethernet jack. So many have, uh, today said that cloud computing has in fact realized this vision. Others have said that we haven't yet
realized this vision; we have come very close to it. This is something for you
to think about, uh, not just now but also throughout the course as we go along. As an aside,
this Multics operating system that I mentioned here was one
of the precursors of, uh, today's Unix operating system. So Multics, for fair- was a fairly heavy-weight
and monolithic operating system, and at some point of time, uh,
a bunch of scientists sat down and said "Let's pare it down
to its minimal, uh, basics and build a smaller,
faster operating system." That operating system
was the Unix, uh, operating system,
which is of course the precursor for many of the popular operating systems today, including, uh, the, uh,
versions of Linux such as Ubuntu, Red Hat,
and so on and so forth. [electronic music]

## 06 - 1.4. Introduction to Clouds What's New in Today's Clouds

Slides: C3_IntroClouds_D_CSRAfinal_v2.pdf

### Transcript

We now return to the question of what is it that is new in today's cloud infrastructures that distinguishes the clouds from previous generations of distributed computing systems. Essentially, there are four major characteristics that distinguish today's clouds and the problems that they raise that are different from previous generations of distributed computing systems and problems. They are: Massive-scale, On-Demand Access, Data-Intensive nature, and new Cloud Programming Paradigms. I'll say a little bit about each of these now but then we'll flush these four points out over this lecture as well as the next few lectures. Massive-scale essentially means that data centers are very large. They contain tens of thousands, sometimes hundreds of thousands of servers and you could run your computation across as many servers as you want and as many servers as your application will scale. On-Demand Access means that you don't sign a contract to purchase resources upfront, there is no upfront commitment. You only pay for what you use, and anyone can do so. You could use it, your family, your mom, your grandmom, anyone could use it. The third aspect is Data-Intensive nature. What used to be megabytes has become terabytes of data. What used to be petabytes has now become exabytes of data. This is data that needs to be stored and it needs to be processed and perhaps it needs to be served up in real time. The data might include daily logs of what's going on at certain web services. It might include forensics, it might include web data, it might include a whole lot of other data. When we talk of large data such as terabytes, petabytes, exabytes, humans have what is known as data numbness just. Like number numbness, we are often unable to tell how large datasets are. For instance, we consider Wikipedia to be a very large dataset but you can compress Wikipedia into just about 10 gigabytes. Wikipedia, by itself, does not count as Big Data or as Data-Intensive; but yet, there are datasets out there that are much, much larger and measured in petabytes and exabytes. Finally, there are new Cloud Programming Paradigms that have made it easier to process such large amounts of data. This includes MapReduce, it's open source implementation Hadoop, as well as storage engines, which allow us to store this data and query it fairly efficiently. This includes key value stores such as Cassandra and NoSQL stores such as MongoDB, which we'll see later on in the course. These new programming paradigms and storage paradigms are very accessible. They are easy to program and easy to configure and many of these systems are open source. Essentially, what I'm saying is that if someone gives you a problem and says, "Hey, here's a cloud computing problem." You may want to test whether or not that problem has, at least one of these four aspects that are listed on this slide. If it has at least one of these aspects, it's very likely to be a new cloud computing problem. If it is missing any or all of these four aspects, then it's possible that it's a problem that is already well-known and that has well-known solutions so it should give you pause. The first important aspect of cloud computing is Massive Scale. Facebook, for instance, today or at least in 2012, ran about 180,000 servers and it had exponentially growing the number of servers from 30,000 in 2009 to 60,000 in 2010 to its current number. Microsoft in 2008 was running 150,000 machines out of which 80,000 were running Bing, their search engine, and they were growing at that point of time at 10,000 machines per month. You can imagine where that size is today. Yahoo in 2009 was running 100,000 machines in the data centers. And these are split into clusters of 4,000 because of the way Hadoop runs. Amazon Web Services was running 40K machines in 2009 with about eight course per machine and, of course, this has grown by now. eBay and HP were also running a lot of machines across many, many data centers; and Google the number is not known but it is widely reputed that it is running one of the largest collections of machines anywhere in the world. What does a data center look like from inside? We'll talk a virtual walk through a data center. This is just to give you an idea of what a data center warehouse actually looks like. There are many links for you to see and I'm going to have the links up here on the slides themselves so that you can go and either read them up or I'll have a few YouTube videos that you can also look at. The main ruminative center is, of course, the servers. They don't look very different from the front or from the back. They're just regular machines except that these might be rack-mounted machines. Inside, they look just like your regular desktops or workstations or laptops. However, some of them might be highly secure. For instance, they might be behind walls if they're storing financial information that is highly sensitive. Where does the power come for these servers and the switches? Well, a lot of the power comes from offsite such as hydro electric power or coal power, which even today is the predominant source of power for data centers. Some data centers have solar panels, which provide for some small fraction of the data center's power usage. In many cases, for instance, solar panels might be used to power the lights inside the data center. However, there's a couple of important metrics that are used to measure the efficiency of the data centers in terms of water usage and power usage. These are known as Water Usage Efficiency or WUE and Power Usage Efficiency or PUE. The water usage efficiency is essentially the annual water usage divided by IT equipment energy and liter per kilowatt hour. A lower number here is good which means that you're using less water per energy that you're using. PUE is total facility power divided by IT equipment power, and then here, a lower number is good because, essentially, this means that you're using a larger percentage of your incoming power for powering your servers and your routers and switches. For instance, Google has one of the lowest PUEs in the world. It's about 1.11. You can never get to a PUE below one, obviously, because you can't use more than 100 percent of your power. Now, when you have power, you have servers, you have heat, and so you have to cool these servers so you might suck in air maybe from the top then you need to purify water and spray the water into the air and then there are motors per server bank that are spraying the air into the servers themselves to then cool the servers. This is just one of the different cooling infrastructures you may have. Other data centers may use completely different cooling infrastructures than the one that I've described on this slide. There's a couple of fun videos to watch as well including a Microsoft GFS Datacenter Tour, as well as a Timelapse of a Datacenter Construction of a Fortune 500 Firm. All these available on YouTube.

## 07 - 1.5. Introduction to Clouds New Aspects of Clouds

Slides: C3_IntroClouds_E_CSRAfinal.pdf

### Transcript

So let's continue discussing, uh, the, uh, new aspects
of clouds. We've distinguished them
from previous generations of distributed
computing systems. We discussed massive scale
in the last, uh, lecture. Today, we move onto
the second aspect, which is the on demand access, uh, and we'll discuss here
as part of this the aaS classification
that is popular industry. So on demand access
basically means that you pay for exactly what you use rather than paying
an upfront cost or buying something upfront. This is sort of like, um, uh, renting a cab versus
what used to be previously, uh, renting a car, where,
uh, you might have to, uh, pay some upfront cost
for using ba- to use servers that others own, or buying a-a-a car which essentially is analogous- analogous to, uh,
buying your own, uh, datacenter. Instead, today's, uh,
services allow you to, uh, pay a few cents
to a few dollars, uh, per CPU hour, and you can use
as many CPUs as you want, as your application needs. For instance,
this is what AWS, uh, EC2, as well as Microsoft Azure provide for you. Or you can pay a few cents
to a few dollars per gigabyte month
that you store. Once again, AWS and Azure
provide these services for you, and there's a variety
of other companies providing similar services
for you at competitive rates. Now in industry
there's often classification of the cloud services
that are provided, uh, based on, uh, the nature
of the services themselves. These are often classified as, um, an aaS classification,
or "as a Service." So HaaS stands for
"hardware as a service." Essentially this means that you get access to
the bare bones hardware machines and you can do whatever you want with them. For instance, if you buy
your own cluster, your own private cloud, then, uh, you're running
a hardware as a service. Uh, but exposing hardware as a service
to other users, especially those that
you don't trust, may not be a good idea because of the security risks involved, uh, with giving, uh,
root access, uh, on your machines
to untrusted users. Infrastructure as a service
allows you to get, m, access, uh, to machines, uh, and,
uh, install your own, uh, operating systems and machines, but without having the security, uh, uh, holds
of the hardware as a service. Essentially, uh, this uses
virtualization so that, uh, you can spawn up
your own VMs and instances, and essentially AWS, uh, Microsoft Azure, uh, and a variety of other players, uh, offer services
that are infructure- infrastructure as a service, and this is one
of the most popular ways of using public clouds,
uh, today. Oftentimes this is said
to subsume, uh, HaS, uh. The, uh, knowledge
of these terms in industry is not uniform; there are conflicting definitions, but, uh, you might often hear that IaaS, uh, subsumes hardware as a service. There are two other
classifications. Platform as a service essentially is, uh, uh, a more of a tightly congealed or, um, um, o-or consolidated service form of IaaS. You don't get access to VMs
but you write your, uh, your, uh, your code, and it's tightly integrated
with the software platform. For instance, Google's AppEngine
allows you to write code in Python, Java or Go, and then it autoscales out your, uh, your, uh, application depending on
the incoming load, but you don't necessarily
think about VMs at, uh, that point in time, and you don't necessarily
need to think about, um, um, installing VMs
or provisioning VMs. A lot of the provisioning
is done for you. So it's easier,
but it's less flexible than, uh, than IaaS. Uh, Finally,
a software as a service, and essentially this gives you access
to software services when you need them,
and again you pay on demand. Uh, this includes Google docs, which I'm sure a lot
of you have used, and also Microsoft Office
on demand and many others, uh, that are out there. Uh, service
oriented architectures, which have been popular
for many decades, are often, uh, said to be subsumed under
the software as a service, so SaaS a-as a definition
is a little bit broader than what I have talked about
on this slide because it also includes
the SOA architectures. The third aspect
that is new in cloud, uh, clouds today
that distinguishes it from previous generations
of distributed systems is that we are dealing
with large amounts of data. And so previously, while, uh, there was computation intensive computing, for instance, uh,
the message passing interface, or MPI based computing, and high performance computing, where you would have a relatively
small amount of data but you'd run fairly intense computations on it, for instance, weather modeling is a computation intensive, uh, uh, computation,
uh, and this includes of course, uh, datacenters such as
NCSA Blue Waters, but data- but data intensive computing
is sort of the reverse, where you have large amounts
of data that are stored in datacenters, and you need to use
compute nodes that are nearby, just because you're dealing with ex- enormous amounts of data, petabytes or terabytes
or exabytes, um, and these computation runs n-, uh, nodes run computation services that
allow you to process the data. So the shift in
computation intensive, uh, computing toward
data intensive computing is a shift away from, uh, computation to the data. You need to pay
more attention to the data; you need to bring compute cycles closer to the data. And then when you look
at the servers themselves, CPU utilization,
which used to be the main metric for measuring,
uh, resource utilization in computation intensive,
uh, clouds, is no longer
the most important metric. Instead, uh, I/O is. This includes, um, uh,
disk I/O and also network I/O. Oftentimes in datacenters
you will find that the disk or the network I/O is
close to being maximized out, while in computation
intensive clouds, uh, the CPU utilization
is going to be fairly high. Once again, this is not
a hard and fast rule. After all, data centers
are just, uh, uh, very super large, uh, clusters, and so,
you can use them to run both computation intensive, uh, jobs
as well as data intensive jobs. Finally you have new pra-
cloud programing paradigms. This includes, uh, ways, uh, in which you can
process the data, which tend to be the bulk of new cloud programing paradigms, and also ways in which
you can store and query the data,
fairly quickly. Google include, uh, uh,
in-induced, uh, in-, um, uh, introduced MapReduce as well as other engines like Sawzall, uh, and these were open sourced, uh, uh, um, or rather open source versions
were written of these, uh, by, uh, Yahoo,
that became Hadoop. It was later open-
unopen sourced, and it is now an Apache,
uh, project. It is also then spun off
as a separate company by Yahoo, uh, as of, uh, this date. MapReduce itself was offered as an elastic MapReduce service
on Amazon, again, as you pay as you go,
uh, as you process your data, and MapReduce is useful for processing very large amounts
of data. For instance, uh, companies, uh, use it, uh, to, uh, uh, process a lot of the data
that is part of their core, uh, mission. So for instance, Google, of course Google is known
for its search engine, but in order to, uh, provide results to you in the search engine, th-they need to index the,
uh, data, the websites, that are crawled
by their crawlers. This indexing, uh, in 2006 was done by a chain of
24 MapReduce jobs. Uh, it, uh, processed about
50 petabytes per month and was using
200,000 MapReduce jobs. Yahoo similarly has
a web map application which is a chain
of 100 MapReduce jobs, uh, process- it processed
280 terabytes of data in 73 hours
when you use 2500 nodes. There's also
another engine there called Pig, uh, which is, uh, uh,
developed on top of Hadoop. Facebook uses Hadoop as well
as another engine called Hive, developed on top of, uh, Hadoop, uh, and once again
they were processing, uh, 55 terabytes per day, uh, and adding 2 terabytes per day
back in 2008. There's a variety
of other companies that use MapReduce to process, uh, their, um, their, uh, data sets
and the daily logs, including companies like
eHarmony.com, which actually use it
to do overnight runs where they match, uh,
dates with each other. Essentially,
that's a MapReduce job. So that's computation. There's also new
cloud programing paradigms where you can store
and query data fairly quickly. MySQL is an industry standard, but, uh, NoSQL
and Key Value Store systems, which are the new
cloud storage systems, are, uh, many orders
of magnitude faster, and you'll see why as we go along later on, in the course. [electronic music]

## 08 - 1.6. Introduction to Clouds Economics of Clouds

Slides: C3_IntroClouds_F_CSRAfinal.pdf

### Transcript

So today we come back to, uh,
one of the issues that we raised in the first lecture in the series which is, uh,
that Clouds are money savers. Are they really all the time? So once again,
just to remind you, uh, when you want to start up your own, uh, service or company you have a couple of options. Either you could use
an existing public Cloud, we have mentioned several
of these names, or you could, um, buy and use
your own private Cloud. Uh, there is a difference
between these, essentially when you use
a public Cloud you're paying, uh,
for CPU hours you use, gigabytes months that you
store but you're not paying for, uh, power for cooling, for,
ah, management costs and so on and so forth. You would be paying those if
you buy your own private Cloud. So the question we raise is,
uh, should you outsource or should you
own your own Cloud? So in order to do this essentially we have to do
a cost calculation so let's do a sample cost
calculation for a sample uh, medium-scale data center that, uh, we bought recently
at Illinois a few years ago, but at least that means that we have the
hardware numbers for it. Uh, this data center was called the Cloud Computing Test Bed
or the CCT. It had a 128 servers,
housed 24 total cores, with 8 cores per server and a little over
500 terabytes of data. Let's assume
that the new company that you are going to run requires exactly
that much amount of, uh, CPU and storage resources, okay? So that's the typical
storage resources that you'd need
to run all the time. So if you outsource and we use
AWS costs here from 2009, uh, then, uh, to store,
uh, uh, 524 terabytes using 12 cents
per gigabyte month, the cost from 2009, um, uh, and we use, uh, the EC2 costs of 10 cents per CPU hour, the storage costs comes
to be about, uh, $62,000. If you add the storage
and CPU costs it comes out
to be about $136,000. So that's the grand total per
month that you'd be paying to AWS in order to run a service
of, uh, this given size. On the other hand if you own,
buy your own private Cloud, uh, then we can take the numbers
from the invoice, uh, the storage total cost was
$349, uh, thousand. And since your service is only
going to run for M months, M is a variable here,
the per month cost is, uh, $349K divided by M. The total cost is $1555K
divided by M that's the total cost here, uh, plus you need to also be paying
for, uh, uh, sysadmin, uh, and this uses an industry
rule of thumb, which says that for a small sca- for a medium scale data center
with a 100 s- with a few hundreds of servers you need one sysadmin
per 100 nodes. And since it's
about 128 servers, uh, we just one sysadmin and use, uh, the, um, uh,
the, uh, monthly rate, uh, that is required for
just, uh, the CCT services. The-the quote out here $1555K also includes, uh, the numbers for, uh, the power
and the network so we-what we did
is we used the invoice number, which of course I can't put out,
uh, uh, in public but I used the invoice numbers along with, uh, the, um, uh, uh, uh, industry rule of thumb which says that if you pay
45 cents for hardware you need to pay 40 cents for power and 15 cents for network amortized over-out
over three years of, uh, lifetime
of the hardware, so using
that we get these numbers. So essentially now it becomes
a comparison of costs right? So, uh, the breakdown analysis
essentially says that it is more preferable
to own rather than outsource if the cost of owning is less than the cost of outsourcing on a per monthly basis. So for storage this says
that it is $39K divided by M less than $62K. And you can use this
to solve for M and it turns out to be M
greater than 5.55 months. Essentially this means
that if you loo- if you focus only on storage, if your service is going
to be running for fewer than 5.55 months then you want to be outsourcing
and using a public Cloud. If it's going
to be running for longer then you want to be using, uh, un, uh, perhaps your
own private Cloud because it's
more cost effective. Overall the calculation says that the cost of, um,
owning is less than the cost of, uh, outsourcing
and that is, uh, true if you solve for M here, you find that M is greater than
12 months, uh, for the overall. Again this means that
if you think your service is going to last
for more than a year, then it's, uh, more, uh, cost effective for you to buy your own private, uh,
data center, but if it's, uh,
less than 12 months then, uh, essentially you may want to outsource and use a public Cloud. This explains
why startup companies, which are not really sure
how long they want to last and, uh, also not sure
of how much competition and, uh, storage
resources they are going to use prefer to outsource
and use public Clouds in their first few months and even their first few years. And later on when the, uh, when
it congeals they might move to buying
their own private Cloud, on the other hand they might not because they've already built
an infrastructure on a well known public Cloud
and it works and, uh, customers and, uh, users
are already going there so they may not want
to change it. Uh, so AW- so, uh, you know, um, uh, companies like AWS and Microsoft, NetZero and, uh, Google Computing
engineered these services, uh, they essentially, uh, are
able to, uh, benefit from you building the stack on those,
uh, software infrastructures and then sticking with them. Also these, uh, Cloud providers
benefit a lot, uh, from storage, as you noticed, uh, the break
even point for storage is much smaller
than the break even point for, uh, for, uh, for the overall, uh, cost and this means
that, um, the, uh, storage is benefiting the Cloud
providers the most but essentially
you're storing data there and it is just sitting there
even though it may not be used you'd be in the you-you'd be paying per gigabyte month. So I want to wrap up
our discussion of the introduction
to the Cloud Computing. Cloud, um, Computing is not, um, has not, uh, been bought
out of the blue it is, uh, a culmination
of many previous generations of distributed systems and it builds on the technical knowledge as well the wisdom of these previous generations. Uh...it is a coming back to full
circle of the timesharing and data processing industry that existed
in the 1960s and 70s except with more scale,
different kinds of workloads and many, many more
users and customers. When someone gives you a problem
that is, uh, that they say is a Cloud Computing problem,
essentially we check whether the problem has
one or more of these traits; large scale, on-demand access, data intensive nature or involved
new programming paradigms. If it does not have
any of these, ah, ah, aspects then it may not be a new problem it may be
an already solved problem with well known solutions. If it has one of these aspects, uh, at least one
of these aspects then it may be a new problem and, um, uh, perhaps
there is a new solution or the- perhaps you can build
a new solution to it. So it's important for us to, um,
check Cloud Computing problems against these,
uh, four criteria.

## 09 - 2.1. A cloud IS a distributed system

Slides: C3_CloudsAreDS_A_CSRAfinal.pdf

### Transcript

[MUSIC] As you know, this course is
titled Cloud Computing Concepts. However a major portion of this
course is going to be spent discussing Distributed Systems Concepts. So what is the relation between clouds and
distributed systems? In this lecture and the next one, I argue that a cloud
is in fact a distributed system. So a cloud consists of hundreds
to thousands of machines on the data center side collected
in an integrated center. This we call as a server side. On the client side there might be
thousands to millions maybe even more machines which are accessing services
that are hosted by these servers. Maybe web pages, maybe websites,
maybe objects that are being stored, and maybe a variety of different services. So that's on the client side. The servers on the data center side
on the server side communicate amongst one another. So there is communication going on there. The clients, of course,
directly communicate with the servers. Each client can communicate with one or
more servers. For instance, every time you
access your Facebook profile, your client process,
whichever browser you're running your Facebook client on is going to
access multiple Facebook servers. Some for the photos, some for the profile,
some for the wall, and so on and so forth. The clients, of course,
may also communicate with each other. This is, of course, something
that happens in a cloud, as well. Now all these communications
that I described mean that a cloud is in
fact a distributed system. The fact that servers communicate
amongst one another means that, that is a distributed system consisting
of many different servers sending and receiving messages amongst one another. We call this as a cluster. A cluster is a collection of machines that are communicating with
one another over a network. The clients communicating with the servers
also make a distributed system. A very large scale distributed system. The clients communicating with each other,
for instance in a peer-to-peer system like Bertard also mean that is a very
large scale distributed system. So all these different aspects
that I've described for a cloud are also aspects
of a distributed system. In fact if you remember the last lecture
where we discussed the four distinguishing features of clouds, all these features are in fact features
of distributed systems as well. The fact that you have
many servers in a cloud, massive scale,
means that that is a distributed system. The fact that you can access multiple
servers any where, the on-demand nature of clouds, means that again that's a feature
of distributed systems as well. And that means that clouds are a special
class of distributed systems. The data and its nature. When you have lots of data you need to
cluster many different machines to store the data and
again that means a distributed system. And of course the programing paradigms
that exist today Hadoop/Mapreduce, NoSQL storage systems. All of these require clusters. All of these require many different
machines communicating with each other. So what I'm essentially saying is that
a cloud is a special kind of distributed system, and in fact a cloud is the latest
nickname for a distributed system. Previous nicknames that you have
already seen in a previous lecture have included peer-to-peer systems,
grids, clusters, and time-shared computers when we
saw the data processing industry. All of these are distributed systems, so
every one of these is a special kind or a special class of distributed systems,
and so is a cloud, cloud is no exception. And so nicknames come and
go and different kinds or classes of distributed systems come and
go but the core concepts that underlie
distributed systems stay the same. And these core concepts continue
to be used decade after decade. As an example Lamport timestamps which you
will study later on in this course were invented way back in the 1970s and 80s but
they still continue to be used today in almost all the cloud and distributed
systems that are implemented today. They're a very core concept and that's
why it's important for us to know it. And this is why this course is really
about these distributed systems concepts. We do not want to be restricted
only to the cloud but in fact want to study the core concepts
that underlie distributed systems. Not just the cloud
computing systems today. But the systems that have existed for
many decades in the past, and that are going to be around for
many decades in the future. For instance, a few years from now,
there may be a new nickname, a new generation of distributed systems. However, the core concepts will
likely remain the same, and they will continue to be
used in real systems. And that's why we focus and
study these core concepts in this course. So our next goal is going to be to try
to define the term distributed system. We'll do that in the next lecture. [MUSIC]

## 10 - 2.2. What is a distributed system

Slides: C3_CloudsAreDS_B_CSRAfinal.pdf

### Transcript

[MUSIC] In this lecture we're going to try to
define the term distributed system. It won't be a perfect definition, but
it will be a definition that will work for us in this course. Before we do that, let's take a step
back and define a different but related term that is the operating system. What is operating system? Well if you have used a machine, if you've
used a device, whether it's a tablet or a smart phone or whether it's a laptop or
a computer or a server, all these devices, each of these devices runs an operating
system also known as an OS. So if you've used a computer,
you have used an operating system. The operating system
runs on the device and it manages the different
components of the device. So let's, before we define
the term operating systems, let's name some examples
of operating systems. Here are some names, some OS's for
big devices included Linux, Mac OS X. Of course there are many
different versions of it. Windows, of course again there
are many different versions. And Unix and FreeBSD. And there are many, many examples of OS's for
large devices which I'm not listing here. For small devices like the handhelds and
the tablets, you have operating systems like Android from Google,
iOS from Apple, TinyOS, which runs on small sensor nodes which
you'll see later on in this course and, of course, many other small operating
systems that I'm not naming here. Now let's try to define
the term operating system. Before we jump to some
well-known definitions, let's try to summarize what we
know about operating systems. The operating system, essentially,
it provides a user interface to hardware. Your computer, any device, any computer,
consists of multiple devices. For instance, your computer
consists of a keyboard, a mouse, a monitor, a hard drive,
maybe multiple hard drives. And of course, the CPU,
and the memory, and many other peripherals
attached to the mother board. All of these hardware
pieces need to be managed. And these are managed by the software
known as the operating system. The operating system runs
a special piece of code for each of the devices
that is attached to it. This piece of code is
called a device driver. So essentially, as a user you do not need
to interact directly with these devices. It's very rare that as a user, we think
you know, I'm clicking the mouse, and now I need to worry about The message
being sent from the mouse to the CPU, all of that is taken care of by the OS. The OS also provides abstractions, for instance if you store your piece of code,
you're rarely thinking of hey how does this code get
stored as blocks on the disk. You're thinking of files,
you're thinking of directories or folders. When you run your code, you're thinking
of programs being initiated as processes. You're not thinking of where
does this run on the CPU? Where does this store memory? And so on and so forth. Those abstractions
are provided to you by the OS. So essentially the OS abstracts away
the hardware specific features and provides to users features that are
understandable and usable by the users. The operating system of course has to
manage these different resources that it is responsible for. Which processes run when on the CPU, which files get accessed when on
the hard drive and so on and so forth. And of course OS is also a means of
communication, whether it's sending and receiving email or
whether it's accessing the web. Or just communicating in
a distributed system. Here is the definition of OS from
the Free Online Dictionary of Computing, also known as FOLDOC. FOLDOC defines an OS as
the low-level software which handles the interface to peripheral hardware,
schedules tasks, allocates storage, and presents a default interface to the user
when no application program is running. And so for instance when you start up your
machine and there's nothing running on it, the OS is running on it, so
it's going to occupy the CPU. I won't go through the rest
of this definition. You can read it by either
pausing the video here, or going to the FOLDOC page online. But essentially this definition seems to
capture the characteristics that we said were true of operating systems
in the previous slide. Let's try to repeat the same exercise,
but for the term Distributed System. Let's name some examples
of distributed systems. Here are some examples, a single client
machine communicating with a server, for instance if you know NFS, if you have
used NFS, Networked File System. Single client may communicate
with a single server, that's a distributed system. A BitTorrent, which BitTorrent is a peer
to peer overlay which consists of many millions of clients
communicating with each other is again another example
of a distributed system. The Internet where you have many
servers and clients and routers and switches communicating with each other is
another example of a distributed system and the web where you have servers and
clients communicating amongst and with each other is an example
of a distributed system. Hadoop which we'll study
later in the course and data centers are all examples
of distributed systems. What are not examples
of distributed systems? Well, if you have a collection of humans,
say in a party, interacting with each other,
that's not a distributed system. At least, that's not the kind of
distributed system that we want to study in this course. I mean they might be interesting,
of course, in other courses but not in this course. A standalone machine not connected to the
network and with only one process running on it is, again, an example of something
that is not a distributed system. Birds out there interacting
with each other, that's again an example of something
that is not a distributed system. It's an interesting, I guess,
social phenomenon which biologists study. But not in a computer science course. So is there a good definition out there? Well FOLDOC, the Free Online Dictionary
of Computing was helpful to us for the OS definition, so let's go back to FOLDOC for
its definition of a distributed system. FOLDOC says that a distributed
system is a collection of automator, when it says automator it essentially it
means programs, whose distribution is transparent to the user so that
the system appears as one local machine. It's saying that essentially the collection of machines appears as one
machine rather than as multiple machines to the user who is using
the distributed system. This is in contrast to a network, where the user is aware that there
are several machines and their location, storage replication, load balancing and
functionality is not transparent. Distributed systems usually use some
kind of client-server organization. So this is the follow up definition for
distributed systems. I claim that this definition is wrong. It's just wrong. And in fact,
there are two mistakes in this definition. The first mistake is that the definition
says that in a distributed system, a collection of machines
appears as one local machine. But if this is true,
then the web is not a distributed system. For instance, on the web, it's often the case that a website A may
be up while a different website B is down. And at a different point of time website
B is up while website A is down. It's never the case that both A and
B are up and both A and B are down. So essentially these two web servers
do not appear as one local machine, yet the web is a distributed system. The second mistake in this definition
is the last sentence which says that distributed systems usually use some
kind of client-server organization. This is not always true. Peer to peer systems like BitTorrent, and
many other peer to peer systems before it, rely largely on the clients
communicating with each other. That's why they are called
peer to peer systems. They do not rely, on a server, except for
some very minor, functionalities. Essentially without the server, these systems would continue
functioning just as normally. So unfortunately the formula
definition doesn't work for us. Well, let's look at a couple
of definitions textbooks. Andrew Tanenbaum in his
textbook on distributed systems defines it as a collection
of independent computers that appear to the users of
the system as a single computer. Again, the same issue, the same error that
we saw in the previous slide as appears in this definition as well,
so it doesn't work for us. Michael Schroeder, another famous
distributed systems researcher defines a distributed system as several
computers doing something together. Thus, a distributed system has
three primary characteristics: multiple computers,
interconnections, and shared state. This definition is closer to what we want,
but it's missing some components. For instance, it doesn't talk about
servers or clients failing, and so that's a little bit worrisome here. So this definition doesn't work for
us either. So all these definitions are short and
looking inadequate to us mostly because we are interested in
the insides of a distributed system. We don't want to behave like
users of a distributed system, we want to go under the hood. We want to go Inside a distributed system,
and study what algorithms run there. How do you design a distributed system, how do you implement a distributed system,
how do you maintain, and of course what are the real
characteristics of distributed systems? As you have seen,
as I've mentioned before, there are some examples that when you see it you
know that it's not a distributed system. Humans or birds interacting with each other, a stand
alone machine not connected to a network. So we know it when we see it, and
this is captured very nicely in a quote by Justice Potter Stewart in a case in
1964 where he said that essentially, I know it when I see it, but
it may be hard to define it. So we're going to venture
forth the definition, and this is my working definition. This will work for
this version of the course. So a distributed system,
this definition says, is a distributed system is a collection
of entities, each of these entities being autonomous, programmable,
asynchronous and failure-prone, and these entities communicate through
an unreliable communication medium. So let me through this definition and
explain each of these objectives here. The entities are essentially processes. So each entity is a process
that is running on some device. Each entity is autonomous,
meaning it's standalone. If left to its own devices, pun intended,
if left to its own, it will run just fine. The entities are programmable. Of course, you have written code
that is running underneath and inside these processes,
so they are programmable. Notice that this is the term
that eliminates humans or birds interacting with each other
as being distributed systems. You can't really program human beings or
birds interacting with each other so that's why those are not
distributed systems. Asynchronous is very important, this
essentially means that each process or each entity runs according to its own
clock and these clocks are different entities are processes,
are not synchronized with each other. They are not always showing
the same time as each other and you will see a lot more and
more of this later on in the course. And finally is these
entities is failure prone, each entity may crash arbitrarily
at any point in time. At any color for instance,
at some point of time. And these entities are communicating
through an unreliable communication medium whereby they send and
receive messages through each other. However, these messages that are being
sent may be dropped completely, or they may be delayed for
inordinately long periods of time. Okay, so that's the definition that
I have for a distributed system. So, entity, when I say an entity, again,
I mean a process on a device, would be it a small pc or be it a pc or a laptop,
be it a tablet or a small sensor mode. And a communication medium may be
a wired network or a wireless network or some combination thereof. So, once again, the programmable objective eliminates
humans interacting with each other. The asynchronous objective distinguishes
distributed systems from parallel systems. Parallel systems include multiprocessor
systems and super computers. But essentially, very large numbers of
processors share the same motherboard. They communicate with each other
over a tightly coupled network, and they all have a synchronized clock. So all the processors are showing
the same clock at all points of time. A distributed system is
very different from that, a distributed system has asynchrony, which
means that clocks are unsynchronized. And that's why distributed systems
are harder to design algorithms for, and implement for. You might remember a process, which
you've seen in the orientation lecture. A process in all its gory detail,
with its code, its stack, its program counter, pointing to where
the code is currently executing, heap and registers and
a whole bunch of other things. Now process is an important
entity in a distributed system. In fact, a distributed system,
as we said, consists of many processes. In this example,
I have a three process P1, P2, P3 but there might be thousands of processes
involved in a distributed system. You have an unreliable communication
network involved underneath. In this course, we are not interested
in the insides of the network, just the fact that we are able to send and
receive messages via this network. So P1 might be able to send a message
m to P3, which then gets delivered at some point of time to P3,
and that receives the message. Okay, so this is essentially what we
see as a distributed system, multiple processes communicating by sending and
receiving messages from each other. When you think of distributed system for
working purposes for this course,
that's really all you need to think about, processes, sending and
receiving messages amongst one another. A caveat here, that's only a working
definition good for this course. You should feel free to come up with your
own definition for distributed systems. I would especially encourage you to try
this exercise after you have seen the many many examples of distributed systems
as you see them in this course. So try it at the end of this course. So, given this definition,
there are many interesting problems for distributed systems people like us,
you and me. Peer to peer systems, which we will
study many of, Cloud Infrastructures, which we'll see some of,
Cloud Storage systems, software systems, Key-value stores and NoSQL, we'll see some
of those, Cassandra and HBase as well. Cloud programming including MapReduce,
Storm and Pregel. Some of this you'll see soon. Coordination including consensus. Protocols like Paxos, leader elections,
snapshots and many others. And of course, managing these many clients
and servers that are interacting with each other via concurrency control techniques
and application control techniques. All these topics that I've listed on this
slide are relevant to this course and you will see them as we move along
in this course in both part one and part two of Cloud Computing Concepts. When we solve these problems, we need to
be aware of several features that are true in the distributed systems underneath and
we need to design for these features. Failures are no longer the exception but
rather a norm. As we've discussed before,
when the scale of your system grows, failures become very, very common. When you have thousands of machines and
terabytes of data, we need to be able to scale any algorithm
you design for a distributed system, this needs to be able to
scale very well to many, many machines at really
large amounts of data. Asynchrony again is a very important
challenge that you have to deal with when designing distributed algorithms. The fact that different processes
have unsynchronized clocks means that you will have a difference
between clocks, clock skew. You'll also have clocks moving apart from
each other that's known as clock drift. Again you'll see these
later on in the course. Of course concurrency is
something we have to deal with. Thousands of machines
accessing the same data, interacting with each other,
are bound to create to risk conditions and are bound to create conditions
where data might be inconsistent. And so we have to be careful to make sure
the data stays consistent even while machines are interacting with each
other and are accessing the same data. So over the next few weeks we will see
several core concepts of distributed systems. Next week you will see gossip and
membership. And then we'll see distributed
hash tables as well, which are an important building block for
peer to peer systems. And we'll alternate the core concepts with
the use of these core concepts in real systems, So when we see distributed hash tables we'll
also see they're in peer-to-peer systems. We also see how some of these building
blocks are used in key-value stores and NoSQL storage systems. For instance these NoSQL storage
systems use distributed hash tables, they use, gossip, they use membership. That's why you study concepts first and then we see how they're
used In real systems. [MUSIC]

## 11 - 3.1. MapReduce Paradigm

Slides: C3_Mapreduce_A_CSRAfinal.pdf

### Transcript

[MUSIC] Hello, in this lecture series,
you will get to see what MapReduce is, the paradigm, what it is. And we'll look a little bit
into the internal details of how MapReduce scheduling works as well. We'll also see a few examples of how
Different applications can use MapReduce, and you'll get to see
a little bit of code as well. So in this first lecture here,
we look at the oral paradigm and I'll try to introduce you
to a very basic level. So the terms map and
reduce which comprise the portmanteau term MapReduce are borrowed from
functional languages such as Lisp. For instance here's how you would
calculate the sum of squares. Suppose we have in teacher say one,
two, three, four. And you want to calculate one square
plus two square plus three square plus four square. The map so first of all square
is a function which can be applied on any one of these integers,
one or two or three or four And at least to
the square of the corresponding digits. So square of 1 is 1, square of 2 is 4,
square of 3 is 9, and so on. So square takes its input 1 in teacher and
spews output 1 in teacher. Map essentially is a metafunction which
applies the function squared to a list of inputs. In this case 1, 2, 3, and 4 are in a list. This is using Function
language terminology. And the output of map square forward
by the list is also a list where the ith element of the list is a square
of the ith element of the input list. So map here essentially is a meta
function which processes each record. When I say record,
I mean integer over here. Sequentially in this particular case, but more importantly it
processes it independently. So the square of 1 can be calculated
independently from the square of 3 and
neither of them follows from the other. So that's the first part. The second part is an addition function
which takes as input again a list of the corresponding squares of
the integers and just sums them up. Reduce here is again a metafunction which
applies plus to a group of records, in this case the records
are just integers. And adds them up and the output in
this particular case is just 30. So once again, as far as we are concerned,
reduce is a metafunction that processes a set of records or a group
of records This may be all the record this may be a subset of all the records and
in group it processes it in batches. So that's a very gentle
introduction to how map and reduce work in the small scale. However if you're given a sample
application word count which happens to be one of the more
popular applications and widely used applications of map reduce And
you're given a huge data set, say, all of the text in Wikipedia or all
of the text in all of Shakespeare's works. And you're asked to produce a count for
every word that appears in that data set. So for instance the word Richard, which
appears in many of Shakespeare's works. How many times does it
appear across the entire and across the entirety of all of
the text in Shakespeare's works? You want to produce a con for that. Similarly you want to produce a con for every single word that appears
in that entire data set. How do you do this? Especially when you're dealing
with large amounts of data? The large amounts of words
the large numbers of words and the large amounts of Text that might
be contained in Shakespeare's works. Well that's where our MapReduce
paradigm comes into place. So the map as a task or as an entity processes individual records,
in this case the records are just words, each record is a word,
to generate intermediate key/value pairs. Okay, so here I have simpler file that
consist of four records or four words. Welcome everyone, hello everyone. And when MAP processes this, it produces the each of
the records one key value pair. So for instance the record Welcome
it produces a key value per Welcome comma one. This essentially means that the word
Welcome was encountered once. That's a key/value pair. Similarly, Everyone, the first Everyone,
generates a key/value pair of Everyone, 1. Hello generates Hello, 1. And everyone again, the second
occurrence indicates everyone comma one. This everyone comma one, the second one, is independent of the generation
of the first everyone comma one. So, once again, these records can be processed
completely independently of each other. In this particular case I
just have one Map Task, so it runs through these
records sequentially. But you can paralyze this
process fairly easily, especially when you have a large data set. You can parallelly process individual
records to generate intermediate key/value pairs and the output is going to be
the same as if you had just one map task. In this example, I have two map tasks. The blue one in the top processes
the first line of input, and produces two key value pairs for
each of the two records in its input. And the bottom green map task produces,
again, two key/value pairs for the two records that are in this input. So once again, output of this is
the same as that in the previous slide. If you have a very large dataset,
you can split up your input dataset. You can shard your input dataset or
split it up And have map tasks assigned to each shot or
each split and the corresponding output will be
the same as if you had one map task. And so you process a large number of
records by using multiple map tasks, and You can scale up the amount of
map tasks with the amount of data. In this particular case I've just shown, each map task's been assigned
just a couple of words. But of course, map tasks are assigned
much larger chunks of data, typically in several megabytes as you'll
see later on this lecture series. because in this particular case,
I have many map tasks processing a fairly large file, and producing output. And output is indistinguishable
from when we had just one map task. Why do we have parallel map tasks? Well, it helps speed up the process. So in the ideal case,
if you double the number of map tasks, the time to complete all the map tasks
will Go down by a factor of two. So you'll process your
input twice as fast. So that's the first step of word count,
but we still don't have a word count for each word. For instance, every one which appears
twice in this carpus still doesn't have a count two associated with it. That's where the reduce comes into play. So the reduce takes this input,
the output of the map Phase. So all the key value pairs that you
saw in our small example earlier are reproduced here. This is the output of the map phase, and that has given us input
to the reduce phase. The reduce processes and merges,
that's the important word here, all the intermediate key value pairs
associated on a per-key basis. So for instance, here it takes all the key
value pairs that have Everyone as the key. In this case,
there are two such key value pairs. And it sums up their values. In this case,
the value turns up to be two. Similarly, it does the same thing for all the key value pairs that
have Welcome as the key. In this case,
there's just one key value pair. And so that output is over here, Welcome
[INAUDIBLE] Similarly Hello comma 1, there's only one instance of it,
and that leads to Hello comma 1. And this is the final output
of the reduce phase, and this is the word count
that we were looking for. So the word Everyone that appears
twice is associated with a value of 2. That's over here. Well again,
how do you parallelize this reduce phase? The reduce phase is not Does not
process these records independently in other words the record everyone
comma one the second record here and the fourth record here need
to be processed together. Their values need to be summed up here. And so
this is not independent processing here. Instead what happens here is
the keys are being grouped. So you want all the key value
pairs with one given key. To appear at one reduce task, so
that their values can be merged together. So the way you do this is by
assigning keys to reducers. So you assign each key to one reduce,
you do this by partitioning the keys. So for instance, this example over here, the key everyone is assigned
to reduce task number one. And so all the key value pairs
that have key equals everyone will arrive at reduce task number 1,
which then will sum up the values for that given key and
produce the outboard Everyone comma 2. Similarly, the keys Welcome and Hello
are assigned to reduce task number 2, which receives those as inputs. For the key Hello, it just outputs Hello comma 1 because
that's the only key value pairs received. And for
the key Welcome it outputs Welcome coma 1. There are different ways of
partitioning keys across reduces. In this case the partitioning has assigned
everyone to reduce Task 1, and Hello and Welcome to reduce Task 2. One way of partitioning is
called hash partitioning. You take the key, you hash it by using
a consistent hash function, say, simple hash algorithm one one, or message
I've used five MD five, or just any other hash function, as long as it's the
same hash function applied to all keys. Then you take modular
the number of reduced servers, the number of servers that are assigned,
and that will give you the number of
reduced tasks, in this particular case. And than will give you the new server on
the reduced task number to which that reduces assign. Why do we use hashing? This leads to fail uniform load
balancing of keys across the reduced tasks in the system. Let's go get some code from Hadoop which
is the open source implementation if map produce. Map produce was of course implemented
by Google and they never. Open source the original implementation
but they wrote a paper on it and published it, and engineers from
Yahoo decided to write an open source implementation of MapReduce,
and that became Apache Hadoop. Apache Hadoop today is widely available
and widely used, as many of you know. A company called Hortonworks
has been spun off from Yahoo, which does a lot of the code
development for Hadoop. So here's what a map might
look like in Hadoop. You have a MapClass which
extends a well-known base and implements a well-known interface. It's a templatized interface for
those of you who are familiar with the Java language. And the main function here is the map. The map text inputs the key and
the value tells us an OutPut Collector. And in case you wanted
whole things into the user. Essentially what it does here is that
it takes the value which in this case is text. So the value might be one line
of text in the input file. And it tokenizes it into strings so here you have the line which is
consisting a collection of strings. Each string is a word. The StringTokenizer essentially
iterates through all the words. In this case they are tokens. And for each word, you output a key value pair which
is that word comma the value one. Okay, and here we have said
that one is the new IntWritable value over here and so that's output
as the intermediate key value pair. So for every word that You encounter in
the line, this map function takes us, produces output that were comma one
as intermediate key value pair. Now this line may not be a line, it may be, in fact be an entire
large block of text over here. And the map would work just fine So
what does a radius look like? Well, here you have the ReduceClass
again here, which has one reduced function and again, that has input
key which is Text over here. And values, because you may have multiple
values associated with a given key You have multiple values over here. This reduce function is called once for every key that is assigned
to that reduce task. So suppose that reduce task is assigned
ten keys, that reduce task is going to call this reduce function ten times, once
for each of the keys that is assigned to it, and the values, in that case, will
be all the values that it has received. From the intermediate key value pairs that
are associated with that particular key. So [INAUDIBLE] essentially, this call
of reduce will simply go through all the values and sum them up and produce as
output key-value pair where the key is the same as the input key and the value
is in fact the sum of the input values. And in fact,
this implementation is an implementation, a correct working implementation of
the work on example that we have seen. So this is,
as opposed to the previous slide, where we had shown the map function,
and the map function, for instance, might be called only
once by each map task, With all of the import given to that map
task as the input to that map function. Now, you also have some glue code such
as the driver which has a run function, specify the job name,
in this case it's mywordaccount. You say that your keys are all words
by setting your output key class. You also set the values are counts,
or integers, by setting the output value class. You set the mapper class and the reducer
class to the ones that we saw in the previous slides, and
then you set what the input path is, where you fetch the data from and
where do you write the data to. As you'll see soon in this lecture series,
essentially, Hadoop runs on top of a distributed file system and
that's where all the data is stored. The input path name and the output
path name are both names of files or directories in the underlying
distributive file system. And finally you tell the job to run. Not shown here is the partitioning
function which can also change in the system. If, for instance,
your data is not Easily hashable, or you want to do something like sort,
as you'll see soon, you may want to have a hand
tailored partitioning function, and you can change that,
too, in the Hadoop code. [MUSIC]

## 12 - 3.2. MapReduce Examples

Slides: C3_Mapreduce_B_CSRAfinal.pdf

### Transcript

In this lecture, uh, we're going
to see some examples of, uh, applications
that use MapReduce. We'll work with, uh, fairly simple examples, but these will, these examples will hopefully show you, uh, the simplicity of programming in MapReduce, and yet, at the same time, how
powerful the paradigm can be. So the first application
is a distributed grep. You have a large set of files with a large amount
of text in them, for instance, uh, these might
be the works of Shakespeare, or in a production cluster these might be, uh, the logs
of, uh, uh, applications that are running, and you want to grep for,
uh, particular words, say of characters
in Shakespeare's works, uh, or, uh,
for error messages, uh, in, uh, your, uh,
production cluster. So essentially,
you may have a pattern which might be a regular,
uh, expression pattern or just a-a word
or a series of words, and you want to output all the
lines that match that pattern. So here's what, uh,
the Map would look like; um, here's how
you would write the Map. The Map essentially would, uh,
look at each line of text and, uh, check
if that line of text matches the supplied pattern. It might use regular grep
for this, and if it does, then it emits that line
of text as the key, with the value being, say, one, it doesn't really matter. The Reduce in turn, uh, simply
copies the intermediate data to the output. It does not do any processing, because each line, uh, essentially, uh,
might be unique, and you don't want to really do any merging of lines
in this case. And the output of, uh, this
particular MapReduce uh, uh, implementation is essentially
the set of lines that match your pattern. The advantage of doing
distributed grep here is that since you have
a very large data set, you could have multiple Map tasks and multiple Reduce tasks which speed up the processing
of your, uh, distributed grep, instead of doing a lot
of the grep on one machine, which might
be very, very slow, uh, because you have to sequentially process all the data, and also you may need
to transfer the data to that single machine. With MapReduce you could run
your, uh, application MapReduce distributed grep application
even though your data is distributed out over
multiple servers. The next application is
a reverse web-link graph. So you have a graph, uh, which is, say, a portion
of the web graph, where you have, uh,
edges (a, b) where a is a webpage
and b is a webpage, and a has a link
that points to b. This is represented, uh,
in the input as tuples (a, b), and that's what your input consists of. It is just pairs
of URLs, uh, (a, b) where ais a URL and b is a URL where the webpage at URL a
points to the webpage at URL b. The output you want
is the reverse. You want for each page, uh, all the list-the list of all
the pages that point to it, okay, so you want to find out
all the pages that point to, say, your homepage. So here's what the Map does. The Map processes the web log, and for each input pair
(source, target), (a, b) that it receives,
it just reverses it. It makes the target as the key
and the source as the value. Why does it do this? Well it does this so that
in the Reduce phase, all of, uh, the key/value pairs that share this target as the key will end up
at the same Reduce task, and that Reduce task in turn can simply list
the corresponding sources. It doesn't need to add them, because you can't
really add URLs. Uh, it just lists them,
makes a list out of the sources, and outputs that
as the key/value pair, or the final key/value pair. So this, ah, is essentially
the output where for each target and key/value pair the
corresponding value is the list of all the URLs that, um,
have pointed to it. Now you could take this a step
further where, uh, instead of, um, uh, listing, you could simply
add up the number of URLs. Okay, in this case, um,
you would output, uh, the number of pages that, uh, point to the target. In that case, you could also
optimize the map, uh, so that the, the, uh,
output of it is (target, 1). So that kind of dovetails
into our next, where, uh, you have, uh,
our next application where you have
a, um, uh, a say a log, which is a, uh,
log of accessed URLs, say from a proxy server, and there you have, uh, one URL for, uh, for every webpage that was fetched
by any client or user inside, for instance, your company
or organization. And you want as output
for each URL the percentage of total accesses for that URL, okay, so you want to say,
for instance, CNN.com accounted
for 13.5% of all accesses, uh, from this particular company, and so on and so forth
for every URL. So here's how the Map and
the Reduce would work. The Map processes the web log. Remember, the web log
has a series of URLs, and for each URL
that it encounters, it outputs
the key/value pair (URL, 1). The Reducers essentially, uh,
do the same thing as we did for the WordCount where each URL is
assigned to exactly one Reducer, and, uh, for that URL it sums up
the, uh, values that it, uh, receives as, um, values associated with that key. So at this point
we have output from, uh,
the MapReduce function, where for each URL
you have a count of the number of times
that URL was accessed. Okay, this is essentially
the WordCount example, but this is not
what we're looking for. We're looking for a percentage
rather than a count. So what you do is you chain
another, uh, MapReduce right after this. So you have the Map phase that
leads to the Reduce phase, and then after the Reduce phase
you chain another Map phase and another Reduce phase
after that, which will do
the percentage part. So the Map receives-receives
as input the output
of the previous Reduce phase, which is
the (URL, URL_count) pairs, uh, and it outputs
(1, the value) as its output. Why does it do this? Well, you just wanna have
one key so that you have
exactly one Reducer in that second
MapReduce phase, and it simply takes, uh, all of these key value pairs
it has received, it extracts the URL count,
it sums them up. Once it has summed them up, it knows the total number
of URL counts, uh, that are there
across all the URLs, and it makes
wa-one more pass, uh, through this, uh, uh, data set, and it divides the URL count
by the overall count, then it is calculated
and then it emits (URL, URL_count/overall_count) for each URL that is
present in its inputs. So this second reducer, uh,
second-phase Reducer, there is only one of it, because, um, you want
to calculate the overall count, right? You can't calculate
the overall count if there are multiple Reducers, and essentially
the Reducers and the maps don't talk with each other, uh, in this particular case, and you won't have
exactly one Reducer. And the Reducer does two passes; one pass to calculate the overall count by summing up all
the URL counts, and the second pass
to calculate the percentages by dividing all the counts
by the overall count. The last example
is, uh, one of sorting, and you might think sorting might be fairly complicated, um, but in fact, uh,
the internal MapReduce, um, uh, technique, uh, internal MapReduce,
uh, engine, uh, the Hadoop engine as well, uh, does some more
of, uh, sorting already, and this helps us right sort very, very easily. Concretely, the output
of the Map task, remember the output
of each Map task is a set of,
uh, key/value pairs, this set of key/value pairs
is already sorted before it is sent out
to the Reduces. This sorting is typically
a quick sort implementation in the Apache Hadoop implementation. For instance, the keys might be
integers or they might be words, and these are sorted uh, uh, based on increasing order
of integers or lexicographically
using the words. The Reduce task,
a given Reduce task, also receives a-a lot of input for multiple key/value pairs. It also sorts all of this input
before it starts its processing. This sorting
is actually fairly important for, uh, the Reduce task, because, uh, then, uh,
the Reduce task can decide, uh, basically once you sort the
key/value pairs by key, uh, all the sorting here
is done by key, uh, once you sort them by key, uh, essentially what happens is that all the key/value pairs associated with a given key are present contiguously
in your sorted, uh, set, and so you can call, uh,
the Reduce function once for that entire batch
of, um, uh, inputs, Reduce inputs that share the same key. So, uh, in order to sort a fairly large data set
in MapReduce, um, the input receives a series
of key/value pairs, and for the output you want to, uh, output
the set of sorted values. The Map function, uh,
that we would write would take the key/value pairs and it would simply output
value comma whatever as the key/value pair. We don't really care what the value here is
for the output key/value pair. Essentially this is
the identity function; it does not do any processing. Similarly, the Reduce
also does no processing; it just outputs
the same key/value pair. You might wonder
"How does this work?" Well, it works because the Map
output is already sorted using Quicksort, and the Reduce output
is also sorted using Mergesort, and so the output of,
uh, the Reducers, as long as the Reducers
are also sorted with respect to each other and you assign the file names for each of the Reducer
outputs appropriately, uh, you will get output
that is also, uh, sorted, um, based on the values. The only concern here
is one of partitioning. You cannot use hash-based
partitioning over here. You want to make sure
that the Reducers themselves are also ordered
so that their output- corresponding output file names can be given increasing um, um, uh, file names, uh,
in increasing order, and they can be
collated appropriately. So, uh, you want to partition
keys across Reducers based on ranges. In other words, you want
to assign each Reducer a range of keys, say Reducer number one gets, uh,
uh, keys 0 through 1,000, uh, Reducer number two gets, uh, keys 1,001 through 2,000, and Reducer number three gets keys 2,001 to-through 3,000 and so on and so forth. So, um, this again goes
into the partitioning function. Ah, in addition, the, uh, values may be, uh,
non-uniformly distributed, so there might be many more keys in, uh, the range say
2,001 through 3,000, so you may want to assign more
Reducers from that range. Okay, and so you want
to-you may want to take the data distribution into account in order to assign, uh,
while assigning ranges, uh, to the keys, uh,
to the, uh, Reduce tasks.

## 13 - 3.3. MapReduce Scheduling

Slides: C3_Mapreduce_C_CSRAfinal.pdf

### Transcript

[MUSIC] In this lecture we will see how
internals of MapReduce work and we'll look at the workings
of the scheduler as well which is a new Hadoop scheduler. So, how do you program MapReduce? For the user, as far as user is concerned,
the user writes the map program, particularly a short map function or
method and also writes a reduce program
short reduce function or method. Then they start up their job. They specify the number of map tasks and
reduce tasks and they submit the job and they wait for the result. Essentially the user's job is very easy
because the user does not need to know much about Hadoop or
distributive programming beyond the number of map tasks or
reduce tasks that they need. Internally, and this is where things
become interesting for us students, for the paradigm, MapReduce paradigm and
the scheduler itself, it has to worry about parallelizing
the map, it has to worry about essentially in the stage, splitting up or sharing of
the data among the different map tasks. It has to transfer the data from
the map to the reduce in a sense it has to work through
the partitioning function here and make sure that the correct data is being
sent to the correct reduce function. There has to paralyze the reduce. In other words, there has to schedule
the reduce tasks themselves. And finally, a sort of on top of these three it has to
implement storage for the Map input, for the Map output, which is the same as the
Reduce input, and also the Reduce output. Also, one of the things we have seen so
far is the way that Map phase works and the way the Reduce phase works after it. Essentially, none of the Reduce tasks can
start before all the Map tasks are done. Why is this? Well this is because if there is
at least one map task running, it's possible that it generates
some key value pairs, while that key has already been processed
by the corresponding reduce, so you essentially you don't want
to start any of the reduces. Now this statement has been fudged,
it's not literally true, because in many of the cases you can
maintain, you can have some of the reduced tasks start earlier, this has actually
been implemented in MapReduce as well. But as far as understanding is concerned,
let's just go with the fact that none of the reduced tasks can start
before all the map tasks are done. This is called a bad year, because it's
essentially you have a bad year between the map phase and the reduced phase, the map phase needs to be completely done
before any of the reduce tasks can start. One of the ways in which this barriers not
really true is that the traffic that goes from the MapReduce, the map output and the
reduce input, which is called the shuffle traffic, can be started parallelly while
the map tasks are still continuing. Okay. So, once the shuffle phase, the shuffle phase can be
parallelized would the map phase and once a shuffle phase is done, then it can,
then the reduced task can start. So how do you solve these problems? Well, in the Cloud essentially
paralellizing the map is easy because remember each map task was independent
of the other map task, and so these map tasks can be assigned
essentially to any server. And you typically want to assign
the map tasks to servers where the data is close by so
that you incur low network overhead. But we'll talk about that later on. Then you also want to make
sure that all the map output records with the same key
are assigned to the same reduce. And that helps you to transfer
the data from the map to the reduce. In this case you use
a partitioning function, for instance as we've discussed earlier
the hash partitioning function may be used where each key is assigned to the earliest
task number which is obtained by hashing the key more than load
the number of reducers. The reducers go from zero to
the number of reducers minus one in id Finalizing the reduce is also easy
because each reduce task is essentially independent of the other. Each reduce task is assigned a set of
keys and these keys are disjoined across reducers, so
reducers do not overlap with each other. And in terms of number of keys,
on the input or the output, and so they can be run
independently of each other. And notice here that it makes it
easy to schedule these map tasks and these reduce tasks because there is no
communication between two map tasks, there's no communication in
between two of these tasks either, they are fully parallelized
with respect to each other. Finally, you need to implement storage. The map input in the beginning and there
is output right at the end of the reduced phase are both sorted in this
distributed file system. This distribute file system is running
typically on the same servers where the map tasks and
the reduce tasks are run. For instance, the Google version of Map
Reduce Runs uses the Google File System, also known as GFS, and Hadoop, the
Apache Hadoop open source implementation uses HDFS, known as
the Hadoop Distributed File System. Typically these five systems will
store multiple replicas of the same input data block. It replicates file blocks a multiple
times typically three times and there are three copies of each file block
located on three different servers. And so when a map task starts up
it needs to fetch the data block that is its input data block from one of
the servers that is storing it currently. It queries the online HDFS file system
to do this and this transfer is faster, obviously, if the server on which
that particular block is located, is in fact the same server on
which the map task is running. So, then we also have to discuss
where the map output is stored. Well the map output is not
stored in the distributed files. And instead the map output is stored to
the local disk at the server on which the map task is running. And the reduce input is read
from these remote disks. Okay, so it is read from
the multiple remote disks, one for each of the map tasks services. The reason why this intermediate
shuffle traffic between the map and the reduce uses the local file
system is you want it to be fast. This intermediate data
is really not needed. It's not really visible to
the external user it's only needed for the reduce phase to start its work. And so essentially you don't want
to incur the high overhead of the underlying distributed file
system which might be replicated which might try to put it
on some other servers. You don't want to incur this high
overhead, you want it to get as fast as possible to the reduce tasks so
that the job can finish quickly. Finally, when the reduce output is done, it is written to the distribute
file system back, so the output of the entire map reduce job is
available in the distributed file system. So let's look at a pictorial depiction of
what goes on in a MapReduce application. So you have the input data set
we just split up into blocks. In this case, I have 7 blocks. Which are stored in
the distributive file system. Again each of these blocks might
be stored at a different server, and each of these blocks might be
replicated at multiple servers. Then you have the map tasks, and in this
case each map task is assigned one block, so I have seven map tasks over here. The resource manager,
which runs a scheduler of MapReduce, and again, here I'm using Hadoop
terminology, is responsible for assigning these maps tasks to servers and
it's also responsible for assigning the reduce tasks,
which appear later on, to servers as well. So it might assign, for instance,
the first two map tasks to server A, the next three map tasks to server B,
and the last two map tasks to server C. And so these map tasks run on
the corresponding servers and they would fetch the corresponding
input and process them. Next the outputs of these map tasks are
sent to the corresponding reduced tasks. I have three reduced tasks
in this particular case. And each of the reduced tasks
might receive output from each of the mapped tasks. because here the map tasks might
have key value pairs with keys for each of the three reduced tasks. Again, as I mentioned
in the previous slide, this shuffle traffic over here is written
locally at these servers and fetched remotely from the corresponding reduce
tasks wherever they may be scheduled. So that scheduling, again, is done by the Resource Manager which
assigns each reduce task to one server. For instance Server A might have some
map tasks that are running on it, that are generating data,
output shuffle data, for the reduce task
that is assigned to it. That data doesn't go anywhere. It does not go on the network. It stays local to A. However, this third map task
might have some output, which needs to be sent to
this first reduce task. And that reduce task will need to go over
the network and be sent to server A. Finally when each of these
reduce tasks is done, their output is written into
the distributor file system. Typically these are written as separate
files into the distributor file system, and they might be named or numbered
based on the reduce task number so that they can be thereafter collated into
either one file or into a directory. So that's how the MapReduce
workflow works. Let's look a little bit into how
the scheduling itself works. I've mentioned one of the terms here,
resource manager, and this is one of the terms that
appears in the YARN scheduler. The YARN scheduler is a new
scheduler that is being used in the Apache Hadoop version two onwards. YARN stands for Yet
Another Resource Negotiator. The main entities of resources that
YARN leaves with anonymous containers. Container is essentially
some CPU plus some memory. So, each server consist of
a collection of containers. So for instance,
if a server has 4 cores and 4 gigabytes of RAM, in each container is
one core and 1 gigabyte of RAM, then that server has 4 containers and essentially it
can run four tasks one on each container. YARN has three main components. The resource manager, node managers,
and application masters. There is one global resource manager
which essentially runs the scheduler. There is one node manager
per server in the system. This is a Daemon that is responsible for
all the server specific management on that particular
server and also responsible for monitoring the failures of tasks that are running
on that particular machine themselves. Then there is the Per-application or Per
job Application Master which also runs in one of the servers and
this is responsible for negotiating containers with the
Resource Manager and the Node Managers. It's also responsible for communicating
with the Node Managers to find out if any of them has died, and so if the tasks
that are running off, the tasks of the job that are running on that particular
server need to be rescheduled as well. So, materially here's what happens, in this figure I have two servers
shown as Node A and Node B. Each of these servers is
running a Node Manager. There are two jobs,
shown as Job 1 and Job 2. Each of these has one application master,
Application Master 1, Application Master 2. A task belonging to the Application
2 has just finished here. I also have a resource
manager that is running. The capacity scheduler which is one
of the popular schedulers in Hadoop. So here what happens in this
timeline is that, the Application 1, rather it's Application Master 1
says to the resource manager, hey, I need a container, I need to run a test. Resource manager doesn't have empty
containers so it queues this up and subsequently the Node Manager B might say,
hey, one container here's completed
when this task is done. And at this point, the resource manager
can tell the Application Master 1, there's a container on node B
that you can run your task on and Application Master 1 that communicates
with node manager B to start that task. So this is typically the flow
of things that might happen in order to assign a new container. Now, this is somewhat, slightly part from
the truth, in truth when a job starts up it immediately tells the resource
manager all of its requirements so there might be multiple containers that
are outstanding, container requests that are outstanding in the resource manager,
also there might be multiple jobs or multiple applications that are requesting
containers at the same time. All those requests will be
outstanding in the resource manager. It will be queued typically
based on the order, some order of the jobs, by default
order is first in and first out for the jobs that have arrived in order
of arrival at the resource manager. Jobs that have arrived earlier
may be given resources earlier. [MUSIC]

## 14 - 3.4. MapReduce Fault-Tolerance

Slides: C3_Mapreduce_D_CSRAfinal.pdf

### Transcript

So in this last lecture on the MapReduce, uh, uh, lecture series we'll see how MapReduce deals with, uh, failures. Uh, failures, as you know,
are very common, and the norm
rather than the exception in, uh, cloud
computing clusters. The most common failure is a failure of the server itself, uh, and the server failure might
need to, uh, lead to multiple, uh, components of the Hadoop
YARN scheduler failing. Remember that the servers are
running the node manager, uh, they're running tasks,
they're running, uh, one of the servers is running the resource manager, and also the Application Master might be running, uh, on a server for each job. So, uh, in order to deal
with server failures, there are heartbeats. The node manager, each
per-server node manager sends heartbeats,
periodic heartbeats, to the central resource manager. If a server fails
and these heartbeats stop, the RM times are waiting for the next heartbeat
from that node manager, and it knows the node manager has failed. It lets all the affected
application masters know, and the AMs, uh, then have the responsibility
of uh, rescheduling their tasks. The, uh, um, node manager also
keeps track of each task running at, uh, its server, so if one of the tasks fails, for instance, uh, due to an auto memory exception, then, uh, the task, uh,
is marked as idle, and, uh, either the node manager could restart it, or it could inform, uh, the resource manager or
the application master, uh, that, uh, the task has failed. Finally, the application master also sends
heartbeats periodically to the resource manager. If, uh, the AM fails
and the RM would restart the AM, which then syncs up
with, uh, its running tasks, and this might get complicated, uh, depending on how many tasks are running, uh, at the AM. The RM itself might fail,
and there is no one, uh, detecting the failure
of the RM, uh, so far. However, one way
to deal with this is to maintain a secondary, uh, hard backup, uh, RM, which, uh,
takes over immediately a-after the RM failure. Now the heartbeat messages that
I've described so far are also useful to send, uh, actual container requests and other, uh, requests. So these are, uh,
the container requests that we saw
in the previous lecture of this MapReduce series are in fact always piggybacked on top of the heartbeat messages, um, and this avoids sending
extra messages, uh, in, uh, the underlying network. This might lead to a smaller, more delay, uh, in sending
the next request across, because heartbeat messages
are sent only periodically. Uh, however, uh,
this, uh, does avoid extra communication overhead. Now, other than, uh, failures,
we might also have some nodes that are slow in, uh,
the, um, uh, cluster, uh, just because they
might be having slower CPUs or, uh, or, uh, uh, or, memory, or because over time these nodes
have, um, uh, incurred, uh, more failures
and have more errors in their-in their, uh, memory banks than other servers. In any case, this is problem
in, uh, in MapReduce because the slowest machine slows down their entire job. Why is this? Well, remember that,
uh, the, um, uh, Map phase has a bad ear
on the end of it, which means that none
of the Reduce tasks can start until all the Map tasks
are done, and this means that the slowest Map jo-the slowest, uh, Map task will slow down
the entire Reduce task. Similarly, the
slowest Reduce task will cause the job completion
time to be delayed even more. Remember, the job is not
considered to be completed until all of its Reduce tasks
are done. Okay, once again, uh,
this slowness may be due to a disk, maybe due to, uh,
network bandwidth being bad near that server, or maybe
to a bad CPU or bad memory. The way, uh, this is tackled
is by keeping, uh, track of the progress of each task. This is essentially
the percentage of input that has already been processed by that task, and, uh, for tasks
that are slow, meaning they have
a very slow progress rate, uh, by replicating them. The way this works is
suppose I have three tasks which are currently-
which had been started all at the same time, um, uh, and these are tasks one, two, and three of the same job, and suppose, uh,
these tasks have completion, uh, progress rates
of 90%, 50% and 10%. Clearly the 10% task
is in trouble, has been making
the slowest progress. What happens here is what is
known as speculative execution. And the MapReduce scheduler, uh,
in this case the AM, uh, might spin up another replica
of the task, number three, which has only a 10%
progress rate, but on a different server than where Task three is running. In essence now you have two
copies of the same task running, and because these
are identical copies and have identical inputs, they will generate
identical outputs, and they are racing
with each other; whichever one finishes fastest will lead to the task
being marked as completed. So the second replica of the-
of that same task number three, which we started on
a different server, gets lucky and finishes fairly quickly, then, uh, the first
replica will be killed, uh, and the task will be marked
as having completed. This is known
as speculative execution. Uh, it's a somewhat
misleading term, uh, because, uh, you don't really
speculate anything. Instead you look at the progress rate and you say, "Well, you know, uh,
the progress rate is slow for this particular task, and so
I'm going to, uh, replicate it." Uh, so really it should be
called replicated execution, but the technical term
is speculative execution. The final thing is locality. Um, so a cloud, uh, typically
has a hierarchical topology. For instance, a cloud
might have multiple racks, and communication inside a rack
is typically much faster than across racks, which goes
across the core switch. Uh, the file system
that is underlying, h-uh, MapReduce or Hadoop,
which might be GFS or HDFS, typically stores three replicas of each of the chunks or blocks. For instance, the blocks
might be 64 megabytes in size. Uh, typically these are
stored on two different racks. There might be two stored
on one rack, two replicas of the block
stored on one rack, and one stored
on a different rack. These are stored
on two different racks so that if one of the racks fails, for instance, the top of the rack
switch goes down, then you at least have one
copy of the file around, uh, or-or the block around. So given this, uh, MapReduce or
Hadoop attempts to schedule a Map task on preferably
a machine or server that contains a replica
of the corresponding input data, so that, uh, the input
to that task, this is typically a Map task, uh, would, uh,
be, uh, uh, fetched without incurring
any network overhead. However, this
may not be possible because all the servers on which-all the three servers on which this Map input
is located might already have all their containers, um, uh, full, meaning they're
already running tasks. In this case, the scheduler
tries to schedule, uh, the Map task on the same rack as a server
that contains the input. Uh, this has the advantage that
the inter, uh, the intrarack, or the inside rack
bandwidth can be used, which is typically much faster than going across racks, in order to transfer, uh,
the input block, and this is going
to be fairly fast, not as fast as running
on the same machine as where the data is, but faster than going across, uh, the core switch. However, this
may not be possible either, because all the servers
or all the racks where, uh, this input block is located
may be using up all of their containers. In this case, uh, the, uh,
MapReduce scheduler would then schedule
the task anywhere where a free container
is available. So essentially, uh, these three are, uh, orders
of, uh, preferring where to schedule a Map task. For scheduling Reduce tasks really, um, you don't have
much of a choice because you don't
really know up front where the data from these Reduce
tasks is gonna be coming from. Remember the data
for a Reduce task comes from one or potentially all
of the Map tasks in that job. Uh, and so typically you want
to schedule the Reduce tasks on the same racks as where
the Map tasks are scheduled uh, but in terms of which machines you want to prefer
in those racks, uh, you may want to prefer
at least those machines where Map tasks are scheduled but you, uh, really
don't know much about uh, which particular Map tasks you want to collocate your Reduce tasks with. So, uh, in summary, in this
MapReduce lecture series we have seen how MapReduce, uh, uses parallelization plus
aggregation in the Map phase and in the Reduce phase to schedule applications
across clusters. You have seen many examples of, uh, applications
that use MapReduce. There are many more out there, and, uh, there are many more
out there that are simple, there are many more out there,
uh, of applications that are fairly complex and have
chains of MapReduce, uh, jobs, one after another, and that leverage these chains, uh, to run fairly
complex applications. Uh, these applications need to schedule, uh, these
tasks across jobs, we have seen the Hadoop YARN scheduler at work, and they also need
to deal with, uh, failure. This is a fairly active area
of research, and there's been a lot of work in the last few years, uh, for both scheduling-efficient scheduling in MapReduce and in Hadoop, and also for fault tolerance
in MapReduce and in Hadoop, uh, and I would encourage you to look at a lot of this
literature that is out there.

## 15 - Interview with Sumeet Singh

### Transcript

So I've been at Yahoo
for about three years. Um, I am currently a senior
director of product management for the cloud and
bigger platforms. Uh, it's a pleasure
speaking with you here. When you think about cloud at
Yahoo, uh, or perhaps any other consumer internet company that operates at web-scale
or the scale we operate at, obviously one
of the first things you would think about is scale. Um, and some the other things
that come to mind are, eh, i-if you ask us or the people across
Yahoo it would be service, would be an attribute
that would come to people, service level agreement, SLA, or latency is another thing
that would come to mind, um, a-and then performance. So these are the types
of attributes that people would associate
to cloud computing right? Ease of use of consuming
technology, um, y-y'know, um, expectations around services, those are the types of things that would come to people, um, peoples' mind, uh,
or our developers' mind because it's a private cloud. Our services are
for internal consumption to Yahoos and Yahoo developers so the products and
applications that we host, uh, or the-the platform services
that we provide to our developers
are for our developers, y'know, and our applications. So Yahoo Mail, uh, some
of our mobile applications, search and all kinds
of other things we do or-or the businesses
we operate in, is what our cloud is supposed
to serve or expected to serve. Uh, we don't offer retail
services to, let's say, y'know, consumers outside of Yahoo or
our publishers or anybody else. So that's what I mean
by a private cloud it's really in my mind, it-it-th-the stacks and
the technologies that we put together are more or less the same,
as let's say, a leading public cloud, but the
primary difference here is, um, what we focus on versus
what they focus on. Uh, and the second is that, uh,
it's not a retail service in any sense,
the IP space is private. Not just Hadoop but if you think
about the big data space we have all kinds of other
services now, um, that either run on the same Hadoop infrastructure like Storm or Spark, um, we have introduced those
years ago, um, at a least
a couple of years ago, uh, when it came to Storm uh, and now have some
of the largest clusters, um, for streaming technologies and other things. So it not
just Hadoop anymore, uh, and that's why I like
to call it now, Hadoop and band big data
platforms a-as our group, uh, and then when you come to more
traditional cloud services, which are beyond big data, uh, particularly
on the serving side, um, a lo-a-lot of it is,
y'know, infrastructure services so we work a straight
back through open stack. Uh, we are a gold
foundation member of the open stack,
uh, consortium. Um, I talked
about storage services, about structured and unstructured services, we also talk about hosted search
service, dynamic serving something, um, that-that we're pretty proud of uh, or is really essential
to a consumer web company is th-the serving stack,
um, so we have o-orchestrated the full serving stack
through our cloud services. Uh, we have a set of shared
services like, y'know, messaging across applications, across data centers, hosted messaging services, um, monitoring services, so a-a lot and-and complete ed services
like suite of, y'know, video hosting service, um, dynamic streaming, we have our own CDM, we have our own prox-cloud
proxy infrastructure so it's a full suite
of service, um, just as you may look at,
let's say, something else which is more
trust-bearing to people outside like Amazon web services and if you look
at their suite of services, our suite of services
look exactly the same. So we live and die
distribute computing, um, and we're the ones
who are building, let's say, the Hadoops,
the Hive, and th-the Hbase and things like those
for our company, alright, as well as contributing to the
open source community, uh, across all of these technologies so for us
it's extremely important, but for a user of Hbase, uh,
for a user of Hadoop it may or may not
be equally important. For them, I guess, what's
more important to know is the capabilities
of these platforms, rather than, um, y'know,
what underlying algorithm does the, uh, does the storage
technologies based off of. So I'll give you a good example we had, eh, we have a storage system called Sherpa. Now Sherpa is based
off of a work that was done out of Yahoo labs a long time ago, um, and it was one of the largest
no-SQL installs anywhere in the world
at that time, it's called Peanuts. Um, and, um, now Sherpa
also uses some of the LSM technologies
and LSM's common across, let's say, Sherpa and-and Hbase. Um, now does a person outside
of our platforms organization need to know about these
things, I'm not quite sure? What they ought
to be worried about is like what's my read latency, what's my write latency, what's my read throughput, what's my write throughput if I'm using this storage system
versus that storage system, is this optimal for my use case, is that for optimal
for my use case. And I think
we help our customers a lot in making those decisions, but at the same time I think customers ought
to be smart enough to disseminate the
nuances between, y'know, a million different DB's and-and
no-SQL stacks up there. Yeah I think-I think we have
a philosophy, I mean we both
contribute heavily to the open source technologies, we have open sourced a lot
of our own technologies, uh, for the benefit
of the community. Hadoop being one that we open
sourced in 2009, which is probably one of
the most successful, um, I would say stories, um, that Yahoo has as far
as open source is concerned. ATS is another one,
Apache Traffic Server, which was earlier Incoming Traffic Server, later became and that's widely used across
companies that operate in the cloud computing space. Um, we're doing a lot of work,
um, in open source as well, um, on technologies that were
not developed at Yahoo. So, I'll give you an example
like Storm, like Spark, like Hbase, like Hive a lot of these were not invented
at Yahoo, right? So we brought them from outside
and we contribute, um, um, a lot to those as well, um, we have done, um, pretty, um, I
would say important work when it comes to Hbase in terms
of developing multi-tenants in security in, y'know types
of things that Yahoo needs, types of things
that our customers need from the platform, we've gone ahead
and built those and these open
source technologies to have brought from outside and in the process of,
or have already contributed a lot of that back
to the community. So, I think the philosophy really is about what's useful for Yahoo, uh, be it, eh, the decision of open sourcing something
that we have developed or bringing something from
outside and contributing to it, uh, and it works both ways. Uh, but really the-the essential
idea behind making that decision is to how it's going
to benefit Yahoo, um, and then how it's going
to benefit the community and what would be
the impact to Yahoo as well as the technology
landscape in the longer term. Y'know the question
can be answered, again as I said earlier to you, uh, in-in, two
different, uh, sort of realms. Um, the enterprises think about
cloud in somewhat different way, uh, particularly
in the industry, um, as we the web-scale cloud
consumer internet companies think about cloud, um, an-and I think if you ask
those people, like the enterprise-centric
people about cloud they would talk about, um, y'know, the debate between
public and private cloud and how everything is evolving
as a hybrid model, uh, where workloads can seamlessly transfer
on-and-off premise. Um, they would talk about things
like, y'know, multi-cloud, and private
an-and, members cloud, and, uh, uh, all kinds
of other notions around, um, how these clouds services,
the public cloud services, will be consumed
by the enterprises, the security models
and things like that a-and I think
the general consensus is this hybrid model, uh, is
how it's going to evolve into. But again, with a
services-centric view, not a technology-centric
view, um, as far as technology
itself is concerned, um, obviously a-a company
that operates on that space will promote its own
technology and agenda, a long-term view of how
things are going to evolve. Some would say it's all gonna
be open or based on open stack or based on something else. Um, somebody will have some
other notion, um, if, but, y'know, as far as
Yahoo is concerned and where things are headed I think, um, we're, um, g-we
will to continue to focus on things
that we're focused on today i-in my opinion that battle
will never cease. A-and I think one
of the primary battles we have in this space
is around latency. Everything we do,
within the data center all the way to the end customer, really reducing
that serving time, from when the request was made, to when the response was served, uh, is something we're going to
continue to focus on, a-across our stack,
across our services. Um, I don't think that will ever
go away, uh, tha-or that focus will ever go away. Ah, this-this notion
of instantaneous response, you click something
and you have the answer, that will never go away. Um, so our technologies, uh,
our services will continue to focus on that. We will continue
to refine our SLAs that we make with our customers, around throughput,
around latencies, um, and they are going to stay
as our focus. Um, I think, I also think that
from a technology standpoint, um, there is a-a blurring
of boundaries between the backstage, um,
infrastructure or platform, as well as the serving
in-infrastructure or platform an-and there now sort
of, eh, eh, converging, right? So Hadoop was sort of our, y'know, asynchronous
processing platform, we had a bunch
of proprietary technologies in this serving stack,
and as you can see a lot of these
are now merging, right? People are demanding
real-time responses from Hadoop type infrastructure as well as people are expecting
more and more, um, y'know, deep edge capabilities, um, deep
analytics capabilities, right? And the edge would be
an event of Internet of things a-a-a-and, um, eh,
and that's not quite possible, um, um, given the,
given the, um, size and the processing powers
of these edge devices. So, eh, I-I think there is a
lot of blurring of this boundary between asynchronous processing
and serving infrastructure and I think technologies will
evolve in both of these spaces, um, that would try to do
more, uh, uh of both. Um, so integrating analytics
on the edge, uh, we can't send everything
back to the data center and expect real time response back to the edge, um, those types of things
will not happen so you will develop
new types of capabilities. As I said our cloud covers
everything from the edge, back to the data center, so there will be
a lot of invention, a lot of, I would say, e-evolution of technologies that we use today, uh, both in our
video infrastructure and CDN in objects. CDN infrastructure
will evolve a-a lot to take care of things like
the-the, um, the evolution of, eh, y'know, internet
of things and other things and as we as consumer
internet company latches on to some of those. Um, so, eh-eh it's-it's, five to ten years is definitely
going to be extremely exciting. That is all I can say. Um, this-this space has, y'know,
millions of possibilities where things will head, uh, but one thing I can say for
confiden-with confidence is that, um, it will-it will
extremely interesting. Absolutely, um,
a-and not just again Yahoo, I would say it's the foun-the
platforms, the cloud platforms, the foundation
of any consumer web company, I mean, not just for Yahoo. Um, in many a cases platforms
and technologies become competitive vantage, um, and so the-the-the usage of
cloud, the importance of cloud, the importance of platforms
have not gone down, it's only becoming
more and more important as we try to bring more, um,
I would say, innovative user experiences, mobile experiences out in the
market at a quicker pace. The role of platform only
impro-, um, I would say increases, um, so i-it actually helps us get
things out on the market faster. Um, a-and that's exactly where
we're focused on right now in terms of delivering new and
interesting user experiences. Um, that, um, eh, as we call as will become
the daily habits of people. Um, and the importance of cloud,
the importance of platform, eh, has really, really increased,
uh, it has not gone down. Wh-so, eh, for me the whole
platform space, the cloud, um, th-the big data space
was very interesting. So when I was making
the transition into Yahoo, um, that was the space
I wanted to get into, so I was somewhat
domain-centric, less company focused. Um, and, um I got all of that,
I got to do all of that and I got to work in cloud, I got to work at scale
that is unbelievable. We have, y'know, give or take
how you-how you define the users 800 to a billion unique users, a-and that drives a lot of interesting scale challenges on the technology side,
on the platform side. You get to see all of that. Um, the other interesting thing
I find, uh, which keeps me extremely happy here is this idea of, so when it comes to big data
or Hadoop, remember, this was the birthplace of Hadoop right? So you have a very strong
development team that has, let's say, more than 50% of it's, um, eh, eh, members as committers or PMC's
in leadership roles in the open source community. Um, so they control a lot of,
um, y'know, what happens, uh, in the, uh,
open source community, um, so-so it's always interesting
to work with them, uh, on the development side and then al-we also have one of
the world's largest footprints in the world when it comes to
the infrastructure itself, uh, and the services we offer
to rest of Yahoo. Uh, pretty much the entire
business runs on the platform, so, y-you to get see both these
sides, uh, at the same place, in the same job, uh,
which is pretty exciting. So, tha-that to me
has been invaluable. I don't think
I-I'm going to get that in a pure software
distribution house, uh, or in a pure
public cloud company. Um, over here I think
I get to see both, th-the all the engineering
and development aspects of the technology, as well the services aspect. When you deploy
a lot of what we develop on one of the world's largest private cloud infrastructures. So, um, no issues,
no complaints. [laughs]

## Quizzes

_No transcript available._
