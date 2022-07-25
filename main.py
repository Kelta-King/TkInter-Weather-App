from Designs import Designs as design
from Actions import Actions
import hidden

def main():
    # Setting the Design object and passing actions object
    ds = design.Designs(Actions.Actions(hidden.api_id))

    # Set the window parameters
    ds.define_window()

    # Designs the window
    ds.top_frame()
    ds.bottom_frame()

    # Executes the app
    ds.execute()


if __name__=="__main__":
    main()