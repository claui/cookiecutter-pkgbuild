# cookiecutter-pkgbuild

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for Arch Linux PKGBUILDs.


## Using cookiecutter-pkgbuild

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```
cookiecutter gh:claui/cookiecutter-pkgbuild
```

### Alternative usage

If you use `cookiecutter-pkgbuild` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```
abbreviations:
    pkgbuild: https://github.com/claui/cookiecutter-pkgbuild.git
```

Then, to generate a project, run:

```
cookiecutter pkgbuild
```


## License

Copyright (c) 2021 – 2025 Claudia Pellegrino <clau@tiqua.de>

Licensed under the BSD Zero Clause License, see [LICENSE](LICENSE).
