# coding: utf-8


def is_empty(value: str) -> bool:
    return (len(value) == value.count(" ") or (value == None))


def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro,
                     municipio, estado, cep, telefone, observacao, cnpj,
                     inscricao_estadual):
    # Implemente aqui
    if is_empty(nome_loja):
        raise Exception("O campo nome da loja é obrigatório")

    if is_empty(logradouro):
        raise Exception('O campo logradouro do endereço é obrigatório')

    if numero == 0:
        numero = "s/n"

    if is_empty(municipio):
        raise Exception('O campo município do endereço é obrigatório')

    if is_empty(estado):
        raise Exception('O campo estado do endereço é obrigatório')

    if is_empty(cnpj):
        raise Exception('O campo CNPJ da loja é obrigatório')

    if is_empty(inscricao_estadual):
        raise Exception('O campo inscrição estadual da loja é obrigatório')

    linha2 = f"{logradouro}, {numero}"
    if not is_empty(complemento):
        linha2 += f" {complemento}"

    linha3 = str()
    if not is_empty(bairro):
        linha3 += f"{bairro} - "
    linha3 += f"{municipio} - {estado}"

    linha4 = str()
    if not is_empty(cep):
        linha4 = f"CEP:{cep}"
    if not is_empty(telefone):
        if not is_empty(linha4):
            linha4 += " "
        linha4 += f"Tel {telefone}"
    if not is_empty(linha4):
        linha4 += "\n"

    linha5 = str()
    if not is_empty(observacao):
        linha5 = observacao

    output = f"{nome_loja}\n"
    output += f"{linha2}\n"
    output += f"{linha3}\n"
    output += f"{linha4}"
    output += f"{linha5}\n"
    output += f"CNPJ: {cnpj}\n"
    output += f"IE: {inscricao_estadual}"

    return output
