"""make.fun entry: Sum up 18 November's world news in one image.

Copies the bundled artwork (art18.jpg, a 1024x1024 JPEG) to
/output/entry.png. Standard library only, no network, deterministic:
running this program twice writes identical bytes.
"""

import pathlib
import shutil


def main() -> None:
    src = pathlib.Path(__file__).resolve().with_name("art18.jpg")
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
