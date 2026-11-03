# Haas Japanese Colab

Notebook do Google Colab para transcrever áudio e vídeo em japonês com Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_pt.ipynb)

## Recursos

- **Gratuito:** Funciona no ambiente de GPU gratuito do Google Colab.
- **ASR de japonês:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), um modelo de aproximadamente 0.6B parâmetros para reconhecimento de fala em japonês.
- **Rápido:** A transcrição pode ser processada rapidamente.
- **Pontuação:** O modelo produz pontuação japonesa estimada.
- **Marcas de tempo e legendas:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Processamento de arquivos longos:** Arquivos longos de áudio e vídeo também podem ser processados.
- **Suporte ao Google Drive:** Envie arquivos diretamente ou leia-os do Google Drive; o ZIP de saída pode ser salvo opcionalmente no Drive.
- **Múltiplas saídas:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifesto e ZIP.

## Uso

1. Escolha `INPUT_MODE` em **1. Settings** e ajuste outras configurações se necessário.
2. Selecione **Runtime → Run all**.
3. Com `INPUT_MODE = "upload"`, escolha os arquivos em **2. File selection / Google Drive mount**.
4. O ZIP de saída é baixado automaticamente após o processamento.

## Modos de marca de tempo

- `none`: sem informação temporal.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decodificador

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Arquivos longos

`CHUNK_SECONDS` controla a duração interna dos blocos usados em arquivos longos. Valores maiores reduzem os limites e preservam mais contexto, mas tornam cada inferência mais pesada e podem aumentar o uso de memória da GPU. Valores menores tornam cada inferência mais leve, mas criam mais limites, o que pode afetar o reconhecimento nesses pontos. O valor padrão é recomendado na maioria dos casos.

## Interface localizada

O próprio modelo ASR é **somente para japonês**. A localização do README e da interface do Colab cobre todos os **183 idiomas ativos do ISO 639 Set 1** (o obsoleto `sh` é excluído).

O inglês (`en`) é a fonte canônica de tradução. O japonês (`ja`) é uma tradução revisada e é copiado para a raiz do repositório como a apresentação padrão `README.md`. O README japonês da raiz **não** é usado como fonte de tradução. Os outros 181 locales são traduzidos automaticamente a partir do inglês.

## Observações

- O notebook para antes da transcrição se uma GPU não estiver disponível.
- O tempo de processamento depende da duração da entrada, das configurações e da GPU atribuída pelo Colab. A primeira execução também baixa o NeMo e o modelo de aproximadamente 1.23 GB.
- Áudio longo é processado em blocos internos, por isso o reconhecimento pode ser afetado próximo aos limites dos blocos.

## Fonte canônica e geração

Fontes canônicas traduzíveis:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` é o snapshot canônico sincronizado. O japonês é mantido como tradução revisada em `locales/ja.json`, e seu snapshot de README é copiado para a raiz como `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

A manutenção das traduções é separada da CI normal. Usuários comuns e a CI não precisam de credenciais de tradução.

## Licença

A estrutura do notebook e os scripts de build/verificação são licenciados sob MIT. O modelo Third Intelligence não é redistribuído aqui e é regido por **Apache-2.0**. Dependências de terceiros mantêm suas próprias licenças.
