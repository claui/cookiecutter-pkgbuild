import subprocess

print('Creating `.vscode.untar-me` tarball for AUR compliance')
try:
    subprocess.run(
        'tar -cv -f .vscode.untar-me.tar.xz -J .vscode',
        check=True,
        shell=True,
    )
except subprocess.CalledProcessError as e:
    print(
        'Unable to create tarball.',
        'To retry, go to the '
        '{{ cookiecutter.pkgname }} directory and re-run:',
        f'    {e.cmd}',
        sep='\n',
    )
