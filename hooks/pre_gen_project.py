"""
{% set gitpkgname = cookiecutter.pkgname.removeprefix("python-").removesuffix("-git") %}
{% set is_vcs = cookiecutter.pkgver == "VERSION" %}
{% set pkgname_var_name = "_gitpkgname" if gitpkgname != cookiecutter.pkgname else "pkgname" %}
{{
    cookiecutter.update({
        "gitpkgname": gitpkgname,
        "is_vcs": is_vcs,
        "pkgname_no_vcs": cookiecutter.pkgname.removesuffix("-git"),
        "pkgname_var": "${" + pkgname_var_name + "}",
        "src_subdir":
            "".join([
                "${",
                pkgname_var_name,
                "}",
                "" if is_vcs else "-${pkgver}",
            ]),
    })
}}
"""
