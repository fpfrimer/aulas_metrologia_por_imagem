from argparse import ArgumentParser
from csv import DictWriter
from pathlib import Path

from PIL import Image


def listar_imagens(pasta):
    extensoes = {".jpg", ".jpeg", ".png"}
    return sorted(
        arquivo for arquivo in Path(pasta).iterdir()
        if arquivo.is_file() and arquivo.suffix.lower() in extensoes
    )


def etapa_por_indice(indice):
    if indice <= 11:
        return "boa"
    if indice <= 21:
        return "intermediaria"
    return "deteriorada"


def media_rgb(caminho, ignorar_fundo=True, limite_branco=220, tamanho_maximo=600, roi=None):
    imagem = Image.open(caminho).convert("RGB")
    if roi:
        x, y, largura, altura = roi
        imagem = imagem.crop((x, y, x + largura, y + altura))

    imagem.thumbnail((tamanho_maximo, tamanho_maximo))

    soma_r = 0
    soma_g = 0
    soma_b = 0
    contador = 0

    for r, g, b in imagem.getdata():
        fundo_branco = r >= limite_branco and g >= limite_branco and b >= limite_branco
        if ignorar_fundo and fundo_branco:
            continue

        soma_r += r
        soma_g += g
        soma_b += b
        contador += 1

    if contador == 0:
        raise ValueError(f"Nenhum pixel valido encontrado em {caminho}")

    return soma_r / contador, soma_g / contador, soma_b / contador, contador


def salvar_csv(linhas, caminho_saida):
    with open(caminho_saida, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["indice", "arquivo", "etapa", "media_r", "media_g", "media_b", "pixels_usados"]
        escritor = DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas)


def salvar_grafico(linhas, caminho_saida):
    import matplotlib.pyplot as plt

    x = [linha["indice"] for linha in linhas]
    r = [linha["media_r"] for linha in linhas]
    g = [linha["media_g"] for linha in linhas]
    b = [linha["media_b"] for linha in linhas]

    plt.figure(figsize=(9, 5))
    plt.plot(x, r, "r-o", label="R")
    plt.plot(x, g, "g-o", label="G")
    plt.plot(x, b, "b-o", label="B")
    plt.xlabel("Indice da imagem")
    plt.ylabel("Intensidade media")
    plt.title("Componentes RGB ao longo da sequencia")
    plt.ylim(0, 255)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=150)


def identificar_etapa(nome, indice):
    if "intermediaria" in nome:
        return "intermediaria"
    if "deteriorada" in nome:
        return "deteriorada"
    if "boa" in nome:
        return "boa"
    return etapa_por_indice(indice)


def main():
    parser = ArgumentParser(description="Calcula medias RGB de uma sequencia de imagens.")
    parser.add_argument("pasta_imagens", help="Pasta com as imagens a processar.")
    parser.add_argument("--csv", default="resultado_rgb.csv", help="Arquivo CSV de saida.")
    parser.add_argument("--grafico", default="grafico_rgb.png", help="Imagem PNG do grafico.")
    parser.add_argument(
        "--imagem-inteira",
        action="store_true",
        help="Usa todos os pixels, inclusive fundo branco.",
    )
    parser.add_argument(
        "--limite-branco",
        type=int,
        default=220,
        help="Limiar usado para descartar pixels quase brancos.",
    )
    parser.add_argument(
        "--roi",
        nargs=4,
        type=int,
        metavar=("X", "Y", "LARGURA", "ALTURA"),
        help="Usa uma regiao retangular fixa antes de calcular a media.",
    )
    args = parser.parse_args()

    imagens = listar_imagens(args.pasta_imagens)
    if not imagens:
        raise SystemExit("Nenhuma imagem encontrada na pasta informada.")

    linhas = []
    for indice, imagem in enumerate(imagens, start=1):
        media_r, media_g, media_b, pixels = media_rgb(
            imagem,
            ignorar_fundo=not args.imagem_inteira,
            limite_branco=args.limite_branco,
            roi=args.roi,
        )
        linhas.append({
            "indice": indice,
            "arquivo": imagem.name,
            "etapa": identificar_etapa(imagem.name, indice),
            "media_r": round(media_r, 2),
            "media_g": round(media_g, 2),
            "media_b": round(media_b, 2),
            "pixels_usados": pixels,
        })

    salvar_csv(linhas, args.csv)
    salvar_grafico(linhas, args.grafico)

    print(f"Imagens processadas: {len(linhas)}")
    print(f"CSV salvo em: {args.csv}")
    print(f"Grafico salvo em: {args.grafico}")


if __name__ == "__main__":
    main()
