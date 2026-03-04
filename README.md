# Gaspar's file organizer

Um software para a organização de arquivos baixados na internet, de forma fácil, pelo terminal.

## 🖥️ Começando.

### 📋 Pré requisitos.

para obter e utilizar os arquivos, são necessárias algumas dependências do projeto.

- PYTHON instalado localmente na máquina.
- PIP(Windows) - já vem instalado com o python
- PIPX(Linux/Mac)
UBUNTU e distros baseadas no instalador APT:
```
  sudo apt install pipx
```
FEDORA e distros baseadas no instalador DNF:
```
  sudo dnf install pipx
```
Apenas mude para o gerenciador de pacotes usado na sua Distro.

### 🔧 Instalação.

1 - Baixar o repositório pelo PIP ou PIPX:
no terminal LINUX:
```
pipx install gaspars-file-organizer
```
No terminal Windows:
```
pip install gaspars-file-organizer
```

2 - definir as variáveis de ambiente:
no terminal LINUX:
```
pipx ensurepath
```
```
nano ~/.bashrc

#dentro do arquivo, no final, adicione as seguintes linhas:

export Destino="{caminho onde os arquivos devem ir}"
export Downloads="{caminho da sua pasta de Downloads}"
```

no Windows:
1. Abra o menu iniciar e pesquise por: editar as variáveis de ambiente do sistema
2. Em variáveis do sistema, clique em "Path" e depois "editar"
3. dentro da aba que abrir, clique em novo e cole o caminho da pasta de scripts do python
   (normalmente fica em C:\Users\seuUsuario\AppData\(Roaming ou local)\Python\Python313\Scripts
4. clique em ok.
5. de volta na aba anterior, clique em novo:
6. em nome da varíavel digite Destino, e no valor, o caminho da pasta que você deseja colocar os arquivos.
7. clique em ok.
8. repita o processo para a varíavel Downloads, com o valor da sua pasta de Downloads.

### 👨‍💻 Utilizando.

para utilizar o software, basta ir no terminal(após ter feito os passos anteriorer) e digite:
```
organizar
```
