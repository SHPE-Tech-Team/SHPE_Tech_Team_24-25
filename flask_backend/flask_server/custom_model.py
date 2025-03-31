


def getting_data():
    from roboflow import Roboflow
    rf = Roboflow(api_key="xIGN2O5hVPAzGUvmfhC7")
    project = rf.workspace("loteria").project("my-first-project-a9nmn")
    version = project.version(3)
    dataset = version.download("yolov8")
                    
                

def custom_model(input_text):
    pass

if __name__ == "__main__":
    getting_data();