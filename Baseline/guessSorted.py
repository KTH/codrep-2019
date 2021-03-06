from pathlib import Path

def main():
    path_to_datasets = Path(__file__).absolute().parent.parent / "Datasets"
    for path_to_dataset in path_to_datasets.iterdir():
        if(path_to_dataset.is_dir()):
            for task in path_to_dataset.iterdir():
                if(task.name.endswith(".txt") and task.name != "out.txt"):
                    with open(task, "r") as file:
                        sortedGuess = list(range(1, len(file.read())+1))
                        print(str(task) + " " + ' '.join(str(pos) for pos in sortedGuess), flush=True)

if __name__ == "__main__":
    main()
