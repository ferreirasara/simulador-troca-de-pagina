def getSettings(file):
    lines = [line.strip() for line in file]
    if len(lines) < 4:
        print('ERRO - Quantidade inválida de linhas')
        return None

    lenght = lines[0]
    initialState = lines[1].split(',')
    processQueue = lines[2].split(',')
    processAction = lines[3].split(',')

    if lenght.isdigit():
        lenght = int(lenght)
        if lenght > 0:
            if len(initialState) == lenght:
                if len(processQueue) == len(processAction):
                    if '0' not in initialState and '0' not in processQueue:
                        return lenght, initialState, processQueue, processAction
                    else:
                        print('ERRO - O digito 0 não deve ser utilizado.')
                else:
                    print('ERRO - A fila de processos e a lista de ações devem ser do mesmo tamanho.')
            else:
                print('ERRO - O estado inicial deve ser do tamanho da memória.')
        else:
            print('ERRO - O tamanho da memória deve ser maior que zero.')
    else:
        print('ERRO - Tamanho da memória deve ser um número.')
