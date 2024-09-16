a3 = [11, 23, 37, 48, 94, 152, 230, 312, 339, 413]
tgt = 457

mem = {}


def targetSum(S, i, tgt):
    k = len(S)

    # If calculation with this input is already computed return result from mem
    if (i, tgt) in mem:
        print("used mem")
        return mem[(i, tgt)]

    if tgt < 0:
        return float("inf")
    if i >= k and tgt >= 0:
        return tgt
    else:
        minimum = min(targetSum(S, i + 1, tgt - S[i]), targetSum(S, i + 1, tgt))

        # Store result of current calculation in mem if needed again later
        mem[(i, tgt)] = minimum
        return minimum


targetSum(a3, 0, tgt)
