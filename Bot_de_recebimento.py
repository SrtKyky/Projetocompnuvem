import telebot

CHAVE_API = "6996825927:AAENGtHWgxH5y2p8NNqrIKiKoWUukW9qI3Q"

bot = telebot.TeleBot(CHAVE_API)
def responder(mensagem):
    bot
@bot.message_handler(commands=["pizza"])

def pizza(mensagem):

    bot.send_message(mensagem.chat.id, " Saindo pizza pra sua casa: Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Podrão: em 10min chega ai")

    @bot.message_handler(commands=["sushi"])
    def salada(mensagem):
        bot.send_message(mensagem.chat.id, "Não tem Salada não, clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["opcao01"])
def opcao01(mensagem):
    texto = """
    o qye voçê quer? (Clique em uma opção)
    /pizza Pizza
    /hamburguer hamburguer
    /salada Salada """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao02"])
def opcao02(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para recalmação@reclama.com")
    
@bot.message_handler(commands=["opcao03"])
def opcao03(mensagem):
    bot.send_message(mensagem.chat.id, " VLW, o pai mandou um abraço de volta")

def verificar(mensagem):
    return True
@bot.message_handler(func=verificar)
def hamburguer(mensagem):
    texto = """

    Escolha uma opção para continuar (Clique no item):
    /opcao01 Fazer um pedido
    /opcao02 Reclamar de um pedido
    /opcao03 Mandar um abraço pro pai
Responder qualquer outra coisa não vai funcionar, Clique em qualquer das opções
    
    """
    bot.reply_to(mensagem, texto)


bot.polling()