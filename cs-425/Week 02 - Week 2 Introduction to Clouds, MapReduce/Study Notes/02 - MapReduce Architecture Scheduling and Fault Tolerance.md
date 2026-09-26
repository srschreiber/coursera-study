# Week 2 — MapReduce Architecture, Scheduling & Fault Tolerance Quick Reference

## Pipeline
```
HDFS input → Map → partition/sort → shuffle → group → Reduce → HDFS output
```

## Map vs. Reduce
- **Map:** processes an input record and emits intermediate key/value pairs.
- **Reduce:** processes a key and the collection of values associated with it.
- Same intermediate key must reach the **same reducer**.

## HDFS
- **NameNode:** filesystem metadata / where blocks are located.
- **DataNode:** stores actual HDFS blocks.
- Input blocks are replicated.

## YARN
- **ResourceManager (RM):** cluster-wide resource allocation/scheduling.
  - Course quiz fact: **Capacity Scheduler runs at the RM.**
- **ApplicationMaster (AM):** coordinates one application/job; requests resources.
- **NodeManager (NM):** runs on each worker and manages execution/resources there.
- **YARN container:** resource allocation (memory/vcores) used to run a task; **not a VM/Docker container**.

## Data locality
For map tasks, prefer:
```
node-local > rack-local > off-rack
```
- **Node-local:** mapper runs on a machine containing an input replica.
- **Rack-local:** mapper is on another machine in a rack containing a replica.
- **Off-rack:** data crosses racks.
- Check **all replicas** when deciding locality.
- Scheduler balances locality against keeping resources busy.

## Why racks matter
```
same rack:   server → ToR → server
cross rack:  server → ToR → higher network → ToR → server
```
Cross-rack transfers consume more shared network resources.

## Shuffle
- Mapper output is partitioned by reducer.
- Reducers fetch their partition from the mappers.
- This can create substantial network traffic.
- Reducers do not have the same simple input-locality advantage as mappers.

## Storage of outputs
- **Input:** HDFS, replicated/durable.
- **Map intermediate output:** mapper worker's local disk, temporary.
- **Final reduce output:** HDFS.

## Failure recovery
- Mapper dies while running → rerun mapper.
- Mapper worker dies after map finished → local intermediate output is lost → rerun mapper to regenerate it.
- Reducer dies → restart/re-execute reducer and refetch map outputs.
- Temporary data can often be **recomputed instead of replicated durably**.

## Stragglers
- **Straggler:** unusually slow task delaying job completion.
- **Speculative execution:** run another copy of a slow task elsewhere; use the successful result.
- Distinguish:
  - failure → task must be rerun;
  - straggler → duplicate may be launched speculatively.

## Heterogeneous workers
Giving identical container counts to machines with very different CPU/RAM can create slow tasks/stragglers.

## Terms worth recognizing
- **HDFS / NameNode / DataNode**
- **YARN**
- **ResourceManager / ApplicationMaster / NodeManager**
- **YARN container**
- **node-local / rack-local / off-rack**
- **shuffle**
- **partitioner**
- **straggler**
- **speculative execution**
- **recomputation**
