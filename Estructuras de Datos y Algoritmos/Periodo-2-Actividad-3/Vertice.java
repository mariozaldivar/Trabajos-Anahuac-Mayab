/**
 * Clase Vertice - Representa un vértice (nodo) de un grafo.
 * 
 * Conceptos reforzados:
 * - Vértice como elemento fundamental de un grafo V(G)
 * - Vértice aislado: no incide arista alguna
 * - Grado de un vértice: número de extremos de aristas que salen de él
 * 
 * @author Mario Andrés Zaldívar de la Cruz
 * @version 1.0
 * Periodo 202660
 */
public class Vertice {

    // ============================
    // ATRIBUTOS
    // ============================
    private String nombre;   // Nombre del vértice (ej: "v1", "v2")
    private int id;          // Identificador numérico único
    private int grado;       // Grado del vértice (se calcula desde Grafo)
    private boolean esAislado; // true si no incide arista alguna (grado == 0)

    // ============================
    // CONSTRUCTORES
    // ============================

    /**
     * Constructor vacío.
     * Inicializa el vértice con valores por defecto.
     */
    public Vertice() {
        this.nombre = ""; 
    this.id = 0; 
    this.grado = 0; 
    this.esAislado = true;
    }

    /**
     * Constructor parametrizado.
     * @param nombre Nombre del vértice (ej: "v1")
     * @param id Identificador numérico único
     */
    public Vertice(String nombre, int id) {
        // TODO: Asignar los parámetros a los atributos correspondientes
        // Inicializar grado en 0 y esAislado en true
      this.nombre = nombre; 
    this.id = id; 

    this.grado = 0; 
    this.esAislado = true;
    }

    // ============================
    // GETTERS Y SETTERS
    // ============================

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre; 
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id; 
    }

    public int getGrado() {
        return this.grado;
    }

    public void setGrado(int grado) {
    this.grado = grado;
    }

    public boolean esAislado() {
        // TODO: Retornar si el vértice es aislado
        return this.esAislado;
    }

    public void setEsAislado(boolean esAislado) {
    this.esAislado = esAislado; 
    }

    // ============================
    // MÉTODOS AUXILIARES
    // ============================

    /**
     * Representación en texto del vértice.
     * Formato esperado: "v1 (grado: 3)" o "v4 (grado: 0) [AISLADO]"
     */
    @Override
    public String toString() {
        // TODO: Retornar una cadena con el formato indicado
        // Si el vértice es aislado, agregar "[AISLADO]" al final
        String returnstring = "v" + this.id + " (grado: " + this.grado + ")";
        if (this.esAislado) {returnstring = returnstring + " [AISLADO]";}
    return returnstring;
    }
}
