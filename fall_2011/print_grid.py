"""
Similar, but not identical, to Downey Ex 3.5 (Ch 3, Ex 5 on the web)
BUT the size of the grid is given by the argument.
For example, print_grid(11) prints the grid in Downey's picture.
"""

def print_grid(size):
    """
    print grid like in Downey, ex 3.5, but integer arg is size of grid
    """
    
    def mk_beam(half_width, corner, strut):
        return(corner + strut * half_width) * 2 + corner

    half_width = (size - 3)/2 # make room for 3 corners, integer division
    beam = mk_beam(half_width, '+', '-')
    panes = mk_beam(half_width, '|', ' ')

    for i in range(2):
        print beam
        for i in range(half_width):
            print panes
    print beam


if __name__ == '__main__':
    print_grid(11)

    
