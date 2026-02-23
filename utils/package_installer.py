"""Utilities for installing third-party dependencies using pip."""

import sys
import subprocess
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version as get_version
from pathlib import Path

try:
    from packaging.specifiers import SpecifierSet
    from packaging.version import InvalidVersion, Version
    _HAS_PACKAGING = True
except Exception:  # pragma: no cover - optional dependency
    _HAS_PACKAGING = False

_REQ_OPERATORS = ("==", ">=", "<=", "!=", "~=", ">", "<")


def install_dependencies(requirements_file: str | Path = "requirements.txt",
                         check_updates: bool = True,
                         update_pip: bool = True, ) -> None:
    """Ensure third-party packages listed in a text file are installed.

    Reads a text file where each non-empty, non-comment line is a package name
    optionally followed by a version specifier (for example, ``>=1.2.0`` or
    ``==2.24.0``). For each package, attempts to import it, and if missing,
    installs it via pip. If installed and updates are allowed, checks for a
    newer version (respecting any version specifier) and upgrades if needed.
    Optionally upgrades pip before the first installation/upgrade.

    Exits function if requirements file not found.
    
    Note: Make sure to import the dependencies after calling this function.

    Parameters:
        requirements_file (str | Path, optional):
            Path to a text file with one package name per line, optionally
            followed by a version specifier (default is "requirements.txt").
        check_updates (bool, optional):
            Whether to check for newer versions and upgrade already-installed
            packages (default is True). When False, packages that can be
            imported are skipped.
        update_pip (bool, optional):
            Whether to upgrade pip before installing (default is True).
            
    Raises:
        OSError: Failed to read requirements file.
        RuntimeError: Failed to install packages.
    """
    print("\nInstalling third-party dependencies...\n")
    
    requirements = _read_requirements_file(requirements_file)
    if not requirements:
        return

    pip_upgraded = False
    for pkg_name, spec in requirements.items():
        requirement = f"{pkg_name}{spec}" if spec else pkg_name
        installed = True
        try:
            import_module(pkg_name)
        except ModuleNotFoundError:
            installed = False

        if installed and not check_updates:
            continue
        if installed and check_updates:
            installed_version = _get_installed_version(pkg_name)
            latest_version = _get_latest_satisfying_version(pkg_name, spec)
            if (installed_version and latest_version and
                    _is_latest(installed_version, latest_version)):
                continue

        try:
            if update_pip and not pip_upgraded:
                print("\nUpgrading pip...\n")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "--upgrade",
                     "pip"]
                )
                pip_upgraded = True

            install_cmd = [sys.executable, "-m", "pip", "install"]
            if check_updates:
                install_cmd.append("--upgrade")
            install_cmd.append(requirement)
            subprocess.check_call(install_cmd)

            print(f"\nSuccessfully installed '{pkg_name}'.")

        except subprocess.CalledProcessError:
            raise RuntimeError(
                f"\nFailed to install '{pkg_name}'. Please install it manually."
            )
        
    print("\nSuccessfully installed dependencies.")
    print("Resuming program...")
    print("\n==============================\n")


def _get_installed_version(pkg_name: str) -> str | None:
    """Return the installed distribution version, or None if not installed."""
    try:
        return get_version(pkg_name)
    except PackageNotFoundError:
        return None


def _get_available_versions(pkg_name: str) -> list[str]:
    """Return available versions from the index, newest first."""
    try:
        output = subprocess.check_output(
            [sys.executable, "-m", "pip", "index", "versions", pkg_name],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        return []

    for line in output.splitlines():
        if "Available versions:" in line:
            versions = line.split("Available versions:", 1)[1].strip()
            if not versions:
                return []
            return [v.strip() for v in versions.split(",") if v.strip()]
        if "LATEST:" in line:
            parts = line.split("LATEST:", 1)[1].strip().split()
            return [parts[0]] if parts else []
    return []


def _get_latest_satisfying_version(pkg_name: str, spec: str) -> str | None:
    """Return latest available version that satisfies spec, or None."""
    versions = _get_available_versions(pkg_name)
    if not versions:
        return None
    if not spec:
        return versions[0]
    if not _HAS_PACKAGING:
        return None

    spec_set = SpecifierSet(spec)
    for version in versions:
        try:
            parsed = Version(version)
        except InvalidVersion:
            continue
        if spec_set.contains(parsed, prereleases=True):
            return version
    return None


def _is_latest(installed_version: str, latest_version: str) -> bool:
    """Return True if installed version is up-to-date."""
    if _HAS_PACKAGING:
        try:
            return Version(installed_version) >= Version(latest_version)
        except InvalidVersion:
            return installed_version == latest_version
    return installed_version == latest_version


def _parse_requirement_line(line: str) -> tuple[str, str]:
    """Parse a requirements line into (name, spec)."""
    stripped = line.split("#", 1)[0].strip()
    if not stripped:
        return "", ""

    normalized = "".join(stripped.split())
    for op in _REQ_OPERATORS:
        if op in normalized:
            name, version = normalized.split(op, 1)
            name = name.strip()
            version = version.strip()
            if not name:
                return "", ""
            return name, f"{op}{version}" if version else op
    return normalized, ""


def _read_requirements_file(requirements_file: str | Path) -> dict[str, str]:
    """Read requirements and return a mapping of package name to spec."""
    requirements_path = Path(requirements_file)
    try:
        lines = requirements_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return {}
    except OSError as exc:
        raise OSError(
            f"\nFailed to read requirements file '{requirements_path}': {exc}"
        )

    requirements: dict[str, str] = {}
    for line in lines:
        pkg_name, spec = _parse_requirement_line(line)
        if not pkg_name:
            continue
        requirements[pkg_name] = spec
    return requirements
