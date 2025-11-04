import gdown

url = "https://drive.google.com/uc?id=1NlHEb2EKqVvhnbZrSxVf_OO3Up0g6EbK"
output = "plant_model.h5"

gdown.download(url, output, quiet=False, fuzzy=True, use_cookies=False)
