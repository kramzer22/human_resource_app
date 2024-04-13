from cx_Freeze import setup, Executable

setup(
    name="Simple_Applicant",
    version="0.1",
    description="Simple Applicant",
    executables=[Executable("main.py")]
)