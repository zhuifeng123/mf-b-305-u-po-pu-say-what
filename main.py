from pathlib import Path

ENTRY = (
    "TypeError: Cannot read properties of null (reading 'hope') - the fix is "
    "merged, it just hasn't reached production. Like your weekend plans."
)

def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
