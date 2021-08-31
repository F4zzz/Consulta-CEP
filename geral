import requests
def newcep():
    novaconsulta = str(input('Deseja realizar uma nova consulta? [Sim/Nao] ')).lower().strip()
    if novaconsulta == 'sim':
        print('-='*25)
        main()
    else:
        print('#' * 21)
        print('## VOLTE SEMPRE :) ##')
        print('#' * 21)
        quit()
def main():
    print('#'*19)
    print('## Consultar CEP ##')
    print('#'*19)
    uf = str(input('Digite a sigla do estado para a consulta: ')).upper().strip()
    cidade = str(input('Digite a cidade para a consulta: ')).strip()
    rua = str(input('Digite a palavra-chave para a consulta: ')).strip()
    request = requests.get(f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/')
    data = request.json()
    if 'erro' in data:
        print('Dados inválidos')
    else:
        for i in range(0, len(data)):
            print(f'CEP: {data[i]["cep"]}')
            print(f'Localização: {data[i]["localidade"]} - {data[i]["uf"]}')
            print(f'Logradouro: {data[i]["logradouro"]}')
            print(f'Bairro: {data[i]["bairro"]}')
            print(f'DDD: {data[i]["ddd"]}')
            print('-=' * 25)
    newcep()
if __name__ == '__main__':
    main()
