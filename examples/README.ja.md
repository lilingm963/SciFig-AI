# 3つの作例を試す

[English](README.md) · [中文](README.zh.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

入力は学習用に作成した架空の例であり、実験の証拠ではありません。チュートリアルのプレビューは別の制作手順を示しており、これらの入力から生成した結果ではありません。

## 概念的な試料調製 · Illustration

### 入力

「試料を採取」「試料を調製」「試料を観察」の3つのラベル付きパネルで概念図を作成してください。白い背景、青緑の配色、左から右へ明確な矢印。架空の装置、数値、生物学的機構は追加せず、「概念的な学習用作例」と記してください。

### 手順と確認事項

Illustration でプロンプトを使います。ラベルと矢印の向きを確認し、チュートリアルで紹介している編集ツールを一つ試してください。実際の実験手順を指定する作例ではありません。

[制作の全工程を見る](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-illustration-tutorial.mp4)

## 架空の時系列測定データ · DataChart

### 入力

[synthetic-timeseries.csv](datachart/synthetic-timeseries.csv)

### 手順と確認事項

DataChart に CSV をアップロードし、time_min に対する signal_a と signal_b を2系列で描きます。縦軸に「任意単位」と記し、各点を CSV と照合します。凡例を確認して、利用できる形式で書き出してください。

[制作の全工程を見る](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-datachart-tutorial.mp4)

## 学習用のデータ確認フロー · FlowChart

### 入力

学習用フローを作成してください：架空のデータを受け取る → 列名と単位を検証する → 欠損値を確認する → 集計する → グラフを確認する → 共有する。検証に失敗したら入力に戻ります。分岐にラベルを付け、共有前の確認を省かないでください。

### 手順と確認事項

FlowChart でフローテキストを使います。各ノード、検証ループ、分岐ラベルを確認します。エディターでノードを一つ変更し、関係が入力内容と一致しているか確認してください。

[制作の全工程を見る](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-flowchart-tutorial.mp4)

共有する前に科学的な意味、ラベル、出典を確認してください。編集・書き出しの選択肢はワークスペースや制作手順によって異なります。チュートリアルで具体例をご覧ください。

SciFig は商用プラットフォームです。このリポジトリは公開リソースの入口であり、製品のソースコードではありません。素材、テンプレート、MIT ライセンスの Skill はそれぞれ別の条件で提供され、他の内容に自動的には適用されません。

[ライセンスと利用について](../docs/example-usage.ja.md)
