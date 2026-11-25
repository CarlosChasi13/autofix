customer = self.env['autofix.customer'].create({
    'name':'Carlos Chasi',
    'birthdate':16-09,
    'id_card':'1860102123',
    'phone':'0987415263'
    'email':'cachasi3@gmail.com',
    'address':'La Troncal',
})

print(customer.id)

vehicle = self.env['autofix.vehicle'].create({
    'brand': 'Toyota',
    'model': 'Corolla',
    'plate': 'PBA-1234',
    'year': 2020,
    'customer_id':customer.id
})

print(vehicle.customer_id.name)
print(vehicle.customer_id.id_card)
print(vehicle.customer_id.phone)

#Buscar vehículos por cliente
vehicles = self.env['autofix.vehicle'].search([('customer_id','=',customer.id)])

for vehicle in vehicles:
    print(vehicle.plate)
    print(vehicle.brand)
    

#Consultar vehículos desde el cliente
customer = self.env['autofix.customer'].search([('name','=','Carlos Chasi')], limit=1)
for vehicle in customer.vehicle_ids:
    print(vehicle.plate)