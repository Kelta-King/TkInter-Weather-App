from Database import History as h

def main():
    hs = h.History("Gandhinagar", "32 cm")
    hs.save()

if __name__=="__main__":
    main()