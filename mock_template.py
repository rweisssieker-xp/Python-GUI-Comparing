import tkinter as tk

def create_mock(name, reason):
    root = tk.Tk()
    root.title(f"{name} Information")
    root.geometry("500x300")
    
    label = tk.Label(root, text=f"Framework: {name}", font=("Arial", 16, "bold"), pady=20)
    label.pack()
    
    info = tk.Label(root, text=reason, wraplength=450, justify="left", pady=10)
    info.pack()
    
    btn = tk.Button(root, text="Close", command=root.destroy)
    btn.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    # This script will be used as a template for non-runnable frameworks
    import sys
    if len(sys.argv) > 2:
        create_mock(sys.argv[1], sys.argv[2])
    else:
        create_mock("Unknown Framework", "No details available for this platform/environment.")
