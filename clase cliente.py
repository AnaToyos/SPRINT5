class Cliente:
    def ClienteClassic(self, datos, transacciones):
        if transacciones['estado'] == 'RECHAZADO':
            razon = Razones(transacciones)
        return(razon)
    
    def ClienteGold(self, datos, transacciones):
        if transacciones['estado'] == 'RECHAZADO':
            razon = Razones(transacciones)
        return(razon)

    def ClienteBlack(self, datos, transacciones):
        if transacciones['estado'] == 'RECHAZADO':
            razon = Razones(transacciones)
        return(razon)

    