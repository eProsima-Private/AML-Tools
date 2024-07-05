# Algebraic AI - Copyright - All Rights Reserved

from amldl import ADD, APP, C, CV, Descriptor, EXC, F, INC, M, R, T, V, S


# Signature for AML-DL Consistency Checker
# def embedding(inconsistent):
#     boardDim = 8


# Signature for AML-DL Debugger
def embedding(boardDim=8):

    _i = 1  # Axis used by T. Use same index if they run over the same axis.

    def ix(x, y):
        return x + y * boardDim

    with Descriptor() as theEmbedding:

        # -- Define constants used for our embedding

        # Vector of Queens at (i,j) [Flatten 2D matrix]
        CV("Q", boardDim * boardDim)
        # Vector of Empty cell at (i,j) [Flatten 2D matrix]
        CV("E", boardDim * boardDim)
        # Vector of Rows. Row(i) indicates that there's at least one Q in row j.
        CV("R", boardDim)
        # Vector of Columns. Columns(j) indicates that there's at least one Q in row i.
        CV("C", boardDim)
        # A complete board, one that is a solution to the problem
        C("B")

        # Set with all possible options
        QE = M("Q", "E")

        # Create a list of vectors with all Q's or E's for a certain coordinate
        # E.g. Q(x=, ) = [Vx=0, Vx=1, ...]
        #      Vx=0 = [Q(0,0), Q(0,1), Q(0,2), ...]
        V("Q(x=, )")
        V("Q( ,y=)")
        V("E(x=, )")
        V("E( ,y=)")
        for _ in range(0, boardDim):
            APP(F("Q(x=, )"), V())
            APP(F("Q( ,y=)"), V())
            APP(F("E(x=, )"), V())
            APP(F("E( ,y=)"), V())
        for x in range(0, boardDim):
            for y in range(0, boardDim):
                APP(F("Q(x=, )", x), F("Q", ix(x, y)))
                APP(F("Q( ,y=)", y), F("Q", ix(x, y)))
                APP(F("E(x=, )", x), F("E", ix(x, y)))
                APP(F("E( ,y=)", y), F("E", ix(x, y)))

        # -- Define duples

        # Create regions as we add duples to the embedding
        theEmbedding.REGION = 1  # --------------------------------------------------

        # {R(i), C(j)} < Q(i,j)
        # Having a Q at (i,j) implies R(j) and C(i)
        for x in range(0, boardDim):
            for y in range(0, boardDim):
                ADD(INC(M(F("R", x), F("C", y)), F("Q", ix(x, y))))

        theEmbedding.REGION = 1
        # R(i) !< {Qx!=i, E}
        # R(x) can only be produced by queens in the row x
        ADD(EXC(T("R", _i), M(R("Q(x=, )", T("Q(x=, )", _i)), "E")))

        theEmbedding.REGION = 2
        # C(j) !< {Qy!=j, E}
        # C(y) can only be produced by queens in the column y
        ADD(EXC(T("C", _i), M(R("Q( ,y=)", T("Q( ,y=)", _i)), "E")))

        # If all cells but one are Empty (in a row or column), then the missing one must be a Queen in the solution board B
        # Qxy < {Ex0, Ex1, ... Ex(y-1), Ex(y+1), ...}
        theEmbedding.REGION = 5
        for x in range(0, boardDim):
            for y in range(0, boardDim):
                Qxy = F("Q", ix(x, y))
                Ex = F("E(x=, )", x)
                Ey = F("E( ,y=)", y)
                ADD(INC(Qxy, M(R(Ex, F(Ex, y)), "B")))
                ADD(INC(Qxy, M(R(Ey, F(Ey, x)), "B")))

        # If there is a Queen at (x,y), every other cell in the same column and row must be Empty in the solution board B
        # {Ex0, Ex1, ... Ex(y-1), Ex(y+1), ...} < {Qxy, B}
        # {E0y, E1y, ... E(x-1)y, E(x+1)y, ...} < {Qxy, B}
        theEmbedding.REGION = 6
        for x in range(0, boardDim):
            for y in range(0, boardDim):
                Qxy = F("Q", ix(x, y))
                Ex = F("E(x=, )", x)
                Ey = F("E( ,y=)", y)
                ADD(INC(S(R(Ex, F(Ex, y))), M(Qxy, "B")))
                ADD(INC(S(R(Ey, F(Ey, x))), M(Qxy, "B")))

        # Q produce empty diagonals
        # E.g. {E(0,1), E(1,2), E(3,4), ...} < Q(2,3)
        #      {E(0,5), E(1,4), E(3,2), ...} < Q(2,3)
        theEmbedding.REGION = 7

        for x in range(0, boardDim):
            for y in range(0, boardDim):
                diags = []
                for xx in range(0, boardDim):
                    for yy in range(0, boardDim):
                        if (x != xx) and (y != yy):
                            if (x - xx) == (y - yy):
                                Exxyyy = F("E", ix(xx, yy))
                                diags.append(Exxyyy)
                Qxy = F("Q", ix(x, y))
                if diags:
                    ADD(INC(M(*diags), M(Qxy, "B")))

        for x in range(0, boardDim):
            for y in range(0, boardDim):
                diags = []
                for xx in range(0, boardDim):
                    for yy in range(0, boardDim):
                        if (x != xx) and (y != yy):
                            if (x - xx) == -(y - yy):
                                Exxyyy = F("E", ix(xx, yy))
                                diags.append(Exxyyy)
                Qxy = F("Q", ix(x, y))
                if diags:
                    ADD(INC(M(*diags), M(Qxy, "B")))

        # Set some Queens as boundary conditions
        theEmbedding.REGION = 9
        if boardDim == 5:
            # Set a Queen at the center cell
            ADD(INC(F("Q", ix(2, 2)), "B"))

        if boardDim == 8:
            # Set two Queens at correct positions
            ADD(INC(M(F("Q", ix(1, 4)), F("Q", ix(3, 3))), "B"))

        # Both, empty and queen are not allowed in the solution board
        # Q(x,y) !< {E(x,y), B} for all (x,y)
        theEmbedding.REGION = 11
        ADD(EXC(M(T("Q", _i), T("E", _i)), "B"))

        # Require all columns and all rows with a queen
        # {R1, R2, ..., C1, C2...} < B
        theEmbedding.REGION = 12
        ADD(INC("R", "B"))
        ADD(INC("C", "B"))

        # Inconsistent
        # theEmbedding.REGION = 14
        # ADD(INC(F("Q", 4), F("E", 4)))

        # -- Prepare output: names of constants, positive duples and negative duples
        constantNames = [el.key for el in F("constants pending transfer to algebra").r]
        p = F("inclusions").r
        n = F("exclusions").r

        return constantNames, p, n
