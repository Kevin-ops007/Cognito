import edu.princeton.cs.algs4.*;

public class Yourprim {
    public static void main(String[] args) {
        In in = new In(args[0]);
        EdgeWeightedGraph G = new EdgeWeightedGraph(in);

        /**
         * 1. Complete the Implementation of Lazy Prims algorithm exactly
         * according to the template that was provided in Week 7 of the labs
         * **/
        boolean[] marked = new boolean[G.V()]; // In the early Monday tutorial,  Boolean is a class whereas boolean is a primitive.
        Queue<Edge> mst = new Queue(); // A linked list could also work.

        marked[0] = true;

        while(true) {
            // In order to find a minimum crossing edge, we loop through all the edges in the graph and
            // add all of the crossing edges to a minimum priority queue.
            MinPQ<Edge> minpq = new MinPQ();
            for (Edge e: G.edges()){
                int u = e.either();
                int v = e.other(u);
                // B)  Check the condition if they are cross edges and insert to pq
                if((!marked[u] && marked[v]) || (marked[u] && !marked[v])) {
                    Edge crossedge = e;
                    minpq.insert(crossedge);
                }
            }

            // If the priority queue is empty, then this means there are no more crossing edges so we are done.
            if (minpq.isEmpty()) {
                break;
            }

            // If the priority queue is not empty, then the minimum element in it is a minimum crossing edge.
            if(!minpq.isEmpty()) {
                // C) get the edge minimum from pq
                Edge crossedge = minpq.delMin();

                // D) Update the (current) MST and  Mark the other vertex
                int u = crossedge.either();
                int v = crossedge.other(u);

                mst.enqueue(crossedge);
                if (!marked[u]) {
                    marked[u] = true;
                } else {
                    marked[v] = true;
                }
            }
        }
        // Once an MST has been found, print its edges and total weight.
        System.out.println("1) Edges in a Minimum Spanning are:");
        for(Edge e:mst){
            StdOut.println(e);
        }
        // E) Evaluate the weight of MST
        double w = 0;
        for(Edge e:mst){
            w += e.weight();
        }
        System.out.println("\nTotal weight is: " + String.format("%.4f", w) + "\n");

        /**
         * 2. Show how to modify your code to find a maximum (weight) spanning tree
         * of an edge-weighted graph.
         * **/
        MaxSpanningTree(G);
    }

    public static void MaxSpanningTree(EdgeWeightedGraph G){
        boolean[] marked = new boolean[G.V()]; // In the early Monday tutorial,  Boolean is a class whereas boolean is a primitive.
        Queue<Edge> mst = new Queue(); // A linked list could also work.

        marked[0] = true;

        while(true) {
            // In order to find a minimum crossing edge, we loop through all the edges in the graph and
            // add all of the crossing edges to a minimum priority queue.
            MinPQ<Edge> minpq = new MinPQ();
            for (Edge e: G.edges()){
                int u = e.either();
                int v = e.other(u);
                // B)  Check the condition if they are cross edges and insert to pq
                if((!marked[u] && marked[v]) || (marked[u] && !marked[v])) {
                    /** vvv Modified vvv **/
                    Edge max = new Edge(u, v, e.weight()*-1);
                    minpq.insert(max);
                    /** ^^^ Modified ^^^ **/
                }
            }

            // If the priority queue is empty, then this means there are no more crossing edges so we are done.
            if (minpq.isEmpty()) {
                break;
            }

            // If the priority queue is not empty, then the minimum element in it is a minimum crossing edge.
            if(!minpq.isEmpty()) {
                // C) get the edge minimum from pq
                Edge crossedge = minpq.delMin();

                // D) Update the (current) MST and  Mark the other vertex
                int u = crossedge.either();
                int v = crossedge.other(u);

                /**vvv Modified vvv**/
                Edge max = new Edge(u, v, crossedge.weight()*-1);
                mst.enqueue(max);
                /** ^^^ Modified ^^^ **/
                if (!marked[u]) {
                    marked[u] = true;
                } else {
                    marked[v] = true;
                }
            }
        }
        // Once an MST has been found, print its edges and total weight.
        System.out.println("2) Edges in a Maximum Spanning are:");
        for(Edge e:mst){
            StdOut.println(e);
        }
        // E) Evaluate the weight of MST
        double w = 0;
        for(Edge e:mst){
            w += e.weight();
        }
        System.out.println("\nTotal weight is: " + String.format("%.4f", w));
    }
}
