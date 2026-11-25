"""Crear un vehículo con estos datos:
Campo	Valor
Marca	Nissan
Modelo	Versa
Placa	PBC-2026
Año	2022
Kilometraje	45000
Combustible	gasoline"""
vehicle=self.env['aitofix.vehicle'].create(
    {
        
        "brand":"Nissan",
        "model":"Versa",
        "plate":"PBC-2026",
        "year":2022,
        "mileaage":45000,
        "fuel":"gasoline"
    }
)

"""Ejercicio 2. Buscar
Buscar todos los vehículos cuya marca sea Nissan."""
vehicles =  self.env['autofix.vehicle'].search([('brand','=',"Nissan")])
"""Ejercicio 3. Buscar con dos condiciones
Buscar vehículos cuyo año sea mayor o igual a 2020 y cuyo combustible sea gasolina."""
vehicles = self.env['autofix.vehicle'].search(
    [('year','>=2020'),
     ('fuel','=','gasoline')
     ]
)
"""Ejercicio 4. Modificar
Actualizar el kilometraje del vehículo con placa PBC-2026 a 50000."""
vehicle = self.env['autofix.vehicle'].serch([('vehicle.plate','=','PBC-2026')])
vehicle.write({
    'mileage':'50000'
})
"""Ejercicio 5. Consultar por ID
Si tienes un ID de vehículo, utilizar browse() para acceder al registro y mostrar su placa."""
vehicle=self.env['autofix.vehicle'].browse(1)
print(vehicle.plate)

"""Ejercicio 6. Reflexionar
¿Qué diferencia existe entre estas dos instrucciones?
vehicle = self.env['autofix.vehicle'].search([    ('plate', '=', 'PBC-2026')])
vehicle = self.env['autofix.vehicle'].browse(15)"""

Search trae todos los elementos con esa placa, browse trae un solo elemento