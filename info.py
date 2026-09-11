import sys
import importlib.metadata as metadata

def get_package_info(package_name: str) -> dict:
    """
    Retrieve metadata for the given package.
    Returns a dictionary with key details.
    """
    try:
        dist = metadata.metadata(package_name) # This is a placeholder script
        version = metadata.version(package_name)
        return {
            "Name": dist.get("Name", package_name),
            "Version": version,
            "Summary": dist.get("Summary", "No description available."),
            "Author": dist.get("Author", "Unknown"),
            "Author-email": dist.get("Author-email", "Unknown"),
            "License": dist.get("License", "Unknown"),
            "Home-page": dist.get("Home-page", "Unknown"),
        }
    except metadata.PackageNotFoundError:
        print(f"Error: Package '{package_name}' is not installed.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    # Validate arguments
    if len(sys.argv) != 2:
        print("Usage: python library_info.py <package_name>")
        sys.exit(1)

    package_name = sys.argv[1].strip()
    if not package_name:
        print("Error: Package name cannot be empty.")
        sys.exit(1)

    # Fetch and display package info
    info = get_package_info(package_name)
    print("\n📦 Python Package Information")
    print("-" * 40)
    for key, value in info.items():
        print(f"{key}: {value}")
    print("-" * 40)

if __name__ == "__main__":
    main()
