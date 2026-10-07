import java.util.ArrayList;

/**
 * Clase Grafo - Representa un grafo no dirigido G = (V, E).
 *
 * Conceptos reforzados:
 * - Grafo G con conjuntos V(G) de vértices y E(G) de aristas
 * - Función punto extremo-arista
 * - Grado de vértice (bucle cuenta doble)
 * - Teorema del Saludo de Mano: gradoTotal = 2 × |E|
 * - Corolario 10.1.2: El grado total de un grafo siempre es par
 *
 * @author Mario Andrés Zaldívar de la Cruz
 * @version 1.0
 * Periodo 202660
 */
public class Grafo {

    // ============================
    // ATRIBUTOS
    // ============================
    private String nombre;                  // Nombre del grafo
    private ArrayList<Vertice> vertices;    // Conjunto V(G)
    private ArrayList<Arista> aristas;      // Conjunto E(G)
    private int gradoTotal;                 // Suma de todos los grados

    // ============================
    // CONSTRUCTORES
    // ============================

    /**
     * Constructor vacío.
     */
    public Grafo() {
        this.nombre = "";
        this.gradoTotal = 0;
        this.vertices = new ArrayList<Vertice>();
        this.aristas = new ArrayList<Arista>();
    }

    /**
     * Constructor parametrizado.
     * @param nombre Nombre del grafo
     */
    public Grafo(String nombre) {
        this.nombre = nombre;
        this.gradoTotal = 0;
        this.vertices = new ArrayList<Vertice>();
        this.aristas = new ArrayList<Arista>();
    }

    // ============================
    // MÉTODOS DE CONSTRUCCIÓN
    // ============================

    /**
     * Agrega un vértice al conjunto V(G) del grafo.
     * @param v Vértice a agregar
     */
    public void agregarVertice(Vertice v) {
        this.vertices.add(v);
    }

    /**
     * Agrega una arista al conjunto E(G) del grafo.
     * @param a Arista a agregar
     */
    public void agregarArista(Arista a) {
        this.aristas.add(a);
    }

    // ============================
    // MÉTODOS DE GRADO
    // ============================

    /**
     * Calcula el GRADO de un vértice.
     *
     * REGLA CLAVE: Un bucle contribuye con 2 al grado del vértice.
     * Una arista normal que incide en v contribuye con 1.
     *
     * Ejemplo del documento:
     * - v3 tiene aristas e1, e2 incidentes + e3 (bucle) → deg(v3) = 2 + 2 = 4
     *
     * @param v Vértice al que se le calculará el grado
     * @return El grado del vértice
     */
    public int calcularGrado(Vertice v) {
        int grado = 0;

        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                if (a.esBucle()) {
                    grado += 2;   // el bucle cuenta doble
                } else {
                    grado += 1;
                }
            }
        }

        v.setGrado(grado);
        v.setEsAislado(grado == 0);
        return grado;
    }

    /**
     * Calcula el GRADO TOTAL del grafo.
     * Es la suma de los grados de todos los vértices.
     *
     * @return El grado total del grafo
     */
    public int calcularGradoTotal() {
        gradoTotal = 0;

        for (Vertice v : vertices) {
            gradoTotal += calcularGrado(v);
        }

        return gradoTotal;
    }

    // ============================
    // MÉTODOS DE TERMINOLOGÍA
    // ============================

    /**
     * Obtiene todos los vértices ADYACENTES a un vértice dado.
     * Dos vértices son adyacentes si están conectados por una arista.
     * Si v tiene un bucle, v es adyacente a sí mismo.
     *
     * @param v Vértice de referencia
     * @return Lista de vértices adyacentes a v
     */
    public ArrayList<Vertice> obtenerAdyacentes(Vertice v) {
        ArrayList<Vertice> adyacentes = new ArrayList<>();

        for (Arista a : aristas) {
            if (!a.incideEn(v)) {
                continue;
            }

            Vertice otro;
            if (a.esBucle()) {
                otro = v;                       // adyacente a sí mismo
            } else if (a.getExtremo1().getId() == v.getId()) {
                otro = a.getExtremo2();
            } else {
                otro = a.getExtremo1();
            }

            if (!adyacentes.contains(otro)) {
                adyacentes.add(otro);
            }
        }

        return adyacentes;
    }

    /**
     * Obtiene todas las aristas que INCIDEN en un vértice dado.
     * Una arista incide sobre cada uno de sus puntos extremos.
     *
     * @param v Vértice de referencia
     * @return Lista de aristas incidentes en v
     */
    public ArrayList<Arista> obtenerAristasIncidentes(Vertice v) {
        ArrayList<Arista> incidentes = new ArrayList<>();

        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                incidentes.add(a);
            }
        }

        return incidentes;
    }

    /**
     * Obtiene todas las aristas ADYACENTES a una arista dada.
     * Dos aristas son adyacentes si comparten al menos un punto extremo.
     *
     * @param a Arista de referencia
     * @return Lista de aristas adyacentes a la arista a
     */
    public ArrayList<Arista> obtenerAristasAdyacentes(Arista a) {
        ArrayList<Arista> adyacentes = new ArrayList<>();

        for (Arista b : aristas) {
            if (b == a) {
                continue; // una arista no es adyacente a sí misma
            }
            if (b.incideEn(a.getExtremo1()) || b.incideEn(a.getExtremo2())) {
                adyacentes.add(b);
            }
        }

        return adyacentes;
    }

    /**
     * Obtiene todos los BUCLES del grafo.
     * Un bucle es una arista con un solo punto extremo.
     *
     * @return Lista de aristas que son bucles
     */
    public ArrayList<Arista> obtenerBucles() {
        ArrayList<Arista> bucles = new ArrayList<>();

        for (Arista a : aristas) {
            if (a.esBucle()) {
                bucles.add(a);
            }
        }

        return bucles;
    }

    /**
     * Obtiene los pares de aristas PARALELAS del grafo.
     * Dos aristas son paralelas si tienen el mismo conjunto de puntos extremos.
     *
     * @return Lista de cadenas describiendo los pares paralelos
     */
    public ArrayList<String> obtenerParalelas() {
        ArrayList<String> paralelas = new ArrayList<>();

        for (int i = 0; i < aristas.size(); i++) {
            for (int j = i + 1; j < aristas.size(); j++) {
                Arista ai = aristas.get(i);
                Arista aj = aristas.get(j);
                if (ai.esParalela(aj)) {
                    paralelas.add("{" + ai.getNombre() + ", " + aj.getNombre() + "}");
                }
            }
        }

        return paralelas;
    }

    /**
     * Obtiene todos los vértices AISLADOS del grafo.
     * Un vértice aislado es aquel en el que no incide arista alguna (grado = 0).
     *
     * @return Lista de vértices aislados
     */
    public ArrayList<Vertice> obtenerVerticesAislados() {
        ArrayList<Vertice> aislados = new ArrayList<>();

        // Se recalcula el grado aquí para no depender de que
        // calcularGradoTotal() se haya llamado antes.
        for (Vertice v : vertices) {
            if (calcularGrado(v) == 0) {
                aislados.add(v);
            }
        }

        return aislados;
    }

    // ============================
    // MÉTODOS DE PRESENTACIÓN
    // ============================

    /**
     * Muestra la TABLA DE FUNCIÓN PUNTO EXTREMO-ARISTA.
     *
     * Formato esperado:
     * | Arista | Punto(s) Extremo(s) |
     * |--------|---------------------|
     * | e1     | {v1, v2}            |
     * | e6     | {v5} [BUCLE]        |
     */
    public void mostrarTablaExtremos() {
        System.out.println("\n--- Tabla Punto Extremo - Arista ---");
        System.out.printf("| %-8s | %-22s |%n", "Arista", "Punto(s) Extremo(s)");
        System.out.println("|----------|------------------------|");

        for (Arista a : aristas) {
            String extremos;
            if (a.esBucle()) {
                extremos = "{" + a.getExtremo1().getNombre() + "} [BUCLE]";
            } else {
                extremos = "{" + a.getExtremo1().getNombre() + ", "
                         + a.getExtremo2().getNombre() + "}";
            }
            System.out.printf("| %-8s | %-22s |%n", a.getNombre(), extremos);
        }
    }


    // ============================
    // MÉTODOS AUXILIARES
    // ============================

    /**
     * Representación en texto del grafo.
     * Muestra: nombre, cantidad de vértices y aristas.
     */
    @Override
    public String toString() {
        return "Grafo " + nombre + ": |V| = " + vertices.size()
             + ", |E| = " + aristas.size();
    }
}
