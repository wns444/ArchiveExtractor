import os
import zipfile
import rarfile
import py7zr
from dataclasses import dataclass

class ArchiveExtractor:
    """
    A comprehensive library for extracting files from various archive formats.
    
    Features:
    - Supports ZIP, RAR, 7z formats (including comic book formats .cbr, .cb7)
    - Preserves directory structure
    - Returns list of extracted files
    - Configurable unrar tool path
    
    Usage:
        extractor = ArchiveExtractor()
        extracted_files = extractor.extract("archive.zip", "output_folder")
    """
    
    def __init__(self, unrar_tool_path: str = "/usr/bin/unrar"):
        """
        Initialize the archive extractor.
        
        Args:
            unrar_tool_path (str): Path to unrar executable. Defaults to '/usr/bin/unrar'.
        """
        self._set_unrar_tool(unrar_tool_path)
    
    @dataclass
    class SupportedFormats:
        """Supported file extensions for different archive formats."""
        ZIP: list[str] = [".zip", ".zipx"]
        RAR: list[str] = [".rar", ".cbr"]
        SEVEN_ZIP: list[str] = [".7z", ".cb7"]
    
    def _set_unrar_tool(self, path: str) -> None:
        """Set the path to unrar executable."""
        if os.path.exists(path):
            rarfile.UNRAR_TOOL = path
        else:
            raise FileNotFoundError(f"unrar tool not found at: {path}")
    
    def extract(self, archive_path: str, output_dir: str | None = None) -> list[str]:
        """
        Extract contents of an archive to specified directory.
        
        Args:
            archive_path (str): Path to the archive file
            output_dir (str, optional): Directory to extract to. Defaults to archive's directory.
        
        Returns:
            List[str]: Paths to all extracted files
            
        Raises:
            ValueError: If input is not a file or output is not a directory
            TypeError: If archive format is not supported
        """
        self._validate_inputs(archive_path, output_dir)
        
        ext = os.path.splitext(archive_path)[1].lower()
        output_dir = output_dir or os.path.dirname(archive_path)
        
        if ext in self.SupportedFormats.ZIP:
            return self._extract_zip(archive_path, output_dir)
        elif ext in self.SupportedFormats.RAR:
            return self._extract_rar(archive_path, output_dir)
        elif ext in self.SupportedFormats.SEVEN_ZIP:
            return self._extract_7z(archive_path, output_dir)
        else:
            raise TypeError(f"Unsupported archive format: {ext}")
    
    def _validate_inputs(self, archive_path: str, output_dir: str | None) -> None:
        """Validate input archive and output directory."""
        if not os.path.isfile(archive_path):
            raise ValueError(f"Not a valid archive file: {archive_path}")
        
        if output_dir and not os.path.isdir(output_dir):
            raise ValueError(f"Output directory doesn't exist: {output_dir}")
    
    def _extract_zip(self, archive_path: str, output_dir: str) -> list[str]:
        """Extract ZIP archive and return list of extracted files."""
        extracted_files = []
        with zipfile.ZipFile(archive_path) as zip_ref:
            zip_ref.extractall(output_dir)
            for member in zip_ref.namelist():
                file_path = os.path.join(output_dir, member)
                if os.path.isfile(file_path):
                    extracted_files.append(file_path)
        return extracted_files
    
    def _extract_rar(self, archive_path: str, output_dir: str) -> list[str]:
        """Extract RAR archive and return list of extracted files."""
        extracted_files = []
        with rarfile.RarFile(archive_path) as rar_ref:
            rar_ref.extractall(output_dir)
            for member in rar_ref.namelist():
                file_path = os.path.join(output_dir, member)
                if os.path.isfile(file_path):
                    extracted_files.append(file_path)
        return extracted_files
    
    def _extract_7z(self, archive_path: str, output_dir: str) -> list[str]:
        """Extract 7z archive and return list of extracted files."""
        extracted_files = []
        with py7zr.SevenZipFile(archive_path, mode='r') as seven_zip_ref:
            seven_zip_ref.extractall(output_dir)
            for member in seven_zip_ref.getnames():
                file_path = os.path.join(output_dir, member)
                if os.path.isfile(file_path):
                    extracted_files.append(file_path)
        return extracted_files