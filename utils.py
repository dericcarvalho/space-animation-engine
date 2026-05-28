import numpy as np

def rotation_matrix(theta):
    """
    Calcula a matriz de rotação 2D para uma rotação no sentido anti-horário.

    Args:
        theta_graus (float): O ângulo de rotação em graus.

    Returns:
        numpy.ndarray: A matriz de rotação 2x2.
    """
    # Converte o ângulo de graus para radianos, pois as funções sin e cos do numpy
    # trabalham com radianos.
    theta_radianos = np.radians(theta)
    
    # Calcula o seno e o cosseno do ângulo
    c = np.cos(theta_radianos)
    s = np.sin(theta_radianos)
    
    # Monta a matriz de rotação
    # R(θ) = [[cos(θ), -sin(θ)],
    #         [sin(θ),  cos(θ)]]
    matriz = np.array([[c, -s], 
                       [s,  c]])
    
    return matriz