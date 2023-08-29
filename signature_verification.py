import tkinter as tk
import tkinter.filedialog
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Similarity Threshold
thresh = 0.88

def compare_signatures(image_path1, image_path2):
    # Read the images
    original_image = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    sample_image = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # Resize images for comparison
    original_image = cv2.resize(original_image, (200, 200))
    sample_image = cv2.resize(sample_image, (200, 200))

    # Display both images
    cv2.imshow("Original Signature", original_image)
    cv2.imshow("Sample Signature", sample_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Verify signatures using the similarity threshold
    verify_signature(original_image, sample_image, thresh)

def browse_file(entry):
    filename = tk.filedialog.askopenfilename(filetypes=[
        ("Image Files", "*.jpeg;*.png;*.jpg"),
    ])
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)

def verify_signature(signature1, signature2, thresh):
    # Resize the images to a consistent size
    signature1 = cv2.resize(signature1, (200, 200))
    signature2 = cv2.resize(signature2, (200, 200))

    # Calculate the SSIM between the two signatures
    similarity = ssim(signature1, signature2)

    # Determine if the signatures match based on the threshold
    if similarity >= thresh:
        tk.messagebox.showinfo("Success: Signatures Match", f"Signatures are {similarity*100:.2f}% similar!")
    else:
        tk.messagebox.showerror("Failure: Signatures Do Not Match", f"Signatures are {similarity*100:.2f}% similar.")


root = tk.Tk()
root.title("Signature Matching")
root.geometry("800x400")  # square geometry
root.configure(bg="light blue")
uname_label = tk.Label(root, text="SIGNATURES :", font=10)
uname_label.place(x=285, y=50)

img1_message = tk.Label(root, text="Original Signature", font=10)
img1_message.place(x=50, y=100)

image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=50, y=130)

img1_browse_button = tk.Button(root, text="OPEN FILE", font=10, command=lambda: browse_file(entry=image1_path_entry))
img1_browse_button.place(x=85, y=170)

img1_message = tk.Label(root, text="Sample Signature", font=10)
img1_message.place(x=450, y=100)

image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=450, y=130)

img2_browse_button = tk.Button(root, text="OPEN FILE", font=10, command=lambda: browse_file(entry=image2_path_entry))
img2_browse_button.place(x=485, y=170)

compare_button = tk.Button(root, text="Run", font=10, command=lambda: compare_signatures(image_path1=image1_path_entry.get(),
                                                                                         image_path2=image2_path_entry.get()))
compare_button.place(x=340, y=250)

root.mainloop() 

for i in range(2,11):
    if i%2==0:
        print(i)
    else:
        print("hello")