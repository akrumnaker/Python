from Misc import dice_simulator as ds

(lo, high) = ds.prompt_dice()

response = ""

while response != "n":
    print(ds.roll_die(lo, high))
    response = ds.prompt_continue()

print("Ok, bye.")
