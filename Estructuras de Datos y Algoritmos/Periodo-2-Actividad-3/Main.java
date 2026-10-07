/**
 * Prueba de Vertice, Arista y Grafo.
 *
 * @author Mario Andrés Zaldívar de la Cruz
 * Periodo 202660
 */
public class Main {

    public static void main(String[] args) {
        Vertice v1 = new Vertice("v1", 1);
        Vertice v2 = new Vertice("v2", 2);
        Vertice v3 = new Vertice("v3", 3);
        Vertice v4 = new Vertice("v4", 4);
        Vertice v5 = new Vertice("v5", 5);

        Grafo g = new Grafo("G");
        g.agregarVertice(v1);
        g.agregarVertice(v2);
        g.agregarVertice(v3);
        g.agregarVertice(v4);
        g.agregarVertice(v5);

        g.agregarArista(new Arista("e1", 1, v1, v2));
        g.agregarArista(new Arista("e2", 2, v1, v3));
        g.agregarArista(new Arista("e3", 3, v1, v3)); 
        g.agregarArista(new Arista("e4", 4, v5, v5)); 

        System.out.println(g);
        g.mostrarTablaExtremos();

        System.out.println("\nGrado total: " + g.calcularGradoTotal() + " (2 x |E| = 8)");
        System.out.println("deg(v1): " + g.calcularGrado(v1));
        System.out.println("deg(v5): " + g.calcularGrado(v5) + " (bucle cuenta 2)");

        System.out.println("Adyacentes a v1: " + g.obtenerAdyacentes(v1));
        System.out.println("Incidentes en v1: " + g.obtenerAristasIncidentes(v1));
        System.out.println("Bucles: " + g.obtenerBucles());
        System.out.println("Paralelas: " + g.obtenerParalelas());
        System.out.println("Aislados: " + g.obtenerVerticesAislados());
    }
}
