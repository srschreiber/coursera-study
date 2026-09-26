# Week 2 Study Notes — 1. Clouds and Distributed Systems

This document covers the Week 2 material before MapReduce. It is organized as a lecture, but it intentionally preserves course-specific definitions and details that may appear on the midterm.

## 1. Why Clouds?

Clouds provide compute and storage without requiring a customer to buy and operate all of the underlying hardware.

Important examples from the lecture include:

- **EC2** — compute using virtual machines.
- **S3** — storage, historically priced per GB-month.
- **EBS** — block storage accessible by EC2 instances.

Two deployment categories:

- **Public cloud:** resources are available to outside customers.
- **Private cloud:** resources are restricted to an organization or privileged users.

Clouds can save both provisioning time and money because customers can obtain resources quickly and pay according to usage rather than purchasing enough hardware up front.

## 2. Course Working Definition of a Cloud

The course deliberately does not try to give a universal definition.

Its working idea is:

> A cloud contains large amounts of storage with compute cycles located nearby.

The direction matters. In a data-intensive system, moving enormous datasets is expensive, so a recurring principle is:

> **Move computation toward the data rather than moving the data toward computation.**

This principle will reappear in Hadoop's locality-aware scheduling.

## 3. What a Datacenter Looks Like

A **single-site cloud** is essentially a datacenter.

The course identifies these major pieces:

- compute nodes / servers,
- servers grouped into **racks**,
- **top-of-rack (ToR) switches**,
- a network topology connecting racks,
- storage/backend nodes,
- front-end machines for client requests or job submission,
- software services running across the infrastructure.

### Rack topology

Conceptually:

```text
                    Core switch
                   /           \
          Top-of-rack         Top-of-rack
             switch              switch
           /   |   \            /   |   \
         S1   S2   S3          S4   S5   S6
             Rack 1               Rack 2
```

Servers in the same rack connect through their **top-of-rack switch**.

Traffic between racks travels upward through the network topology, such as through a **core switch** in a simple two-level hierarchy.

Switches have finite:

- bandwidth,
- port counts.

At sufficiently large scale, a two-level topology may therefore need to grow into a deeper hierarchy.

This physical topology matters later in Hadoop because scheduling a Map task on the machine containing its input is better than transferring the block across the network; if that is impossible, using a machine in the **same rack** can still be preferable to crossing racks.

### Backend and front-end nodes

**Backend/storage nodes** emphasize storage capacity, such as SSDs or larger numbers of disks.

**Front-end servers** receive client requests or job submissions.

### Geo-distributed clouds

A geographically distributed cloud contains **multiple datacenter sites** connected together. Sites can have similar or different internal structures and software stacks.

## 4. History: Clouds Are Not the First Distributed Systems

The course frames cloud computing as another generation in a long history of distributed computing.

Rough progression:

- 1940s–50s: very large early computers such as ENIAC/ORDVAC/ILLIAC.
- 1960s–70s: timesharing and data-processing industry.
- 1980s: PCs, networks of workstations, clusters, grids.
- 1990s–2000s: large peer-to-peer systems such as Napster, Gnutella, BitTorrent.
- Modern era: very large cloud/datacenter systems.

The conceptual point is more important than memorizing every date:

> Cloud computing builds on decades of distributed-systems ideas rather than replacing them.

The lecture also describes the old vision of **computing as a utility**: obtaining computing resources in the way users obtain electricity or water.

### Hardware trends

The lecture discusses historical exponential improvements in:

- compute capacity,
- storage per dollar,
- network bandwidth.

It notes that CPU clock-frequency growth hit a power wall, so growth increasingly came from more cores/processors rather than ever-increasing clock speed.

## 5. Four Characteristics of Modern Clouds

The course explicitly identifies **four major characteristics** distinguishing modern clouds from earlier generations:

1. **Massive scale**
2. **On-demand access**
3. **Data-intensive workloads**
4. **New cloud programming paradigms**

These four are worth memorizing.

### 5.1 Massive scale

Modern datacenters can contain tens or hundreds of thousands of machines.

At this scale:

- failures become routine,
- algorithms must scale,
- networking and storage architecture matter,
- manual administration does not scale.

### 5.2 On-demand access

Users obtain resources without purchasing them permanently or making the same up-front hardware commitment.

This leads to pay-as-you-go models such as:

- CPU-hours,
- GB-months of storage.

Elasticity means the amount of provisioned resources can change as demand changes.

### 5.3 Data-intensive computing

Traditional high-performance computing can be **compute intensive**: relatively modest input data but heavy computation.

Cloud workloads are often **data intensive**: enormous datasets must be stored, read, transferred, processed, and queried.

Therefore:

> **Bring computation to the data.**

In data-intensive systems, **disk I/O and network I/O** can be more important bottlenecks than CPU utilization.

### 5.4 New programming/storage paradigms

Examples in the course include:

- MapReduce,
- Hadoop,
- key-value stores,
- NoSQL systems such as Cassandra and MongoDB.

These abstractions make it easier to program and store data across large clusters.

## 6. Cloud Service Models

The lecture introduces the **aaS — "as a Service" — classification**.

### HaaS — Hardware as a Service

Access to bare hardware. Exposing raw hardware to untrusted users raises security concerns.

### IaaS — Infrastructure as a Service

Users obtain virtualized machines/infrastructure and can install their own operating systems and software.

Virtualization provides isolation and is a major reason IaaS can safely expose infrastructure to many users.

### PaaS — Platform as a Service

Users write applications against a managed platform rather than directly provisioning/managing VMs.

Tradeoff:

> **Easier / more managed, but less flexible than IaaS.**

### SaaS — Software as a Service

Users consume the finished software service itself.

The important progression is roughly:

```text
hardware → virtual infrastructure → managed application platform → finished software
 HaaS            IaaS                    PaaS                 SaaS
```

## 7. Datacenter Efficiency: PUE and WUE

### Power Usage Effectiveness (PUE)

```text
PUE = total facility power / IT equipment power
```

IT equipment includes useful computing/network equipment such as servers, routers, and switches.

Because total facility power includes IT power:

```text
PUE >= 1
```

**Lower is better; 1 is the theoretical ideal.**

Example:

```text
Total power = 1200 kW
IT power    = 800 kW

PUE = 1200 / 800 = 1.5
```

Rearranging:

```text
Total facility power = PUE × IT power
```

Thus PUE 1.2 with 600 kW IT power gives:

```text
1.2 × 600 = 720 kW total
```

### Water Usage Efficiency (WUE)

The lecture also mentions **WUE**:

```text
WUE = annual water usage / IT equipment energy
```

The stated unit is liters per kWh.

Again, **lower is better**.

Cooling matters because servers and networking equipment generate heat, so datacenters consume resources beyond the electricity directly used by IT equipment.

## 8. Economics: Own vs. Outsource

Public-cloud economics are not simply "cloud is always cheaper."

The lecture compares:

- **outsourcing to a public cloud**, versus
- **buying and operating a private cloud**.

Public cloud costs scale with usage, such as CPU-hours and GB-months.

Owning infrastructure includes costs such as:

- hardware,
- power,
- networking,
- system administration.

The lecture performs a **break-even analysis**. Its historical example found different break-even points depending on what costs were considered; the important general idea is:

> Short-lived or uncertain workloads often favor outsourcing because there is little up-front commitment. Long-running predictable workloads may eventually make owned infrastructure economically attractive.

The exact historical prices are old, but the method is testable: compare monthly outsourced cost against amortized ownership + operating cost and solve for the lifetime at which one becomes cheaper.

The lecture also mentions an old rule of thumb for datacenter cost allocation:

- 45 cents hardware,
- 40 cents power,
- 15 cents network,

per dollar-like unit of infrastructure cost, amortized in its example over three years.

## 9. A Cloud Is a Distributed System

The course treats clouds as a **special class of distributed systems**.

Earlier generations/classes include:

- time-shared systems,
- clusters,
- grids,
- peer-to-peer systems,
- clouds.

The names and architectures change, but core distributed-systems problems survive across generations.

## 10. The Course's Working Definition of a Distributed System

This is important: the course rejects several simpler textbook definitions.

For example, it rejects the requirement that the entire system must **appear to the user as one local computer**. The Web is distributed even though users can observe that one website is available while another is unavailable.

It also rejects requiring a client-server organization because peer-to-peer systems are distributed systems too.

### Definition used by this course

> **A distributed system is a collection of entities that are autonomous, programmable, asynchronous, and failure-prone, communicating through an unreliable communication medium.**

The entities are generally **processes running on devices**.

You should know every adjective.

### Autonomous

Each entity can operate independently.

### Programmable

The entities execute programs. This helps exclude things such as groups of humans or birds from the computer-science definition being used in the course.

### Asynchronous

Each process operates according to its own clock.

The clocks are **not assumed to be synchronized**.

This produces later problems involving:

- clock skew,
- clock drift,
- ordering events across machines.

### Failure-prone

Processes can crash independently and at arbitrary times.

### Unreliable communication medium

Messages may:

- be dropped,
- be delayed for an arbitrarily/inordinately long time.

For this course, the essential mental model is:

```text
Process P1 ---- messages ---- Process P2
       \                       /
        \---- unreliable -----/
               network
```

Distributed algorithms therefore cannot treat communication as instantaneous or perfectly reliable.

## 11. Distributed vs. Parallel Systems

This distinction is more specific in the course than simply "one machine versus many machines."

A **parallel system** such as a multiprocessor/supercomputer can have many processors executing simultaneously while being tightly coupled and sharing a synchronized clock.

A distributed system is **asynchronous**: independent processes have unsynchronized clocks and communicate by messages over an unreliable medium.

So:

> **Parallelism is about simultaneous computation. Distribution adds autonomous asynchronous entities and unreliable communication.**

A 64-core machine can perform massive parallel computation without satisfying the course's distributed-system model.

## 12. Partial Failure and Failure Detection

A distributed system can suffer **partial failure**.

Suppose A and B can communicate but C becomes unreachable. A and B may continue changing state while C misses those changes.

When C returns, its state may be stale.

Worse, if A sends a message to C and hears nothing, A cannot determine from that observation alone whether:

- C crashed,
- C is overloaded,
- the request was lost,
- the response was lost,
- the network is congested,
- the network is partitioned,
- the message is simply delayed.

This uncertainty is central to later topics such as failure detectors and membership protocols.

## 13. Scale Makes Failures Normal

If one machine has failure probability `p` during some interval and failures are independent, then with `n` machines:

```text
P(no failures) = (1 - p)^n

P(at least one failure) = 1 - (1 - p)^n
```

Example: 100 machines, each with a 1% weekly failure probability:

```text
P(at least one failure)
= 1 - 0.99^100
≈ 0.634
≈ 63.4%
```

This illustrates a major course principle:

> **At large scale, failures are the norm rather than the exception.**

## 14. Other Core Challenges

The distributed-system definition leads to several recurring challenges.

### Scalability

Algorithms must continue working efficiently as machine count and data volume grow.

### Asynchrony

There is no perfectly synchronized global clock.

### Concurrency

Many processes may access or modify related state simultaneously, creating races and consistency problems.

### Failure

Processes and communication can fail independently.

These ideas motivate later course topics such as gossip/membership, distributed hash tables, key-value stores, timestamps, consistency, and coordination.

## 15. Why More Machines Do Not Guarantee Linear Speedup

10,000 machines do not imply a 10,000× speedup.

Costs include:

- communication,
- network latency,
- limited network bandwidth,
- synchronization,
- scheduling,
- aggregation,
- failure recovery,
- serial portions of the workload.

For sufficiently small workloads, distributing the computation can cost more than doing it locally.

---

# Midterm Checklist

You should be able to explain or derive all of the following:

- Public vs. private cloud.
- Course working definition of a cloud.
- Why computation is moved toward data.
- Datacenter components: servers, racks, ToR switches, core/network topology, backend storage, front end.
- Single-site vs. geo-distributed cloud.
- Broad historical progression leading to clouds.
- Four modern-cloud characteristics: massive scale, on-demand access, data intensive, new programming paradigms.
- HaaS, IaaS, PaaS, SaaS and their differences.
- Compute-intensive vs. data-intensive workloads.
- PUE, including rearranging the equation.
- WUE and why lower is better.
- Own-vs.-outsource break-even reasoning.
- Why a cloud is a distributed system.
- Why "appears as one computer" is not required.
- Why client-server architecture is not required.
- Course definition: autonomous, programmable, asynchronous, failure-prone entities + unreliable communication.
- Distributed vs. parallel systems, especially asynchronous clocks.
- Partial failures and why silence does not prove a crash.
- Failure probability at scale.
- Scalability, asynchrony, concurrency, and failures as core challenges.

# Practice Problems

1. Draw a simple two-rack datacenter topology containing servers, two top-of-rack switches, and a core switch. Trace traffic from a server in rack 1 to a server in rack 2.

2. Why does Hadoop later prefer a node containing the input data, then a node in the same rack, over an arbitrary node elsewhere?

3. Name the four characteristics the course gives for modern clouds.

4. A customer wants full control over a VM's operating system. Which aaS layer best matches this? How does that differ from PaaS?

5. A datacenter consumes 900 kW total and 600 kW powers IT equipment. Calculate its PUE.

6. A datacenter has PUE 1.25 and IT equipment consumes 800 kW. Calculate total facility power.

7. Explain why "all machines appear as one computer" is not a requirement in the course's definition of distributed systems.

8. State the course's working definition of a distributed system and explain each adjective.

9. Why does the course use asynchrony to distinguish distributed systems from tightly coupled parallel systems?

10. Machines A and B can communicate, but neither can reach C. Give at least three explanations other than C having crashed.

11. Each machine in a 200-machine cluster has an independent 0.5% probability of failure during a day. Write the expression for the probability that at least one machine fails.

12. A startup expects to run for an uncertain amount of time and does not know its future traffic. Explain why public-cloud economics may initially be attractive even if owning hardware could eventually have a lower monthly cost.
