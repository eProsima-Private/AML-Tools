from amldl import (
    ADD,
    CV,
    Descriptor,
    EXC,
    F,
    M,
    R,
    T,
)


def embedding():

    with Descriptor() as theEmbedding:

        n = 3
        CV("black", n)  # black[0], black[1], black[2]
        CV("white", n)  # white[0], white[1], white[2]

        axis = 1
        blackDuples = EXC(T("black", axis), M("white", R("black", T("black", axis))))
        whiteDuples = EXC(T("white", axis), M("black", R("white", T("white", axis))))

        ADD(blackDuples)
        ADD(whiteDuples)

        return {
            "constants": [el.const for el in F("constants pending transfer to algebra").r],
            "constantsNames": [el.key for el in F("constants pending transfer to algebra").r],
            "positiveDuples": [(el.rl_L.s, el.rl_H.s) for el in F("inclusions").r],
            "negativeDuples": [(el.rl_L.s, el.rl_H.s) for el in F("exclusions").r],
            "blackConstants": [el.const for el in F("black").v],
            "whiteConstants": [el.const for el in F("white").v],
        }  # fmt:skip
