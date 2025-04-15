# Função que retorna o texto baseado no idioma
def get_text(language):
    if language == "Português(BR)":
        return homepage_text_pt
    return homepage_text_en

homepage_text_pt = """
## Sobre o Projeto

O OlimpusChat é um projeto que busca aprofundar as capacidades de alguns modelos de Inteligência Artificial, verificando sua capacidade de atuação, argumentação e entendimento de diversos temas e contextos.

O Olimpus foi criado para ser executado através do Ollama e do Gemini, mas futuramente iremos expandir para diversos outros tipos de modelos.

A aplicação funciona da seguinte forma: Você escolhe um tema, seleciona dois deuses, e quais as suas ideias e põe eles para darem seus pontos de vista.

Você pode realizar diversas combinações de modelos, temas e deuses até onde a sua imaginação o levar. Boa sorte e bom divertimento!

## Tecnologias
"""

homepage_text_en = """
## About the Project

OlimpusChat is a project that aims to enhance the capabilities of AI models, examining their ability to act, argue, and understand various topics and contexts.

Olimpus was created to be run through Ollama and Gemini, but in the future, we will expand to other types of models.

The application works as follows: You choose a topic, select two gods, and their ideas, and let them present their viewpoints.

You can make various combinations of models, topics, and gods as far as your imagination goes. Good luck and have fun!

## Technologies
"""
