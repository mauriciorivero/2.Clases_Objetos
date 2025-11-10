"""
TEMA 5: POLIMORFISMO EN PROGRAMACIÓN ORIENTADA A OBJETOS
=========================================================

El POLIMORFISMO es la capacidad de objetos de diferentes clases de responder 
al mismo mensaje (método) de diferentes maneras.

En términos simples: "Una interfaz, múltiples implementaciones"

TIPOS DE POLIMORFISMO EN PYTHON:

1. POLIMORFISMO DE SUBTIPOS (mediante herencia):
   - Objetos de diferentes clases hijas pueden ser tratados como objetos de la clase padre
   - Cada clase hija puede implementar métodos de forma diferente

2. DUCK TYPING (polimorfismo implícito):
   - "Si camina como pato y grazna como pato, entonces es un pato"
   - Python no verifica el tipo, solo que el objeto tenga los métodos necesarios

3. SOBRECARGA DE OPERADORES:
   - Permitir que operadores (+, -, *, etc.) funcionen con objetos personalizados

Este ejemplo usa un sistema de nómina con diferentes tipos de empleados
para demostrar el polimorfismo.
"""


class Empleado:
    """
    CLASE BASE: Empleado
    
    Esta es la clase padre que define la interfaz común para todos los empleados.
    Define métodos que DEBEN ser implementados por las subclases.
    """
    
    # Contador de empleados
    contador_empleados = 0
    
    def __init__(self, nombre, identificacion, fecha_ingreso):
        """
        Constructor base para todos los empleados.
        
        Parámetros:
            nombre (str): nombre completo del empleado
            identificacion (str): número de identificación
            fecha_ingreso (str): fecha de ingreso en formato "DD/MM/AAAA"
        """
        self.nombre = nombre
        self.identificacion = identificacion
        self.fecha_ingreso = fecha_ingreso
        self.activo = True
        
        Empleado.contador_empleados += 1
        self.numero_empleado = Empleado.contador_empleados
        
        print(f"✓ Empleado #{self.numero_empleado} registrado: {nombre}")
    
    def calcular_salario(self):
        """
        Método BASE que debe ser implementado por cada subclase.
        
        Este es el método clave para demostrar POLIMORFISMO.
        Cada tipo de empleado calculará su salario de forma diferente.
        
        Returns:
            float: salario calculado
        
        Nota: En una implementación real, este sería un método abstracto
        que OBLIGA a las subclases a implementarlo.
        """
        raise NotImplementedError("Las subclases deben implementar calcular_salario()")
    
    def mostrar_informacion(self):
        """
        Muestra información básica del empleado.
        
        Este método puede ser sobrescrito por las subclases para agregar más información.
        """
        return f"""
        --- Empleado #{self.numero_empleado} ---
        Tipo: {self.__class__.__name__}
        Nombre: {self.nombre}
        ID: {self.identificacion}
        Fecha de ingreso: {self.fecha_ingreso}
        Estado: {'Activo' if self.activo else 'Inactivo'}
        """
    
    def trabajar(self):
        """Método común a todos los empleados."""
        return f"{self.nombre} está trabajando 💼"
    
    def tomar_descanso(self):
        """Método común a todos los empleados."""
        return f"{self.nombre} está tomando un descanso ☕"
    
    def __str__(self):
        """Representación en string del empleado."""
        return f"{self.__class__.__name__}: {self.nombre}"


class EmpleadoTiempoCompleto(Empleado):
    """
    SUBCLASE: Empleado de Tiempo Completo
    
    Estos empleados tienen un salario mensual fijo.
    
    POLIMORFISMO: Implementa calcular_salario() de forma específica.
    """
    
    def __init__(self, nombre, identificacion, fecha_ingreso, salario_mensual):
        """
        Constructor para empleado de tiempo completo.
        
        Parámetros:
            nombre (str): nombre del empleado
            identificacion (str): ID del empleado
            fecha_ingreso (str): fecha de ingreso
            salario_mensual (float): salario mensual fijo
        """
        super().__init__(nombre, identificacion, fecha_ingreso)
        self.salario_mensual = salario_mensual
        self.beneficios = []
        print(f"  → Tipo: Tiempo Completo | Salario mensual: ${salario_mensual:,.2f}")
    
    def calcular_salario(self):
        """
        IMPLEMENTACIÓN POLIMÓRFICA de calcular_salario().
        
        Para empleados de tiempo completo, el salario es simplemente el salario mensual.
        
        Returns:
            float: salario mensual fijo
        """
        return self.salario_mensual
    
    def agregar_beneficio(self, beneficio, valor):
        """
        Agrega un beneficio adicional al empleado.
        
        Parámetros:
            beneficio (str): nombre del beneficio
            valor (float): valor monetario del beneficio
        """
        self.beneficios.append({"nombre": beneficio, "valor": valor})
        print(f"Beneficio agregado a {self.nombre}: {beneficio} (${valor:,.2f})")
    
    def calcular_salario_con_beneficios(self):
        """
        Calcula el salario total incluyendo beneficios.
        
        Returns:
            float: salario mensual + beneficios
        """
        salario_base = self.calcular_salario()
        total_beneficios = sum(b["valor"] for b in self.beneficios)
        return salario_base + total_beneficios
    
    def mostrar_informacion(self):
        """SOBRESCRITURA que extiende el método base."""
        info = super().mostrar_informacion()
        info += f"        Salario mensual: ${self.salario_mensual:,.2f}\n"
        if self.beneficios:
            info += "        Beneficios:\n"
            for beneficio in self.beneficios:
                info += f"          - {beneficio['nombre']}: ${beneficio['valor']:,.2f}\n"
            info += f"        Salario total: ${self.calcular_salario_con_beneficios():,.2f}\n"
        return info


class EmpleadoPorHoras(Empleado):
    """
    SUBCLASE: Empleado por Horas
    
    Estos empleados cobran por hora trabajada.
    
    POLIMORFISMO: Implementa calcular_salario() basándose en horas trabajadas.
    """
    
    def __init__(self, nombre, identificacion, fecha_ingreso, tarifa_por_hora):
        """
        Constructor para empleado por horas.
        
        Parámetros:
            nombre (str): nombre del empleado
            identificacion (str): ID del empleado
            fecha_ingreso (str): fecha de ingreso
            tarifa_por_hora (float): pago por cada hora trabajada
        """
        super().__init__(nombre, identificacion, fecha_ingreso)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = 0
        self.horas_extra = 0
        print(f"  → Tipo: Por Horas | Tarifa: ${tarifa_por_hora:,.2f}/hora")
    
    def registrar_horas(self, horas, son_extra=False):
        """
        Registra horas trabajadas.
        
        Parámetros:
            horas (float): número de horas trabajadas
            son_extra (bool): True si son horas extra (pagan más)
        """
        if son_extra:
            self.horas_extra += horas
            print(f"✓ {horas} horas EXTRA registradas para {self.nombre}")
        else:
            self.horas_trabajadas += horas
            print(f"✓ {horas} horas normales registradas para {self.nombre}")
    
    def calcular_salario(self):
        """
        IMPLEMENTACIÓN POLIMÓRFICA de calcular_salario().
        
        Para empleados por horas, el salario depende de las horas trabajadas.
        Las horas extra se pagan al 150% (1.5x la tarifa normal).
        
        Returns:
            float: salario calculado según horas trabajadas
        """
        salario_normal = self.horas_trabajadas * self.tarifa_por_hora
        salario_extra = self.horas_extra * self.tarifa_por_hora * 1.5
        return salario_normal + salario_extra
    
    def resetear_horas(self):
        """Reinicia el contador de horas para el nuevo período."""
        self.horas_trabajadas = 0
        self.horas_extra = 0
        print(f"Horas de {self.nombre} reiniciadas para nuevo período")
    
    def mostrar_informacion(self):
        """SOBRESCRITURA que extiende el método base."""
        info = super().mostrar_informacion()
        info += f"        Tarifa por hora: ${self.tarifa_por_hora:,.2f}\n"
        info += f"        Horas normales trabajadas: {self.horas_trabajadas}\n"
        info += f"        Horas extra trabajadas: {self.horas_extra}\n"
        info += f"        Salario calculado: ${self.calcular_salario():,.2f}\n"
        return info


class EmpleadoPorComision(Empleado):
    """
    SUBCLASE: Empleado por Comisión
    
    Estos empleados tienen un salario base pequeño + comisiones por ventas.
    
    POLIMORFISMO: Implementa calcular_salario() basándose en ventas realizadas.
    """
    
    def __init__(self, nombre, identificacion, fecha_ingreso, salario_base, porcentaje_comision):
        """
        Constructor para empleado por comisión.
        
        Parámetros:
            nombre (str): nombre del empleado
            identificacion (str): ID del empleado
            fecha_ingreso (str): fecha de ingreso
            salario_base (float): salario base mínimo
            porcentaje_comision (float): porcentaje de comisión sobre ventas (ej: 0.05 = 5%)
        """
        super().__init__(nombre, identificacion, fecha_ingreso)
        self.salario_base = salario_base
        self.porcentaje_comision = porcentaje_comision
        self.ventas = []  # Lista de montos de ventas realizadas
        print(f"  → Tipo: Comisión | Base: ${salario_base:,.2f} + {porcentaje_comision*100}% comisión")
    
    def registrar_venta(self, monto):
        """
        Registra una venta realizada por el empleado.
        
        Parámetros:
            monto (float): monto de la venta
        """
        self.ventas.append(monto)
        print(f"✓ Venta de ${monto:,.2f} registrada para {self.nombre}")
    
    def calcular_total_ventas(self):
        """
        Calcula el total de ventas realizadas.
        
        Returns:
            float: suma total de ventas
        """
        return sum(self.ventas)
    
    def calcular_comision(self):
        """
        Calcula la comisión ganada sobre las ventas.
        
        Returns:
            float: comisión calculada
        """
        total_ventas = self.calcular_total_ventas()
        return total_ventas * self.porcentaje_comision
    
    def calcular_salario(self):
        """
        IMPLEMENTACIÓN POLIMÓRFICA de calcular_salario().
        
        Para empleados por comisión, el salario es:
        salario_base + (ventas_totales * porcentaje_comision)
        
        Returns:
            float: salario base + comisiones
        """
        return self.salario_base + self.calcular_comision()
    
    def resetear_ventas(self):
        """Reinicia el registro de ventas para el nuevo período."""
        self.ventas = []
        print(f"Ventas de {self.nombre} reiniciadas para nuevo período")
    
    def mostrar_informacion(self):
        """SOBRESCRITURA que extiende el método base."""
        info = super().mostrar_informacion()
        info += f"        Salario base: ${self.salario_base:,.2f}\n"
        info += f"        Porcentaje de comisión: {self.porcentaje_comision*100}%\n"
        info += f"        Total de ventas: ${self.calcular_total_ventas():,.2f}\n"
        info += f"        Comisión ganada: ${self.calcular_comision():,.2f}\n"
        info += f"        Salario total: ${self.calcular_salario():,.2f}\n"
        return info


class EmpleadoFreelance(Empleado):
    """
    SUBCLASE: Empleado Freelance
    
    Estos empleados cobran por proyecto completado.
    
    POLIMORFISMO: Implementa calcular_salario() basándose en proyectos completados.
    """
    
    def __init__(self, nombre, identificacion, fecha_ingreso):
        """Constructor para empleado freelance."""
        super().__init__(nombre, identificacion, fecha_ingreso)
        self.proyectos = []  # Lista de proyectos: {"nombre": str, "pago": float, "completado": bool}
        print(f"  → Tipo: Freelance | Pago por proyecto")
    
    def agregar_proyecto(self, nombre_proyecto, pago):
        """
        Agrega un nuevo proyecto al freelancer.
        
        Parámetros:
            nombre_proyecto (str): nombre del proyecto
            pago (float): pago acordado por el proyecto
        """
        proyecto = {
            "nombre": nombre_proyecto,
            "pago": pago,
            "completado": False
        }
        self.proyectos.append(proyecto)
        print(f"✓ Proyecto '{nombre_proyecto}' asignado a {self.nombre} (${pago:,.2f})")
    
    def completar_proyecto(self, nombre_proyecto):
        """
        Marca un proyecto como completado.
        
        Parámetros:
            nombre_proyecto (str): nombre del proyecto a marcar como completado
        """
        for proyecto in self.proyectos:
            if proyecto["nombre"] == nombre_proyecto and not proyecto["completado"]:
                proyecto["completado"] = True
                print(f"✓ Proyecto '{nombre_proyecto}' completado por {self.nombre}")
                return True
        print(f"❌ Proyecto '{nombre_proyecto}' no encontrado o ya completado")
        return False
    
    def calcular_salario(self):
        """
        IMPLEMENTACIÓN POLIMÓRFICA de calcular_salario().
        
        Para freelancers, el salario es la suma de todos los proyectos completados.
        
        Returns:
            float: suma del pago de proyectos completados
        """
        total = sum(p["pago"] for p in self.proyectos if p["completado"])
        return total
    
    def mostrar_informacion(self):
        """SOBRESCRITURA que extiende el método base."""
        info = super().mostrar_informacion()
        info += f"        Total de proyectos: {len(self.proyectos)}\n"
        
        proyectos_completados = [p for p in self.proyectos if p["completado"]]
        proyectos_pendientes = [p for p in self.proyectos if not p["completado"]]
        
        info += f"        Proyectos completados: {len(proyectos_completados)}\n"
        if proyectos_completados:
            for p in proyectos_completados:
                info += f"          ✓ {p['nombre']}: ${p['pago']:,.2f}\n"
        
        info += f"        Proyectos pendientes: {len(proyectos_pendientes)}\n"
        if proyectos_pendientes:
            for p in proyectos_pendientes:
                info += f"          ○ {p['nombre']}: ${p['pago']:,.2f}\n"
        
        info += f"        Salario total (completados): ${self.calcular_salario():,.2f}\n"
        return info


# ============================================================================
# SISTEMA DE NÓMINA (Demuestra el uso del polimorfismo)
# ============================================================================

class SistemaNomina:
    """
    Sistema de nómina que demuestra el POLIMORFISMO en acción.
    
    Este sistema puede procesar diferentes tipos de empleados
    sin necesitar saber el tipo específico de cada uno.
    """
    
    def __init__(self, nombre_empresa):
        """
        Constructor del sistema de nómina.
        
        Parámetros:
            nombre_empresa (str): nombre de la empresa
        """
        self.nombre_empresa = nombre_empresa
        self.empleados = []
        print(f"\n{'='*70}")
        print(f"Sistema de Nómina Inicializado: {nombre_empresa}")
        print(f"{'='*70}\n")
    
    def agregar_empleado(self, empleado):
        """
        Agrega un empleado al sistema.
        
        Parámetros:
            empleado (Empleado): cualquier objeto que herede de Empleado
        """
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)
            print(f"✓ {empleado.nombre} agregado al sistema de nómina")
        else:
            print("❌ Error: Solo se pueden agregar objetos de tipo Empleado")
    
    def calcular_nomina_total(self):
        """
        DEMOSTRACIÓN DE POLIMORFISMO:
        
        Este método llama a calcular_salario() en cada empleado,
        sin importar qué tipo específico de empleado sea.
        
        Cada tipo de empleado responderá al mismo mensaje (calcular_salario)
        de forma diferente, según su propia implementación.
        
        Returns:
            float: suma total de todos los salarios
        """
        total = 0
        print(f"\n{'─'*70}")
        print(f"Calculando nómina para: {self.nombre_empresa}")
        print(f"{'─'*70}")
        
        for empleado in self.empleados:
            # AQUÍ OCURRE EL POLIMORFISMO:
            # calcular_salario() se ejecuta de forma diferente según el tipo de empleado
            salario = empleado.calcular_salario()
            total += salario
            
            # Mostrar desglose
            tipo = empleado.__class__.__name__
            print(f"{empleado.nombre:.<30} [{tipo:.<25}] ${salario:>10,.2f}")
        
        print(f"{'─'*70}")
        print(f"{'TOTAL NÓMINA':.<55} ${total:>10,.2f}")
        print(f"{'─'*70}\n")
        
        return total
    
    def generar_reporte_detallado(self):
        """
        Genera un reporte detallado de todos los empleados.
        
        OTRO EJEMPLO DE POLIMORFISMO:
        Llama a mostrar_informacion() en cada empleado.
        """
        print(f"\n{'='*70}")
        print(f"REPORTE DETALLADO DE EMPLEADOS - {self.nombre_empresa}")
        print(f"{'='*70}")
        
        for empleado in self.empleados:
            # Polimorfismo: cada tipo de empleado muestra su información de forma específica
            print(empleado.mostrar_informacion())
    
    def listar_empleados_por_tipo(self):
        """Lista empleados agrupados por tipo."""
        from collections import defaultdict
        
        por_tipo = defaultdict(list)
        for emp in self.empleados:
            tipo = emp.__class__.__name__
            por_tipo[tipo].append(emp)
        
        print(f"\n{'='*70}")
        print(f"EMPLEADOS POR TIPO - {self.nombre_empresa}")
        print(f"{'='*70}\n")
        
        for tipo, empleados in por_tipo.items():
            print(f"{tipo}: {len(empleados)} empleado(s)")
            for emp in empleados:
                print(f"  - {emp.nombre}")
            print()
    
    def obtener_estadisticas(self):
        """Genera estadísticas del sistema de nómina."""
        if not self.empleados:
            print("No hay empleados en el sistema")
            return
        
        nomina_total = sum(emp.calcular_salario() for emp in self.empleados)
        promedio = nomina_total / len(self.empleados)
        salario_max = max(emp.calcular_salario() for emp in self.empleados)
        salario_min = min(emp.calcular_salario() for emp in self.empleados)
        
        print(f"\n{'='*70}")
        print(f"ESTADÍSTICAS - {self.nombre_empresa}")
        print(f"{'='*70}")
        print(f"Total de empleados: {len(self.empleados)}")
        print(f"Nómina total: ${nomina_total:,.2f}")
        print(f"Salario promedio: ${promedio:,.2f}")
        print(f"Salario más alto: ${salario_max:,.2f}")
        print(f"Salario más bajo: ${salario_min:,.2f}")
        print(f"{'='*70}\n")


# ============================================================================
# DEMOSTRACIÓN DE USO
# ============================================================================

def demostrar_polimorfismo_basico():
    """Demuestra el polimorfismo básico con diferentes tipos de empleados."""
    print("="*70)
    print("1. POLIMORFISMO BÁSICO - Diferentes implementaciones del mismo método")
    print("="*70)
    
    # Crear diferentes tipos de empleados
    print("\n--- Creando empleados ---")
    emp1 = EmpleadoTiempoCompleto("Ana García", "TC001", "01/01/2023", 3500.00)
    emp2 = EmpleadoPorHoras("Carlos Ruiz", "PH001", "15/03/2023", 25.00)
    emp3 = EmpleadoPorComision("María López", "COM001", "10/02/2023", 1000.00, 0.08)
    emp4 = EmpleadoFreelance("Roberto Silva", "FR001", "01/06/2023")
    
    # Configurar datos específicos de cada empleado
    print("\n--- Configurando datos ---")
    emp2.registrar_horas(160)  # 160 horas normales
    emp2.registrar_horas(20, son_extra=True)  # 20 horas extra
    
    emp3.registrar_venta(10000)
    emp3.registrar_venta(15000)
    emp3.registrar_venta(8000)
    
    emp4.agregar_proyecto("Sitio Web Corporativo", 5000)
    emp4.agregar_proyecto("App Móvil", 8000)
    emp4.completar_proyecto("Sitio Web Corporativo")
    
    # DEMOSTRACIÓN DE POLIMORFISMO:
    # Todos responden al método calcular_salario() de forma diferente
    print("\n--- POLIMORFISMO EN ACCIÓN ---")
    print("Todos los empleados responden a calcular_salario() de forma diferente:\n")
    
    empleados = [emp1, emp2, emp3, emp4]
    
    for empleado in empleados:
        # La misma llamada (calcular_salario) produce resultados diferentes
        # según el tipo de empleado
        salario = empleado.calcular_salario()
        print(f"{empleado.__class__.__name__:.<30} {empleado.nombre:.<20} ${salario:>10,.2f}")


def demostrar_sistema_nomina_completo():
    """Demuestra un sistema de nómina completo usando polimorfismo."""
    print("\n" + "="*70)
    print("2. SISTEMA DE NÓMINA COMPLETO - Polimorfismo en un sistema real")
    print("="*70)
    
    # Crear sistema de nómina
    sistema = SistemaNomina("TechSolutions S.A.")
    
    # Crear y agregar empleados de diferentes tipos
    print("\n--- Creando empleados ---\n")
    
    # Empleados de tiempo completo
    emp_tc1 = EmpleadoTiempoCompleto("Laura Martínez", "TC001", "01/01/2020", 4000.00)
    emp_tc1.agregar_beneficio("Bono de transporte", 200.00)
    emp_tc1.agregar_beneficio("Seguro médico", 300.00)
    
    emp_tc2 = EmpleadoTiempoCompleto("Diego Torres", "TC002", "15/06/2021", 3800.00)
    emp_tc2.agregar_beneficio("Bono de transporte", 200.00)
    
    # Empleados por horas
    emp_ph1 = EmpleadoPorHoras("Sandra Ramírez", "PH001", "10/03/2022", 28.00)
    emp_ph1.registrar_horas(150)
    emp_ph1.registrar_horas(15, son_extra=True)
    
    emp_ph2 = EmpleadoPorHoras("Miguel Ángel Cruz", "PH002", "20/08/2022", 22.00)
    emp_ph2.registrar_horas(180)
    emp_ph2.registrar_horas(10, son_extra=True)
    
    # Empleados por comisión
    emp_com1 = EmpleadoPorComision("Patricia Morales", "COM001", "05/01/2021", 1200.00, 0.10)
    emp_com1.registrar_venta(15000)
    emp_com1.registrar_venta(22000)
    emp_com1.registrar_venta(18000)
    emp_com1.registrar_venta(12000)
    
    emp_com2 = EmpleadoPorComision("Fernando Vargas", "COM002", "12/04/2021", 1000.00, 0.12)
    emp_com2.registrar_venta(25000)
    emp_com2.registrar_venta(30000)
    
    # Freelancers
    emp_fr1 = EmpleadoFreelance("Gabriela Herrera", "FR001", "01/09/2023")
    emp_fr1.agregar_proyecto("Diseño UI/UX", 4000)
    emp_fr1.agregar_proyecto("Landing Page", 2500)
    emp_fr1.agregar_proyecto("Logo empresarial", 1500)
    emp_fr1.completar_proyecto("Diseño UI/UX")
    emp_fr1.completar_proyecto("Landing Page")
    
    emp_fr2 = EmpleadoFreelance("Andrés Mendoza", "FR002", "15/10/2023")
    emp_fr2.agregar_proyecto("Sistema de inventario", 12000)
    emp_fr2.completar_proyecto("Sistema de inventario")
    
    # Agregar todos al sistema
    print("\n--- Agregando empleados al sistema ---\n")
    todos_empleados = [emp_tc1, emp_tc2, emp_ph1, emp_ph2, emp_com1, emp_com2, emp_fr1, emp_fr2]
    for emp in todos_empleados:
        sistema.agregar_empleado(emp)
    
    # POLIMORFISMO: El sistema procesa todos los empleados de forma uniforme
    sistema.calcular_nomina_total()
    sistema.listar_empleados_por_tipo()
    sistema.obtener_estadisticas()
    sistema.generar_reporte_detallado()


def demostrar_duck_typing():
    """
    Demuestra el Duck Typing (polimorfismo sin herencia).
    
    "Si camina como pato y grazna como pato, entonces es un pato"
    """
    print("\n" + "="*70)
    print("3. DUCK TYPING - Polimorfismo sin herencia")
    print("="*70)
    
    # Clases que NO heredan de una clase común,
    # pero implementan los mismos métodos
    
    class Perro:
        def hacer_sonido(self):
            return "¡Guau guau!"
    
    class Gato:
        def hacer_sonido(self):
            return "¡Miau miau!"
    
    class Vaca:
        def hacer_sonido(self):
            return "¡Muuu!"
    
    class Radio:
        """Clase completamente diferente, pero tiene hacer_sonido()"""
        def hacer_sonido(self):
            return "♪♫ Música ♪♫"
    
    def hacer_sonar(cosa):
        """
        Función polimórfica que funciona con CUALQUIER objeto
        que tenga un método hacer_sonido().
        
        No le importa el tipo del objeto, solo que tenga el método.
        Esto es DUCK TYPING.
        """
        print(f"{cosa.__class__.__name__}: {cosa.hacer_sonido()}")
    
    print("\n--- Duck Typing en acción ---")
    print("Diferentes objetos, mismo método:\n")
    
    # Crear objetos de diferentes clases
    objetos = [Perro(), Gato(), Vaca(), Radio()]
    
    # Todos funcionan con la misma función, aunque son de tipos diferentes
    for obj in objetos:
        hacer_sonar(obj)
    
    print("\n✓ Todos funcionaron porque tienen el método hacer_sonido()")
    print("✓ No importa que no compartan una clase padre")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "═"*68 + "╗")
    print("║" + "DEMOSTRACIÓN COMPLETA: POLIMORFISMO EN POO".center(68) + "║")
    print("╚" + "═"*68 + "╝\n")
    
    # Ejecutar demostraciones
    demostrar_polimorfismo_basico()
    demostrar_sistema_nomina_completo()
    demostrar_duck_typing()
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN: CONCEPTOS CLAVE DE POLIMORFISMO")
    print("="*70)
    print("""
    ✓ POLIMORFISMO: "Una interfaz, múltiples implementaciones"
    
    ✓ TIPOS DE POLIMORFISMO:
    
      1. POLIMORFISMO DE SUBTIPOS (con herencia):
         - Clases hijas implementan métodos de forma diferente
         - Objetos de diferentes clases pueden tratarse uniformemente
         - Ejemplo: calcular_salario() en diferentes tipos de empleados
      
      2. DUCK TYPING (sin herencia):
         - "Si camina como pato y grazna como pato, es un pato"
         - Python no verifica el tipo, solo que tenga los métodos necesarios
         - Más flexible, pero menos seguro
      
      3. SOBRECARGA DE OPERADORES:
         - Personalizar operadores (+, -, *, etc.) para clases propias
         - Usar métodos especiales (__add__, __sub__, etc.)
    
    ✓ BENEFICIOS:
      - Código más flexible y extensible
      - Facilita agregar nuevos tipos sin modificar código existente
      - Permite escribir código genérico que funciona con múltiples tipos
      - Reduce acoplamiento entre componentes
    
    ✓ EJEMPLO PRÁCTICO:
      Un sistema de nómina que procesa diferentes tipos de empleados
      sin necesitar saber el tipo específico de cada uno.
      Cada empleado responde a calcular_salario() de forma diferente.
    
    ✓ PRINCIPIO CLAVE:
      "Programa hacia interfaces, no hacia implementaciones"
      - Define lo que los objetos deben hacer (interfaz)
      - No te preocupes por cómo lo hacen (implementación)
    """)
    
    print("\n" + "="*70)
    print("¡Demostración completada!")
    print("="*70)

