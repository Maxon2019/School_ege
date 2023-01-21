n = int(input())
# i don't support this bruh
defs = 540  # mins
defs += 45
if n == 1:
    print(defs // 60, defs - defs // 60*60)  # f
if n > 1:
    defs += 5
    defs += 45  # s
    if n == 2:
        print(defs // 60, defs - defs // 60*60)

    if n > 2:
#t
        defs += 15
        defs += 45
        if n == 3:
            print(defs // 60, defs - defs // 60*60)

        if n > 3:
#4
            defs += 5
            defs += 45
            if n == 4:
                print(defs // 60, defs - defs // 60*60)

            if n > 4:
#5
                defs += 15
                defs += 45
                if n == 5:
                    print(defs // 60, defs - defs // 60*60)

                if n > 5:
#6
                    defs += 5
                    defs += 45
                    if n == 6:
                        print(defs // 60, defs - defs // 60 * 60)

                    if n > 6:
    # 7
                        defs += 15
                        defs += 45
                        if n == 7:
                            print(defs // 60, defs - defs // 60 * 60)

                        if n > 7:
    # 8
                            defs += 5
                            defs += 45
                            if n == 8:
                                print(defs // 60, f"0{defs - defs // 60 * 60}") #можете убрать формат, если не заходит

                            if n > 8:
#9
                                defs += 15
                                defs += 45
                                if n == 9:
                                    print(defs // 60, f"0{defs - defs // 60 * 60}")
                                if n > 9:
                                    # 9
                                    defs += 5
                                    defs += 45
                                    if n == 10:
                                        print(defs // 60, defs - defs // 60 * 60)