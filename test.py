import datasets
hagrid = datasets.load_dataset("miracl/hagrid", split="train", trust_remote_code=True)
print(hagrid[0])

hagrid = datasets.load_dataset("miracl/hagrid", split="dev", trust_remote_code=True)
print(hagrid[0])