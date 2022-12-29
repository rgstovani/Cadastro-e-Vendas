import datetime as datetime

from interface import *
from datetime import datetime


dados = []
v = []
t = []

while True:
    cria_bd()
    janela, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break

    if janela == janela1:   #Interações Janela 1 - Tela Login
        if eventos == 'Login':
            if (valores['-usuario-'] == 'admin') and (valores['-senha-'] == 'admin'):
                janela1.hide()
                janela3 = tela_menu_admin()
            else:
                login = teste_login(valores['-usuario-'], valores['-senha-'])
                if login == False:
                    sg.Popup('Usuario/senha invalido.')
                if login == True:
                    janela1.hide()
                    janela3 = tela_menu_admin()

        if eventos == 'Esqueci a Senha':
            janela1.hide()
            janela2 = tela_esqueci_senha()

    if janela == janela2:   #Interações Janela 2 - Alterar Senha
        if eventos == 'Alterar Senha':
            janela2.disable()
            janela10 = tela_redefinir_senha()
        if eventos == 'Voltar':
            janela2.hide()
            janela1 = tela_login()

    if janela == janela3:   #Interações Janela 3 - Menu ADM
        if eventos == 'Novo Cliente':
            janela3.hide()
            janela7 = tela_cadastro_cliente()
        if eventos == 'Consultar Cliente':
            janela3.hide()
            janela11 = tela_consulta_cliente()
        if eventos == 'Nova Venda':
            janela3.hide()
            janela9 = tela_nova_venda()
        if eventos == 'Consultar Venda':
            janela3.hide()
            janela13 = tela_consulta_vendas()
        if eventos == 'Novo Usuario':
            janela3.hide()
            janela5 = tela_cadastrar_usuario()
        if eventos == 'Excluir Usuario':
            janela3.hide()
            janela6 = tela_exclusao()
        if eventos == 'Novo Produto':
            janela3.hide()
            janela8 = tela_cadastro_produtos()
        if eventos == 'Consultar Produto':
            janela3.hide()
            janela12 = tela_consulta_produtos()
    # Interações Janela 4 - Menu User



    if janela == janela5:   # Interações Janela 5 - Cadastro de Usuario
        if eventos == 'Cadastrar':
            if valores['-senha-'] == valores['-repsenha-']:
                cadastra_user(valores['-usuario-'], valores['-senha-'], valores['-email-'])
                sg.PopupOK('Usuario Cadastrado')
                janela5.hide()
                janela5 = tela_cadastrar_usuario()
            else:
                sg.Popup('As Senhas não coincidem.')
        if eventos == 'Voltar':
            janela5.hide()
            janela3 = tela_menu_admin()

    if janela == janela6:   # Interações Janela 6 - Exclusão de Usuario
        if eventos == 'Confirmar':
            selecao = valores['del_selecao']
            deleta_user_bd(selecao)
            sg.PopupOK('Usuario deletado.')
            janela6.hide()
            janela6 = tela_exclusao()

        if eventos == 'Voltar':
            janela6.hide()
            janela3 = tela_menu_admin()

    if janela == janela7:   # Interações Janela 7 - Cadastro de Cliente
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
                janela7['-endereco-'].update(r[1])
                janela7['-bairro-'].update(r[2])
                janela7['-cidade-'].update(r[3])
                janela7['-estado-'].update(r[4])
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
                    janela7.hide()
                    janela7 = tela_cadastro_cliente()
                else:
                    sg.Popup('Verifique o CPF do Cliente.')
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            janela7.hide()
            janela3 = tela_menu_admin()

    if janela == janela8:   # Interações Janela 8 - Cadastro de Produtos
        if eventos == 'Cadastrar':
            if valores['-produto-'] or valores['-marca-'] or valores['-unidade-'] or valores['-valor-'] != "":
                add_produtos_bd(valores['-produto-'],valores['-marca-'],valores['-unidade-'],valores['-valor-'])
                sg.Popup('Produto cadastrado.')
                janela8.hide()
                janela8 = tela_cadastro_produtos()
            else:
                sg.Popup('Preencha todos os campos.')

        if eventos == 'Voltar':
            janela8.hide()
            janela3 = tela_menu_admin()

    if janela == janela9:   # Interações Janela 9 - Nova Venda
        if eventos == 'Selecione o Cliente':
            janela9.disable()
            janela16 = tela_cons_cliente()

        if eventos == 'Adicionar':
            janela9.disable()
            janela17 = tela_adiciona_produto()

        if eventos == 'Finalizar Venda':

            data = datetime.now().strftime("%d-%m-%y %H:%M:%S")
            cliente = valores['-cliente-']
            rua = valores['-endereco-']
            numero = valores['-num-']
            cidade = valores['-cidade-']
            #produtos = 'Roteador', 'Tp-Link', '100', 1, 100, 'monitor', 'lg', '500', 2, 1000
            pagamento = valores['-pagto-']
            valor = sum(v)

            add_vendas_bd(data, cliente, rua, numero, cidade, pagamento, valor)


        if eventos == 'Voltar':
            dados = []
            janela9.hide()
            janela3 = tela_menu_admin()

    if janela == janela10:  # Interações Janela 10 - Redefinir Senha
        if eventos == 'Redefinir':
            pass

        if eventos == 'Cancelar':
            janela2.hide()
            janela10.hide()
            janela1 = tela_login()

    if janela == janela11:  # Interações Janela 11 - Consulta Clientes
        if eventos == 'Excluir':
            janela11.disable()
            janela15 = tela_excluir_cliente()

        if eventos == 'Voltar':
            janela11.hide()
            janela3 = tela_menu_admin()

    if janela == janela12:  # Interações Janela 12 - Consulta Produtos
        if eventos == 'Excluir':
            janela12.disable()
            janela14 = tela_excluir_produto()

        if eventos == 'Voltar':
            janela12.hide()
            janela3 = tela_menu_admin()

    if janela == janela13:  # Interações Janela 13 - Consulta Vendas
        if eventos == 'Voltar':
            janela13.hide()
            janela3 = tela_menu_admin()

    if janela == janela14:  # Interações Janela 14 - Exclusão de Produtos
        if eventos == 'Confirmar':
            selecao = valores['del_selecao_prod']
            deleta_produto_bd(selecao)
            sg.PopupOK('Produto deletado.')
            janela12.close()
            janela12 = tela_consulta_produtos()
            janela14.hide()

        if eventos == 'Voltar':
            janela12.enable()
            janela14.hide()

    if janela == janela15:  # Interações Janela 14 - Exclusão de Clientes
        if eventos == 'Confirmar':
            selecao = valores['del_selecao_cli']
            deleta_cliente_bd(selecao)
            sg.PopupOK('cliente deletado.')
            janela11.close()
            janela11 = tela_consulta_cliente()
            janela15.hide()

        if eventos == 'Voltar':
            janela11.enable()
            janela15.hide()

    if janela == janela16:  # Interações Janela 16 - Exclusão de Clientes
        if eventos == 'Confirmar':
            selecao = valores['compra_selecao_cli']
            info_cliente = retornar_info_cliente_bd(selecao)
            janela9.enable()
            janela9['-cliente-'].update(info_cliente[0][0])
            janela9['-endereco-'].update(info_cliente[0][5])
            janela9['-num-'].update(info_cliente[0][6])
            janela9['-cidade-'].update(info_cliente[0][8])
            janela16.hide()

        if eventos == 'Voltar':
            janela9.enable()
            janela16.hide()

    if janela == janela17:

        if eventos == 'Adicionar':
            if valores['-selec_prod-'] != '':
                produto = valores['-selec_prod-']
                quant = int(valores[0])
                iprod = (retornar_info_produto_bd(produto))
                v_total = (int(iprod[0][3]) * quant)
                v.append(int(v_total))
                dados.append([iprod[0][0], iprod[0][1], iprod[0][3], quant, v_total])
                janela9['-tabela-'].update(values=dados)
                janela9['-valortotal-'].update(sum(v))
                janela9.enable()
                janela17.hide()


        if eventos == 'Cancelar':
            janela9.enable()
            janela17.hide()

    print(eventos, valores)


