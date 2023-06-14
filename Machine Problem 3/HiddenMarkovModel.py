"""
Machine Problem 3 - Hidden Markov Model

References:
    https://towardsdatascience.com/hidden-markov-model-implemented-from-scratch-72865bda430e?gi=5d1e73d86e55
    https://medium.com/@kangeugine/hidden-markov-model-7681c22f5b9
    http://www.infocobuild.com/education/audio-video-courses/computer-science/cs188-spring2015-berkeley.html

    T: length of the observation sequence.
    N: number of latent (hidden) states.
    M: number of observables.
    Q: {q₀, q₁, …} - hidden states.
    V: {0, 1, …, M — 1} - set of possible observations.
    A: state transition matrix.
    B: emission probability matrix.
    π: initial state probability distribution.
    O: observation sequence.
    X: (x₀, x₁, …), x_t ∈ Q - hidden state sequence.

"""


class HMM:
    def __init__(self, Q: set, V: set, A: list[list], B: list[list], π: list):

        self.N = len(Q)
        self.M = len(V)
        self.Q = Q
        self.V = V
        self.A = A
        self.B = B
        self.π = π
