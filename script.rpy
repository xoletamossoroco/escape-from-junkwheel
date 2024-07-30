# Define o título do jogo e o nome do personagem
define e = Character('Sky')

# Imagens de fundo, personagens e outros ativos podem ser definidos aqui
# Exemplo:
# image cela = "images/cela.png"
# image bg_city = "images/cidade.png"
# image cela_olho = "images/cela_olho.png"
# image char_sky = "images/sky.png"

label start:

    # Cena de abertura
    scene cela_olho with dissolve
    "Você acorda em uma cela escura e desconhecida. Sons estranhos ecoam ao redor."
    
    e "Onde estou? Como vim parar aqui?"
    
    scene cela with dissolve
    "Enquanto tenta entender a situação, você percebe que precisa escapar antes que seja tarde demais."
    
    menu:
        "Explorar a cela":
            jump explore_cell
        "Tentar sair imediatamente":
            jump immediate_escape

label explore_cell:
    scene cela with dissolve
    "Você examina a cela em busca de uma saída. Há uma pequena janela na parede, mas está trancada."
    
    e "Talvez haja algo que eu possa usar para abrir a janela."

    # Exemplo de interação com objetos
    menu:
        "Procurar por ferramentas":
            # Código para encontrar uma ferramenta
            jump find_tool
        "Gritar por ajuda":
            # Código para possíveis respostas
            jump call_for_help

label find_tool:
    "Você encontra um pedaço de metal no chão que pode ajudar a forçar a janela."
    e "Isso deve funcionar."

    # Mudança de cena
    scene bg_city with dissolve
    "Com a janela aberta, você consegue sair da cela e começa a explorar a cidade flutuante."
    
    # Progredir para exploração da cidade
    jump city_exploration

label immediate_escape:
    "Você tenta forçar a porta da cela, mas está trancada com um sistema complexo."
    e "Preciso de uma ferramenta para isso."

    # Redirecionar para exploração
    jump explore_cell

label city_exploration:
    scene bg_city with dissolve
    "A cidade é uma mistura de tecnologia avançada e natureza em harmonia, mas algo está muito errado."

    e "A cidade está começando a ficar estranha. Preciso descobrir o que está acontecendo."

    menu:
        "Procurar por pistas":
            jump search_for_clues
        "Procurar ajuda":
            jump seek_help

label search_for_clues:
    "Você encontra vários documentos e anotações que falam sobre experimentos científicos e corrupção política."
    e "Há algo muito sombrio acontecendo aqui."

    # Revelações perturbadoras
    jump disturbing_revelations

label seek_help:
    "Você encontra um grupo de habitantes que parecem estar tão confusos quanto você, mas não podem oferecer muita ajuda."
    e "Preciso continuar procurando por respostas."

    # Voltar para explorar a cidade
    jump city_exploration

label disturbing_revelations:
    scene bg_darkness with dissolve
    "Os documentos revelam que a cidade está sendo consumida por uma força sinistra que transforma os habitantes em criaturas distorcidas."

    e "Eu preciso sair daqui e parar isso."

    # Corrida contra o tempo
    jump race_against_time

label race_against_time:
    scene bg_city with dissolve
    "Com a força sinistra se espalhando, a cidade está ficando cada vez mais perigosa."

    e "Eu preciso encontrar a saída antes que seja tarde demais."

    menu:
        "Continuar a busca":
            jump final_confrontation
        "Tentar encontrar uma maneira de lutar contra a força sinistra":
            jump fight_force

label final_confrontation:
    "Você chega à fonte da força sinistra e se depara com uma entidade poderosa."
    e "Eu tenho que enfrentar isso para salvar a cidade."

    # Código para o confronto final
    menu:
        "Usar tudo o que aprendeu":
            jump escape_with_allies
        "Enfrentar a entidade diretamente":
            jump face_entity

label fight_force:
    "Você tenta lutar contra a força sinistra, mas ela é muito poderosa. É preciso encontrar uma estratégia."

    # Voltar para o confronto final
    jump final_confrontation

label face_entity:
    "Após um confronto intenso, você consegue derrotar a entidade e escapar da cidade."

    e "Finalmente, estou livre."

    # Final do jogo
    jump game_end

label escape_with_allies:
    "Você consegue reunir alguns aliados e juntos enfrentam a entidade, escapando da cidade."

    e "Nós conseguimos! A cidade ainda tem esperança."

    # Final do jogo
    jump game_end

label game_end:
    scene bg_darkness with dissolve
    "Dependendo das suas escolhas, a história pode terminar de diferentes maneiras."

    e "A cidade está salva, mas o que mais está lá fora?"

    return
