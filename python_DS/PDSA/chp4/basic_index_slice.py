import numpy as np
import pprint

"""
[
   [
      [1,2,3],
      [4,5,6],
   ],
   [
       [7,8,9],
    [10,11,12],
   ],
]
"""
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])


def index_nparray():
    print(f"arr3d origin: {arr3d}")
    print(f"arr3d 1 index: {arr3d[0]}")
    print(f"arr3d 2 index : {arr3d[0,1]}")
    print(f"arr3d 3 index: {arr3d[0,1,1]}")


def assign_nparray():
    old_values = arr3d[0].copy()
    arr3d[0] = 42
    print(arr3d)

    arr3d[0] = old_values
    print(arr3d)


def bool_indexing():
    # 0, 3
    names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"], dtype="<U4")
    # dt = np.dtype("<U4")
    # print(dt.name)
    data = np.random.randn(7, 4)
    print(f"name.shape:{names.shape}")
    print(f"data.shape: {data.shape}")
    print(f"data: {data}")
    print(f"data[names == 'Bob']: {data[names == 'Bob']}")
    print(f"data[names == 'Bob', 2:] {data[names == 'Bob', 2:]}")
    print(data[~(names == "Bob")])
    cond = names == "Bob"
    print(f"invert: {data[~cond]}")
    # 0, 2, 3, 4
    mask = (names == "Bob") | (names == "Will")
    print(f"mask:{mask}")
    print(f"data[mask]: {data[mask]}")
    # not 1, 5, 6
    not_Joe_cond = names != "Joe"
    print(f"data[not_joe]: {data[not_Joe_cond]}")
    data[not_Joe_cond] = 7
    print(f"data[not_joe=7]: {data}")


def fancy_indexing():
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print(f"data: {arr}")
    print(f"data[[4,3,0,6]]: {arr[[4, 3, 0, 6]]}")
    print(f"data[[-3.-5,-7]]: {arr[[-3, -5, -7]]}")

    arr = np.arange(32).reshape((8, 4))
    print(f"arr: {arr}")
    print(f"arr[[1,5,7,2], [0,3,1,2]]: {arr[[1,5,7,2],[0,3,1,2]]}")
    print(f"arr[[1,5,7,2]][:, [0,3,1,2]]: {arr[[1,5,7,2]][:, [0,3,1,2]]}")


"""
[
    [
        [0,1,2,3],
        [4,5,6,7]
    ],
    [
        [8,9,10,11],
        [12,13,14,15]
    ]
]

"""

"""
[
    [
        [0,1,2,3],
        [8,9,10,11],
    ],
    [
        [4,5,6,7],
        [12,13,14,15],
    ]
]
"""

""" 6,5,2
 [
    [
        [ 0  1]
        [ 2  3]
        [ 4  5]
        [ 6  7]
        [ 8  9]
    ]
    [
        [10 11]
        [12 13]
        [14 15]
        [16 17]
        [18 19]
    ]
    [
        [20 21]
        [22 23]
        [24 25]
        [26 27]
        [28 29]
    ]
    [
        [30 31]
        [32 33]
        [34 35]
        [36 37]
        [38 39]
    ]
    [
        [40 41]
        [42 43]
        [44 45]
        [46 47]
        [48 49]
    ]
    [
        [50 51]
        [52 53]
        [54 55]
        [56 57]
        [58 59]
    ]
]
"""

"""
[
    [
        [ 0  1]
        [10 11]
        [20 21]
        [30 31]
        [40 41]
        [50 51]
    ]
    [
        [ 2  3]
        [12 13]
        [22 23]
        [32 33]
        [42 43]
        [52 53]
    ]
    [
        [ 4  5]
        [14 15]
        [24 25]
        [34 35]
        [44 45]
        [54 55]
    ]
    [
        [ 6  7]
        [16 17]
        [26 27]
        [36 37]
        [46 47]
        [56 57]
    ]
    [
        [ 8  9]
        [18 19]
        [28 29]
        [38 39]
        [48 49]
        [58 59]
    ]
]

"""
"""
        [[[ 0,  1],
        [ 8,  9]],

       [[ 2,  3],
        [10, 11]],

       [[ 4,  5],
        [12, 13]],

       [[ 6,  7],
        [14, 15]]]

"""


def transpose_array_swap_axes():
    # arr = np.arange(15).reshape((3, 5))
    # print(f"arr:{arr}")
    # print(f"arr transpose:{arr.T}")
    # 0 axis = 6, 1 axis = 5, 2 axis = 2
    arr = np.arange(16).reshape((2, 4, 2))
    print("arr:")
    pprint.pprint(arr)
    print("arr transpose:")
    pprint.pprint(arr.transpose(1, 0, 2))
    print(arr.transpose((1, 0, 2)).shape)

    swapaxes = arr.swapaxes(1, 2)
    print(swapaxes)
    print(swapaxes.shape)


def array_oriented():
    # 10 / 0.01
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    print(f"ys: {ys}")
    z = np.sqrt(xs**2 + ys**2)
    print(f"z:{z}")


def expression_condition_logic():
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    # True -> x , false -> y
    result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
    print(result)


def math_statistical_method():

    ## quantiles
    large_arr = np.random.randn(1000)
    large_arr.sort()
    print(large_arr[int(0.05 * len(large_arr))])
