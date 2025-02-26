from amldl import (
    ADD,
    C,
    Descriptor,
    INC,
    F,
    N,
)


def embedding():

    with Descriptor() as theEmbedding:
        C("cold")
        C("warm")

        ADD(INC("cold", N("temperature", 8)))
        ADD(INC("warm", N("temperature", 25)))

        return {
            "constants": [el.const for el in F("constants pending transfer to algebra").r],
            "constantsNames": [el.key for el in F("constants pending transfer to algebra").r],
            "positiveDuples": [(el.rl_L.s, el.rl_H.s) for el in F("inclusions").r],
            "negativeDuples": [(el.rl_L.s, el.rl_H.s) for el in F("exclusions").r],
        }  # fmt:skip
