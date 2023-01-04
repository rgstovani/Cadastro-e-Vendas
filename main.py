from interface import *
from datetime import datetime

dados = []
v = []
t = []

while True:
    cria_bd()
    jan, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

    if jan == jan1:   #Interações jan 1 - t Login
        if eventos == 'Login':
            if (valores['-usuario-'] == 'admin') and (valores['-senha-'] == 'admin'):
                jan1.hide()
                jan3 = t_menu_admin()
            else:
                login = teste_login(valores['-usuario-'], valores['-senha-'])
                if login == False:
                    sg.Popup('Usuario/senha invalido.')
                if login == True:
                    jan1.hide()
                    jan3 = t_menu_admin()

        if eventos == 'Esqueci a Senha':
            jan1.hide()
            jan2 = t_esqueci_senha()

    if jan == jan2:   #Interações jan 2 - Alterar Senha
        if eventos == 'Alterar Senha':
            if esqueci_senha_user_bd(valores['-usuario-'], valores['-email-']) == True:
                usuario = valores['-usuario-']
                jan2.disable()
                jan10 = t_redefinir_senha()
            else:
                sg.Popup('Usuario ou E-mail\nnao estão cadastrados.')
        if eventos == 'Voltar':
            jan2.hide()
            jan1 = t_login()

    if jan == jan3:   #Interações jan 3 - Menu ADM
        if eventos == 'Novo Cliente':
            jan3.hide()
            jan7 = t_cadastro_cliente()
        if eventos == 'Consultar Cliente':
            jan3.hide()
            jan11 = t_consulta_cliente()
        if eventos == 'Nova Venda':
            jan3.hide()
            jan9 = t_nova_venda()
        if eventos == 'Consultar Venda':
            jan3.hide()
            jan13 = t_consulta_vendas()
        if eventos == 'Novo Usuario':
            jan3.hide()
            jan5 = t_cadastrar_usuario()
        if eventos == 'Excluir Usuario':
            jan3.hide()
            jan6 = t_exclusao()
        if eventos == 'Novo Produto':
            jan3.hide()
            jan8 = t_cadastro_produtos()
        if eventos == 'Consultar Produto':
            jan3.hide()
            jan12 = t_consulta_produtos()
    # Interações jan 4 - Menu User



    if jan == jan5:   # Interações jan 5 - Cadastro de Usuario
        if eventos == 'Cadastrar':
            if valores['-usuario-'] and valores['-senha-'] and valores['-email-'] != '':
                if valores['-senha-'] == valores['-repsenha-']:
                    cadastra_user(valores['-usuario-'], valores['-senha-'], valores['-email-'])
                    sg.PopupOK('Usuario Cadastrado')
                    jan5.hide()
                    jan5 = t_cadastrar_usuario()
                else:
                    sg.Popup('As Senhas não coincidem.')
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            jan5.hide()
            jan3 = t_menu_admin()

    if jan == jan6:   # Interações jan 6 - Exclusão de Usuario
        if eventos == 'Confirmar':
            if valores['del_selecao'] != '':
                selecao = valores['del_selecao']
                deleta_user_bd(selecao)
                sg.PopupOK('Usuario deletado.')
                jan6.hide()
                jan6 = t_exclusao()
            else:
                sg.Popup('Selecione um usuario.')

        if eventos == 'Voltar':
            jan6.hide()
            jan3 = t_menu_admin()

    if jan == jan7:   # Interações jan 7 - Cadastro de Cliente
        if eventos == 'Validar':
            validade_cpf = validador_cpf(valores['-cpf-'])
            if validade_cpf == True:
                sg.Popup('CPF Valido.')
            if validade_cpf == False:
                sg.Popup('CPF Invalido.')

        if eventos == 'Verificar':
            cep = valores['-cep-']
            cep = cep.replace('-','').replace('.', '').replace(' ','')
            if len(cep) == 8:
                r = consulta_cep(cep)
                jan7['-endereco-'].update(r[1])
                jan7['-bairro-'].update(r[2])
                jan7['-cidade-'].update(r[3])
                jan7['-estado-'].update(r[4])
            else:
                sg.Popup('CEP invalido.')

        if eventos == 'Cadastrar':
            if valores['-nome-'] and valores['-cpf-'] and valores['-telefone-'] and valores['-email-'] and \
                    valores['-cep-'] and valores['-endereco-'] and valores['-num-'] and valores['-bairro-'] and \
                    valores['-cidade-'] and valores['-estado-'] != "":
                validade_cpf = validador_cpf(valores['-cpf-'])
                if validade_cpf == True:
                    add_clientes_bd(valores['-nome-'], valores['-cpf-'], valores['-telefone-'], valores['-email-'],
                                    valores['-cep-'], valores['-endereco-'], valores['-num-'], valores['-bairro-'],
                                    valores['-cidade-'], valores['-estado-'])
                    sg.Popup('Cliente Cadastrado\ncom sucesso!')
                    jan7.hide()
                    jan7 = t_cadastro_cliente()
                else:
                    sg.Popup('Verifique o CPF do Cliente.')
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            jan7.hide()
            jan3 = t_menu_admin()

    if jan == jan8:   # Interações jan 8 - Cadastro de Produtos
        if eventos == 'Cadastrar':
            if valores['-produto-'] and valores['-marca-'] and valores['-unidade-'] and valores['-valor-'] != "":
                add_produtos_bd(valores['-produto-'],valores['-marca-'],valores['-unidade-'],valores['-valor-'])
                sg.Popup('Produto cadastrado.')
                jan8.hide()
                jan8 = t_cadastro_produtos()
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            jan8.hide()
            jan3 = t_menu_admin()

    if jan == jan9:   # Interações jan 9 - Nova Venda
        if eventos == 'Selecione o Cliente':
            jan9.disable()
            jan16 = t_cons_cliente()

        if eventos == 'Adicionar':
            jan9.disable()
            jan17 = t_adiciona_produto()

        if eventos == 'Finalizar Venda':
            if (valores['-cliente-'] != '') and (valores['-endereco-'] != '') and (valores['-num-'] != '') and (
                    valores['-cidade-'] != '') and (valores['-pagto-'] != '') and (valores['-valortotal-'] != ''):
                data = datetime.now().strftime("%d-%m-%y %H:%M:%S")
                cliente = valores['-cliente-']
                rua = valores['-endereco-']
                numero = valores['-num-']
                cidade = valores['-cidade-']
                produtos = dados
                pagamento = valores['-pagto-']
                valor = sum(v)

                add_vendas_bd(data, cliente, rua, numero, cidade, pagamento, valor)
                sg.Popup('Venda Registrada \ncom sucesso!')
                jan9.hide()
                jan3 = t_menu_admin()
            else:
                sg.Popup('Preencha todas as informações.')

        if eventos == 'Voltar':
            dados = []
            jan9.hide()
            jan3 = t_menu_admin()

    if jan == jan10:  # Interações jan 10 - Redefinir Senha
        if eventos == 'Redefinir':

            if valores['-novasenha-'] == valores['-repnovasenha-']:
                altera_senha_bd(usuario,valores['-novasenha-'])
                sg.Popup('Senha Alterada.')
                jan2.hide()
                jan10.hide()
                jan1 = t_login()

        if eventos == 'Cancelar':
            jan2.hide()
            jan10.hide()
            jan1 = t_login()

    if jan == jan11:  # Interações jan 11 - Consulta Clientes
        if eventos == 'Excluir':
            jan11.disable()
            jan15 = t_excluir_cliente()

        if eventos == 'Voltar':
            jan11.hide()
            jan3 = t_menu_admin()

    if jan == jan12:  # Interações jan 12 - Consulta Produtos
        if eventos == 'Excluir':
            jan12.disable()
            jan14 = t_excluir_produto()

        if eventos == 'Voltar':
            jan12.hide()
            jan3 = t_menu_admin()

    if jan == jan13:  # Interações jan 13 - Consulta Vendas
        if eventos == 'Voltar':
            jan13.hide()
            jan3 = t_menu_admin()

    if jan == jan14:  # Interações jan 14 - Exclusão de Produtos
        if eventos == 'Confirmar':
            if valores['del_selecao_prod'] != '':
                selecao = valores['del_selecao_prod']
                deleta_produto_bd(selecao)
                sg.PopupOK('Produto deletado.')
                jan12.close()
                jan12 = t_consulta_produtos()
                jan14.hide()
            sg.Popup('Selecione um Produto.')

        if eventos == 'Voltar':
            jan12.enable()
            jan14.hide()

    if jan == jan15:  # Interações jan 14 - Exclusão de Clientes
        if eventos == 'Confirmar':
            selecao = valores['del_selecao_cli']
            deleta_cliente_bd(selecao)
            sg.PopupOK('cliente deletado.')
            jan11.close()
            jan11 = t_consulta_cliente()
            jan15.hide()

        if eventos == 'Voltar':
            jan11.enable()
            jan15.hide()

    if jan == jan16:  # Interações jan 16 - Seleção de Clientes
        if eventos == 'Confirmar':
            selecao = valores['compra_selecao_cli']
            info_cliente = retornar_info_cliente_bd(selecao)
            jan9.enable()
            jan9['-cliente-'].update(info_cliente[0][0])
            jan9['-endereco-'].update(info_cliente[0][5])
            jan9['-num-'].update(info_cliente[0][6])
            jan9['-cidade-'].update(info_cliente[0][8])
            jan16.hide()

        if eventos == 'Voltar':
            jan9.enable()
            jan16.hide()

    if jan == jan17:

        if eventos == 'Adicionar':
            if valores['-selec_prod-'] != '':
                produto = valores['-selec_prod-']
                quant = int(valores[0])
                iprod = (retornar_info_produto_bd(produto))
                v_total = (int(iprod[0][3]) * quant)
                v.append(int(v_total))
                dados.append([iprod[0][0], iprod[0][1], iprod[0][3], quant, v_total])
                jan9['-tabela-'].update(values=dados)
                jan9['-valortotal-'].update(sum(v))
                jan9.enable()
                jan17.hide()

        if eventos == 'Cancelar':
            jan9.enable()
            jan17.hide()
