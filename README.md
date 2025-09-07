# imgbatch v1.0
A lightweight Python tool for batch image conversion and archiving

## 🚀 Platform Support

![Linux](https://img.shields.io/badge/Linux-Supported-brightgreen?logo=linux)
![macOS](https://img.shields.io/badge/macOS-Supported-brightgreen?logo=apple)
![FreeBSD](https://img.shields.io/badge/FreeBSD-Supported-brightgreen?logo=freebsd)
![Windows](https://img.shields.io/badge/Windows-Supported-brightgreen?logo=windows)

**imgbatch** is a powerful yet simple command-line tool for batch image processing. Convert multiple images between formats, create ZIP archives, and use smart search features to process exactly the files you need.

## ✨ Features

- 🖼️ **Format Conversion**: Convert images between popular formats (JPG, PNG, WebP, etc.)
- 📦 **Batch Processing**: Convert multiple files at once with concurrent processing
- 🗂️ **ZIP Archiving**: Package converted images into a single ZIP file
- 🔍 **Smart Search**:
  - File-based search with fuzzy matching
  - Date-based filtering
  - Recursive directory search support

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/booo2233/imgbatch.git
cd imgbatch
```

2. Install dependencies:
```bash
pip install -r src/imgbatch/requirements.txt
```

3. Run the tool:
```bash
python -m imgbatch --help
```

## 📚 Usage Examples

### Basic Conversion
Convert all JPG images in current directory to PNG:
```bash
python -m imgbatch convert --input jpg --output png
```

### Create ZIP Archive
Convert and create a ZIP archive:
```bash
python -m imgbatch zip --input jpg --output png --zipname my_images
```

### Smart Search
Use interactive file selection:
```bash
python -m imgbatch spsearch --input jpg --output png
```

### Advanced Options
- `--directory (-f)`: Specify input directory
- `--recurse (-r)`: Search in subdirectories
- `--delete (-d)`: Delete original files after conversion
- `--zipname (-zn)`: Custom name for ZIP archive

## 🛠️ Commands

| Command | Description |
|---------|-------------|
| `convert` | Convert images between formats |
| `zip` | Convert and create ZIP archive |
| `spsearch` | Interactive file selection and conversion |

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 🎉 Acknowledgments

Thanks to all contributors and users of this project!

