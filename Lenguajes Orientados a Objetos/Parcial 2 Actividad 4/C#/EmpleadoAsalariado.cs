namespace SistemaNomina
{
    public class EmpleadoAsalariado : Empleado
    {
        private decimal _salarioSemanal;

        public decimal SalarioSemanal
        {
            get { return _salarioSemanal; }
            set { _salarioSemanal = value < 0 ? 0 : value; }
        }

        public EmpleadoAsalariado(string nombre, string apellido, string nss, decimal salario)
            : base(nombre, apellido, nss)
        {
            SalarioSemanal = salario;
        }

        public override decimal Ingresos() => SalarioSemanal;

        public override string ToString()
        {
            return $"empleado asalariado: {base.ToString()}\nsalario semanal: {SalarioSemanal:C}";
        }
    }
}



