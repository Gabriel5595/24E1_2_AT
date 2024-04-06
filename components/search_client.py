def search_client(db_clients, term, name_or_surname=True):
    result = []
    
    if name_or_surname:
        for index in range(len(db_clients)):
            if db_clients[index][1] == term:
                result.append(index)
        return result
    else:
        for index in range(len(db_clients)):
            if db_clients[index][2] == term:
                result.append(index)
        return result