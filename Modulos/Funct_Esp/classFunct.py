import pathlib

class classFunRecArc:
    def __init__(self, dir):
        self.dir = dir
        return
    
    def reachArchiLis(self):
        lv_urR = f"{self.dir}/"
        lv_path = pathlib.Path(lv_urR)

        for item in lv_path.iterdir():
            if item.is_file(): 
                print(item.name)
        return 
    def reachArchiUni(self, nam):
        lv_urR = f"{self.dir}/{nam}"
        lv_path = pathlib.Path(lv_urR)


        
        if lv_path.is_file and lv_path.exists():
            print(f"Es un archivo: {lv_path.name}")
            return  lv_urR
        else:
            print("No exite")