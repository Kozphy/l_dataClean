import numpy as np

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
    mask = (names == "Bob") | (names == "Will")
    print(mask)
    print(data[mask])
