# Week 07 - Week 7 Classical Distributed Algorithms

## 01 - Week 7 Introduction

### Transcript

[MUSIC] Congrats, you have made it to week five
and in this week five, we continue our deep-dive into the heart of distributed
systems by studying a few more of the core critical concepts that have been using
this to a distance for many decades and continue to be used today in clouds and
will continue to be used in the future. These concepts include snapshots
they include multicast and they include consensus and specifically
the paxos protocol these are very important concepts for
us to know as cloud computing people. [MUSIC]

## 02 - 1.1. What is Global Snapshot

Slides: C3_Snapshots_A_CSRAfinal.pdf

### Transcript

Hi there. Uh, in this, uh, series of lectures, uh, we'll see, uh, what, uh, the concept of a global snapshot is, uh, how do you calculate
a global snapshot, and, uh, the kinds of things that it can be used to detect. So here's an example
of a global snapshot where, uh, the, uh, premiers, or the representatives
of several nations, uh, gathered in one place
and, uh, took a photograph. Uh, this was done
in Paris in 2011. Uh, so this is the easy way
of calculating the snapshot, uh, but that's not
what we wanna do. This problem really, uh,
becomes challenging when, uh, the country's representatives are sitting in their
respective capitals and they're exchanging messages,
say, via emails, uh, sent to each other. In that case, uh,
in this very distributed system, calculating a global snapshot becomes very, very challenging. In fact, it's not even clear what a global snapshot even means when there are messages, uh, in transit among these different processes in the, in the system. What I've described is in fact a distributed system
of representatives. You can think of, uh, this being analogous to our distributed system of processes, uh, which are also exchanging messages with each other. In the cloud, for instance,
you might have an application or service that is running
on multiple servers. The servers are handling
concurrent events and interacting with each other via messages, and the ability
to obtain a "global photograph" or a global snapshot
of the system is really useful for detecting
many kinds of properties. You might want to checkpoint
the system, uh, so that, uh, the entire distributed computation is checkpointed across multiple processes
so that if you have a failure, then you can restart
from the latest checkpoint. You might want
to garbage collect objects. For instance, you might want
to detect objects, uh, that don't have
any other objects or servers pointing to them, so that these
can be garbage collected; these are orphan objects. You might want
to de-detect deadlocks, um, in database transaction systems. You might want to detect
termination of computation in @Home applications like
Folding@Home, uh, or SETI@Home, which some of you
might be familiar with, or in, uh, batch computations that might be running in, uh, the cloud. But what is a global snapshot? So a global snapshot,
or a global state, consists of an individual state for each process in the distributed system, along with a state for each
of the communication channels in, uh, the distributed system. Essentially, we want
to calculate, uh, or capture the instantaneous state
of each process in the system, and also the instantaneous
state of each of, uh, the, uh, channels in the system. When I say a channel I mean
a point-to-point channel that goes from one process p
to another process p. So, uh, one, uh, obvious solution to this is to synchronize the clocks
of all the processes using one of the well-known synchronization algorithms, uh, which we have discussed elsewhere in the course, um, and then fix a time at which all the processes record, uh, their own states. The issues with this are one, that time synchronization always, uh, is error-prone, uh, with the error being a function of the round-trip time, uh, and/or the message latencies in the network. You really don't want
your banker to inform you that "Hey, we had a 1-millisecond clock skew among our, uh, servers, and this resulted in us losing your, uh,
entire bank balance, and so we don't know, we are, your bank balance is 0." Uh, also this algorithm does not
record the state of the messages in the channels themselves. Uh, thankfully, uh, causality comes to our rescue again. Uh, we don't really need
time synchronization here; we can again, uh,
make due with causality. What do I mean by causality? So let's see an example
of a system moving from one global state
to another, or one glob-
global snapshot to another via a series of causal steps. In this system I have two
processes only, Pi and Pj with two channels
going each way. Uh, C goes from Pi to Pj,
and C goes from Pj to Pi. Uh, so, uh, here is an
example of global snapshot. We call this Global Snapshot 0
of the system, where Pi's state has
$1,000 and 100 iPhones, and Pj's state has
$600 and 50 Android phones. The states of the channels
C and C are both empty. Uh, these four put together, uh, are, comprise
the global snapshot 0. Now a development might happen
in the system. For instance, uh,
Pi might send $299 and an order for
one Android phone over to Pj. This changes, uh,
the state of, uh, Pi. It also changes the state
of the channel C, which now has
a message in transit. So, uh, with this one event happening in the system, uh, uh, because s-uh, somewhere in the system
some state has changed, the entire global snapshot has also changed, 'kay? So we call this new snapshot
as a Global Snapshot number 1. Next, another event
might happen in the system, which might be, the fact that, Pj might send an order for an iPhone, along with $499 to Pi. This results in the balance
at Pj going down to $101, and also, uh, the state
of channel C changing, um, uh, to have
one message on it. So once again, this changes
the state of the entire system, so this is
Global Snapshot number 2. Uh, then, uh, the message
from Pj is received at Pi. Uh, the state of the channel
Cbecomes empty now, Pi's balance goes up, it has an outstanding order
of one iPhone, and so the state of channel
Pi also changes. This is a third global snapshot
of the system. In moving from one global
snapshot to the next, what you're seeing is that an event happens somewhere
in the system, and, uh, this is, uh, a s-a series of causal events, um, uh, in the system. Nowhere here, uh,
in the snapshots are we talking about time at all, or physical time at all. Uh, next what happens is that, uh, Pisends the iPhone, uh, order over to the channels, um, to, uh, Pj, and this is sent
on channel C. The channels are ordered FIFO,
which is first-in, first-out, which means that C will deliver the first message sent on it first, and later messages
will be delivered afterwards. Uh, but, in any case, here
the state of channel Picha-uh, the state of the channel
Cchanges because it has one extra message which it has to deliver now, and the state of Pihas also changed because it's now fulfilled
its outstanding order, and so this is another Global Snapshot number 4 in the system. The Android, uh, order
is received from Pi at Pj. Uh, Pj's balance goes up and it has the outstanding Android order, and then, uh, the iPhone
also is received at, uh, Pj, and both of these result in two different global snapshots. And the system
continues like this, moving from one
global snapshot to the next via a series of events. Essentially these are causal, uh, paths that global snapshots, uh, move, uh, through. So, whenever an event happens
anywhere in the system, whether a process
receives a message, a process sends a message, a process takes a step, one event is enough for the entire global state to change, because the global state captures everything
in the system. Um, and so the state to state
movement obeys causality. Uh, next, uh, lecture we'll see,
um, uh, um, an algorithm to actually calculate this global snapshot, uh, uh, b-uh, in, uh, concurrently with the application still, uh, running, 'Kay, that's called
the Chandy-Lamport, or the Global Snapshot Algorithm.

## 03 - 1.2. Global Snapshot Algorithm

Slides: C3_Snapshots_B_CSRAfinal.pdf

### Transcript

Okay, so in this lecture we'll see the actual, uh, algorithm, the classical algorithm
that is used, uh, to calculate a global snapshot,
uh, in a distributed system. So once again,
just to remind you, uh, the goal here is
to record a global snapshot which consists of a state
for each of the processes in the system and a state for each
of the channels in the system. Uh, once again, when someone
gives you a problem, just make sure that you know
what the system model is under which you're trying
to solve the problem. Uh, here the system model
is as follows. We have N processes
in the system. Between every pair of processes there are two communication channels, one going each way. So between two processes Pi
and Pj, there is two channels, one from Pi to Pj,
one from Pj to Pi. Each of these
communication channels, uh, the goes one process
to another, is FIFO ordered. When I say FIFO it means
first-in, first-out. This means that if, uh,
on a channel from Pi to Pj, a message M1 is sent first
and then message M2 is sent, M1 is received first at Pj
and only then is M2 received. We also assume that there
are no failures at processes, and also that messages
are not dropped, they are intact, and that they are not duplicated. Uh, w-uh, some
of these assumptions, especially the failure
and message assumptions, uh, have been addressed
by subsequent variants of the classical protocol
we are gonna discuss, okay, but for now we'll just assume,
uh, what was assu-assumed in the original, uh,
classical algorithm. So some of the requirements are that the snapshot calculation must not interfere with the normal application
operations or messages. It must not require processes
to, uh, stop doing what they're trying to do or,
um-uh, stop sending messages. We want, uh, the algorithm to continue concurrently
and simultaneously with the other application,
um, operations. We want each process to be able
to record its own state. When I say a process state,
I really mean, uh, either an application-
defined state or, uh, failing that, a state
that captures the entire, uh, state of the process, uh, its heap registers, program, uh, code, program counter, code,
um, stack, and anything else that might appear
in the coredump of that process. Uh, the global state
is collected in a distributed manner. We do not want centralized
collection of, uh, the, uh, of, uh, of the state, and, uh, we want any process
to be able to initiate or start
the snapshot collection. Now there might be
multiple snapshot collections that might occur in the system,
perhaps even simultaneously. Each of these runs
would be distinguished by using a unique ID. For now, for most of
our examples we'll just assume there's one run
of the snapshot algorithm that is happening in the system. So, uh, here is the snapshot
algorithm in two slides. Uh, in the first slide we say
what the initiator process does, and in the second slide we'll
say what the other processes do. Uh, the initiator process, uh,
first records its own state, and again, by state I mean
either application state or the coredump state. Then the initiator process
creates special messages called marker messages, and on each of the,
um, and these marker messages, um, are not
application messages. They do not interfere
with application messages, but when a marker message
is sent on a channel, it is ordered alongside
other application messages. In other words, if a process Pi
sends some application messages and then a marker message, uh,
the marker message is delivered only after those application
messages on that channel. Similarly, any application
messages sent after the marker are delivered only after
the marker is received on that channel. So, returning to the algorithm,
once the initiator has recorded its own state, it then sends out a marker on each of the N-1
outgoing channels, from Pi itself to the other
processes, uh, Pj, where j is not
equal, uh, to i. Uh, finally it starts recording,
uh, the incoming messages of each of the incoming channels
at Pi-that is Cji for um, again these are N-1
incoming channels at Pi. So markers were sent
out from the initiator. What happens when a process
Pi receives a marker? This could be any process in the
system, not just the initiator. When Pi receives a marker
on an incoming channel, say Cki, which means that Pi is receiving
the marker from process Pk, if this is the first time that the, uh, Pi,
process Pi is seeing a marker, meaning it's the first marker
that Pi is receiving, then the first thing that Pi
does is record its own state. This could be the application
state or a coredump of Pi, or anything that captures
the history of Pi. Next, uh, Pi marks the state
of the incoming channel Cki on which it received this first
marker as being empty, okay, so this is going to be the
final state of this channel Cki in the final global snapshot. Then on the, uh, uh,
N-1 outgoing channels, um, Cij from Pi outwards,
uh, Pi sends a marker out, okay? Uh, finally, uh, Pi starts
recording the incoming messages on each of- of the
incoming channels at Pi except the one that it just, uh, marked at state 4, which is Cki. So for the other N-2 incoming
channels, other than Cki, uh, it starts recording, uh,
the incoming messages on them. This is important because we want to, uh, capture
the messages in transit as well, so when Pi receives a marker
for the second or the third time where it's already seen
a marker message before, and this, uh, duplicate
marker message is being received on channel Cki, then, uh, Pi marks
the state of channel Cki as consisting of all those
messages that have arrived on Cki since Pi first turned
on recording, okay? So between the time that Pi
received its first-first marker until a marker was received
on channel Cki, uh, all the messages that have
been received on channel Cki are considered
to be part of Cki's state. So essentially here what
I'm saying is that, uh, all the processes
will end up sending, uh, marker messages
to each other, and this will ensure
that all the channels have their states snapshotted. Uh, of course, the state of a
channel is snapshotted only at, uh, the, um, uh, process
that is at the receiving end of that channel. The algorithm terminates when
all the processes have received, uh, one marker message so that
they record their own states, and then, um, all the channels
have had one marker message, uh, transit through them
and be received at them. This would make sure that, uh, all the, uh,
N-1 incoming channels at each process
have their states recorded. Later on, if needed,
a central server can collect all these partial
snapshot pieces to calculate
the global snapshot, and then, uh, you know,
check whatever global property is required, but again, that's
optional; that's not required. The global snapshot calculation
and collection itself, the original collection is
in fact a distributed operation. So let's see an example of this,
um-uh, snapshot algorithm, uh, at work. So here's an example
of three processes. Time goes from left
to right again. Uh, the, uh, events shown here, both, um, uh, instructions
such as A and C, uh, as well as message sends
like B and the message-receives like E are
all application messages. Uh, so, uh, when P1
the initiator starts its, uh, collection, this is being done
concurrently and simultaneously alongside the
application messages. So as initiator P1 starts its,
um, uh, uh, algorithm by recording its own state, we'll call that as S1, it sends out markers on the two outgoing channels C12 and C13, and it turns on recording on the incoming
channels C21 and C31. Next, uh, P3 receives
the marker from P1. This is the first marker
that P3 is seeing, so it records its own state; let's call that state as S3. It marks the state
of the incoming channel on which the marker just came
in, which is C13, as MT. Next it turns on recording
on the other incoming channels, which is just C23 in this case. Finally it sends out markers on, uh, all the outgoing channels over here, okay, which is C31 and C32. I'll summarize that via
this, uh, simple text here. Uh, next, um-uh, the marker
from P3 is received at P1. Uh, clearly this is a duplicate
marker that P1 is seeing, so, uh, at this time
it stops recording the state of the channel on which it just received
the marker, which is C31. Uh, it started recording
the state, uh, when it recorded
its own state S1, and in the meantime, no messages
have been received from, uh, P3, so the state of channel
C31 is marked as being empty. Next, uh, the, uh, marker
for P3 is received at P2. This is the first marker
that P2 is seeing. The marker from P1 that was
sent to P2 is still in pr- in progress, it's still
in transit in the network. Uh, so when P2 receives
this marker, the first marker it's seeing, and, uh, so it records its own
state as, um, uh, own state; we call that as S2. It marks the state
of the channel on which the marker just came in, C32, as being empty, and finally it turns
on recording on the-on the other
incoming channel, which is C12, and it also sends out markers, because this is the first marker that it's seen. Uh, next, uh, the marker
from P1 is received at P2. This is a duplicate marker,
so P2 stops recording, uh, messages on the channel C12 and marks the state of channel
C12 to all the messages that have been
received since S2. That is empty, and so the state
of channel S-C12 is marked as empty. Uh, we are not yet done. P2 next, uh, s-uh, uh,
P2's marker is received at P1. This is duplicate, so it's, uh,
so the channel C21's state on which the marker
has just been received is marked as consisting
of all the messages since, uh, S1 until a marker
is received on C21. Notice that this message, uh,
that had the send event of G and the receive event of D, uh, was received in between
when S1 was recorded until C21's, uh,
state stopped being recorded. So that message is, uh,
considered to be a part of the state of the channel C21. Obviously, uh, this
doesn't refer to, uh, the, um, an actual
physical point of time at which this g-global snapshot
has been calculated, but at some, uh,
past point of time at which the snapshot
was in fact true. Next, uh, the, um-uh, marker
for P2 is received at P3, and again this is
a duplicate marker, and, uh, the state
of the channel C23 is, uh, said to be consisting
of all the messages that were received since S3
was calculated, and that's just empty
in this case. So at this point,
the algorithm has terminated because all the, uh, processes have calculated their,
uh, states, and all the channel states of all the six channels in the
system have been calculated. Uh, you could, if you wanted, uh, to collect the global snapshot pieces in one place and then calculate
whatever global property you want to calculate on this, but this is again optional; uh, it's not really needed for the original global
snapshot calculation itself. Now, the global
snapshot calculated by the Chandy-Lamport algorithm is not actually, may not actually be,
have been true at any physical point
of time in the past, but it is causally correct, so, uh, it is correct
in the sense of causality. What does this really mean? We'll see this
in the next lecture.

## 04 - 1.3. Consistent Cuts

Slides: C3_Snapshots_C_CSRAfinal.pdf

### Transcript

[MUSIC] In this lecture we continue discussion
of the Chandy-Lamport Global Snapshots algorithm, and
see why it was causally correct. So we discuss this notion
known as consistent cuts. Before we discuss consistent cuts,
let's discuss a cut. A cut is a time frontier at each process
and at each channel in the system. So essentially at each process and at each
channel, you decide a time point, and everything to the left of that
time point on that process or channel is considered to be in the cut. And anything to the right of that time
point is considered to be out of the cut. So, that is a cut. Some cuts are consistent, and in order for a cut to be consistent you need to make
sure that every pair of events, e and f, that occurred in the system at any
processes, they need not be at the same process, such that e is in
the cut and f happened before e, if these two conditions are true then it
is also true that f is also in the cut. Okay, if this is true then
the cut obeys causality and is said to be a consistent cut. So let's see two examples of cuts. The green cut on the left is a consistent
cut because it obeys the two conditions. Notice here, the messages over here,
B happened before E, and E is in the cut and
so B is also in the cut. H happened before F, F is out of the cut,
H is in the cut, and that's okay. So in this particular cut, the message
H to F is set to be in transit and is captured by the cut
itself as being in transit. The red cut on the other hand, shown
in the right, is not a consistent cut, because consider this message that has
a send event G and the receive event D. D is in the cut, but G which
happened before D is out of the cut. And that is not allowed by
the consistency predicated, so this red line I've drawn out here is
a cut, but it is not a consistent cut. So our Global Snapshot algorithm which you
saw in the last lecture, calculated this particular snapshot over here which
consists of each of the process states, S1, S2, S3, and the states for
each of the channels C, I, J, which are six channels in the system. So our Global Snapshot algorithm
in fact results in a snapshot that is causally correct in the sense that
it corresponds to a consistent cut. By the green dotted line here I am showing
the consistent cut that is captured by our Global Snapshot algorithm. You'll notice that the place where
the cut cuts across each process timeline is in fact the time at which
that process state is calculated, S1 for P1, S2 for P2 and S3 for P3. And also this consistent cut cuts
across the message G to D which is also a part of the Global Snapshot calculated
by the Chandy-Lamport algorithm. So the consistent cut shown by
this green dotted line is in fact the same as the state captured by
the Global Snapshot algorithm. In fact,
you can show that in any invested system, any run of the Chandy-Lamport
Global Snapshot algorithm always results in a global snapshot
that corresponds to a consistent cut. Let's see why this is true. Let's look at the proof. Let ei be an event occurring at Pi, and ej be an event occurring at Pj,
such that ei happens before ej. This is Lamport's happens
before relationship. The snapshot algorithm ensures
that if ej is in the cut, then ei is also in the cut, okay? We are going to prove this fact. If this fact were true, then this would
mean that the consistency condition for the consistent cut is obeyed and so the result of the snapshot algorithm
is in fact a consistent cut. In other words, what we want to show is that if ej happens
before Pj records its own state, meaning ej actually belongs to the cut calculated
by the Global Snapshot algorithm, then it must also be true that ei happens
before Pi records its own state, that is ei is also a part of the cut calculated
by the Global Snapshot algorithm. So let's prove this by contradiction. Let's assume that the first condition
is true, which is that ej is a part of the cut, so ej happens before
Pj records its own state. But that the second condition is not true
which is that Pi records its own state is in fact happens before ei, okay? So, because all the events at Pi
are ordered linearly because Pi's clock, if its not true that ei happened before
Pi records its own state, the reverse must be true which is that Pi records
its own state must happen before ei. Along with this, you also have
the fact that ei happened before ej. So, consider the causal path
that goes from ei to ej, along that causal path consider all
the sequences of process timelines, and all the channels on which messages
pass along that causal path. Due to the FIFO ordering
on the causal paths and the linear ordering of events at
each process, it must be true that the markers on each link above proceed
the regular application messages. Why do the markers proceed
the regular application messages? Because Pi records its own
state before ei happens and so the markers are sent out when Pi records
its own state, and so the markers which proceed on the causal path from ei to
ej will proceed the ei to ej messages. But then this automatically means
that the marker is received at the process Pj before the event
ej happens that crosses Pj. But then this means that Pj must have
received the marker before ej, and so it cannot be true that ej happened
before Pj records its own state. And so we have a contradiction here. And so what we assumed in the green
statement over here at the top of the slide must be false. And so it must be true that
if ej belongs to the cut, then ei also belongs to the cut. That completes our proof. In the next lecture, we'll see some examples of kinds of
properties which the Chandy-Lamport algorithm is used to detect in
the global distributed system itself. [MUSIC]

## 05 - 1.4. Safety and Liveness

Slides: C3_Snapshots_D_CSRAfinal.pdf

### Transcript

Uh, in this lecture we'll see
two very important properties that are, uh, desired
in distributed systems; these properties are called
safety and liveness, and along the way
we'll also discuss the kinds of, um, properties that, uh, the global snapshot
algorithm can be used to detect
in a distributed system. So correctness in distributed
systems is, uh, highly desired, and there are two properties
that can be used to, uh, specify
correctness requirements. These properties are known
as liveness and safety. Uh, the definitions
are distinct, uh, but they are often confused with each other, so its' very important for us
to be able to distinguish one from the other. Let's look at liveness first. Uh, in a nutshell, liveness is
a guarantee that something good will happen eventually, okay? Uh, eventually does not imply
a time bound, but if you let the-the system run long enough, then it-it guarantees,
uh, liveness. Uh, so examples of this, uh,
are, in the real world, uh, the guarantee that
in an Olympics 100 meter dash, at least one of the athletes will win the gold medal. This is a liveness
guarantee, something good, which is winning the medal,
happens eventually. Uh, a criminal
will eventually be jailed is a liveness guarantee that legal systems in many
countries, uh, try to guarantee. It's hard to guarantee it,
but it-it is a desired property. In a distributed system, uh,
the termination property is a liveness property. You want a distributed
computation-computation to terminate, and, uh, this is the, uh,
guarantee that something good, which is termination,
will happen eventually. Completeness and
failure detectors, uh, is a liveness property. This is a property
that says that eventually, every failure will be detected by the other non-faulty
processes in the system. In consensus, uh, liveness says that all processes eventually
decide on a value. Safety, on the other hand, is
a guarantee that something bad will never happen
in the system, okay? So notice that there we are
using "bad" instead of "good" earlier in the liveness, and we are saying
will never happen, uh, because we desire that it
never happens in the system. Again, in the real world, a
peace treaty between two nations is an example
of a safety property, uh, which guarantees that war will never happen
between those two nations. Again, this is
a desired property; this is not always what happens. Uh, wars have happened
in spite of treaties, um, so treaties are clearly
not safe all the time, but it's an example
of a desired safety property. Uh, legal systems try
to guarantee the safety property that an innocent person
will never be jailed; that would be really bad. In a distributed system, uh, the fact that we
do not want deadlocks in a distributed
transaction system is an example of a safety
property which we desire. The fact that we do not want
objects to be orphaned, meaning they don't have any
pointers pointing to them, is an example
of a safety property. Accuracy and failure detectors
is a safety property because it says that we do not
want any mistaken detections of non-faulty processes
being marked as failed. And in consensus, we do not
want two different processes to decide
on two different values, uh, because that would be bad and that would be unsafe. Uh, guaranteeing both liveness
and safety is very hard. In failure detectors
guaranteeing, um, uh, liveness and safety, which is
completeness and accuracy, is, uh, impossible in an
asynchronous distributed system, especially if you want these
to be time-bounded. Uh, in c-in the consensus
problem, uh, making decisions, uh, within a time bound and, uh,
correct decisions, um, uh, making sure that the correct decisions
are correct cannot both be guaranteed in an asynchronous
distributed system. You can guarantee
eventual liveness, which is what algorithms
like Paxos, uh, guarantee, but time-bounded liveness
cannot be guaranteed. And of course,
as many of us know, it's very hard for legal systems to guarantee both, uh, liveness and safety, and in fact to guarantee
either liveness or safety is very hard. Um, it's-it does happen that some criminals
never serve any jail time, and it also does happen
that innocents are jailed. So in the language
of global states; remember that
a distributed system moves from one global state
to another via causal steps, um, which you saw
in an earlier lecture in the snapshot series, uh, liveness with respect
to a property Pr in a given state S
essentially means that, uh, the state S satisfies Pr, and if this is,
uh, not true, then there is some causal path that goes from
the state S to another state S', global state S',
where S' would satisfy Pr. Okay, so all you require here
is that there is some way to get from the current state
to another state, um, that, uh,
satisfies liveness. If this is true for every state
that you are in, that whate-whatever state
you are in, you can reach another state that um, uh, that satisfies liveness uh, the liveness property Pr, then this system
is said to be satisfying the liveness property. Notice that you do not require
all the states, uh, reachable to satisfy this property Pr, just some causal path
and some end state to satisfy the property Pr. Safety, on the other hand,
with respect to property Pr, says that, um, in state S,
S satisfies the property Pr, and all global states S'
that are reachable from S via causal paths
also satisfy Pr. If this is true, then
the safety property is true. So how do we use
a global snapshot algorithm to detect global properties? Well, the snapshot algorithm can be used to detect global properties that are stable. When I say stable,
I mean properties that, once they are true, they st-they stay
true forever afterwards. Uh, these could be either
stable liveness properties or stable non-safety properties. A stable liveness property
might be of the kind the computation has terminated. Once a computation
has terminated, it stays terminated forever, and this is obviously
an example of a good property that we want to be true, so it's a liveness property
that is stable, and it can be u-and
it can be detected using the global
snapshot algorithm. Stable non-safety properties
include, um, uh, the fact that
there is a deadlock. Once a deadlock happens
in the system, it will stay forever until
you do something about it. Also, uh, once an object
is orphaned, uh, that is, it has no pointers
pointing to it, it will stay that way until you
do something about it. Both these are examples
of non-safety properties that are stable, and so the global snapshot, uh,
algorithm which we discussed, the Chandy-Lamport algorithm, can be used to detect,
uh, these stable properties. Uh, why can you use to dete- these to detect
the sto-stable properties? Because Chandy-Lamport algorithm is guaranteed
to be causally correct. Even though the Chandy-Lamport
algorithm does not, uh, guarantee that the snapshot
calculated by it holds at any physical point
of time in the past, it does guarantee
causal correctness, uh, which means
that it does not violate our, uh, human being's understanding of what happens causally
in the distributed system, and so it can be used to detect,
uh, stable properties. Wrapping up our discussion
of snapshots, the ability to calculate
a global snapshot is really important
in a distributed system, uh, but you
want to calculate the snapshot, uh, concurrently and parallelly while allowing the application to continue proceeding and sending
its application messages, and the Chandy-Lamport algorithm allows us to do exactly that. The output of a
Chandy-Lamport algorithm is a, uh, global snapshot
that obeys causality. In other words,
it satisfies a consistent cut, it's equivalent
to a consistent cut, and it can be used to detect
stable global properties which are either, uh,
liveness properties or non-safety properties. We've also discussed
two very important definitions, liveness and safety, which, um, are
relevant of course to the snapshot-
snapshots discussion. These are properties
that appear, uh, elsewhere and in other parts
of this course, uh, because these
are very important, uh, classes of properties that we desire
in distributed systems.

## 06 - 2.1. Multicast Ordering

Slides: C3_Multicast_A_CSRAfinal.pdf

### Transcript

Hi there. In this, uh,
series of lectures, uh, we'll be discussing the distributed computing
problem known as multicast, which is very widely used
as a building block in, uh, many of the
cloud computing systems today. Uh, in this lecture today we'll be discussing the ordering
property of, uh, multicast. So multicast, again,
in a nutshell, uh, is a message
that needs to be sent out in a group of, uh, processes. Um, uh, these processes are
running at internet-based hosts. Uh, for instance, here I have
a group of processes, each denoted by a circle. A-a red circle, a red process,
has some piece of information that needs to be sent out
to all the other processes in that, uh, group. Uh, this is
only one multicast message. There might be multiple, uh,
multicast messages that are being sent out
by that sender one after another uh, and also multiple senders
in the group might be, uh, trying
to send multicast messages, uh, to the other processes
in the group. So, uh, multicast in a nutshell
is a message sent to a group of, uh, processes,
a selected group. A broadcast, on the other hand, is a message that is sent
to all the processes anywhere, uh, in the system and
in fact anywhere in the world. Broadcasts are also
very widely used, um, uh, but of course broadcasts can be pretty expensive, uh, because, uh, processes
that don't, uh, really, uh, have any interest
in the message might also receive
the multicast message or the broadcast message. A unicast message is, uh,
the most common kind of message that we have seen, uh,
so far in this course. Essentially it's
a point-to-point message; there is one sender process
and one receiver process. Uh, in terms of, uh, uh,
this terminology, the multicast has, uh, one sender and, uh,
multiple receivers per message. The broadcast has one sender and everyone else as a receiver
for that one message. So here in this lecture we'll
focus on, uh, multicasts only, which are messages sent out
to a group of processes. So who uses the multicast? It's a widely used
building block by many cloud computing systems. For instance, key value stores
like Cassandra, which are storage systems,
and database systems, use multicast internally. For instance, a given key might have multiple
replica servers which are replicating
the values for that key. So in that case, uh, the writes
and reads that are sent to that key from, uh, any client
will then be multicast inside the group so that all
the replicas are up to date and reflect the same values for the key
at any point of time. You don't want to send
the values for that key to other servers beyond
the replica group because they are not interested in that particular, uh, key itself. Also, these systems use
membership information, uh, such as, uh, gossip-style, uh, membership, uh, protocols
in these systems, and essentially,
uh, membership, uh, information requires information
about joins, leaves and failures of processes to be multicast out within a group of servers that are running
that storage system. Uh, multicasts are also used
in user facing scenarios, so for instance online
scoreboards of sporting events such as ESPN, French Open tennis the FIFA World Cup, essentially have each
of the clients, uh, be subscribed to certain topics, and essentially whenever there is an update for a topic, such as an update
to a score for a match, that update is multicast out
to all the clients, all the browsers out
there in the world that are interested
in this particular update. So that's a multicast being used
in a user, uh, facing scenario. Multicast is also used in the floor of, uh,
stock exchanges and air traffic control systems. For instance, on the floor
of a stock exchange, the group might be the set
of broker computers, and whenever there is a trade on any one of the broker computers, it's then sent out the other broker computers on the floor. This ensures all the broker
computers are up to date at all points of time and are
reflecting the latest updates and stock trades on the floor. Multicast is also used in
high-frequency trading among the servers that are trying to do
high-frequency trading, and here it's fairly important
for the multicasts to be fast, uh, as well as reliable as well. In the air traffic
control system, all the air traffic controllers are seeing a picture of the sky, and you want
all the, hm, pictures to be consistent
with each other. You don't want one
air traffic controller, uh, seeing a slightly stale
or outdated picture, and so any update done by one air traffic controller's
computer is then multicast out to the group of other air
traffic controllers' computers. So you see two things, eh,
emerging from here. One is you need
reliable multicast; you want all the processes in the group
to receive the multicast. And the second one is you need
to worry about ordering; you want, uh, all the multicasts
to be received, uh, in the same somewhat consistent order at all the processes
in the group. So let's look
at the FIFO ordering first. Uh, in FIFO ordering, essentially multicasts
from each sender are received in, uh, the
same order that they are sent at all receivers. This means that
if two multicasts are sent by, uh, these same sender,
they're of course sent in an order depending
on that senders um, uh, timeline and the sender's clock, and they need to be
delivered in exactly that order at all the receivers
in the group. However, if two multicasts are
from different senders, then we don't really care about which order
they're delivered in. Uh, some multicasts, uh, some
processes might deliver those two multicasts from
different senders in one order, and, uh, other receivers
might deliver them in the opposite order, and that's fine as far
as FIFO ordering is concerned. So a little bit more formally,
if a correct process, uh, issues or sends
a-a multicast, uh, m to a group g, uh, and then sends a multicast m' to the same group g, then every correct process
that delivers, uh, the second message m'
would already have delivered m. In other words, you are saying
that, um, you deliver m' only after you have delivered m. And notice that here we're
talking about correct processes, which means that we're talking
about, uh, non-faulty processes. This accounts for, uh,
failures, if processes fail, then we don't necessarily know
what they did, and so we don't want
to worry about them. We a, uh, we only want
to make sure that processes
that have not failed, uh, follow, uh, the particular, uh, ordering guarantee that we are trying to provide. So as an example,
here is a timeline. Again, here we have four
processes; P1, P2, P3, P4. Time runs from left to right, and you notice that
there are multiple multicasts being sent out, so process P1 sends out multicast, uh, 1 over here,
shown as, uh, M1:1. Process P1 also sends out
a second multicast, M1:2. Uh, process P3 sends out
a multicast M3:1. And so you'll notice here
that because M1:1 and M1:2 are multicasts sent
by processes-process P1, which is the sender,
in that order, they need to be delivered
in exactly that order at all the recipient processes. So P2 delivers M1:1 first, uh, and only then
does it deliver M1:2. Similarly,
P3 delivers M1:1 first, and only then
does it deliver M1:2. Similarly for P4 as well. However, as far as M1:2,
sent by process P1 and M3:1 sent by process P3
are concerned, they are sent
by different senders, so FIFO doesn't
worry about them. In fact, they can be delivered
in opposite orders at, uh, different, uh, process. So P2, for instance,
delivers M3:1 first, while P4 delivers M1:2 first, and that's fine. This still obeys FIFO ordering because we are only bothered about, uh, the messages that originate
from the same sender. Here, if, uh, P3 had sent
a second message M3:2, say over here, then that should have been
delivered, uh, after M3:1 at all the recipient processes. So let's look
at the next flavor, which is known
as causal ordering. Uh, this is an extension
of, uh, FIFO ordering. Uh, in this,
um, kind of ordering, multicasts whose send events
are causally related must be received in
the same causality-obeying order at all receivers. What this is trying to tell you
is that if two multicast sends are, uh, related
in the-by a causal path, so if the multicast send
of one message m, uh, causally
happened before the multicast, uh, uh, the send of
the multicast mech-message m', uh, then m must be delivered
before m' at all receivers. If two message sends, m and m', are not causally related, meaning that their send events
do not have a causal path between them, then, well,
all bets are off, and, uh, it's not
necessarily required that their multicasts
be delivered in the same order. They can in fact be flipped
at different processes. Formally, uh, if a multicast
message m is sent to a group g, and the multicast send event
causally happens before, this is Lamport's happens-before relationship over here, shown by the horizontal arrow, if that causally happens before
the multicast send event of another message m',
a multicast message m', then any correct process
that delivers m' would already
have delivered m. In other words,
you deliver m first, and only then
can you deliver m'. So let's look at an example
again with our timeline of four processes P1 through P4. This is a slightly different set
of multicast messages from the earlier example
you saw. Here, process P1 sends out
a multicast message M1:1, uh, which is received by process
P2 along with other receivers, but then subsequently P2 sends
out a multicast message M2:1. Now, because the multicast
message M1:1 was received by P2 before it sent out
its multicast message M2:1, the send event of M1:1 happens before the send event of M2:1, and so we want those two multicasts to be received in the same order
at all the other processes in, uh, the system. Similarly, M1:1 is received
by P3 before P3 sends outs it- sends out
its first multicast M3:1, and so M1:1 happens before M3:1, and we wanna make sure that those two messages
are delivered in that causality-obeying
order at all the recipients. Of course, M3:1 happens
before M3:2 because, uh, causality implo-implies FIFO ordering, and so these messages M3:1
and M3:2 are also delivered in that same order
at all receivers, okay? So that-that obeys
FIFO ordering, and since M1:1
happens before M3:1, and transitively
M1:1 happens before M3:2, we want the delivery order
to be, uh, obeying that ordering which is M1:1 first,
then M3:1, and then M3:2. You can verify for yourself
that this ordering is in fact, uh, obeyed
by-at all the processes in this example. Now let's look at two messages
here: M2:1 sent by process P2, and M3:1 sent by process P3. There is no causal path in
between these two send events, so these two send events are
in fact, uh, concurrent events, and so their delivery, uh,
may be in different orders at different processes. So for instance, P1 delivers
M2:1 first, while P4 delivers M3:1 first, and only then M2:1. And this is fine; this obeys
causal-causal ordering, because concurrent send events
may be ordered in any, uh, order at different recipients. The only thing that you're
trying to guarantee here is that if two send events
are causally related, then they are in fact delivered in the causality-obeying-
obeying order at all recipients. So let's compare a little bit,
uh, the causal ordering that we just saw with the FIFO
ordering which we saw before. Causal ordering that is satisfied by multicast protocol implies that
that multicast protocol also satisfies FIFO ordering. Why is this true? Well, um, consider
a multicast protocol that satisfies causal ordering. If two multicasts,
M and M' are sent by the same-same
sender process P, and M was sent before M',
then, um, it's true that M happened before M',
because time progresses only linearly at, uh,
the sender process, uh, P, and so because
the multicast protocol already satisfies
causal ordering, it must be true that M
is delivered first, and only then is M' delivered. Okay, this means
that a multicast protocol that implements causal ordering will automatically obey
FIFO ordering. However, the reverse
is not true. If I give you
a multicast protocol that obeys FIFO ordering, it may not obey
causal ordering, because FIFO ordering
does not worry about, uh, multicast sends, uh-uh,
from different, uh, processes, even if they
are causally related. Why prefer causal
ordering at all? Uh, well, causal ordering
is pretty intuitive, and therefore it is actually used in several, uh,
scenarios, uh, whether multicast or not. For instance, you might have
a group of, uh, friends on a social network, one of the more popular social networks, choose your own. Uh, if a friend
sees your message m, say you post a message m, uh, and, uh, your friend then
posts a response, uh, comment m' to it, you want your other friends
to be seeing m, uh, before they see m'. If they see m' first
before they see m, then the comment doesn't necessarily make sense to them, because it is a-it is
in the context of the message m. Uh, so, uh, before-because m
happens before m', you want their delivery orders
at the other, uh, processes in the group-which in this case
are your other friends, uh, or rather
your common friends between you and
the posting other friend, uh, to see, um, m
first and only then m'. However, if, uh, two friends,
uh, post m" and n" concurrently, and these are
concurrent send events, then they can be seen
in any order, and that's still fine. A variety of systems implement, uh, this kind
of causal ordering. This includes social networks,
uh, bulletin boards, uh, including, uh, news groups
and, um, uh, posts on the news servers, uh, and comments on websites,
and so on and so forth. Finally we come
to our third flavor of ordering, which is total ordering. Total ordering is sometimes
called as atomic, uh, broadcast. Unlike FIFO and causal ordering, uh, the definition
of this total ordering doesn't necessarily pay
any attention to the order in which
multicasts are sent. What it is into-instead
trying to guarantee is that all the receivers receive all the
multicasts in the same order. Uh, notice that I'm not saying
anything about the order in which they are sent. All I am saying is
that if a correct process P delivers the message m- multicast message m, before another multicast
message m', independent of what
the senders did, then any other correct process in the system P', uh, that delivers m'
would already have delivered m. In other words, what we are
saying is that if any process, uh, delivers message m
before m', then every other correct
process in the group will also be, uh, delivering
message m before, uh, m'. So here is an example
of, uh, total ordering. Again, this is, uh,
the same example from before. Here, uh, we wanna make sure
that all the multicasts, uh, sent here, the four multicasts that are
sent in this particular run, are delivered in the same
order at all the processes. So for instance, at P1,
M1:1 is delivered first, then M2:1 is delivered, then M3:1 is delivered, and then M3:2 is delivered. Now we we need to make sure
that all the other processes deliver these four multicast
in exactly that order, so M1:1 first, then M2:1,
then M3:1, and then M3:2. Let's look at P2. P2 delivers M1:1 first, then
M2:1, then M3:1, and then M3:2. So far so good. Then, uh, P3 delivers
M1:1 first, then it needs to deliver M2:1, but, uh, M2:1
has not yet been received when M3:1 is being sent out, so the, uh, delivery
of M3:1 at P3 itself needs to wait until M2:1
is delivered, and then M3:1
can be delivered, and finally M3:2 is delivered. This delivery order at P3
obeys, uh, the total ordering. Finally, at P4,
M1:1 is delivered first, then M2:1 is delivered, then M3:1,
and finally M3:2 is delivered, and this satisfies
total ordering because all the other processes, ah, in-all the processes
in the group deliver their multicasts, ah, deliver all the
multicasts in the same order, uh, as all the other
processes in the group. Now this of course means just
that some processes like P3 may need to d-delay the delivery
of, uh, the multicast messages, perhaps even
at the sending process of that particular multicast. Okay, so those are
the three flavors we have seen. Uh, those are not the only
three flavors possible. Um, since FIFO and
causal ordering, uh, uh, look at this, uh,
the sending order, and total ordering looks
at the receiving order, they are orthogonal, and so we have the possibility
of hybrid protocols. You could have a FIFO total
hybrid, uh, protocol for multicast ordering, which satisfies both FIFO
ordering and total ordering. In other words, this protocol
would give you a total order for multicast messages
that obeys the, uh, FIFO ordering ordering
of multicast sends. A causal-total hybrid protocol
is also possible for multicast ordering, which obeys both, uh, causal
as well as total ordering. This means that you have
a total ordering of, uh, multicast messages which, uh, also obeys
the, uh, causality. Notice that causal-total
ordering would mean, uh, that um, even concurrent events, um, concurrent multicast sends, are in fact ordered the same way at all the processes
in the group, uh, but because
they are concurrent, we don't really care
which order it is. Any order is fine
as long as it's consistent. Uh, multicast sends that are
causally related are of course, uh, delivered
in the causality-obeying order at all the processes
in the group. Uh, so we have discussed
so far what the ordering mean, what the flavors are. Uh, in the next lecture
we'll discuss how to im- how to implement each
of these, uh, orderings.

## 07 - 2.2. Implementing Multicast Ordering 1

Slides: C3_Multicast_B_CSRAfinal.pdf

### Transcript

Hi there. So, uh, in, um, uh,
the next couple of lectures we'll be seeing how to implement the flavors
of multicast ordering which we saw
in, uh, the previous lecture. Uh, these flavors were FIFO,
causal and total ordering. In this lecture, uh, today we'll
see, uh, how to implement FIFO as well as, um, uh,
total ordering, and in the next lecture
we'll see, uh, causal ordering. So here's how
to implement FIFO ordering. Each receiver in the group maintains a per-sender
sequence number. These sequence numbers
are integers, uh, starting from zero. Uh, suppose we have N processes
in the group, P1 through PN. Uh, essentially, Pi,
which is the ith process, would maintain a vector of sequence numbers, uh, Pi[1...N]. Initially, all these,
um, elements in the vector are, uh, zeros. Uh, Pi[j], which is
the jth element in Pi's vector, is the latest sequence number
that Pi has received from the process Pj. If j=i, remember
that Pi will have, uh, its, uh, an, uh,
a sequence number for itself. This would be
the latest sequence number that Pi has sent out to the, uh, other processes
in the group. So, uh, what do you do? How do you update these vectors? So, um, uh, when you want
to, uh, uh, send a, uh, multicast message, uh, from a process Pj, uh, the first thing you do,
uh, at process Pj is that you set the jth element
of Pj's vector, uh, to be one more than itself, so you increment
the j's element, j-j's element-jth element
of P's vector. Uh, then you include, uh, this,
uh, jth element, the new Pj[j], in a multicast message
as the sequence number of that multicast message. You also say that of course Pj
is the center of this multicast. Now what does
the process, uh, Pi do when it receives
this multicast message from Pj? Uh, it looks at, uh, the sender,
which is Pj, it looks at the sequence number in the message, which, say, is S, uh,
it checks whether or not, uh, S is, uh, equal
to the jth, uh, element of Pi's, uh, sequence number
vector, plus 1, okay? Essentially it checks whether or
not, uh, the sequence number S being received from Pj
is the next sequence number that Pi expects
to receive from Pj. If so, then it can deliver, uh,
the, uh, multicast message to the application, and the m-and the application
can do whatever it wants with this particular
multicast message, and then it can-it can set,
uh, the jth element of its own, uh, vector, uh,
to be, uh, 1 plus its old value. However, if this condition
is not true, uh, if this is not, uh, the next, uh, element
in the vector, uh, then it buffers
this multicast, uh, message. Now it buffers it,
essentially we are assuming here that, uh, the sequence number is going to be
later on, um, in the series. So for instance,
if the next sequence number that Pi is expecting
from Pj is 5, and it receives, uh,
the sequence number um-uh-uh, 7 then it needs to wait until, uh, 5 has been received and delivered, and then 6 has been received
and delivered, and only then can it deliver 7. However, if duplication
is possible in the network, for instance, if the next,
um-uh, message that Pi is waiting from, uh, Pj should have a sequence number 5, but you receive, uh, um, uh,
a multicast from Pj with the sequence number 3, then you can drop
that multicast message, uh, and, uh, safely,
because you already know that you have delivered
that to the application. Okay, uh, let's look
at an example of, uh, how the
FIFO ordering algorithm works. So here are four processes
P1 through P4. Time moves from left to right
for each of the processes. Each process maintains a vector. The number of elements
in the vector is 4 because there are four processes in the system. Remember that the jth element
at, say, process P1 corresponds to how many
multicasts P1 has received so far from, uh, Pj. So here are all the multicasts
that are sent out in the group. P1 sends two multicasts, uh,
one followed by another, and then P3 later on
sends another multicast. So let's see what happens with
the first multicast from P1. P1's sequence number, uh,
for this first multicast is 1 because it's sent
no multicasts so far. P1's first element
of its vector is 0. That's incremented to 1, and that, uh, new value
is assigned as a sequence number to the multicast message. When P2 receives
this multicast message, it checks its first element
of the vector, which is zero, and so in fact
the sequence number is the next sequence
number it's expecting, and the multicast is delivered, and the vector-
the vector is updated to be 1 followed by three 0. The same is true at, uh, P4, which also delivers
a multicast message and updates its vector to be one
followed by three zeros. Uh, however, when P1's multicast
is, uh, received at P3, P1's second multicast
has already been received, and if P3 delivered
these multicasts in this order
shown in the slide, then you would violate
FIFO ordering, because, uh, P1's two multicasts are delivered
in the wrong order at P3. So let's see what happens with
the second multicast from P1. When it's sent out it has
a sequence number of 2, because P1's first element
is already one. That's incremented to be two, and that is included
as sequence number. When this multicast is received
at, uh, P3 early, uh, it sees-P3 sees
that P1-its element for P1 is in fact 0, and the next
sequence number it is expecting is, uh, 1, and so
the sequence number 2 message that has just been received
needs to be buffered. However, later on at some point
of time soon after, uh, P3 receives
a first multicast from P1. This is in fact the next
sequence number it is expecting. It then delivers this second
multicast message immediately, and then after this, the sequence number that it's
expecting from P1 is now 2, because P3
has updated its vector to be one followed
by three zeros. And at this point immediately
the sequence number 2 message from P1 can be delivered
right away. After P1's sequence
number 1 message, the vector can be updated to be 2 followed by three 0, and we have satisfied
FIFO ordering. When, uh, P2 receives P1's
multicast, second multicast, delivers it because that's the next sequence
number 2 is expecting, then, uh, P3 sends out
its multicast message. This is a sequence number of 1 because P3 has not sent
any multicasts yet. P3's third element,
uh, is in fact 0. That's incremented to 1,
and that is included as a sequence number
in the multicast message. P1 and P2, when they receive
this multicast message from P3, they check that their third
elements of the vector are 0, and so the sequence number 1
is in fact what they're expecting from P3, and they deliver
the multicast message and update
their vectors accordingly. However, P4, when it receives
this, what does it do? Well, when P4 receives
the multicast message from P3, first it can deliver it, because it's the next sequence
number it's expecting from P3, and that's fine, and then later on it, uh, receives the sequence num- the sequence number 2 message
from P1, and it can deliver it right away and update its vector
to be 2,0,1,0. This is fine;
this satisfies FIFO ordering, even though the P3 sequence number 1 message was delivered first at P4 before P1's sequence
number 2 message, while this ordering of
deliveries was reversed in P3. But this is fine, because FIFO
doesn't necessarily look at the order-ordering
of messages sent by different
sending processes. So that was, uh, FIFO. Next, uh, we'll look
at total ordering and how to implement it. Once again, just to remind you,
total ordering ensures that, uh, uh, the, um, ordering
of deliveries of messages at all the processes
are the same, uh, somewhat independent
of what order they were sent in. So a-a popular approach
to implement total ordering is to use sequencer- uh,
is to use a sequencer. Uh, a special process is elected
as a leader or a sequencer. Uh, you will, uh, have seen
leader election elsewhere in this course, um, and essentially in order
to send a multicast message, there's what
the process Pi does. It simply sends a multicast
message M to the group, along, uh, with sending it
to the sequencer as well. The sequencer in turn maintains
a global sequence number S, which initially
has a value of 0. When the sequencer receives
the multicast message M from any process, it increments S and
then it multicasts M along with the
sequence number S. Okay, and this is multicast
to the entire group again. What does the process Pi do when
it receives a multicast message? Well Pi maintains a local received global
sequence number, Si, okay? This is only one integer, not
a vector, just a single integer. This, um-uh, represents
the next, uh, globally ordered or totally ordered multicast
that Pi is expecting to receive. If Pi receives a multicast M,
uh, message M from Pj, it buffers that
multicast message M until it receives
the sequence number message for that same message M
from the sequencer, so until it receives, um, a message
from the sequencer that says "Hey, for the multicast
message M, the sequencer i -the sequence number is S(M)," and, um, but
receiving this mult-this, uh, sequencer message
doesn't necessarily entail that the multicast
can be delivered right away. The sequence numbers
have to match up. In other words, it has to wait
until the S(M) value in, uh, the message from the sequencer
is one more than, uh, the global sequence number Si that Pi is waiting for, okay? So this ensures that in fact,
uh, the multicast message, uh, that Pi delivers next
is in fact the next one that Pi is waiting for. Once it, uh, once this is true,
it can then deliver the message, this multicast,
to the application, and then it can increment Si,
and then at this point of time, if any buffered messages,
uh, satisfy, uh, these two conditions here, then in fact they
can be delivered as well, and Si can be incremented. So next, uh, lecture we'll see
how to implement, uh, causal ordering for multicasts.

## 08 - 2.3. Implementing Multicast Ordering 2

Slides: C3_Multicast_C_CSRAfinal.pdf

### Transcript

In this lecture
we continue our discussion of how to implement
multicast ordering. Uh, in this lecture
we'll look at how to implement,
uh, causal ordering. Once again, just to remind you,
causal ordering ensures, uh, that if two multicasts are such that their, uh, send events are causally related, meaning that there
is a causal path between them, then, uh,
the, uh, received order of uh, those multicast messages, uh, should obey causality. In other words, if the
multicast send of a message M happened before multicast
message of a message- multicast send of a message M', then M should
be delivered first, and only then M' at all correct
processes in the system. So, uh, here's how
to implement causal ordering. Uh, each receiver, again,
maintains a vector of per-sender sequence numbers. Uh, these are integers. This is sort of like FIFO
multicast, uh, but the meanings of, uh, the, uh, um,
sequence numbers are different, and updating rules
are slightly different. Once again we have
processes P1 through PN. Uh, Pi maintains a vector, eh,
of N elements, uh, Pi[1...N]. Initially, all the elements
in the vector are zeroes. The jth element of Pi's vector
is the latest sequence number that Pi has received from Pj. This is very similar, again, to the FIFO example you have
seen in the previous lecture, but again, the interpretations and the updating rules
are going to be different. So here are the rules,
in all their gory detail, and then we'll see an example
that discusses these rules. So when you want
to send a multicast message, uh, at process Pj, uh, Pj looks at the jth element
of its vector and increments it by one, then it sends out
the multicast message. However, unlike FIFO
it includes the entire vector in the multicast message
as a sequence number. The entire vector is important
because we want to check for causality. We wanna make sure that
all the receivers are in fact obeying causality. So what do receivers do when they receive
a multicast message? When Pi receives
a multicast message from Pj, and there is a vector M
in, uh, the multicast message, which is the timestamp
of that multicast message itself then, uh, you buffer
that multicast message until two conditions are true. First, this is the next
multicast message that Pi is expecting from Pj. In other words, the jth element
of the message's vector is in fact one more than
the jth element of Pi's vector. So that's the first condition. Second, you wanna make sure that the receiver
satisfies causality. All the multicasts
anywhere in the group which happen
before this message M have already been received
at Pi, okay? In other words, you want
to make sure that for all k, uh, not equal, uh,
to j, the sender, the kth element
of the message's vector is less than or equal
to the kth element of the receiver
Pi's vector, okay? This makes sure that
the receiver has already seen all the multicast messages
on which Pi already depended, or in other words, all the multicast
messages that happen before M's. When these two conditions
are true, then you can deliver the multicast message M
to the application, and you can set the jth element of Pi's vector to the jth element
of M's vector, showing that this message
has been delivered. You do not update any
of the other elements of the-of the- of Pi's vector, because you
don't necessarily know of the other multicast messages that have been sent out in the group. So let's see an example again. Here is a timeline with four
processes, P1 through P4. Time runs from left to right. Each process maintains a vector. The vector contains
four elements, because there are four processes in the group. P1 sends out a multicast,
uh, which is received by all the other processes. Notice that P2 receives
P1's multicast first and then sends out
another multicast. So P1's multicast
here happens before; causally happens
before P2's multicast, and so we want to make sure
that these two multicasts are delivered in the same order
at all the recipients. Similarly, P1's multicast
is received at its P4, at P4, and then P4 sends out
a multicast, so again, these two multicast sends from
P1 and P4 are causally related. However, P2's multicast send
and P4's multicast send are concurrent, and so they
are not causally related. So let's look at the vectors. So P1 then sends out
a multicast, simply increments
its sequence number, which is
the first sequence number, and that entire vector 1
followed by three 0 is included as the sequence nu- as the timestamp of
the message when it is sent out. When receivers receive
this multicast message, they use this to check whether
or not to deliver the message. P2, when it receives
this message, in fact checks that this is
in fact the next, uh, vector is-it is expecting from P1, and it in fact
satisfies causality because all the vectors, all the elements, all
the other elements are 0, and so it can deliver
this multicast message from P1. P4, uh, the rule is likewise,
and can- it goes ahead and delivers P1's
multicast message. Now, when P2 sends out
its multicast, it increments the second element of its vector, so the vector
for uh, the time stamped vector for this multicast message
from P2 is 1,1,0,0. When P1 receives
this multicast message from P2, it sees that in fact this is the next sequence
number it is expecting from P2, and that the receiver
satisfies causality because all the other elements are identical to the incoming message, and so it can deliver
this multicast from P2. However, when P3 receives
this message from P2, it sees that the first element
in the incoming vector is one. However, the first element
in its local vector is 0. In other words, P3 has not yet
gone beyond the causality and has not yet received
some messages on which P2's send
is dependent upon. So because it is missing
the sequence number one from P1 uh, it buffers
this multicast message from P2. Subsequently, P4 sends out
the multicast message, which now has vector, uh,
timestamp of 1,0,0,1. P1 and P2 both
receive this message, and they are able to deliver it because the receiver
satisfies causality. You can verify
this for yourself. However, when P3 receives
this multicast message, it sees that it is missing, again uh, the message 1 from P1 which is included in
the incoming multicast from P4 because P4's first element is 1. However, P3's first element
is a 0, and so it buffers
this multicast from P4 as well. Uh, thereafter,
when P1's multicast is finally received at P3, it sees that this is in fact the next multicast message
that it needs to deliver, because causality is true, and so it updates its timestamp to be 1 followed by three 0, and at this point it can deliver
both P4's buffered multicast as well as
P2's buffered multicast. It can deliver these two
multicasts in any order, because these are, uh,
not causally dependent on each other, otherwise
the vectors would show it, and so it goes ahead
and delivers this, and it updates its, uh,
vector to be, uh, [1,1,0,1]. And finally of course P4
receives the multicast from P2 and it can go ahead and
deliver this multicast message and update its final vector
to be 1, 1 and, ah, 0 and 1. So, uh, that wraps up
our discussion of multicast ordering. Uh, the ordering
of multicast is important because it affects correctness of distributed systems that use multicast
as a building block. On the stock exchange floor, uh, you want to make sure that all the stockbrokers are receiving, uh, the stock trades in the same order as everyone else. Uh, this ensures fairness
in the marketplace. Uh, in, uh,
the air traffic control system, you want to make sure that all the, uh,
air traffic controllers' are seeing the updates
in the same order as all the other
air traffic controllers. This ensures correctness
and safety of the airplanes. There are three popular ways
of implementing ordering. Uh, these are, uh, FIFO,
or first-in, first-out, causal, and total ordering. We have seen what these mean. We have also seen how
to implement them. What we have not seen
so far is reliability and, uh, fault tolerance. What happens when, uh, some of
the processes in the group fail? How do we ensure that all the
correct processes in the group still continue
receiving multicasts? We'll see this in the next two
lectures, uh, in this series.

## 09 - 2.4. Reliable Multicast

Slides: C3_Multicast_D_CSRAfinal.pdf

### Transcript

In this lecture and the next we'll look
at reliable multicast. So what is reliability? Uh, a multicast protocol that
is reliable, uh, loosely means that every process in the group
receives all the multicasts. Now, reliability is orthogonal
to ordering that we have seen, um, uh, so far, which means that you can implement a reliable multicast that is FIFO ordered, or you can implement
a reliable multicast that is causal ordered, or you can implement
a reliable multicast protocol that is total ordered, or a reliable hybrid, uh,
ordering protocol as well. Okay, so reliability, what we are discussing
is completely orthogonal to, uh, the ordering,
uh, that you have seen earlier in this lecture series. So coming back
to the definition, uh, reliable multicast loosely says that all the processes in the group receive multicasts. However, when you have
process failures, you don't necessarily know
what the failed or the faulty processes uh, did, so the definition becomes
a little bit vague. So we need
to spruce up the definition. We need all
the correct processes, meaning all the non-faulty process in the group, to receive
the same set of multicasts as all the other
processes, okay? So faulty processes are, uh, not
necessarily, uh, predictable, and we don't necessarily know
what happened to them, so we won't worry about them. We were seeing is that
in a single run of the system, uh, at the end of the run when you have a small set
of correct processes, uh, which are-which
did not fail, uh, the set of multicasts received at any one of those processes in that small set is the same as the set
of multicasts received at any other process
in that same set. So, uh, essentially,
reliable multicast sends that- says that all the multicasts
that are sent to the group are either received
at, um, all the processes that are correct or none of
the processes that are correct. That's what reliability
really means. Uh, so let's, uh, see how to
implement reliable multicasts. Let's assume
that underneath we have as a, um, uh, building block
a reliable unicast protocol such as, say, TCP, which allows
us to send point-to-point or process-to-process messages
in a reliable, uh, way, uh,
that is also, say, ordered. It-the ordering is really
not important to us. All that is important to us is that when we send a unicast message from one process to a single recipient process,
it is delivered. So the first-cut way to
implement the reliable multicast is the following. Uh, the sender of the multicast
process runs in a For-loop where it, uh, goes through, uh, all the addresses of the other, uh, processes
in the group, and to each process it sends
a reliable unicast message, uh, that contains
a multicast message. Well, this, uh, works as long
as the sender is alive. Uhm, uh, if the sender
is alive, in fact, uh, all the correct processes will receive
that multicast message. However, if the sender dies
halfway through the For-loop, then you are in trouble because, uh, some correct processes
in the system would have received
the multicast message M, but the others that, uh,
were not touched by the For loop before the sender's failure, uh, would not have received
the same multicast message M. And, so this is not really
a-a multicast protocol that satisfies reliability,
so we eliminate this. So how do you really implement
reliable multicast protocol? Well, you can implement- you can ex- you can extend the,
uh, exa-the protocol that you saw
in the previous slide, and, um, uh, make it reliable. How do you do this? Well, you do this by having the receivers
also help the sender process. Uh, once again, in this,
uh, new multicast protocol that is reliable, the sender process
sequentially through a for loop sends a reliable unicast, uh, to each
of the group, uh, processes. However, when a receiver
receives a multicast message M for the first time, it, uh,
also, uh, uh, goes through a for loop where it sends out
the multicast message M to all other processes
in the group. In other words, if for instance
if all the, uh, processes in the group are non-faulty, then you end up with N copies
of the multicast being sent, one by each of the processes
in the group. Of course this could
be fairly inefficient. This is not
the most efficient protocol, but it is-it is reliable. Uh, it says that, uh, if at least one correct process receives a multicast message M, then every other correct process will also have received that same multicast message M. The proof of this
is by contradiction. Suppose we have
two correct processes Pi and Pj. These are the two processes
in the small set that are, uh, non-faulty
at the end of the, uh, run. Uh, and, uh, say a multicast
message M was sent to the group and Pi received M but Pj
did not receive M, right? This is the contradiction
which says that this protocol does not, uh,
guarantee reliability. Well, then when Pi received
the multicast message M the first time, it would have,
uh, gone through a for loop, and because Pi did not fail, the for loop
would have touched, uh, Pj, and Pi would have directly sent
a reliable unicast message to Pj and Pj would have received
the multicast message M, okay? This means
that we have a contradiction which means
that our assumption is not true, and so, uh, the, uh,
opposite must be true, which is that,
uh, any correct- any pair of correct processes would have received the same set of multicast, uh,
messages, um, M. Okay, so this just shows
that our extended protocol, though slightly
inefficient, wasteful, still does, uh, preserve reliability in, uh, the system. Now of course there is a variety
of other protocols that are- that have been invented, uh, since this early
classical protocol that are reliable
and far more efficient. In the next lecture we'll see
how to combine fault-tolerance as well as, uh,
multicast, uh, reliability.

## 10 - 2.5. Virtual Synchrony

Slides: C3_Multicast_E_CSRAfinal.pdf

### Transcript

[MUSIC] So in this lecture we're going to look at
how to combine a membership protocol or failure introduction
along with a Multicast. This is often and very popularly implemented in
an abstraction known as virtual synchrony. Virtual synchrony also known as view
synchrony attempts to preserve multicast ordering and reliability in spite of
failures of what happened in the system. It combines a membership protocol
with a multicast protocol. Systems that implemented
virtual synchrony or view synchrony, such as Isis from
Cornell University have been used in many important scenarios including
the New York Stock Exchange, the French Air Traffic Control System,
and the Swiss Stock Exchange. Virtual synchrony or view synchrony has
an important concept known as Views. Each process maintains
a membership list and you've seen how membership protocols
work earlier in the course. This membership list is called a View. An update to the membership
list is called a View Change. For instance, if a process joins,
this may be reflected in the view and that would be a View Change. If a process leaves or a process fails then those would
be reflected in the view as well. That would be a View Change. Multiple changes may be made to a view and
that would just count as a single View Change if
those changes are made simultaneously. So for instance. A process P1 might be
added to the view and simultaneously process P2
might be drop from the view. That would just be a single view change
where both those updates were done simultaneously. Virtual synchrony or views synchrony
guarantees that all the view changes are delivered in the same order at
all the correct processes in the group. So for instance if a correct
process P1 receives views, which are somewhat like the following. The first view has only itself, P1. The second view has itself along
with two other processes, P1, P3. The next view only has P1 or
P2, P3 was dropped. And the next view has P1,
P2 and P4, where P4 was added. Then any of the correct process also
received the same sequence of view changes after it joins the group. So, for instance, if you construct P2 and
the views it receives, P2's first view would be P1, P2, P3,
because that's when it joins the group. But after that,
its next view would be P1, P2. It would have to be the same
as the next view that P1 got. And then the third view that P2
reviews would also be the same as P1's next view which will be P1,
P2, P4 over here. That is the same as P1's,
our next view as well. In other words, as long as you can see
only the correct process in the group of the sequence of view changes
that they receive is in fact the same as all the other
current processes in the group. When the process fails,
then you stop considering it. But as long as the process is alive,
all the views that it receives are in fact in the same order as
the other correct process in the system. Now the times at which the views
are delivered at the processes might be different at different process,
but the ordering is the same. So again, here the insistence is on
the ordering of them being the same. In other words, the views being totally
audited in all of the processes, but they may of course be delivered
at different physical times. And this is why it is somewhat
known as virtual synchrony, but we'll come back to the name later on. So that's about abuse. What about the multicasts that are sent
out among the processes in the group? Now a multicast M is said to be delivered
in a view V at a process Pi If and only if Pi receives the view V. And then before Pi delivers the next
view after V, it delivers multicast M. because in other words multicast M
is delivered in between view V and the next view that follows V. Then M is said to be
delivered in the view V. In other words, what we are saying
is that when M is delivered view V was the membership
list at the process Pi. Now multisynchronicity requires that
the set of multicasts delivered in a given view is the same set of multicasts
at all the correct processes that are in that view. This says that suppose
the view consists of to P3 then the set of multicasts
received at P1 in that same view is the same the set of multicasts
received P2 in the same view. In other words,
what happens in a view stays in that view. It does not go outside that view. Okay, this is a good rule of thumb
to remember virtual synchrony by. He also required the sender of
the mutlicast message to believe to that view otherwise it would make sense for
a multicast to be received. Within a view when the sender is
not a part of the view itself. And what this means is that, if a process
Pi does not deliver a multicast M in view V, while other processes in the view V
delivered multicast M in that same view, V, then Pi will be forcibly removed
from the next view delivered. After we've add these other processes. So, yo have to go with what he rest of
the group is doing otherwise you might be forcibly removed from that group
if you don't satisfy group. So, let's see a few examples that are both
correct from the and also incorrect form the viewpoint of So here's our first
example with process P1, P2, P3, and P4. The first view that all of them deliver
consists of all four processes, so that's our group. Then P1 sends out a multicast message M1,
P2 sends out a multicast message M2, P4 sends out a multicast message M3,
but P4 crashes after that. Because P4 crashes, the next view that is
delivered at P1, P2, P3, the remaining members in the group Consists of only P1,
P2, P3, and that's fine, okay? Now the message M1 is
delivered in the first view, which causes all the four processes. M2 is also delivered in the first view. M2 is not delivered in P4, but
that's fine because P4 crashed anyway. Now the message M3 from P4 is also
delivered at P1, P2, P3 as well as P4 and it is delivered in the same view that
consists of all the four processes. Okay, so satisfies virtual synchrony. This particular run over here. However if I make a small change which
is that a P3 delivers the second view first and only then delivers
the multicast n one from p one. This would not satisfy virtual synchrony
because what happens in the view does not stay in the view. In other words m1 is delivered
by p2 in the earlier view but delivered at p3 in the second view. And that does not satisfy
virtual synchrony. This satisfies virtual synchrony,
where P3 is forced out of the group, and only P1 and P2 are left in the group. And the set of multicast
messages of P1 and P2 received in the old
first view are identical. Okay, this satisfies virtual synchrony. Here's another example of a route that
does not satisfy virtual synchrony. Why does it not satisfy virtual synchrony? Well Notice here that we have the modech as message m2 that is received at process
p1 but is not received at process p3. But p3 was is a part of the next view so in other words this is a multi
pass message m that is not completely reliably delivered inside
the group inside the old view. Okay so
this does not satisfy virtual synchrony. This satisfies virtual synchrony here
because M2 is in fact not delivered at any of the members in
the group in the old view. It's not delivered at P2 either, and this
has virtual synchrony because essentially M2 as a multicast was never sent out,
so never delivered at all in the group. Does not satisfy what you need here you
notice that the multi-cache text message, m1 and m2 willing to the correct view,
and the older view in all across but m3 is delivered in the next view
at process v1 and process v2. And it's delivered in all view process p3, because this does not
satisfy virtual synchrony. You might think that moving this view
ahead now satisfied both virtual synchrony because [INAUDIBLE] at all the other
processes in the system and all the current processes but this [INAUDIBLE] because by the time
the semantic [INAUDIBLE] is delivered. The view does not include the sender p 4
of that multicast message anymore, and so because p 4 is not part of the second
view delivered at the correct processes, the run that I'm showing here is also not correct as far as virtual
synchrony is concerned. And finally here is an example
where dropped by the system and it's not able to tolerate any of
the processes of the group and this satisfies of course virtual
synchrony because what happens in the view stays in the view and
before it has crashed. So, virtual synchrony or virtual
synchronous systems implement membership protocols in the form of views, and also
multicasts in terms of reliability, and they want to ensure
reliability within each view. If you want to implement ordering in a
virtual synchronous system you can do that too because ordering is
orthogonal to reliability, so you can have a Virtually synchronous
system that implements FIFO. Or a virtually synchronous system
that implements causal ordering, or one that implements total ordering, or
one that has a hybrid ordering scheme. Now the name virtual synchrony comes
about, or came about because it's part of running on top of an asynchronous network
with unpredictable delays and failures. The order of membership changes and multicasts that each process sees is
the same at all the other processes. If you use a total ordering protocol, even
if it's a hybrid total ordering protocol, then all the processes see
the event in the system happening in the same order as all
the other processes in the system as long as the processes that you're
talking about are the correct processes. Okay, so instead of landing
on top of an asynchronous network the view the processes behave
are able to behave as if they're running on top of a synchronous system
where all the membership changes and all the multi-cast messages
are delivered in the same order. But then actually the question should
arise whether or not such an abstraction could be used to implement a protocol
that solves the consensus problem. And the answer to this is no because
virtually synchronous systems are still susceptible to what is
known as partitioning. This may happen due to inaccurate failure
detections because a process may be mistakenly detected they will
be removed from the group Also processes may be
forcibly removed from groups. So an example of partitioning is
shown on this slide, where initially, all the four processes, P1, P2,
P3, and P4 are a part of the view. But subsequently, even though P4 is the
only one that crashes, the view has become partitioned where P1 considers only
itself to be a part of the view. And P2 and P3 are different view which
consider only themselves to be a part of the membership list. So P1 is partitioned away from P23, and
such partitions can happen in a virtually synchronous system and this is the feature
that prevents socially synchronous or view synchronous systems from
implementing consensus on top of them. So, that wraps of our
discussion of Multicast. Multicast is an important building block
for cloud computing systems that has been so far many use to it systems for
many decades. Depending on the application need, you can implement either
a flavor of Multicast Ordering. As far as your application
requires level Multicast Ordering. If you don't care about
efficiency then you can implement the Multicast Ordering Reliability. Protocol that we saw or
there are other radians of multicache library protocols that we
have discussed as well in this course. And if you need something really, really strong then you can implement
virtual synchrony or real synchrony. In fact there are many real systems out
there that use these forms of multicast in terms of their ordering that are and
even a devotedly synchronize of framework. [MUSIC]

## 11 - 3.1. The Consensus Problem

Slides: C3_Paxos_A_CSRAfinal.pdf

### Transcript

In this next series of lectures, uh, we'll see, uh,
the consensus problem, which is one of the most important distributed
computing problems. Uh, we'll see what
the problem is, uh, we'll see why it is,
um, hard to solve, and then we'll, uh, try to see
a few solutions, uh, uh, to it. So, uh, you might have seen that
a lot of wendors, uh, publish, uh, their, uh, solutions, their software, their products, their services as having
several 9's of reliability. Some vendors might say we
have five-9's of reliability. Essentially this means that, uh, their service is available 99.999% of the time. Uh, seven 9's would have
seven 9's in there. but none of the vendors ever, uh, promise 100% reliable services or products. This is not because, uh,
of the fallibility of, uh, of hu-of human beings or, uh, the fact that today's
companies are not good enough. Uh, the-the main reason for this is that a lot of these services, especially the
distributed services, uh, need to solve a problem known as consensus, and it turns out that consensus is impossible to solve under certain, uh, system models and under certain situations. Uh, so we'll see in this lecture
series what exactly consensus is and why is this, uh,
impossibility even there, and how we can get around it. So here are a set of problems that, uh, many, uh, distributed computing, um, scenarios need to tackle, many cloud computing environments need to tackle. The first is a group of servers
that are trying to make sure that all of them receive the same updates in the same order as each other. Uh, these might be the servers
in a storage system that are receiving rights,
uh, from a set of clients and they want to make sure
that all these, uh, rights are reliably received
by all the servers and they are also
received in the same order. Um, a group of servers that is
trying to, uh, keep local lists, uh, membership lists
that know about each other, and when any one, any of the servers leaves
the group or fails from the group, uh, all the, uh, membership lists are updated simultaneously. A third scenario is, uh,
one where a group of servers wants to elect
a leader among them and then let everyone else
in the group know who the leader is. And finally, the fourth scenario
is one where all these servers want to, uh, obtain mutually
exclusive access to a resource, so when one of the servers
is accessing the resource, none of the others are able to access
the resource at the same time. Think of this as locking. So these are four, uh, classic
and very import- classical and very
important problems in distributed, uh, systems, um,
and they have names. The first one is called
Reliable, uh, Multicasts, uh, the second is called Membership
or Failure Detection, the third
is called Leader Election, and the fourth
is called Mutual Exclusion. Um, you would have seen or you
will see each of these problems elsewhere in this
particular course, but for now what
is relevant to us is that all of these problems
are directly related to the consensus problem. So what really is common
among these problems? Well let's just call each
server a process, okay? So think of the daemon
that is running, uh, at each of these servers, and so, uh, when I
say a group of processes, I essentially mean
a group of processes communicating over a network. These processes
might be anywhere; they might be on a few servers, they might be on a large number
of, uh, servers. Uh, all these examples that we
saw, uh, just now were examples of groups of process attempting
to coordinate with each other and reach agreement
about something, um, either the ordering
or the reliability of messages, or the up/down status
of a suspected fail process in a failure detector example, or who the leader is
in the leader election example, or who has access
to the critical resource in the mutual exclusion example. So all of these are related
to the consensus problem, which essentially tries to have
a group of servers coordinate with each other and agree
on the value of something. So what really is consensus? Formally, uh, we
have N processes. Um, each process p
has two variables. These variables only have
bit values, um, so, uh, the input variable called xp
is initially either 0 or 1. This is the processes-that
particular process's piece, um, uh, contribution or
proposal, uh, for the group. And each process p also
has an output variable, uh, called as yp, which is initially,
um, undecided, or what is known as just b,
it's undecided. And, uh, the concern
it is that p can change, uh, the output variable
at most once. Once it is changed, once it is
set to either 0 or 1, it can't be changed afterwards. So the problem that we have,
the consensus problem, is to design
a distributed protocol so that at the end
of that protocol, um, uh, all the processes decide the same value
for their output variables. So either all the processes set
their output variables to be 0's, so you have
an all-0's outcome, or all the processes set
their output variables to be 1, so you have an all-1's outcome. So why is this problem so,
uh, challenging at all? Well, uh,
before we go into that, a little bit of, um, summary, or a different way
of putting the same problem, so every process
contributes a value, and the goal is to have
all the processes deciding, uh, the same value, whatever
value it is, either 0 or 1, uh, but once a process
makes a decision, it cannot change that decision. And the reason
for this is typically because the decision
is communicated up to the application, and the application might
take certain actions based on that decision. Now in addition to the, uh,
main requirements for consensus that we saw
in the previous slide, in practice there might be
a few other constraints. Uh, they are validity,
integrity and non-triviality. Validity says that if everyone
in the group, all the processes, propose the same value, say all
of them propose 0, then, um, the group should decide it is 0. Alternately, if all
the processes propose a 1, then the group should
decide a 1. Integrity, the second
condition, says that, um, the decided value must have been proposed by some process, uh, and this is of course related to, uh, validity. Um-uh, some process
must have proposed a 0 value for it to be decided
by the entire group. Non-triviality says that there is at least one
initial system state that leads to, uh,
an all-0's outcome, and at least one initial state that leads
to an all-1's outcome. Uh, if you didn't have this
non-triviality condition, then essentially you could solve
consensus by saying "Hey, everyone just set
your output variables to be 0 "and we are done
because we have consensus," but then that would mean that you always decide 0
all the time, and that's not really
a practical or useful distributed protocol. You want to decide 0 or 1, uh, depending on what's going
on in the group. So, uh, the consensus problem
is important, uh, because, uh,
several important, uh, distributed computing problems are, uh, related to it. They are either
equivalent to consensus, which means that, um, they are in fact the same problem, if you can solve consensus, you can solve
the other problem, and if you can solve
the other problem you can solve consensus. Or in some cases, uh, the distributed computing problems are harder than, uh, consensus. So failure detection, which, uh,
we have discussed, uh, earlier, uh, is related to consensus in the sense that it
is equivalent to consensus. So perfect failure detection, uh, that, uh, always detects
failures, uh, all the time and never makes any mistakes
about detections is, uh, equivalent to consensus, which means that if you had
a protocol to solve consensus, you could design
a perfect failure detector and vicey versa. Leader election, um, where
you want to elect a leader and want-want to, uh, have everyone
in the group know about it is also, um, equivalent
to consensus. Agreement where you want to decide on not just a bit value but, um, maybe an integer value, um, or something more complex is actually harder than consensus. Uh, if you had
a solution to agreement, you would be able
to solve consensus. So before, um, uh,
we solve consensus, uh, we need to ask what
is the system model under which the consensus
problem is being solved. Uh, this is a practice that I would
like you to develop whenever someone gives you
a problem statement. The first thing
you should figure out is what are the assumptions
or what is the system model under which we are trying
to solve the problem. So there are two more, uh, most
popular, um, uh, system models in distributed systems;
the synchronous system model and the asynchronous, uh,
distributed system model. Let's look at each of these. The synchronous distributed
system model, the one, uh, without the "a," um, has bounds on everything. It has a bound
on how long a message takes to be delivered
at a recipient process. As long as the sender
and recipient, uh, processes are alive, the message will be delivered
within that bounded time, and that bound is a global bound across the entire
distributed system. The second is that processes, uh, local clocks do not drift away from each other too much. Uh, there is an upper bound on the drift rate between
any two processes' clocks. The third is that, uh, each process has a minimum speed
and also a maximum speed at which
it executes instructions. Uh, in other words,
each step in a process takes a time that is lower bounded by a well-known value, and is also upper-bounded
by a well-known value. Uh, examples of synchronous
distributed systems are collections of processors that,
uh, share a communication bus and are on the same
motherboard-for instance, a multiprocessor system,
one that you might buy, uh, from a well-known company, uh,
one of these computers today. Uh, or even a supercomputer,
uh, machine, um, is an example of the
synchronous distributed system. The asynchronous distributed
system model, on the other hand, does not have any
bounds on anything. It does not have bounds on how
fast or slow processes are. Processes might be
arbitrarily fast; they might be arbitrarily slow. A process might execute
an instruction, um, every nanosecond, and another process
might execute an instruction every 3 years or
every million years. You don't know how
slow processes are. Uh, processes' clocks can drift
away from each other arbitrarily fast or slow, uh,
and also a message might take arbitrarily long, uh,
to reach its recipient. A message that you send
might be delivered within the next nanosecond
or picosecond, or it might, uh, take forever to be delivered
at, uh, the recipient process. And the asynchronous
distributed system model is an interesting model because a lot of the very
widely-used distributed systems, um, uh, adhere to this. So the internet is an example of an asynchronous
distributed system, as are wireless ad-hoc
networks and sensor networks. Obviously, the asynchronous
distributed system model is more challenging in, uh, in terms of a model
in which to solve problems, compared to the
synchronous system model, because there are
no bounds on anything. And so if you
are able to solve a problem in the asynchronous
distributed system model, you can be sure
that it will also work, the same protocol will also work in the synchronous
distributed system model. However, the reverse
is not true. If you, uh, solve a problem in the synchronous
distributed system model with the well-known bounds, it doesn't mean, uh, that, uh, the same
protocol will work in the asynchronous distributed system model as well. This is why a lot
of the distributed systems and cloud computing
literature focuses on the asynchronous
s-system model where there are
no bounds on anything. So in the synchronous system
model, the consensus problem, which we discussed,
is in fact solvable, and we'll see a solution to that, um,
in this lecture series. In the asynchronous distributed
system model, however, consensus is
impossible to solve. And what this means is that, uh, whatever protocol
or algorithm you suggest which claims to solve consensus, there is always a worst-case possible execution scenario where some processes fail and, uh, some messages are
delayed just the wrong amount that will always prevent the
system from reaching consensus where everyone decides
the same value. This is of course a very
powerful impossibility result. Um, this is sort of like
the Np completeness,um, uh, uh, equivalent, uh,
in distributed systems, um, and, uh, for those
of you who are interested, there is an optional optional lecture in this series which will cover,
uh, the FLP proof that pr-that shows that, uh,
the, uh, consensus problem is impossible to solve
in asynchronous systems. Subsequently, several safe
and probabilistic solutions have become quite popular. This includes
a solution of Paxos, which you'll also see later
in this lecture series. So in the next lecture we'll,
um, just try to solve consensus. We'll see, uh,
how do you solve consensus in the synchronous system model.

## 12 - 3.2. Consensus In Synchronous Systems

Slides: C3_Paxos_B_CSRAfinal.pdf

### Transcript

So in this, uh, lecture today we'll see, uh, how to solve
the consensus problem in the synchronous system model. Uh, once again, if someone
gives you a problem, uh, always remember to make sure you know what the system model is, what are the assumptions
under which you're trying to solve the problem. In the synchronous
distributed system model there are bounds
on message delays, there are bounds on, uh, how, uh-uh, fast each process, uh, can take steps,
and there are bounds, of course, on, uh, the clock drift rates. For instance,
multi-processor systems, uh, which have a common
shared clock across processors fall into this category. Uh, here processes
can crash, as well. Uh, synchronous systems do not
mean there are no failures. Processes can crash by stopping. When a process crashes, uh,
it doesn't execute any more instructions, thereafter. This is typically called
a crash failure or a crash-stop failure. We'll just refer to it
as a failure itself. Uh-uh, this does not include kinds of failures where processes recover
after, uh, crashing. Uh, those can be accommodated
by allowing the process to rejoin
with a different identifier after it crashes. So, uh,
the consensus protocol, uh, in the synchronous system model, uh, assumes that there are,
at most, f processes that crash during the protocol. Uh, f is the number that is less than or equal to n, the total number
of processes in the group. Uh, if you're not sure what
the number of failures is, then just f-f-set f to the n. Uh, all the processes
in this protocol are synchronized
and operate in rounds of time. Uh, so for instance,
here I'm illustrating three rounds, uh,
in the protocol. Uh-uh, the rounds, uh,
are essentially, um-uh, demarcated by specific times at which processes
finish a round and start the next round. And you can do this
in the synchronous system model because, uh, the, uh,
process clocks are, um-uh, not drifting
by more than a bound, so you can
actually specify times at which all the processes
will end their previous round, and then start the next round. So the algorithm proceeds
in f+1 rounds where, remember, f is the number
of processes that crash, that-the maximum number
of processes that crash, um, and, uh, the algorithm uses
reliable communication, to all members. Think of this as, uh,
using some variant of, uh, TCP. Uh, the algorithm uses an area
known as values, uh, _i^r. Uh, this refers
to the set of proposed values that are known
to the process P_i, that's the subscript, at the beginning
of round number r, where r goes from 1 to f+1. This will come through
in, uh, the algorithm pseudocode which we'll see
on the next slide. So here is the algorithm
in all its glory. Uh, initially at process pi, this is the algorithm
for process pi, the values array
is set to be empty. This is at the beginning
of round 0. Then at the beginning
of the first round you include process pi's
own contribution, small vi, into the values array. Then in each
of the following rounds you do the same
following thing. First of all, you ma-m-you
multicast all new values that you have received
since the previous round. So in the first round this would just be the process pi as value, uh, small vi, but in the subsequent rounds
you might receive other values from other processes
and you would multicast these new values
that you've received in just the last round. You wait to receive values
from the other processes, so you set your values
for the next r+1th round to be the same as your values
in the rth round, and then for every new value Vj that you receive from the other processes, you include Vj
in the values array. In the next round,
r+1th round, you would use this
particular values array to multicast out
to all the other processes. Now when I say multicast,
essentially the process pi, uh, goes through loops
through a for loop where it goes through all
the other processes in the system and sends them,
individually, a message, just a single,
point-to-point message. Since this is a synchronous
system, if the sending process and the receiving process
are both non-faulty, this message will be received before the end of the round. If any one of them is faulty, then the message
may not be received. And then finally,
after you do this, uh, f+1 times, after f+1 rounds, so i-so this
is one round, right, what I'm showing over here, and this is done for f+1 rounds at each of the processes, so each of the processes executing one execution of this, uh, for loop
in each of the rounds. So after you do this f+1 times, you simply look
at your values array, all the values that you
have received, and you can look
at the minimum value that you've received. This could either be the, uh,
minimum ID process who has sent you a value, or it could just be
the minimum value that you have received, and you set your
decision variable or your output variable
to be that minimum value. Now why does this work? This seems like
a very strange algorithm where everyone seems
to multicast their values to each other, and if different processes end up with different
values arrays at the end of the f+1 rounds, then they will end up
deciding different values. Well it turns out that
this protocol ensures that all the non-faulty processes
in the group, the ones that have not crashed, end up with the-
with identical values arrays at the end
of the, uh, f+1 rounds so that when they take
this minimum operation, they all end up
with the same decision value. Why is this true? Let's see the proof, uh,
for this. Uh, so once again the claim here
is that after f+1 rounds, all non-faulty processes
would have received the same set of values,
and so they will end up making the same decision using the minimum operation. Let's assume, uh,
that this is not true. Let's assume that two,
non-faulty processes, say pi and pj, differ in their
final set of values after f+1 rounds. Uh, assume,
without loss of generality, that pi possesses a value, v, that pj does not have. If the reverse is true,
that pj has a value v that pi does not have,
you just flip i and j and do the same proof. So pi must have received this
value v in the very last round, the f+1th round
of the protocol. Why? Well, if it
had received it earlier, in the fth round or before, then pi would have multicast the value in the f+1th round, and because pi did not fail
and pj did not fail, pj would have received
this value and would have had the value v. So essentially, uh,
pi got this value v in the very last round,
the f+1th round, um, and, um, uh, this means that some
of the process pk, say pk must have sent
the value, uh, v to pi but must have crashed
before sending the value v to pj, when it went
through the full loop, trying to send the value v
to all the processes in the group. So some process pk crashed
in the very last-that is, f+1th-round of the protocol. Now, you have a scenario where in the fth round
of the protocol, or the end of the fth round
of the protocol, uh, you have a process, uh,
pk, that received the value v but another process pi
that did not receive the value v. This is the last-but-one round,
or the fth round. Right? Um, or you can also
consider pk and pj as-as-as the slide, uh, shows. But essentially,
using this, once again, you can use the same argument
as we did for the f+1th round to show that, um-uh,
again there must have been some other process, say pk', that must have crashed
in that fth round, uh, as well. And using this sort
of reverse induction, uh, we can infer that
in each of those f+1 rounds, a unique process
must have crashed. However, this
is a contradiction, because this means that we have a total of f+1 crashes, uh, during the execution
of the protocol, but we assume that there are
at most f crashes in, uh, the protocol. In other words,
if you let f to be N, you run the protocol
for N+1 rounds, you will end up concluding
from this, uh, assumption that there are N+1 failures, which cannot be true in a group of N processes. This means that our original
assumption must be false, uh, that, um, after f+1 rounds,
um-uh, um-uh, two non-faulty processes differ in their final set of values, and so the converse
of that must be true, which is that all
the non-faulty processes end up with the same values
at the end of f+1 rounds, and so, with the minimum operation applied on the values' array,
they do decide the same, uh, values for their
decision variables. So that's the, uh,
consensus protocol that works in the synchronous system model
and also the proof for it. But what about
the asynchronous system model? Can we just go ahead
and solve it? Well, we'll see how
to do that in the next lecture

## 13 - 3.3. Paxos, Simply

Slides: C3_Paxos_C_CSRAfinal.pdf

### Transcript

[MUSIC] Finally, we get to see the solution or
in courts the solution to the consensus problem in
the Asynchronous Distributed System Model. One of the most popular solutions that
is used in industry, and that has also been proven to be theatrically
sound is what is known as Paxos. And we'll see a sort of, simplified
version of Paxos in this lecture. So as you have all ready seen consensus is
impossible to solve in the asynchronous distributed system model. And this is been proved by Fischer,
Lynch and Patterson also known as
the FLP Proof in the 1980s. And the key to the proof is that it is
impossible to distinguish a failed process from one that is very, very, very slow. And because you cannot distinguish these
two scenarios the rest of the group, even though they may be very healthy. And they may not have too many delays,
they can't really decide whether you know, that one process sent any messages,
whether it's already made a decision, and so everyone should decide the same thing. And so
they might always be ambivalent about which decision to make either zeroes
decision, or all ones decision. But consensus as we've seen, is very important because it maps to
many of the most important problems that are there in distributed computing,
and in cloud computing. So of course, the question rises, can
we just, can't we just solve consensus? And in fact, Paxos does solve consensus, in a sense it's the most popular
consensus solving algorithm. It doesn't really solve
consensus because you cannot there is impossibility of proof,
obviously. We've already shown that. It provides what is known as safety,
and eventual liveness, if it provided just liveness, time-bounded liveness,
then that would have solved consensus but since the possibility result is there
it can only provide eventual liveness. A lot of systems use Paxos, or a variants of it Apache Zookeeper which
was originally built by Yahoo, uses it. Google Chubby which is very deep
in the Google stack uses it, and many other companies use it as well. Just give you a moment here to guess,
who invented Paxos it is our friend Leslie Lamport,
who also invented the Lamport timestamps. So Paxos provides the two properties
of safety and eventual liveness. Safety essentially,
says that consensus is not violated. This means that two processes,
non-faulty processes, do not end up deciding on different
values where one process decides a zero, the other process decides a one, okay. That's if that happened,
that would be violation of safety. Once again, just to remind you,
safety is the guarantee that nothing bad ever happens and
the bad thing here would be two, two different processes that are
non-faulty deciding on different values. Liveness is the guarantee that something
good eventually, happens in this case, something good is that processes
actually reach a decision. If things go well in the future, for
instance, messages and failures are just the right way, then there's a good chance
that consensus will be reached, and everyone will decide the same,
will decide a value and because of safety this value
will end up being the same. But there is no guarantee that liveness
will actually be achieved within a time-bound, or even within our lifetime. The guarantee is only eventual. However, implementations of Paxos
often reach consensus fairly quickly. 'Kay, so Paxos is not guaranteed to reach
consensus ever, or within a time-bound. So FLP, the FLP impossibility
result still applies, but in practice,
a consensus is reached fairly quickly. So here's how Paxos works, and again
this is a simplified version of Paxos. There are a lot of optimizations in Paxos
which we won't be discussing here, and those optimizations are in fact,
important for its correctness. Paxos works in rounds just like
the synchronous consensus protocol we saw earlier, and you might wonder here, how do we set rounds if the process clocks
are not synchronized with each other, as is the case in asynchronous
distributed systems. Rounds are in fact, asynchronous here,
time synchronization is not required. If you are, if you are a process that is
in round j, and you hear a message that is tagged with round j plus 1, you abort
everything that you are doing in round j, and simply move over to round j plus 1. 'Kay, so this is completely asynchronous. You also use timeouts, if timeouts happen
you just move over to the next round, and of course, timeouts may be pessimistic and
this is okay, because we only are trying to give eventual
liveness not time-bounded liveness. Each round has a unique ballot ID which
distinguishes the round and you'll see this ballot ID playing out, as we see
the Paxos protocol in the next few slides. Each round is broken into three phases,
and again, these phases might be
asynchronous by themselves. The first phase is called the Election
phase where a leader is elected, the second phase is called a Bill phase
where this leader proposes a value, and the other processes in the group ack,
or acknowledge this value. And finally, the third phase which is
called the Law phase, where the leader multicasts this final value to the other
processes, and they accept this value. 'Kay, so we'll see these three phases
play out over the next few slides. So the first phase is the Election phase. Eventually, the leader
chooses unique ballot ID and this ballot ID is chosen to be
higher than anything seen so far. Now there might be multiple
potential leaders in, who are trying to become
the actual leader in the group. So the potential leader needs to get votes
from the other processes in the group. So this potential leader sends out
the unique ballot ID to the other processes in the group. Processes wait to receive ballot IDs
from multiple potential leaders, and they respond once each
process works exactly, once to the highest ballot
ID it has seen so far. If the potential leader sees
a higher ballot ID highest, higher ballot ID it
refuses to be the leader. Nicely so essentially,
when process has received, and a potential leader has
received a majority, or a quorum of okay messages, it is then
permitted to be the leader in the group. 'Kay, this means that because each process
works at most once, you cannot have two leaders in the group, essentially, because
then it would mean that two quorums intersect and some process has watered
multiple times, and that's not allowed. Okay?
However, it's possible that no
one reaches a majority because processes voted too early, and they voted for the wrong potential
leaders, and no one reaches a majority. And if this is the case, you just start the next round again,
where, you start again with the Election. However, there are some corner cases
where multiple leaders may be elected, in this case, and Paxos works even there
correctly, but we'll just discuss the case where there is only one leader elected
at the beginning of the Election phase. Now processes also log the received ballot
ID on disk, and this is important because if processes crash, and then recover, then
they can look at the log and, and, and then start where they left off, 'kay. So, again, if things go right
a round cannot have two leaders just because two quorums intersect, and
a process cannot work more than once. So that's the Election phase where the
potential leader sends out a please elect me message, and everyone responds with
an OK, and then the leader waits for a majority, or a quorum and if so,
then it becomes the leader. If it doesn't get a majority or
quorum, it then starts the next round. In the Bill phase the leader
sends a proposed value v to all. The only constraint here is that the
leader if it already knows of a value that has been decided in
a previous Paxos round, it needs to reuse that same value v prime,
'kay. If no value has been decided in a previous
round then it can use whatever value including, for instance,
its own proposed value. Recipients, when they receive this
proposed value, they log it on disks, so that they can recover from failures, and
then they respond back with an OK message. That's the Bill phase. Finally, you have a Law phase, where the leader waits to hear
a majority of OKs from the bill phase. When it hears a majority of OKs, when it reaches a quorum, it lets
everyone know of the new decided value v. And when recipients receive a decision,
they log it on disk, and then they send their decision variables. So that's the Paxos protocol in
a nutshell fairly simplified here. 'kay. Now the question here is
what is the point in order. When has consensus already
been reached in the system? You might think that consensus
has been reached when the Law phase is done at the end of the
final value being multicast but in fact, consensus is reached slightly earlier even
though the processes don't know it yet. In fact, consensus is reached
in the middle of the Bill phase, when the majority of processes have
heared, have heard of the propo, proposed value and have logged it. They may not have responded
to it with an OK but because they have logged it,
they would start where they left off, and that would eventually,
lead to a majority of OKs. The processes may not know it yet, but
a decision has been made for the group. And even a leader may not know it yet, and that's the point of no return after which
that value will be decided in the future, and no other value will
be decided in the future. If the leader fails after that,
you simply restart the round, and processes will then respond back with
the old decided value v in this case, which the leader is then forced
to use in the Bill phase. Because that's what we discussed
earlier the leader has to do. So, why does this
algorithm guarantee safety? In other words, why does it ensure that
two different values are not decided by two different processes? Well, if some round has a majority,
that is a quorum, hearing proposed value v prime and accepting it in the middle of
Phase 2, then subsequently at each round either the round chooses v prime as
its decision, or the round fails. In other words, either it obeys safety,
or it just starts another round. Okay?
So it doesn't decide any other value other than v prime. Well, the reason for this seeing through
is that potential leader waits for a majority OKs in Phase 1, and
because this is a majority or quorum, and a quorum has already heard
a proposed value v prime. That quorum that the leader waits for, and the quorum that has accepted v prime
will intersect in at least one process. And that process will send the value
of v prime to the potential leader, and the potential leader will be forced to use
that value v prime for the Bill phase. And so if the round ever makes a decision,
it will be the value of v prime. The round might, however, fail and in that
case the round will just restart again, a new round will start, and in that case,
again, the value v prime will be used in the Bill phase for the same
reasons as we have just talked about. So the key here again, is that success
requires a majority or a quorum, and any two majority sets or
quorums intersect in this particular case. So that safety what about liveness? Well, again,
there's only eventual liveness. Eventually, if things go right,
if there are not too many failures, and if messages are not delayed just the
wrong time then there's a good chance that the Paxos protocol, some round of
the Paxos might actually, end up with a decision being a maid, and the Law
phase succeeding at all the processes. A lot of things could go wrong that could
prevent rounds from succeeding, and these need actions to be taken
by the Paxos protocol so that it's still trying to reach liveness. For instance processes might fail,
and a majority may not included. When the process restarts,
it just uses its log which is on disk and so it's durable. To retrieve a past decision,
and passing ballot IDs, and then it tries to know of the past
decisions and continue with the protocol. The leader might fail, if this is so, then
the other processes timeout waiting for a bill from it, or
a law message from it, and then one of them will just
start the next round. Messages might get dropped the value
proposals of the OK messages might get dropped quorums might not be reached or
processes might timeout. If things are too flaky, then timeouts
will make sure that another round starts, and then all the proceeds will just
automatically move over to the next round. A round can start at any point of time. So, the current round, maybe about any point of time any process
might a timeout waiting for a reply. Are a Bill or a Law message and
start the next round. And this means that the protocol
may actually never end, and this is a direct outcome
of the impossibility result. You cannot guarantee time-bound liveness
you can only guarantee eventual liveness. If things go well, in the future
then consensus will be reached. So a lot of more things could go wrong. What we've seen is a highly simplified
view of the Paxos protocol. Leslie Lamport's original paper
outlined the Paxos protocol in terms of a parliament, and
even though the paper is hard to read, I encourage you to take a look at it. There are a couple of variants of this
paper that are out there that have tried to present a simplified
version of this Paxos algorithm. Do you might want to take
a look at those as well. So in summary consensus is a very
important problem because it's equivalent to many distributed computing problems
that have to do with reliability. Examples being failure detection,
leader election and also agreement. Consensus is possible to solve in
the synchronous system model, where message delays, and processing delays
as well as clock drifts are bounded. But it is impossible to solve
when these are unbounded. In other words, in the inc, in
the asynchronous distributed system model. And again, the key here is that slow
processes are hard to be distinguished from processes that have just failed. The Paxos protocol is a widely
used implementation of a consensus solution that is safe, but only eventually
alive, and it's used in Apache Zookeeper, Google's Chubby system, Active Disk Paxos,
and many other cloud computing systems. So that would end
the consensus lecture series I have an optional lecture
series coming up after this. Which for those of you who are brave that
lecture will show you the FLP Proof. The Impossibility of Consensus in
the asynchronous split system. It's kind of an interesting proof because
it several interesting concepts in it, and it will give you a feel for why? No matter what protocol you propose
to solve consensus the asynchronous system model always has a way of keeping
the system away from making a decision. [MUSIC]

## 14 - 3.4. The FLP Proof [Mandatory, not Optional]

Slides: C3_Paxos_D_CSRAfinal.pdf

### Transcript

In this lecture we'll see the, um, FLP proof of
the impossibility of consensus in asynchronous
distributed systems. So consensus is
impossible to solve in the asynchronous
distributed system. This is a result
that was proved, uh, in a now-famous result
by Fischer, Lynch and Patterson in 1983, also known
as the FLP result, using the, uh, first letters
of the last names of the three coauthors
of that paper. Uh, before then, many distributed systems designers had been claiming
100% reliability, uh, for their systems, and this result stopped
them dead in their tracks. A lot of claims of reliability
vanished overnight, and one of the, uh,
long-term side effects of this was the multiple 9s
of reliability, um, offerings that vendors
now publicize for their products and services. So once again,
just to remind you, um, the asynchronous distributed system has no bounds on message delays
and p-or processing delays or, uh, clock drift rates. These might be arbitrarily
long or arbitrarily short. The consensus problem requires
each process, uh, p, uh, to decide on the same value. So each process p has a state which consists of the program counter, the registers, the stack, the local variables, the heap, anything else that you would consider to be a part of the, uh, core, uh,
dump of the process. It also has initial, um,
an input register xp, which is initially
either 0 or 1. Different processes
might have different, uh, input register values, that is, those processes', uh, um, proposal to the group, and then each process also has an output register yp which is initially undecided
but needs to be set to 0 or 1. The only constraint is
once you set the output register you cannot change it. And remember that each, uh, process has
its own output register, um, and you want to make sure, uh, that the consensus, uh, uh, protocol at the end, um, uh, has all
the non-faulty processes set their output variables
to be all-0s or-or all-1s. So you want an all-0s decision among the non-faulty processes or an all-1s decision among
the non-faulty processes. Once again, this problem just
by itself, just with these, uh, two, uh, constraints is enough,
uh, to solve consensus because you can just say, "Well, everyone set their
output variables to be 0 all the time,
and that solves it," but that is not interesting
or, uh, useful at all. So we have the non-triviality
clause that says that at least one initial
system state leads to each of the above outcomes, meaning that at least
one initial system state leads to an all-0s outcome, and at least
one initial system state leads to an all-1s outcome. So let's try
to set up the proof. Uh, for the impossibility proof, uh, we'll consider
a more restrictive system model and an easier problem. Well, essentially this is okay
because if you can show that an easier problem is
also impossible to solve, then obviously
the consensus problem, the harder consensus problem, is easier to solve,
is impossible to solve. Uh, if you also sh-if you show that in a more
restrictive system model, uh, the consensus problem is, uh, impossible to solve, then obviously in the less restrictive system model, um, it's impossible
to solve, as well. So, uh, what do I mean
by restrictive system model? Uh, instead of considering
the entire network, we'll consider the network to be a simple global message buffer. When a process p sends a message
to a process p', message m, the message m
just gets deposited in the global message buffer. Subsequently, p' may, uh, call the global message buffer with, uh, receive, and this may return either the message m that is waiting for it or it may return null, and it may continue
returning null, uh, for a while, or maybe even forever, because the message m might be delayed for arbitrarily long. Okay, so we have abstracted
out our network to be just this, uh, global message buffer that is sitting underneath
all the processes. Uh, we also define, uh,
the state of a process, which we have seen before. It consists of its,
uh, program counter, heap, registers, stack
and everything else, along with the input
and output variables, but we also define a state
for the entire system. We call this global
state a configuration. Uh, now, uh, the configuration
or global state consists of a collection
of states, one state for each process, alongside the state
of the global buffer itself. So the state
of all the processes along with the state
of the network is, uh, the global state,
or the configuration. Now we also define an event. This is slightly different
from the Lamport events you've seen before. An event consists of, uh, three steps which are executed atomically, or in one shot. Uh, the event starts
with the receipt of a message by a process, say a process p. Then the message
is processed by the process p. Uh, this may change
the recipient's state. Process p's state might change
as a result of this, and p might also resi-decide
to send out some messages, as a result of this receipt, and those messages
that then result, are then deposited
in the global message buffer. Uh, so all these three,
uh, steps put together, uh, determine an event. So an event essentially consists of a process p
receiving a message, uh, processing it and
then depositing the resulting, uh, messages into the
global message buffer and then, uh, that's an event. Next we'll define a schedule. A schedule is simply
a linear sequence of events, so one event followed by another event followed by another event, that's a schedule, okay? So here on the left is
an example of a schedule. You start with a configuration
or a global state; we label that as c. An event e'
is applied to it. This means that process p'
receives m', uh, processes it and deposits any resulting messages into the global message buffer. That changes the state
of process p'. It also changes the state of the global
message buffer potentially, and that means the configuration itself has changed, and it has changed to something else which we label as c'. A different event, e'', will change the configuration again similarly to, uh, another configuration c''. Now, these two events,
e' followed by e'', is a schedule, because it's
a linear sequence of events, and we call that a schedule s. When the schedule s is applied
on the initial configuration c, this c here is the same
as this c here, it results
in the configuration c''. Again, this c'' is the same
as the c, this c''. So the left side of the slide is equivalent to the right side of the slide. 'Kay, so the schedule
is, essentially, a compact way of representing
a sequence of events rather than mentioning
each event separately. So, here is our first, uh,
lemma, or our first result. It says that disjoint
schedules are commutative. What does this mean? If I have a schedule s1, consisting of some sequence
of events, and another schedule s2, consisting of another sequence of events, if the sets of receiving processes in s1, remember that each schedule consists of a set of messages being received
as a set of processes, if I consider
all these processes in s1, which received messages, and all the processes in s2, that receive messages, if these two sets are disjoint, meaning there are
no processes in common, uh, receiving messages
in both s1 and s2, then these schedules
are commutative. In other words,
their order can be flipped. So if you apply s1 first
on a configuration c and then s2 to reach,
to reach a state c'', then in a different scenario, if you apply s2 first on,
uh, c, and then s1, you would reach
the same final configuration, c'', okay? So, uh, w-why is this true? Well, um, this is true because these are disjoint sets
of receiving processes, and applying s1
or s2 in any order would result
in the same final outcome. In fact, interweaving s1 and s2 would also result
in the same outcome, which would be
the configuration c''. So earlier, uh, we
saw consensus problem here. We tried to prove
the impossibility about an easier consensus problem where some process, not just all, but some process, eventually sets its yp variable, its upper variable,
to be 0 or a 1. 'Kay, and also we'll assume
that only one process crashes, but we are free to choose
which process, uh, crashes. Uh, we define configurations
to have valences. Uh, configuration C may have a set of decision values V reachable from it, and since we are only considering 0 or 1 decisions, um, there might be either 2 or 1 decisions reachable from it. If both the decisions, both, and all-0s and an all-1s outcome are reachable from it, then we say that the size
of the valency is 2, and we say that
the configuration C is bivalent. If only one decision
is reachable from it, either a 0, an all-0s decision, or an all-1s decision,
uh, not both, uh, then the configuration C
is said to be, uh, 0-valent or 1-valent,
respectively. Bivalent essentially means that the configuration C
is unpredictable. That is, it doesn't know which
value it's going to reach, and essentially what we're going to show is that, um, a system can always be kept
in the bivalent state. That it-that is,
it can always be prevented from ever making a decision and ever being sure
about its decision. So the FLP proof
shows two things. First, it shows that there is
some initial configuration, the global state,
that is bivalent by itself, and second it shows
that there is some sequence, there is always some sequence
of events that happen, uh, in a system that start
from a bivalent configuration that keeps the system state or the configuration also bivalent. So, essentially,
there is always some, uh, things that could happen
in the system, um, that, uh, keeps the system moving from one bivalent
configuration to another, and so prevents the system
from ever reaching a decision, uh, with respect to consensus. So let's show the first, um,
part of this proof, that's the second lemma. Uh, i-uh, here we show that some initial configuration
is bivalent. Well let's assume, uh,
that this is not true; let's prove it by contradiction. Let's assume that all initial
configurations are either 0-valent or 1-valent, okay? Now, if there are N processes
in the system, there are 2^N positive
initial configurations. Well, why is this? Well each of the processes
can propose either 0 or 1 for its input variable, and so you have two possibilities for each process, and so this means
that there are 2^N possible initial configurations. Now we create a lattice here, this is, of course,
a virtual lattice, uh, where the nodes
in the lattice are the initial configurations, so there are 2^N, uh, nodes
in this lattice. This lattice is essentially a
hypercube, uh, with dimension N. uh, we, uh, link two, uh,
configurations together, we join them by an edge, uh, if they're d-if they differ
in the initial xp, the initial input variable value
for exactly one process, okay? Uh, this means that, uh, you know, suppose I have, uh,
2 processes, P1 and P2, uh, then I'm going to have a lattice that has, uh, four, um, uh, nodes in it,
four initial configurations where the initial values for,
uh, the, um, uh, for the, uh, uh, uh, ini-for the input variables are 0,0,1,0,1,1, and um, uh, 0,1. And in this, uh, the 0,0 node
is going to be linked to the 1,0 node because they, uh, differ in the input variable values for P1 only, exactly 1 process. Also, the 1,1, uh, node is going
to be linked to the, um, 1,0 node because, uh,
these 2 configurations differ in the input variable
values for P2. And so, essentially, the hypercube in this 2 process case looks like a square. The hypercube
for the 3 process case looks like a cube, and so on and so forth, okay? Now, essentially, um, this, uh, here we are saying that each configuration is either 0-valent or 1-valent, there are
no bivalent configurations. So we tag each configuration
with a 0 or a 1 according to its, uh, valency, either 0-valent or 1-valent. And because there is
at least one 0-valent state, at least one configuration stacked with a 0, and at least one
1-valent state, at least one configuration
tagged with a 1, and because everything
is connected, uh, in just one hypercube, it has to be the case that at least one 0-valent configuration is linked directly to a 1-valent configuration, okay? This, you can, uh,
imagine the hypercube and, uh, you will see that this is true. So this means that
these two configurations differ in the input variables
for exactly one process, say that process is p, and let's say we consider around where this process p
has crashed; that is,
it is silent throughout. Both the initial configurations
are indistinguishable, because the only thing
that differed between these configurations
is the state of p, but p has crashed, so as far as the system running is concerned, p has no effect on it, but this means that both these initial configurations are in fact the same. One of them will, in fact, result in an all-0's outcome, the 0-valent configuration, and the other one will result
in a one-in an all-1's outcome because it's
a 1-valent configuration. So this initial configuration, either one of these
two configurations where p has crashed is, in fact, a bivalent configuration because it may result
in an all-0's decision or it may result
in an all-1's decision. 'Kay, so we have shown that when you have
one process that could crash, and we can choose which process is the one that crashes, you can have at least one
bivalent configuration that is the initial configuration in the system. Okay, so that's
the first part of the proof. Next we need to show that, um, starting from
a bivalent configuration, there is always another bivalent configuration that is reachable. Notice that this proof
doesn't say that you can never reach consensus ever. It says that there
is always some way in which you can be prevented
from reaching consensus. Let the red configuration
be a bivalent configuration, and let, uh, the event e, which consists of the process p receiving a message m, that is the global message buffer in the red configuration, the sum event that is applicable
to the initial configuration, so m is in the global message
buffer in the red configuration. Now let's put our hand on e and
prevent e from being applied. This means that you
might be able to still apply some other events
on the red configuration, and there are
some configurations that you might be able to reach, starting from
this red configuration. We call that set to be C, okay? Those are
the blue configurations that are shown in the triangle. These are the configurations that are reached without applying the special event e. why are we not applying e? You'll see in a moment,
there is a reason for it. Now, if you take
any one of these blue or the red configurations in the-in the triangle, and you apply the single
event e to it, the special event e to it, you will reach another
dark blue event. Let that set of events,
the dark blue set of events, be called as D, 'kay? Once again, D, any event in, any configuration D is reached by applying the special event e on any one of the configurations in the triangle. Now, this is the summary
of what we have discussed. You have the initial bivalent
configuration, the red one. You don't apply the event e
to it, and you reach, and all the possible states, uh, that are reachable are
in the triangle. You take one of the
configurations in the triangle and you apply the event e to it, you'll reach a state that is, or a configuration that
is in the set D. Okay, so we claim that the set D contains a bivalent configuration, okay, and, again, the proof here
is by contradiction. If you can show that
the state D contains a bivalent configuration, then you can show that there is a sequence that consists of at least one event that starts from a bivalent configuration, the red one, that also leads to another bivalent configuration. Let's assume the contradiction. Suppose that D only has 0 and
1-valent contradiction, uh, configurations and no, uh,
bivalent ones. Okay, So there are
these states in D, are going to be tagged
with a 0 or a 1, and because each stated D has a parent in, uh, C from which, on which e was applied
to obtain that D state, we also, uh, tag its parent
with the corresponding 0 or 1. Now what you have is you have
a C of mixing 0's and 1's here, and therefore, just by the same
argument that we use before, where we showed that there has to be at least one bivalent configuration because at least one 0-valence state and one 1-valence state are adjacent to each other, you can show here as well,
that in this triangle there's going to be
at least two configurations, that are adjacent to each other, because all of them are linked by other events other than e so that one is tagged with a 0, the other is tagged with a 1. In other words, it has to be
the case that there are states or configurations D0 and D1, both in D, and C0 and C1 both in C such that D0 is 0-valent,
D1 is 1-valent. D0 is obtained
from C0 by applying e, D1 is obtained from C1 by applying e,
and C1 is adjacent to C0, which means that C0 is,
on C0 if you apply some event e' a special event e',
you will obtain C1. So given this,
there are two possibilities. First, that the process,
receiving the message p' in the special event e'
is the same as p, which is the process receiving the message in event e, and the second case is that p' is, uh, not the same as p, 'Kay, so let's consider
the first case, p' is not the-the same as p. from the previous slides, C0, when you apply e'
to it, you get C1. C0, when you apply
e to it, you get D0. C1, when e is applied
to it you get D1. Since e and e' have different sets
of receiving processes, these are disjoint sequences, and so flipping the order
in which they are applied, e' first, followed by e,
or e followed by e', will give you the same
final configuration. In other words, you can draw
this red arrow here and show that you can reach from D0 you can reach D1 as well. But this is a contradiction,
because we said D0 was 0-valent, but we have just showed that from D0 you can reach
a 1-valent state as well, which means that
in fact D0 is bivalent, and that is a contradiction. So that's the first case,
where p' is not the same as p. That was the easy case because e and e'
were commutative over here, and we could use
our first lemma. So what about the second case? The second case
looks a bit complicated, but just bear with me. I'll try to explain it. So once again, here C0
applied e gets you D0, C0 applied e' gets you C1, C1 applied e gets you D1, okay? So let's say C0 has
a schedule s which is finite, it consists of a finite set
of steps, because we say that consensus is in fact reachable in a finite set of steps, and it's a deciding round,
in which p takes no steps. The special process p, which is the process p
in receiving the message in the event e,
that is arbitrarily slow, so it does not receive
any messages over here, uh, and it
does not take any steps in this schedule s over here. But it's a deciding round, which means that when final configuration A is reached, a decision has been made, okay? Now, what is that decision? Well, we don't know
what the decision is. So now, since p is not there
in the schedule s, the schedule s is disjoint
from the schedule consisting of the single event e, and so these two schedules
can be commutated. So if you apply e first
followed by schedule s, that is, you apply schedule s
on D0, you reach some state E0, which has to be a 0-valent state because D0 is 0-valent. On the other hand, if you apply
schedule s first followed by e, in other words,
when you apply e on A, you get the same
0-valent state E0. On the other hand, if you apply
e' and e followed by s, or s followed by e' and e, remember that these
two schedules are disjoint because p appears in only this schedule but doesn't appear here and then what you will see is that you, uh, reach from A another sche-configuration E1, which is also reachable from D1. But because
it's reachable from D1, E1 must be
a 1-valent configuration. However, we said that A
was a deciding state in which either
an all-0's decision or an all-1's decision
had already been reached. However, here you can see that
from A you can reach both a 0-valent configuration E0 as well as 1-valent configuration E1. This is a contradiction, because
said that A is a deciding state, and this means that from C0 you, might never, ever be able to reach a decision, okay? So this is a contradiction
for the second case, and this completes our proof. Here we have shown that, uh, starting from
a bivalent configuration, there is always another bivalent
configuration that is reachable by applying at least one event, uh, from the initial
bivalent configuration. Okay, so essentially
this means that, um, uh, there is always something that can go wrong in the system that, uh, keeps the system
in a bivalent state. This doesn't mean that the system
will never reach consensus. It means that there is
at least some path, some sequence of events, that, um, will prevent the system from reaching consensus, that is, it stays
bivalent forever. So in summary here, the consensus problem
is an important problem because it deals with agreement in distributed systems. Solutions exist
in the synchronous system model, but we have just shown here that it is impossible to solve in the asynchronous
system model. Uh, this is important because
asynchronous system model is what is true in the internet, um, um, uh, and the other, uh, distributed systems that appear
in cloud computing systems. The key idea in the FLP
impossibility proof is that just one slow or, uh, crashed process can prevent the other processes in the system from ever reaching a-a decision. And again, nowhere in the proof
that we've seen, so far, have we actually discussed details of the consensus protocol that you might propose. Uh, wh-what we
have discussed so far applies to any consensus protocol that you might propose, and that's the beauty
of the proof, that it is generic and it applies no matter what the protocol is trying to do. It, all it assumes is that
protocols, uh, send messages. Okay, and this is one
of the most fundamental results in distributed systems, uh, and
that's why we have discussed it.

## 15 - Interview with Tushar Chandra

### Transcript

[MUSIC] My name is Tushar Chandra and I've
been a software engineer at Google for about ten years. I got my PhD in computer science,
gosh, a little more than 20 years ago. And then I was at IBM research for
about ten years, and then came to Google. So, I've spent most of my career
working in distributed systems, specifically for distributed systems. Though oft late I've been looking
at large scale machine learning, which I view as the next
layer up in the stack. Where we use distributive systems to
solve, you know, large scale problems. [MUSIC] Yeah, so from my perspective,. We started working on cloud computing
before cloud computing got the name. So I don't actually see that that
transition the way many others do. But the environment we work in is
a very large distributed system. We have lots and lots of computers
over a very, very large network. In fact,
we have multiple data centers, right? And these are interconnected
to high speed links. And then our problems
are very large scale as well, so many of the problems you work on
cannot be solved on a single computer. So we are forced to build these
highly scalable solutions that span multiple computers and
multiple data centers. That's what they call cloud computing now,
but that's what we've been doing essentially since I've been
at Google for the last ten years. >> Absolutely, absolutely. So Paxos is a kind of
distributive consensus algorithm. And there's been, you know, in your
course you've covered a lot of that. But this is very practical, it's a core primitive that we use in
in our cloud computing solutions. So when you have a lot of computers and
you're building higher level primitives. Like MapReduce and BigTable and a distributed file
system like the Google file system. Even at that level you need to
coordinate these computers. Often you need a single leader who's
going to coordinate all the activity in a MapReduce on, in an,
in GFS or in Big Table. And you need, you know, in that setting you need
a leader election kind of mechanism. That leader election mechanism needs to
guarantee that there's just one leader. He needs to notify the rest of
the system when the leader failed, bring in a new leader, that sort of thing. You need to have a distributed
lock managers so that when multiple different computers
are trying to solve the same problem. They don't sort of trip on each other. So things like this and many many other things require low level
distributive computing primitives. Things like distributed consensus. And we do use Paxos extensively. Leader election mechanisms. You know? [MUSIC] The Paxos algorithm that
Lamport talks about. Which is what, our algorithm, our implementation's
definitely based on those ideas. So, I don't want to take away from that,
at all. But, the Paxos algorithm that he talks
about can be expressed in a page or two. Our implementation is like,
more that 10,000 lines of code, right? So, there's something between
what Lamport talks about, which is a core ideas, and
the actual implementation. Some of that is just like,
boilerplate code. You know, how do you send a message,
how do you receive a message, how do you time out,
all the details of that. But some of those, some of it is also
algorithmic fixers that are spelled out in different places in the literature,
but never really put back together. And when you put them together,
the implementation becomes more complex. The way I like to view it is, with every
new feature you add to an algorithm like, a distributed consensus
algorithm like Paxos. You roughly double
the complexity of the algorithm. So, if you add one idea, like, you know,
allowing multiple rounds to happen at the same time, well,
you've doubled the complexity. If you add another idea, like leader election, you double the
complexity again, and so on and so forth. So, you add three or four ideas and
then suddenly you've got a 26,000 line or 50,000 line code base, right? So there's lots of detail in that. The other thing is when you scale from, you know, a two-page paper to tens
of thousands of lines of code. Your proofs, I mean, you have no hopes
of your proofs carrying through. They just can't. You have, you know, a multi-thousand-line
program and you can't prove it correct. We don't we don't really have
the tools to do that yet but there is a lot of
research work on that. So the focus then has to
shift away from the paper and its proofs, and much more towards testing. And so when I built this Paxos
implementation my primary focus was testing. I built a distributed system before of,
of this nature at IBM. And there the focus was algorithms and I realized that was a mistake,
when I built that system. So when I was building this one,
the focus was testing. I kind of knew I would get the algorithm
rola, right, so I didn't even focus on it. And I think that was the right decision. So, what you learn about in
academia about proofs gets replaced to some extent
by testing in industry. Now, you have to know how this
algorithms work because you don't want to start off with a random algorithm. You want to start off with an algorithm
that is almost surely correct, but then from there you take it to a,
to actually correct. I think the best hope we have is testing. [MUSIC] My focus has moved to large
scale machine learning. So I view this as moving up in the stack. And, really, from my point of view,
I've gone from being a developer of distributed computing primitives for
cloud computing. To being a user of those primitives. So, now, I've become a user of MapReduce. And so, implicitly, a user of you know,
a Paxos implementation. And that's really changed my perspective. So, I want to talk a little bit about
that because I think that's what your students will be interested in. so, one of the key ideas that
we had was we did not want to build a distributive system. When you're building
the low-level primitives, your entire job is about
building these primitives. When you're using it. You don't even want to go there. Because when you think about
distributed systems explicitly, it, it, you can take a simple idea and
make it horribly complicated. And that's really not our focus, right? We are in the business
of working on solutions. So we wanted to focus on
the machine learning algorithms, not distributed systems algorithms. And we decided not to build
a distributed system. So instead we use primitive like,
MapReduce and, you know, the Google file system and our classroom
management software and so, on. But we don't do anything on top
of that and that's by design. So for the students in your class, I would really like you to realize
if you're building this stuff. Do it in a way so that people on top
of you don't have to think about it. This should be like plumbing,
it should be in the walls, shouldn't have to think about it. [MUSIC] So let me just step back a little bit and that, Google is, you know,
still growing rapidly as a company. So we are definitely hiring. As you can imagine,
we deal with very large data sets. Think of a data set as, you know,
people doing searches on Google. You can imagine that there are zillions
of such people doing that. And so, you know,
we deal with very large data there. Can think about it other properties,
YouTube, Gmail, Google Docs, Google Plus,. You know, increasingly messed. These are all properties with lots and
lots of data. Now, what we've discovered is that when
you, manipulate this data the right way, when you look at it. You can make, you can have insights that you wouldn't
have if you had a much smaller data set. So, you can learn lots of nuance
things from this very large data and then you can use that to
make a better product. So there's a capability that's
only emerged very recently. With the internet, but
also the scale of the internet. Probably in the last few years. So it's a new field. I don't know how to clearly define
exactly what skills you need. That is still evolving. But what we are looking for is people who
can handle these large data sets, right. Now terabyte is your atomic unit. Data sets are much larger than that. You want to be able to look at
those data sets, understand them, make insightful observations with them,
build systems around them. And in my case, build a closed loop. So when you look at these
large datasets look at how people have responded to specific
documents we've shown them. And then, if you've responded well
to a document we've shown you. It means that next time we should
show the same document to, you know,
to the next user in the same context. So, those are the insights
you only get with big data. Again, multi terabytes of data, you know very complicated large systems,
all distributed systems all cloud based. And on the value side, you know when
you have such a large data set when you make a small improvement it's
actually a big improvement. Because it gets multiplied by a zillion
users, so very valuable yeah. If you think about Moore's Law. If you think about how our
data centers are scaling. You can be sure that things
are going to grow at least 10x in the next five years and
at least 100x in the next ten years. So we'll have that many more computers and
networks will be that much faster. Maybe we'll have that many more color and
so on and so forth. [COUGH] So another way to think about is,
when I said that you know, terabyte is kind of the atomic unit, maybe it'll increasingly be a parrabyte
that will be the atomic unit. And I don't see I, I see the focus being more on distributed
systems than on single computers. That the single computers have their
own constraints and their limitations. But distributive systems
seem easier to scale out. So, you know,
where we're running jobs with 10 or 20 machines today,
maybe 100 machines today. Maybe be running them at
1,000 machines down the road. I also think many of these primitives
that you've been teaching your students about will continue to mature. To become more powerful, become more
efficient, move higher up in the stack. And as that happens, I think they'll
become more accessible to people as well. And so, we'll see more development there. So the way I hope it will play
out is that is the following. Within a data center we tend not to
worry so much about disconnections. Because that's much more reliable and
trustworthy. It's when you run across data centers,
when somebody does something crazy to your wire that's connecting
one data center to the other. That you really suffer from
these kinds of problems. Now once upon a time people wondered
about insider data center too. So you've already seen a little
bit of evolution there where. We tend not to worry so
much when inside a data center. I think that it boils down,
to some extent, at least, to how much you're willing to invest. If you're willing to put in a more robust
network, it'll cost you a little bit more. But it makes everything simpler for you. So, the infrastructure providers,
I think, should be thinking about this. It's worth investing that extra bit. So that your programmers
don't have to think about it. Another way to think about it
is that distributed systems does not come naturally to most people. And when it does, we all make mistakes. I certainly make my, my own fair set of mistakes when I don't
plan for a certain kind of failure. And I have a PhD in behavior, right? So, these mistakes can be very,
very expensive. You know, you have some inconsistency in,
say, a bank and you lose money. We should think like
the compiler guys did. They said, you know,
let's lose a little bit. Let's pay up, let's make the platform
more expensive if that's what it takes. But make the programming parameters
simpler for our programs. And that's where I, I hope we will go. I hope we'll have more reliable networking
that you can trust more and more. And that, increasingly we'll be
able to think about programming in a strongly consistent environment. And I think everybody
will be happy with that. So actually, I have something
personal to share with you. I reach my ten year anniversary
at Google in about two weeks. >> Nice.
>> Thank you. And there's a reason for it- it's because I've had
a really really good time. It's a fantastic work environment. It was a fantastic work
environment when I started, you know,
a little bit before Google's IPO. But, in my mind, things haven't
changed a whole lot, since then. Even though the,
the company's grown about 25 fold. It's still very much
a bottom's up environment, where an individual can, is empowered,
and can make a difference. It's still very much a,
an environment that is based on data. So, it's not really your opinion
that counts, as much as you know, gather the data, get the evidence,
and then work with the evidence. That makes it a less, much less of
a conflict environment than when you have two opinions that you can't resolve. It's also an environment where people,
very, very hard, to hire, you know,
very strong people. So, I personally find it very exciting,
when I come in, I'm dealing with, you know, the best and
the brightest in the world. [MUSIC]

## 16 - Conclusion to Cloud Computing Concepts, Part 1

Slides: C3_Part1Outro_CSRAfinal.pdf

### Transcript

[MUSIC] At this point, in the course as we begin to wrap up the
part one of the cloud computing concepts, we are essentially taking a pause,
in the concepts that we have seen so far. Hopefully what you've seen so
far has been a good sampling of what underlies to these cloud
computing systems. You've seen a little bit of
distributive algorithms, and, in the second part of the cloud computing
concepts course, we'll continue our, tool. What you've learned so far has been
an introduction, to the idea of cloud computing concepts including mapreduce and
key-value stores, many classical precursors and widely used algorithms that
underly today's cloud computing systems. And also we have started to
look at classical algorithms, as, the end of the course came up. In the second part of the course,
we'll continue with, the same thread. We'll continue looking at
more classical algorithms. You also looked at some
interviews with managers and researchers from industry
as well as academia. What's coming up after the pause in C
three part two, the second part of this course, is a more classical
algorithms including leader election, mutual exclusion and scheduling. Discussion of scalability,
how can you support millions of clients? How can you support hundreds or
thousands of servers, replicating data? We look at new trending areas
such as stream processing, distributive graph processing. As well as,
wisdom on structure of networks. As well as exciting ideas
like sensor networks. And we'll look at a variety of ideas that
have, some relation to cloud computing, including distributed file systems, distributed shared memory,
security, and we'll look at some case studies of what happens
when things go wrong in data centers. And of course we continue interviews with, our friends in academia
as well as industrial. The goal of, C3-Part 2, which is coming
up, remains the same as, Part 1. We continue to look at the internals of
cloud computing, meaning the listable systems and algorithms that underly
to these cloud computing systems. We'll discuss concepts, techniques,
and industry systems that use these concepts and techniques,
including open-source industry systems. Again the format of C3 Part 2 should be
familiar to you, it is just like C3 part one, you have two homeworks, and one exam
and an optional programming assignment. While in C3 Part 1, you will build
a membership protocol in C3 Part 2, you will be building a key
value store inside an emulator. But one again, just like part one, the
emulator is better so that the code can be taken as is, and ported easily
over a reall distributor cluster. C3 Part 1, that you have been involved in
so far, is a prerequisite for C3 Part 2. Which means that you are perfectly pleased
to move forward to C3 Part 2 right now. You have all the necessary,
background that, you need to actually
take C three part two. Cloud computing continues to
be an exciting media, and, one that is dynamically changing and
continuously changing. So I invite you to continue this,
journey with me as we move forward and continue our journey,
through the landscape. I'm looking forward to seeing you again
in Cloud computing concepts Part 2. [MUSIC]

## Quizzes

_No transcript available._
