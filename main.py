import os
import sys

# Thử import thư viện rich (Nếu không dùng uv, Colab sẽ báo lỗi vì chưa cài cái này)
try:
    from rich import print
    from rich.panel import Panel
except ImportError:
    print("LỖI: Không tìm thấy thư viện 'rich'!")
    sys.exit(1)


def main():
    # Lấy thông tin phiên bản Python đang chạy
    py_version = sys.version.split()[0]

    # Lấy đường dẫn của file python.exe đang chạy
    py_executable = sys.executable

    # In ra màn hình bằng thư viện Rich (Màu xanh lá cây)
    print(
        Panel.fit(
            f"[bold yellow]KIỂM TRA MÔI TRƯỜNG UV[/bold yellow]\n\n"
            f"[bold cyan]Python Version:[/bold cyan] [white]{py_version}[/white]\n"
            f"[bold cyan]Python Path:[/bold cyan]    [white]{py_executable}[/white]\n"
            f"[bold cyan]Rich Library:[/bold cyan]    [green]Đã cài đặt và hoạt động tốt![/green]",
            title="UV Proof of Concept",
            border_style="green",
        )
    )

    # Kiểm tra logic: Có đúng là Python 3.9 không?
    if py_version.startswith("3.9"):
        print(
            "\n[bold green]✅ THÀNH CÔNG: Đang chạy đúng Python 3.9 (Do uv quản lý)![/bold green]"
        )
    else:
        print(
            f"\n[bold red]❌ THẤT BẠI: Đang chạy Python {py_version} (Có thể là mặc định của Colab)![/bold red]"
        )


if __name__ == "__main__":
    main()
