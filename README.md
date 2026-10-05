# 🚀 DevOps (4th semester)

Coursework from **Operaciones y desarrollo** — cleaned portfolio (shell, Python, GitHub Actions, ASP.NET CI demo).

**Author:** José Alberto Rocha Munguía

## 📦 Contents

| Folder | Topic |
|---|---|
| `activity-04-shell-scripts/` | Bash: hello world, file attributes, copy, product split |
| `activity-05-vim-intro/` | Vim intro notes + tiny shell helper |
| `activity-06-python-basics/` | Python loops / functions / class (`@author josea`) |
| `activity-07-python-oop-tests/` | Inheritance, ABC, `unittest` |
| `activity-11-ci-hello/` | Script run by the Python GitHub Action |
| `exploring-actions/` | ASP.NET Core WeatherForecast API + xUnit test |
| `.github/workflows/` | Actions demos (env vars, Python job, .NET tests) |

## ▶️ Quick tests

```bash
# Shell
cd activity-04-shell-scripts
bash hola_mundo.sh
bash atributos.sh .
bash copia_archivos.sh copia.txt
bash consolidado_producto.sh

# Python
cd ../activity-06-python-basics
printf '4\n' | python3 act6_print.py

cd ../activity-07-python-oop-tests
python3 -m unittest act7_4_unit_test.py act7_unit_test.py -v

# .NET
cd ../exploring-actions
dotnet test ExploringActions.sln
```

## 📝 Notes

- Original Spanish prompts / filenames kept where they were part of the delivery.
- Python headers keep `Created on …` + `@author josea`.
- Visual Studio junk (`bin/`, `obj/`, `.vs/`) was removed from the portfolio.
