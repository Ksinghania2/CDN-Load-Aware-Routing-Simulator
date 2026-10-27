# Load-Aware CDN Routing Simulator

A small Python simulation that selects an edge-server entry from a fixed list using client-to-server Euclidean distance and a load penalty. It demonstrates a routing heuristic; it does not send network traffic or measure real CDN performance.

## Routing rule

For each configured server, the script computes `distance + 0.2 * load_pct`. Entries at 95% load or higher are skipped. The example uses four hard-coded locations and loads.

## Run

```bash
python cdn_simulator.py
```

## Scope and limitations

This is a standalone demonstration with static coordinates and load values, not a distributed CDN, health-check system, or production router. The coordinates are illustrative rather than geographic measurements. If every server is at or above the skip threshold, no route is selected and the current script does not handle that case.
