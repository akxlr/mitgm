import os

params = [
        (x, y) for x in [4,5,6] for y in range(5, 15) if x <= y
]

for (n_obj, n_loc) in params:
#     print("Making fg (%s, %s)" % (n_obj, n_loc))
    os.system("python mit_gm.py %s %s > model-%s-%s.fg" % (n_obj, n_loc, n_obj, n_loc))
#     print("Running junction tree")
    os.system("./mit_gm model-%s-%s.fg %s %s" % (n_obj, n_loc, n_obj, n_loc))
