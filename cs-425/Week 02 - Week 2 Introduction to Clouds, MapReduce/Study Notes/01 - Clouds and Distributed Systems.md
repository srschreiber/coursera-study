# Week 2 Study Notes — 1. Clouds and Distributed Systems

These notes are organized as a lecture rather than a transcript. The goal is to understand the concepts well enough to answer conceptual, calculation, and scenario-based midterm questions.

## 1. Why Clouds?

Cloud computing lets users acquire computing resources when they need them rather than owning enough hardware to handle their maximum possible demand.

Suppose a service normally needs 20 servers but needs 200 servers for a few hours during peak traffic. If the company owns its infrastructure and provisions for peak demand, most of those 200 servers sit idle most of the time. A cloud can instead let the company acquire additional resources during the peak and release them afterward.

This motivates two important ideas:

- **Elasticity:** resources can be scaled up and down as demand changes.
- **Pay-as-you-go:** users pay for resources they consume rather than making the same large up-front infrastructure investment.

These properties help make clouds economically attractive when workloads vary over time.

## 2. What Makes a Cloud Different?

Cloud computing did not invent distributed computing.

Older distributed systems already had independent machines communicating and coordinating over networks. The defining similarity between clouds and earlier distributed systems is therefore:

> **Servers coordinate with other servers over a network.**

What distinguishes modern cloud computing is the combination of properties such as:

- very large scale,
- elastic/on-demand resource provisioning,
- resource sharing and virtualization,
- pay-as-you-go economics,
- infrastructure exposed as services.

So if an exam question asks what clouds and previous generations of distributed systems have in common, do not choose elasticity or cloud pricing. The basic shared property is **networked machines coordinating with one another**.

## 3. Public vs. Private Clouds

A **public cloud** provides cloud resources to external customers.

A **private cloud** uses cloud-style infrastructure for a restricted organization or set of users. For example, an internal company cluster accessible only to that company's employees is a private cloud.

"Private" does not mean that the machines stop being distributed or stop using cloud techniques. It describes who can access the infrastructure.

## 4. Datacenter Efficiency and PUE

A datacenter consumes power both for its useful IT equipment and for supporting infrastructure such as cooling and power delivery.

The course uses **Power Usage Effectiveness (PUE)**:

```text
PUE = Total datacenter power / IT equipment power
```

Because total datacenter power includes IT power, PUE is at least 1.

**Closer to 1 is better.**

### Example

A datacenter consumes 1,200 kW total, while servers, networking, and storage consume 800 kW:

```text
PUE = 1200 / 800 = 1.5
```

If a datacenter has PUE 1.2 and consumes 600 kW of IT power:

```text
Total power = PUE × IT power
            = 1.2 × 600
            = 720 kW
```

For PUE 1.8 with the same IT load:

```text
Total power = 1.8 × 600 = 1080 kW
```

## 5. What Is a Distributed System?

A useful definition for this course is:

> **A distributed system is a collection of independent machines that communicate over a network and coordinate to accomplish a common task.**

The word **independent** matters. Multiple CPU cores inside one computer can execute work in parallel, but this is not what we normally mean by a distributed system.

For example:

- 64 CPU cores on one server processing an array: **parallel computation, not distributed computation under the usual definition**.
- 64 independent servers communicating over a network to process a dataset: **distributed computation**.

A distributed system may also hide this complexity from its users. A user may interact with what appears to be one service even though a request is handled by many cooperating machines.

### Distribution does not imply fault tolerance

Do not put fault tolerance into the definition itself.

A distributed system **may be fault tolerant**, and fault tolerance is extremely important in distributed systems, but a badly designed distributed system can fail as soon as one machine fails.

So keep these concepts separate:

- **Distributed:** independent networked machines coordinate.
- **Parallel:** multiple computations happen simultaneously.
- **Fault tolerant:** the system can continue operating despite some failures.

## 6. Why Distributed Systems Are Harder

A major complication is **partial failure**.

In a single-machine program, a process may simply crash. In a distributed system, some machines can continue operating while another machine is dead, slow, disconnected, or partitioned from the network.

Suppose machines A and B can communicate but C becomes unreachable. A and B can continue changing their state while C misses those changes. If C later returns, the system must decide how to reconcile its stale state.

This creates problems that do not appear in the same form inside a single process.

### Failure vs. slowness

If machine A sends a request to B and receives no response, A cannot conclude merely from that observation that B has crashed.

Possible explanations include:

- B crashed,
- B is overloaded,
- the request packet was lost,
- the response packet was lost,
- the network is congested,
- A and B are separated by a network partition,
- the communication is simply taking a long time.

This uncertainty becomes important later when studying failure detectors and membership protocols.

## 7. Scale Makes Failure Normal

Even if individual machines are reliable, a sufficiently large distributed system experiences failures frequently.

If each machine independently has probability `p` of failing during some period, then for `n` machines:

```text
P(no machines fail) = (1 - p)^n

P(at least one fails) = 1 - (1 - p)^n
```

### Example

If each of 100 machines has a 1% chance of failure during a week:

```text
P(at least one failure)
    = 1 - 0.99^100
    ≈ 0.634
    ≈ 63.4%
```

So a failure that is rare for one machine becomes ordinary at cluster scale. Distributed systems therefore need to be designed with failures in mind.

## 8. More Machines Do Not Mean Linear Speedup

A system using 10,000 machines is not automatically 10,000 times faster than one machine.

Reasons include:

### Communication overhead

Machines must exchange information over a network. Sending data, coordinating tasks, and combining results all consume time.

### Network latency and bandwidth

Local memory access is very different from transferring data across a network. For a small workload, distributing the data can cost more than simply processing it locally.

### Work may not be perfectly parallelizable

Some portions of an algorithm may depend on previous work and therefore cannot all execute simultaneously.

### Coordination overhead

Scheduling, synchronization, metadata management, failure recovery, and aggregation all add work that a single-machine implementation may not need.

This is why distributed processing is especially useful when the workload is large enough that the benefits of parallel work outweigh the cost of distribution.

---

# Midterm Checklist

You should be able to:

- Define a distributed system.
- Distinguish distributed computation from parallel computation.
- Explain why fault tolerance is not part of the definition of a distributed system.
- Explain elasticity and why it changes cloud economics.
- Distinguish public and private clouds.
- Calculate PUE and solve for total or IT power.
- Explain partial failure.
- Explain why a timeout does not prove that another machine has crashed.
- Calculate the probability that at least one of many machines fails.
- Explain why adding N machines does not generally produce an N-times speedup.

# Practice Problems

1. A datacenter consumes 900 kW total and 600 kW powers IT equipment. Calculate its PUE. Is a PUE of 1.25 more or less efficient?

2. A service needs 50 machines normally and 500 machines for two hours each day. Explain why elasticity can improve resource utilization.

3. A program uses 32 cores on one physical server. Is it necessarily a distributed system? Explain.

4. Machines A and B can communicate, but neither can reach C. List at least three possible explanations other than C having crashed.

5. Each machine in a 200-machine cluster has a 0.5% probability of failure during a day. Write the expression for the probability that at least one machine fails.

6. Explain why a 1,000-machine distributed implementation of an algorithm might be slower than a single-machine implementation for a tiny input.
