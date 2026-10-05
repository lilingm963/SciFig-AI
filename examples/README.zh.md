# 三个跟做示例

[English](README.md) · [中文](README.zh.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

这些输入是合成教学示例，不是实验依据。教程预览展示的是独立的产品流程，并非由这些示例输入生成的结果。

## 概念性样品制备流程 · Illustration

### 输入

创建三个带标注面板的概念插图：采集样品、制备样品、观察样品。白色背景，蓝绿色配色，清晰的从左到右箭头。不虚构仪器、数值或生物机制。标注“概念性教学示例”。

### 步骤与核对

在 Illustration 中使用提示词。检查标注与箭头方向，再尝试教程展示的一项编辑工具。示例不代表真实实验方案。

[查看完整流程](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-illustration-tutorial.mp4)

## 合成的时间序列测量数据 · DataChart

### 输入

[synthetic-timeseries.csv](datachart/synthetic-timeseries.csv)

### 步骤与核对

在 DataChart 上传 CSV，将 time_min 与 signal_a、signal_b 绘制为两条序列。纵轴注明“任意单位”，逐点对照 CSV，检查图例，再使用当前流程提供的选项导出。

[查看完整流程](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-datachart-tutorial.mp4)

## 教学用数据审查流程 · FlowChart

### 输入

创建教学流程：接收合成数据集 → 核验列名与单位 → 检查缺失值 → 汇总 → 审查图表 → 分享。核验失败时返回输入步骤。标注判断分支，保留分享前的审查步骤。

### 步骤与核对

在 FlowChart 中使用流程文本。检查各节点、核验回路与判断标注。在编辑器修改一个节点，再确认关系仍与输入一致。

[查看完整流程](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-flowchart-tutorial.mp4)

分享前请核对科学含义、标注与来源。编辑和导出选项因工作区与流程而异，教程展示了具体示例。

SciFig 是商业平台。本仓库是公开资源入口，不是产品源码。素材、模板和采用 MIT 许可的 Skill 各有独立条款，任何一项许可都不自动覆盖其他内容。

[许可与使用](../docs/example-usage.zh.md)
