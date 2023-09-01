def sv(offset, spaces, startsv, endsv, rep, snap, svfun, bpm):
    svoutput = ""  # output string
    increment, velocity = 0, 0
    division = 60000 / (bpm * snap)
    # Linear Function
    if svfun == "Linear":
        increment = (max(startsv, endsv) - min(startsv, endsv)) / spaces  # calculates the per-step sv increment
        for i in range(rep):
            velocity = startsv
            for j in range(spaces):
                # inherited point generation
                svoutput = svoutput + f"{int(offset)},-{round(100 / velocity, 12)},4,1,0,100,0,0" + "\n"
                # determines if sv function is ascending or descending
                if endsv > startsv:
                    velocity = velocity + increment
                else:
                    velocity = velocity - increment
                offset = offset + division
    # Wave Function
    elif svfun == "Wave":
        increment = (max(startsv, endsv) - min(startsv, endsv)) / (spaces / 2)
        velocity = min(startsv, endsv)  # ignores sv assigning and defaults to the lowest
        for i in range(rep):
            for j in range(spaces):
                svoutput = svoutput + f"{int(offset)},-{round(100 / velocity, 12)},4,1,0,100,0,0" + "\n"
                # wave sv function implementation
                if j < spaces / 2:
                    velocity = velocity + increment
                else:
                    velocity = velocity - increment
                offset = offset + division
    return svoutput  # Returns what to display in the SV text box
