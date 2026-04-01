namespace SistemaNomina
{
    public class EmpleadoPorPiezas : Empleado
    {
        private decimal _sueldoPorPieza;
        private int _piezas;

        public decimal SueldoPorPieza
        {
            get { return _sueldoPorPieza; }
            set { _sueldoPorPieza = value < 0 ? 0 : value; }
        }

        public int Piezas
        {
            get { return _piezas; }
            set { _piezas = value < 0 ? 0 : value; }
        }

        public EmpleadoPorPiezas(string nombre, string apellido, string nss, decimal sueldo, int cantidad)
            : base(nombre, apellido, nss)
        {
            SueldoPorPieza = sueldo;
            Piezas = cantidad;
        }

        public override decimal Ingresos() => SueldoPorPieza * Piezas;

        public override string ToString()
        {
            return $"empleado por piezas: {base.ToString()}\nsueldo por pieza: {SueldoPorPieza:C}; piezas: {Piezas}";
        }
    }
}



