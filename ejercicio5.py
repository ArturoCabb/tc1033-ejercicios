class VehiclesAD:
    def metodo(self,item):
        file = open("vehicles.csv", "w")
        file.writelines(item)
        file.close()