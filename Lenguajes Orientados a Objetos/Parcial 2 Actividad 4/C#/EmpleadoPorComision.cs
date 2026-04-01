namespace SistemaNomina
{
    public class EmpleadoPorComision : Empleado
    {
        private decimal _ventasBrutas;
        private double _tarifaComision;

        public decimal VentasBrutas
        {
            get { return _ventasBrutas; }
            set { _ventasBrutas = value < 0 ? 0 : value; }
        }

        public double TarifaComision
        {
            get { return _tarifaComision; }
            set { _tarifaComision = (value > 0 && value < 1) ? value : 0; }
        }

        public EmpleadoPorComision(string nombre, string apellido, string nss, decimal ventas, double tarifa)
            : base(nombre, apellido, nss)
        {
            VentasBrutas = ventas;
            TarifaComision = tarifa;
        }

        public override decimal Ingresos() => (decimal)TarifaComision * VentasBrutas;

        public override string ToString()
        {
            return $"empleado por comision: {base.ToString()}\nventas brutas: {VentasBrutas:C}; tarifa de comision: {TarifaComision:F2}";
        }
    }
}


