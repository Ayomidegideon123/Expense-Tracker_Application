# adding frames to the window to provide structure to the other widgets
frameLeft = Frame(main_win, bg = "#FFF8DC")
frameRight = Frame(main_win, bg = "#DEB887")
frameL1 = Frame(frameLeft, bg = "#FFF8DC")
frameL2 = Frame(frameLeft, bg = "#FFF8DC")
frameL3 = Frame(frameLeft, bg = "#FFF8DC")
frameR1 = Frame(frameRight, bg = "#DEB887")
frameR2 = Frame(frameRight, bg = "#DEB887")

# using the pack() method to set the position of the above frames
frameLeft.pack(side=LEFT, fill = "both")
frameRight.pack(side = RIGHT, fill = "both", expand = True)
frameL1.pack(fill = "both")
frameL2.pack(fill = "both")
frameL3.pack(fill = "both")
frameR1.pack(fill = "both")
frameR2.pack(fill = "both", expand = True
