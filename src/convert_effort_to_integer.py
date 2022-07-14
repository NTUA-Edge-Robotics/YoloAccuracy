import pandas

efforts_order = ["lightning", "thunder", "falcon", "cheetah", "hare", "wombat", "squirrel", "kitten", "tortoise"]

def convert_effort_to_integer(frame:pandas.DataFrame) -> list:
    efforts = list(frame["effort"].unique())

    efforts.sort(key=efforts_order.index)

    frame["effort_id"] = frame["effort"].apply(lambda x: efforts.index(x))

    return efforts