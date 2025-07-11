# Archive Extractor Library

A Python library for extracting files from various archive formats (ZIP, RAR, 7z) with support for comic book formats (.cbr, .cb7).

## Features

- Supports multiple archive formats:
  - ZIP (.zip, .zipx)
  - RAR (.rar, .cbr)
  - 7-Zip (.7z, .cb7)
- Preserves directory structure
- Returns list of extracted files
- Configurable unrar tool path
- Comprehensive error handling

## Installation

1. Install required packages:
```bash
pip install rarfile py7zr
```
For RAR support, ensure you have unrar installed on your system:

Linux (Debian/Ubuntu):

```bash
sudo apt-get install unrar
```

MacOS (using Homebrew):

```bash
brew install unrar
```
## Usage
### Basic Example
```python
from archive_extractor import ArchiveExtractor

# Initialize extractor
extractor = ArchiveExtractor()

# Extract archive
extracted_files = extractor.extract("archive.zip", "output_folder")
print(f"Extracted {len(extracted_files)} files")
```
### Advanced Example
```python
from archive_extractor import ArchiveExtractor

# Initialize with custom unrar path
extractor = ArchiveExtractor(unrar_tool_path="/custom/path/to/unrar")

try:
    # Extract to same directory as archive
    files = extractor.extract("comic.cbr")
    for file in files:
        print(f"Extracted: {file}")
except ValueError as e:
    print(f"Input error: {e}")
except TypeError as e:
    print(f"Unsupported format: {e}")
except Exception as e:
    print(f"Extraction failed: {e}")
```
### API Reference
#### Initialize the archive extractor.
```python
ArchiveExtractor(unrar_tool_path: str = "/usr/bin/unrar")
```
Parameters:

- unrar_tool_path - Path to unrar executable (default: "/usr/bin/unrar")

#### Extract contents of an archive.
```python
extract(archive_path: str, output_dir: Optional[str] = None) -> List[str]
```
Parameters:

- archive_path - Path to archive file

- output_dir - Directory to extract to (defaults to archive's directory)

Returns:

- List of paths to extracted files

Raises:

- ValueError - If input is not a file or output is not a directory

- TypeError - If archive format is not supported

- FileNotFoundError - If unrar tool is not found

## Supported Formats
| Format  | Extensions       |
|:-------:|:----------------:|
| ZIP     | .zip, .zipx      |
| RAR     | .rar, .cbr       |
| 7-Zip   | .7z, .cb7        |
