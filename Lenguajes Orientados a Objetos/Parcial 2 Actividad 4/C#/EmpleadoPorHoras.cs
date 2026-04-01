namespace SistemaNomina
{
    public class EmpleadoPorHoras : Empleado
    {
        private decimal _sueldo;
        private double _horas;

        public decimal Sueldo
        {
            get { return _sueldo; }
            set { _sueldo = value < 0 ? 0 : value; }
        }

        public double Horas
        {
            get { return _horas; }
            set { _horas = (value >= 0 && value <= 168) ? value : 0; }
        }

        public EmpleadoPorHoras(string nombre, string apellido, string nss, decimal sueldoPorHoras, double horasTrabajadas)
            : base(nombre, apellido, nss)
        {
            Sueldo = sueldoPorHoras;
            Horas = horasTrabajadas;
        }

        public override decimal Ingresos()
        {
            if (Horas <= 40)
                return Sueldo * (decimal)Horas;
            
            return (40 * Sueldo) + ((decimal)Horas - 40) * Sueldo * 1.5m;
        }

        public override string ToString()
        {
            return $"empleado por horas: {base.ToString()}\nsueldo por hora: {Sueldo:C}; horas trabajadas: {Horas:F2}";
        }
    }
}






