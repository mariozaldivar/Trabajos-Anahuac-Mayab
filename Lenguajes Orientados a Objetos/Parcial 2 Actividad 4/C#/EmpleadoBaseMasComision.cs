namespace SistemaNomina
{
    public class EmpleadoBaseMasComision : EmpleadoPorComision
    {
        private decimal _salarioBase;

        public decimal SalarioBase
        {
            get { return _salarioBase; }
            set { _salarioBase = value < 0 ? 0 : value; }
        }

        public EmpleadoBaseMasComision(string nombre, string apellido, string nss, decimal ventas, double tarifa, decimal salario)
            : base(nombre, apellido, nss, ventas, tarifa)
        {
            SalarioBase = salario;
        }

        public override decimal Ingresos() => SalarioBase + base.Ingresos();

        public override string ToString()
        {
            return $"con salario base {base.ToString()}; salario base: {SalarioBase:C}";
        }
    }
}



