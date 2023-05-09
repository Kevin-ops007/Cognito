import edu.princeton.cs.algs4.*;

public class test{
    public static void main(String[] args) {
        In in = new In(args[0]);
        EdgeWeightedGraph G = new EdgeWeightedGraph(in);

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
                    // test
//                    Edge max = new Edge(u, v, e.weight()*-1);
//                    minpq.insert(max);
                    // test
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

                // test
//                Edge max = new Edge(u, v, crossedge.weight()*-1);
//                mst.enqueue(max);
                // test
                mst.enqueue(crossedge);
                if (!marked[u]) {
                    marked[u] = true;
                } else {
                    marked[v] = true;
                }
            }
        }
        // Once an MST has been found, print its edges and total weight.
        StdOut.print(mst);
        // E) Evaluate the weight of MST
        double w = 0;
        for(Edge e:mst){
            w += e.weight();
        }
        System.out.println("\nmst weight is: " + String.format("%.2f", w));
    }

    //find the error

    public static  void  hamilton(String[] args) {
        In in = new In(args[0]);
        Graph G = new Graph(in);
        Cycle finder = new Cycle(G);
        boolean flag=false;
        int c=1;
        if (finder.hasCycle()) {
            for (int v : finder.cycle()) {
                StdOut.print(v);
                c=c+1;
            }

            if (c==G.V())
            {
                flag=true;
                StdOut.print("\n YES! \n");
            }

            if (flag==false)
            {
                StdOut.print(" \n  NO! \n");
            }

            StdOut.println();
        }
        else {
            StdOut.println("Graph is acyclic");
        }
    }





    private static Object length(int v) {
        // TODO Auto-generated method stub
        return null;
    }





    private static Object size(int v) {
        // TODO Auto-generated method stub
        return null;
    }
}

