/**
 * Clase Arista - Representa una arista (conexión) de un grafo.
 * 
 * Conceptos reforzados:
 * - Arista como elemento de E(G) que conecta puntos extremos
 * - Bucle: arista con un solo punto extremo (extremo1 == extremo2)
 * - Aristas paralelas: dos aristas distintas con los mismos extremos
 * - Incidencia: una arista incide sobre cada uno de sus puntos extremos
 * 
 * @author Mario Andrés Zaldívar de la Cruz
 * @version 1.0
 * Periodo 202660
 */
public class Arista {

    // ============================
    // ATRIBUTOS
    // ============================
    private String nombre;     // Nombre de la arista (ej: "e1", "e2")
    private int id;            // Identificador numérico único
    private Vertice extremo1;  // Primer punto extremo
    private Vertice extremo2;  // Segundo punto extremo
    private boolean esBucle;   // true si extremo1 == extremo2

    // ============================
    // CONSTRUCTORES
    // ============================

    /**
     * Constructor vacío.
     * Inicializa la arista con valores por defecto.
     */
    public Arista() {
        this.nombre = "";
        this.id = 0;
        this.extremo1 = null;
        this.extremo2 = null;
        this.esBucle = false;
    }

    /**
     * Constructor parametrizado.
     * Determina automáticamente si la arista es un bucle.
     * 
     * @param nombre   Nombre de la arista (ej: "e1")
     * @param id       Identificador numérico único
     * @param extremo1 Primer vértice (punto extremo)
     * @param extremo2 Segundo vértice (punto extremo)
     */
    public Arista(String nombre, int id, Vertice extremo1, Vertice extremo2) {
        this.nombre = nombre;
        this.id = id;
        this.extremo1 = extremo1;
        this.extremo2 = extremo2;
        this.esBucle = mismoVertice(extremo1, extremo2);
    }

    // ============================
    // GETTERS
    // ============================

    public String getNombre() {
        return nombre;
    }

    public int getId() {
        return id;
    }

    public Vertice getExtremo1() {
        return extremo1;
    }

    public Vertice getExtremo2() {
        return extremo2;
    }

    public boolean esBucle() {
        return esBucle;
    }

    // ============================
    // MÉTODOS DE LÓGICA
    // ============================

    /**
     * Determina si esta arista es PARALELA a otra arista.
     * Dos aristas son paralelas si tienen el mismo conjunto de puntos extremos.
     * 
     * Ejemplo: e2{v1,v3} y e3{v1,v3} son paralelas.
     * 
     * @param otra La otra arista a comparar
     * @return true si ambas aristas comparten los mismos puntos extremos
     */
    public boolean esParalela(Arista otra) {
        if (otra == null || this.id == otra.id) {
            return false; // una arista no es paralela a sí misma
        }

        boolean mismoOrden = mismoVertice(this.extremo1, otra.extremo1)
                          && mismoVertice(this.extremo2, otra.extremo2);

        boolean ordenInverso = mismoVertice(this.extremo1, otra.extremo2)
                            && mismoVertice(this.extremo2, otra.extremo1);

        return mismoOrden || ordenInverso;
    }

    /**
     * Determina si esta arista INCIDE en un vértice dado.
     * Una arista incide sobre cada uno de sus puntos extremos.
     * 
     * @param v El vértice a verificar
     * @return true si el vértice es uno de los puntos extremos de esta arista
     */
    public boolean incideEn(Vertice v) {
        if (v == null) {
            return false;
        }
        return mismoVertice(extremo1, v) || mismoVertice(extremo2, v);
    }

    // ============================
    // MÉTODOS AUXILIARES
    // ============================

    /**
     * Compara dos vértices por id (o ambos null).
     * Comparar por id evita fallos si existen dos objetos Vertice
     * distintos que representan el mismo vértice.
     */
    private boolean mismoVertice(Vertice a, Vertice b) {
        if (a == null || b == null) {
            return a == b;
        }
        return a.getId() == b.getId();
    }

    /**
     * Devuelve el nombre del vértice, o "null" si no existe.
     */
    private String nombreDe(Vertice v) {
        return (v == null) ? "null" : v.getNombre();
    }

    /**
     * Representación en texto de la arista.
     * Formato: "e1: {v1, v2}" o "e6: {v5} [BUCLE]"
     */
    @Override
    public String toString() {
        if (esBucle) {
            return nombre + ": {" + nombreDe(extremo1) + "} [BUCLE]";
        }
        return nombre + ": {" + nombreDe(extremo1) + ", " + nombreDe(extremo2) + "}";
    }
}
