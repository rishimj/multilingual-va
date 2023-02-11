import subprocess

def convert():
    input_dir = input("Enter input directory name: ")
    output_dir = input("Enter output directory name: ")
    format_type = input("Enter format to convert to [ENTER for .mp3]: ")

    if format_type == "":
        format_type = ".mp3"

    subprocess.run(["audioconvert", "convert", input_dir, output_dir, "--output-format", format_type])

convert()
