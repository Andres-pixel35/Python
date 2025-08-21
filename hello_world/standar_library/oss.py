import os

cwd = os.getcwd()
print(cwd)

txt_files = [f for f in os.listdir(".") if f.endswith(".py")]

print(txt_files)