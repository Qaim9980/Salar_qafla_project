from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox

from ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Universal Editable Design Converter")
    try:
        window = MainWindow()
        window.show()
        return app.exec()
    except Exception as exc:
        log_path = Path(__file__).with_name("editor-error.log")
        log_path.write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        QMessageBox.critical(
            None,
            "Editor could not start",
            f"The editor encountered an error.\n\n{exc}\n\nDetails were saved to:\n{log_path}",
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
