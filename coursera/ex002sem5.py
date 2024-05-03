def eh_primo(num):
    """
    Função auxiliar para verificar se um número é primo.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def maior_primo(n):
    """
    Função para encontrar o maior número primo menor ou igual a n usando um loop while.
    """
    while n >= 2 and not eh_primo(n):
        n -= 1
    return n if n >= 2 else None  # Retorna None se nenhum primo for encontrado

# Exemplo de uso


