import sys

def ArctanDenom(d, ndigits):
    # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
    total = term = (10**ndigits) // d
    n = 0
    while term != 0:
        n += 1
        term //= -d * d
        total += term // (2 * n + 1)
    print('ArctanDenom({}) took {} iterations.'.format(d, n))
    return total

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('USAGE: generate_pi.py ndigits outfile')
        sys.exit(1)

    xdigits = 10             # Extra digits to reduce trailing error
    ndigits = int(sys.argv[1])
    outFileName = sys.argv[2]

    # Use Machin's Formula to calculate pi.
    pi = 4 * (4*ArctanDenom(5,ndigits+xdigits) - ArctanDenom(239,ndigits+xdigits))

    # We calculated extra digits to compensate for roundoff error.
    # Chop off the extra digits now.
    pi //= 10**xdigits

    # Write the result to a text file.
    with open(outFileName, 'wt') as outfile:
        # Insert the decimal point after the first digit '3'.
        text = str(pi)
        outfile.write(text[0] + '.' + text[1:] + '\n')

    print('Wrote to file {}'.format(outFileName))
    sys.exit(0)
