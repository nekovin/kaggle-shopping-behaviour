
import kagglehub


def pull_data():
    
    path = kagglehub.dataset_download("ranaghulamnabi/shopping-behavior-and-preferences-study")

    print("Path to dataset files:", path)

def setup():
    pull_data()

if __name__ == '__main__':
    setup()