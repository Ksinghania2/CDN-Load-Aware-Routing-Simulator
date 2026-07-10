import math

# Edge Registry: Global server distribution layout mapping coordinates and active workloads
EDGE_SERVERS = [
    {"name": "North-America-Edge", "x": 10.0, "y": 20.0, "load_pct": 85},
    {"name": "Europe-Edge",        "x": 70.0, "y": 80.0, "load_pct": 40},
    {"name": "Asia-Pacific-Edge",  "x": 120.0, "y": 30.0, "load_pct": 95},
    {"name": "India-Mumbai-Edge",  "x": 90.0, "y": 25.0, "load_pct": 30}
]

def calculate_distance(x1, y1, x2, y2):
    """Computes baseline geometric distance using the Euclidean formula."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def route_request(client_x, client_y):
    """Evaluates the optimal target edge server based on distance and workload limits."""
    print(f"\n[INCOMING REQUEST] Client Location: ({client_x}, {client_y})")
    print("-" * 65)
    
    best_server = None
    min_score = float('inf')

    for server in EDGE_SERVERS:
        # Compute spatial proximity
        distance = calculate_distance(client_x, client_y, server["x"], server["y"])
        
        # Load-Aware Routing Heuristic
        load_penalty = server["load_pct"] * 0.2
        routing_score = distance + load_penalty
        
        print(f"Server: {server['name']:20} | Dist: {distance:6.2f} | Load: {server['load_pct']}% | Score: {routing_score:6.2f}")
        
        if routing_score < min_score:
            # Circuit breaker condition for critically overloaded nodes
            if server["load_pct"] >= 95:
                print(f" -> [WARNING] Skipping {server['name']} due to critical overload threshold.")
                continue
            min_score = routing_score
            best_server = server

    print("-" * 65)
    print(f"[SUCCESS] Routed client request to: {best_server['name']}")

if __name__ == "__main__":
    # Simulate routing calculation for a client near local coordinate metrics
    route_request(client_x=95.0, client_y=22.0)