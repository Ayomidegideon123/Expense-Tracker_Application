# ---------------- Adding widgets to the frameL1 frame ----------------

# adding the label to display the heading
headingLabel = Label(
frameL1,
text = "EXPENSE TRACKER",
font = ("Bahnschrift Condensed", "25"),
width = 20,
bg = "#8B4513",
fg = "#FFFAF0"
)

.# adding the label to display the subheading
subheadingLabel = Label(
frameL1,
text = "Data Entry Frame",
font = ("Bahnschrift Condensed", "15"),
width = 20,
bg = "#F5DEB3",
fg = "#000000"
)
# using the pack() method to set the position of the above labels
headingLabel.pack(fill = "both")
subheadingLabel.pack(fill = "both")
