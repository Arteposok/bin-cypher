import random


def gen_part(seed):
    part = (seed[0:3], seed[3:])
    return part


def keys(seed):
    keys = []

    for i in range(6):
        keys.append(seed)
        seed = seed[-1] + seed[:-1]

    return keys


print("KEYLIST: AUTOMATIC")
print("INFO: STARTING GEN")
letters = list("abcdef")
all_keys = []
for i in range(4):
    key = []
    key.append(f"=day {i+1}=")
    random.shuffle(letters)
    keys_gen = keys("".join(letters))
    for k in keys_gen:
        key.append(f"{k[:3]} {k[3:]}")
    all_keys.append(key)
for (k1, k2), (k3, k4) in zip(
    zip(all_keys[0], all_keys[1]), zip(all_keys[2], all_keys[3])
):
    print(f"{k1}    {k2}    {k3}    {k4}")
print("use only your day's keys, just the 6")
print("tomorrow use the next set of keys etc")
print("so #1 today, then 2 -> 3 -> 4")
