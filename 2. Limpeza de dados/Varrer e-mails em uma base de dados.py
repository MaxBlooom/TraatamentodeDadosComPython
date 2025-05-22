# Importando Regular Expressions
import re

# Base com os e-mails presentes numa lista de strings
texto = """
Aqui estão alguns e-mails: joao.silva@gmail.com, maria_1990@yahoo.com.br,
contato@empresa.com, email.invalido@com, outro.email@site.info. Expressões 
regulares são padrões usados para combinar ou encontrar ocorrências de sequências 
de caracteres em uma string. Em Python, expressões regulares são geralmente usadas 
para manipular strings realizar tarefas como validação de entrada de dados, extração
 de informações de strings e substituição de texto.
"""

# Expressão regular para encontrar e-mails
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', texto)

# Imprimir somente os e-mails
print(emails)


