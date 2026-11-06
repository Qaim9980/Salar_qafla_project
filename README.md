# Universal JPG to Editable Design Converter

Local-first Python desktop application for reconstructing ordinary flattened images into editable projects.

## Safety boundary

The application can open, analyze, archive, and redact protected documents, but it does not provide editing or export controls for identity information, photographs, signatures, barcodes, seals, or official markings in government, identity, financial, or similar records. Detection is conservative and can be overridden only for clearly fictional samples.

## Requirements

- Python 3.11+
- PySide6
- Pillow
- NumPy
- OpenCV (optional, used for analysis)
- EasyOCR (optional, used for OCR)

Install:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

On Windows, double-click **Open Editor.bat**. In the application:

1. Click **Open** and choose an image.
2. Use **Text** or **Shape** to add editable layers.
3. Select a layer in the right panel and change its position, size, opacity, text, or color.
4. Click **Save project** to save an editable JSON project.
5. Click **Export PNG** or **Export SVG** when working with an ordinary design.

If the window closes unexpectedly, run **Open Editor.bat** again. It will pause and show the error instead of closing immediately. The details are also saved in `editor-error.log`.

OCR requires EasyOCR and OpenCV. Install them with `python -m pip install easyocr opencv-python`; the first OCR run downloads the local recognition model. The application remains usable as a layer editor without OCR.

## Features

- Open JPG, JPEG, PNG, and WebP while preserving the original file.
- Non-destructive canvas with image, text, and shape layers.
- Layer visibility, locking, opacity, ordering, duplication, deletion, and renaming.
- Select, move, resize, and rotate layers.
- OCR layer generation when EasyOCR is available.
- Local image analysis report with dimensions, color statistics, and protected-document classification.
- JSON project files with embedded or referenced assets.
- PNG/JPG export and editable SVG export for permitted projects.
- Protected-document mode with archival and redaction workflows.

PSD export is intentionally not included: PSD writing requires a specialized format writer and can create misleadingly editable copies of protected documents. The JSON project and SVG export are the supported editable formats.

## Run tests

```powershell
pytest
```

## Troubleshooting

- **PySide6 installation is large:** install with `python -m pip install PySide6` on a stable connection; the Qt wheels include native desktop libraries.
- **OCR is unavailable:** the editor still works without OCR. Install `easyocr` and run OCR again; the first run downloads its local model.
- **A document is protected:** this is intentional. The original can be viewed and saved as a project for archival, but sensitive official content cannot be altered or exported.
- **Exported SVG images do not embed pixels:** SVG keeps image assets as file references so they remain replaceable. Keep the referenced files beside the SVG.
