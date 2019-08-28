monthConversions={
    0:"January",
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "July":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",

}

print(monthConversions["Oct"])
print(monthConversions[0])
print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get("lov"))
print(monthConversions.get("Luv","Not a Valid Key"))
