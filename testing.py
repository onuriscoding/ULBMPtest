from encoding import Encoder, Decoder
import time

def arithmetic_mean(values):
    return sum(values) / len(values)

def testing_image(file_path, ulbmp_version, bpp_depth, rle):
    load_exec_times = []
    saving_exec_times = []
    new_file = "tested_image"
    for i in range(10):
        start_loading = time.time()
        # Loading the image
        image_to_test = Decoder.load_from(file_path)
        load_exec_times.append(time.time() - start_loading)

        # Encoding the image
        start_encoding = time.time()
        image_to_test_encoded = Encoder(image_to_test, ulbmp_version, depth=bpp_depth, rle=rle)
        image_to_test_encoded.save_to(
            "/Users/onur/Documents/GitHub/BAC-1-Q2/F106/Projet2/testing_images/" + 
            new_file + ".ulbmp") 
        saving_exec_times.append(time.time() - start_encoding)
        
        # To create a new file every iteration
        new_file += f"{i}"
    return [arithmetic_mean(load_exec_times), arithmetic_mean(saving_exec_times)]
load_save_runtimes = testing_image(file_path="/Users/onur/Downloads/imgs/checkers4.ulbmp", ulbmp_version=4, bpp_depth=24, rle=True)
load_ms = load_save_runtimes[0] * 1000
save_ms = load_save_runtimes[1] * 1000
print(f"Average time to load an image: {load_ms} ms")
print(f"Average time to save an image: {save_ms} ms")
