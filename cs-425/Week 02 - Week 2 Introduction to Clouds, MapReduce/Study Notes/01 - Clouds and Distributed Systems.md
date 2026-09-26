# Week 2 — Clouds & Distributed Systems Quick Reference

## Cloud basics
- **Cloud:** lots of compute + storage, with compute near the data.
- **Public cloud:** outside customers can rent resources.
- **Private cloud:** restricted to one organization.
- Core principle for data-heavy workloads: **move compute to data**.

## Datacenter architecture
- Servers are grouped into **racks**.
- Each rack typically connects through a **Top-of-Rack (ToR) switch**.
- Racks connect through higher-level/core network switches.
- **Same-rack traffic** stays nearer the ToR; **cross-rack traffic** traverses more shared network infrastructure.
- **Backend/storage nodes:** storage-heavy.
- **Front-end nodes:** receive client requests/jobs.
- **Geo-distributed cloud:** multiple datacenters/sites.

## Four characteristics of modern clouds
Memorize:
1. **Massive scale**
2. **On-demand access / elasticity**
3. **Data-intensive workloads**
4. **New programming paradigms** — MapReduce, key-value/NoSQL systems

## Service models
- **HaaS:** bare hardware.
- **IaaS:** virtual infrastructure/VMs; user controls OS/software.
- **PaaS:** managed runtime/platform; less control, easier management.
- **SaaS:** finished application.

## Datacenter efficiency
### PUE
```
PUE = total facility power / IT equipment power
```
- Minimum/theoretical ideal = **1**
- **Lower is better.**

### WUE
```
WUE = annual water usage / IT equipment energy
```
- Typically liters/kWh.
- **Lower is better.**

## Cloud economics
- Public cloud: usage-based cost, little upfront commitment, elastic.
- Private/owned infrastructure: upfront + hardware + power + networking + administration.
- **Break-even questions:** compare cumulative cloud cost against ownership/operating cost.
- Course historical cost rule of thumb: **45 hardware / 40 power / 15 network**.

## Course definition: distributed system
> Autonomous, programmable, asynchronous, failure-prone entities communicating through an unreliable communication medium.

Know every word:
- **Autonomous:** entities operate independently.
- **Programmable:** execute programs.
- **Asynchronous:** no perfectly synchronized global clock/timing assumption.
- **Failure-prone:** entities may crash independently.
- **Unreliable communication:** messages may be lost or delayed.

### Not required
- Does **not** need to appear as one computer.
- Does **not** need client/server architecture.

## Distributed vs. parallel
- Parallel: simultaneous computation, often tightly coupled.
- Distributed: autonomous asynchronous entities communicating by messages over an unreliable medium.
- A many-core machine can be parallel without being distributed under the course model.

## Partial failure
If A cannot hear from B, A cannot know from silence alone whether:
- B crashed,
- network/request/response failed,
- B is slow,
- network is partitioned/delayed.

**Silence != proof of failure.**

## Failure at scale
If each of `n` independent machines fails with probability `p`:
```
P(at least one failure) = 1 - (1-p)^n
```
At cloud scale, some failures become routine.

## Terms worth recognizing
- **Elasticity**
- **Data intensive vs. compute intensive**
- **ToR switch**
- **Rack**
- **Partial failure**
- **Clock skew/drift**
- **Scalability**
- **Concurrency**
- **Computing as a utility**
