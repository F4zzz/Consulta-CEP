import requests
def newcep():
    novaconsulta = str(input('Deseja realizar uma nova consulta? [Sim/Nao] ')).lower().strip()
    if novaconsulta == 'sim':
        print('-=' * 25)
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
    cep = input('Digite o CEP para a consulta: ')
    if len(cep) != 8:
        print(f'{cep}: CEP inválido')
        print('-=' * 25)
        newcep()
    request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = request.json()
    if 'erro' in data:
        print(f'{cep}: CEP inválido')
        main()
    else:
        print(request.json())
        print(f'CEP: {data["cep"]}')
        print(f'Localização: {data["localidade"]} - {data["uf"]}')
        print(f'Logradouro: {data["logradouro"]}')
        print(f'Complemento: {data["complemento"]}')
        print(f'Bairro: {data["bairro"]}')
        print(f'DDD: {data["ddd"]}')
    newcep()
if __name__ == '__main__':
    main()
