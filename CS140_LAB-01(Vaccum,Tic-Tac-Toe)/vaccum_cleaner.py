import random
room = {
    "A":random.choice(["clean","Dirty"]),
     "B":random.choice(["clean","Dirty"])
}
position = random.choice(["A","B"])
for _ in range(3):
    print(f"vacuum at room {position},room states:{room}")
    if(room[position]=="Dirty"):
        print(f"cleaning room {position}..")
        room[position]="clean"
    else:
        print(f"room {position} already cleaned")
    if position=="A":
        position="B"
    else:
        position="A"
