from db.database import connect, query, close

def consultaInventario(jogador):

    [cursor, connection] = connect()
    idjogador = query(
        cursor, f'select id from jogador where nome = \'{jogador}\';')
    idjogador = idjogador[0]

    inventario = query(
        cursor, f'select item from instancia_item_jogador where jogador = {idjogador[0]};')
    if not inventario:
        print('\nO inventário está vazio!\n\n')
    else:
        print('\n')
        i = 0
        for row in inventario:
            item = query(
                cursor, f'select nome from item where id = {row[0]};')
            item = item[0]
            i = i+1
            print(f'{i} - {item[0]}')
        print('\n')
    close(connection, cursor)
    input(f'\n\nAperte qualquer tecla para sair: ')