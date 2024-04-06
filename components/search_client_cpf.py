def search_client_cpf(db_clients, cpf):
    result = []

    for index in range(len(db_clients)):
        if db_clients[index][0] == cpf:
            result.append(index)
    
    return result