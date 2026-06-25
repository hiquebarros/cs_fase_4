# cs_fase4

Estrutura base de projeto Python com ambiente virtual.

## Como usar

Ative o ambiente virtual no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale o projeto com dependencias de desenvolvimento:

```powershell
python -m pip install -e ".[dev]"
```

Execute a aplicacao:

```powershell
python -m cs_fase4.main
```

Execute os testes:

```powershell
pytest
```
