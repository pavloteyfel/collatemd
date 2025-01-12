import os
import argparse

# Map file extensions to code block languages for Markdown
EXTENSION_LANGUAGE_MAP = {
    "py": "python",
    "html": "html",
    "js": "javascript",
    "ejs": "html",
    "css": "css",
    "sql": "sql"
}

def collect_files_to_markdown(root_dir, output_file, extensions, skip_folders):
    """
    Recursively collect files with given extensions and write their contents
    into a Markdown document, using the relative file path as the Markdown heading.
    """
    with open(output_file, "w", encoding="utf-8") as md_file:
        for root, dirs, files in os.walk(root_dir):
            # Remove directories to skip from the search
            dirs[:] = [d for d in dirs if d not in skip_folders]
            
            for file in files:
                # Only process files that match the provided extensions
                # and skip the script file itself (if it happens to be in the same folder)
                if file.split(".")[-1] in extensions and file != os.path.basename(__file__):
                    filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(filepath, root_dir)

                    # Use the relative path as the Markdown heading
                    md_file.write(f"# {relative_path}\n")

                    # Determine the language for the code block
                    extension = file.split(".")[-1]
                    language = EXTENSION_LANGUAGE_MAP.get(extension, "")

                    # Add file content wrapped in code blocks
                    md_file.write(f"```{language}\n")
                    with open(filepath, "r", encoding="utf-8") as f:
                        md_file.write(f.read())
                    md_file.write("\n```\n\n")

def main():
    parser = argparse.ArgumentParser(description="Collect files into a Markdown document.")
    parser.add_argument("-p", "--path", type=str, default=".", 
                        help="Path to start searching (default: current directory)")
    parser.add_argument("-e", "--extensions", type=str, default="py,html",
                        help="Comma-separated list of extensions to include (default: py,html)")
    parser.add_argument("-o", "--output", type=str, default="output.md",
                        help="Output Markdown file name (default: output.md)")
    parser.add_argument("--skip-folder", type=str, default="",
                        help="Comma-separated list of folder names to skip")

    args = parser.parse_args()

    root_directory = args.path
    output_markdown = args.output
    extensions = args.extensions.split(",")
    skip_folders = args.skip_folder.split(",") if args.skip_folder else []

    collect_files_to_markdown(root_directory, output_markdown, extensions, skip_folders)
    print(f"Markdown document created: {output_markdown}")

if __name__ == "__main__":
    main()
