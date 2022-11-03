def oxford_comma(items):
    # if len(items) == 1:
    #     return items[0]
    # elif len(items) == 2:
    #     return " and ".join(items)

    # last_item = items[-1]
    # oxford_string = ", ".join(items[0:-1])
    # oxford_string += f", and {last_item}"
    # return oxford_string
    if len(items) > 1:
        items[-1] = f"and {items[-1]}"

    if len(items) > 2:
        return ", ".join(items)
    else:
        return " ".join(items)
