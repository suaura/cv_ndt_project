from __future__ import annotations

import argparse
import random
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

CLASSES = [
    "crazing",
    "inclusion",
    "patches",
    "pitted_surface",
    "rolled-in_scale",
    "scratches",
]
NAME2ID = {n: i for i, n in enumerate(CLASSES)}


def parse_xml(xml_path: Path):
    root = ET.parse(xml_path).getroot()
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    objs = []
    for obj in root.findall("object"):
        name = obj.find("name").text
        cid = NAME2ID[name]
        b = obj.find("bndbox")
        xmin = float(b.find("xmin").text)
        ymin = float(b.find("ymin").text)
        xmax = float(b.find("xmax").text)
        ymax = float(b.find("ymax").text)

        xc = ((xmin + xmax) / 2) / w
        yc = ((ymin + ymax) / 2) / h
        bw = (xmax - xmin) / w
        bh = (ymax - ymin) / h

        objs.append((cid, xc, yc, bw, bh))
    return objs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, required=True)
    ap.add_argument("--dst", type=Path, required=True)
    args = ap.parse_args()

    random.seed(42)

    for split in ["train", "validation"]:
        img_dir = args.src / split / "images"
        ann_dir = args.src / split / "annotations"

        out_img = args.dst / "images" / ("val" if split == "validation" else "train")
        out_lbl = args.dst / "labels" / ("val" if split == "validation" else "train")
        out_img.mkdir(parents=True, exist_ok=True)
        out_lbl.mkdir(parents=True, exist_ok=True)

        for xml in ann_dir.glob("*.xml"):
            labels = parse_xml(xml)
            img = next(iter([p for p in img_dir.rglob("*") if p.is_file() and p.stem == xml.stem]), None)

            if img is None: continue
            shutil.copy2(img, out_img / img.name)
            with open(out_lbl / f"{xml.stem}.txt", "w") as f:
                for cid, xc, yc, bw, bh in labels:
                    f.write(f"{cid} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

    print("OK: NEU-DET → YOLO 변환 완료")


if __name__ == "__main__":
    main()
