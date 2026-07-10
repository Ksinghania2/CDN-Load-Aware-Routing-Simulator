# Intelligent Content Delivery Network (CDN) Load-Aware Routing Simulator

A high-performance network infrastructure simulation engine engineered in Python to model real-time client traffic distribution across a distributed topological network of global edge nodes.

Rather than relying purely on static spatial proximity metrics, this engine implements an active load-aware routing heuristic. This strategy dynamically steers client request vectors toward the optimal server node, mitigating transit latency while preventing structural resource starvation across the infrastructure.

## Architectural Framework

1. Spatial Proximity Computation: Utilizes standard Euclidean distance formulations to calculate real-time geometric distance metrics between an incoming client request and target edge server nodes.

2. Load-Aware Latency Penalty Logic: Injects dynamic numerical routing penalties proportional to live server capacity statistics. This balances traffic distribution away from edge components encountering active load spikes.

3. Failover Defense System: Enforces automatic node circuit-breaking thresholds. Server units operating at critical system capacity (95% and above) are systematically dropped from the active routing pool to maintain network integrity.

## Deployment and Verification

Execute the standalone simulation engine using the native Python runtime via the command line interface:

```bash
python3 cdn_simulator.py